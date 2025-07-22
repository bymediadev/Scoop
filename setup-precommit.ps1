# Navigate to repo root
cd C:\Scoop-clean

# Create .gitattributes
@"
# Set default behavior to automatically normalize line endings
* text=auto

# Explicitly declare text files you want to always normalize
*.py text eol=lf
*.ps1 text eol=crlf
*.md text eol=lf

# Binary files (don't modify)
*.png binary
*.jpg binary
*.exe binary
"@ | Set-Content -Path .gitattributes -Encoding UTF8

# Create .pre-commit-config.yaml
@"
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-added-large-files
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-case-conflict
      - id: forbid-binary
      - id: check-json
  - repo: https://github.com/detailyang/pre-commit-secrets
    rev: v0.1.7
    hooks:
      - id: detect-private-key
      - id: detect-aws-credentials
"@ | Set-Content -Path .pre-commit-config.yaml -Encoding UTF8

# Install pre-commit if not installed
if (-not (Get-Command pre-commit -ErrorAction SilentlyContinue)) {
    Write-Host "Installing pre-commit via pip..."
    pip install pre-commit
} else {
    Write-Host "pre-commit is already installed."
}

# Install git hooks
pre-commit install

# Add new files to git
git add .gitattributes .pre-commit-config.yaml
git commit -m "Add .gitattributes and pre-commit hook config"
git push

Write-Host "Setup complete. pre-commit hooks installed and configured."
