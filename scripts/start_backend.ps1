Set-Location "$PSScriptRoot\..\backend"

if (-not (Test-Path ".venv")) {
    Write-Host "Virtual environment not found."
    exit
}

& ".\.venv\Scripts\Activate.ps1"

uvicorn app.main:app --reload