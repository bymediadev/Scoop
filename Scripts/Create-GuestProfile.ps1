# Create-GuestProfile.ps1

$fullName = Read-Host "Full Name"
$role = Read-Host "Title or Role"
$company = Read-Host "Company"
$achievementsRaw = Read-Host "List 1–2 key achievements (comma separated)"
$location = Read-Host "Location (optional)"
$prevCompaniesRaw = Read-Host "Previous companies (comma separated, optional)"
$flair = Read-Host "Fun personal fact (optional)"

$achievements = $achievementsRaw -split "," | ForEach-Object { $_.Trim() }
$prevCompanies = $prevCompaniesRaw -split "," | ForEach-Object { $_.Trim() }

$guestProfile = @{
    full_name = $fullName
    role = $role
    company = $company
    notable_achievements = $achievements
    location = $location
    previous_companies = $prevCompanies
    flair = $flair
}

# Save to JSON
$guestProfile | ConvertTo-Json -Depth 3 | Set-Content -Path "C:\PodcastResearchTool\guest_profile.json" -Encoding UTF8

Write-Host "`n✅ guest_profile.json created successfully." -ForegroundColor Green
Read-Host -Prompt "Press Enter to close"
