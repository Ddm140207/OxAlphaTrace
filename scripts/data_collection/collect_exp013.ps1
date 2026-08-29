param()
$ErrorActionPreference = "Continue"
$outRoot = "results\raw\reference"
$model = $args[0]
$mShort = ($model -replace "opencode/","" -replace "openrouter/","" -replace "[/:]","_")
New-Item -ItemType Directory -Path "$outRoot\$mShort\exp013" -Force | Out-Null

$src = Get-Content "results\raw\exp013_meta_cognition.json" -Raw | ConvertFrom-Json
foreach ($t in $src.trials) {
  $file = "$outRoot\$mShort\exp013\$($t.id).txt"
  if ((Test-Path $file) -and (Get-Item $file).Length -gt 10) { Write-Output "SKIP $mShort/$($t.id)"; continue }
  $ok = $false
  $json = ""
  foreach ($attempt in 1..3) {
    $json = opencode run -m $model --format json $t.prompt 2>$null | Out-String
    if (-not (Select-String -InputObject $json -Pattern '"type":"error"' -Quiet)) { $ok = $true; break }
    Start-Sleep -Seconds 8
  }
  $texts = @()
  foreach ($line in ($json -split "`n")) {
    $ln = $line.Trim()
    if (-not $ln) { continue }
    try { $o = $ln | ConvertFrom-Json } catch { continue }
    if ($o.type -eq "text" -and $o.part.text) { $texts += $o.part.text }
  }
  $content = ($texts -join "`n")
  if (-not $ok) { $content = "[COLLECTION_ERROR] $content" }
  $content | Out-File -LiteralPath $file -Encoding utf8
  Write-Output "DONE ok=$ok $mShort/$($t.id) :: len=$($content.Length)"
}
