param()
$ErrorActionPreference = "Continue"
$outRoot = "results\raw\reference"
$model = $args[0]
$mShort = ($model -replace "opencode/","" -replace "openrouter/","" -replace "[/:]","_")
$src = Get-Content "results\raw\exp013_meta_cognition.json" -Raw | ConvertFrom-Json
$diag = @("M4","M5","M8","M9","M3")   # most diagnostic probes
New-Item -ItemType Directory -Path "$outRoot\$mShort\seeds" -Force | Out-Null

# Pass 1: standard 12-probe collection if missing
foreach ($t in $src.trials) {
  $file = "$outRoot\$mShort\exp013\$($t.id).txt"
  New-Item -ItemType Directory -Path (Split-Path $file) -Force | Out-Null
  if ((Test-Path $file) -and (Get-Item $file).Length -gt 10) { Write-Output "SKIP $mShort/$($t.id)"; continue }
  $ok = $false; $json = ""
  foreach ($attempt in 1..3) {
    $json = opencode run -m $model --format json $t.prompt 2>$null | Out-String
    if (-not (Select-String -InputObject $json -Pattern '"type":"error"' -Quiet)) { $ok = $true; break }
    Start-Sleep -Seconds 8
  }
  $texts = @()
  foreach ($line in ($json -split "`n")) {
    $ln = $line.Trim(); if (-not $ln) { continue }
    try { $o = $ln | ConvertFrom-Json } catch { continue }
    if ($o.type -eq "text" -and $o.part.text) { $texts += $o.part.text }
  }
  $content = ($texts -join "`n")
  if (-not $ok) { $content = "[COLLECTION_ERROR] $content" }
  $content | Out-File -LiteralPath $file -Encoding utf8
  Write-Output "DONE ok=$ok $mShort/$($t.id) :: len=$($content.Length)"
}

# Pass 2: extra seeds for diagnostic probes (seed 2 and 3)
foreach ($pid_ in $diag) {
  foreach ($s in @(2,3)) {
    $file = "$outRoot\$mShort\seeds\$($pid_)_s$s.txt"
    if ((Test-Path $file) -and (Get-Item $file).Length -gt 10) { Write-Output "SKIP seed $mShort/$($pid_)_s$s"; continue }
    $prompt = ($src.trials | Where-Object { $_.id -eq $pid_ }).prompt + "`n(Trial ${s}: answer again naturally.)"
    $ok = $false; $json = ""
    foreach ($attempt in 1..3) {
      $json = opencode run -m $model --format json $prompt 2>$null | Out-String
      if (-not (Select-String -InputObject $json -Pattern '"type":"error"' -Quiet)) { $ok = $true; break }
      Start-Sleep -Seconds 8
    }
    $texts = @()
    foreach ($line in ($json -split "`n")) {
      $ln = $line.Trim(); if (-not $ln) { continue }
      try { $o = $ln | ConvertFrom-Json } catch { continue }
      if ($o.type -eq "text" -and $o.part.text) { $texts += $o.part.text }
    }
    $content = ($texts -join "`n")
    if (-not $ok) { $content = "[COLLECTION_ERROR] $content" }
    $content | Out-File -LiteralPath $file -Encoding utf8
    Write-Output "SEED ok=$ok $mShort/$($pid_)_s$s :: len=$($content.Length)"
  }
}
