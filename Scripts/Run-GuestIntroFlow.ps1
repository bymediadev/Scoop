# Run-GuestIntroFlow.ps1

# Step 1: Collect guest profile
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

# Save JSON
$jsonPath = "C:\PodcastResearchTool\guest_profile.json"
$guestProfile | ConvertTo-Json -Depth 3 | Set-Content -Path $jsonPath -Encoding UTF8
Write-Host "`n✅ guest_profile.json created at $jsonPath`n" -ForegroundColor Cyan

# Step 2: Generate Guest Bio
function Generate-GuestBio {
    param (
        [string]$FullName,
        [string]$Role,
        [string]$Company,
        [string[]]$Achievements,
        [string]$Location = "",
        [string[]]$PreviousCompanies = @(),
        [string]$Flair = ""
    )

    $bio = "Today’s guest is $FullName, $Role at $Company."

    if ($Achievements.Count -gt 0) {
        $bio += " " + ($Achievements | ForEach-Object { "$_." }) -join " "
    }

    if ($PreviousCompanies.Count -gt 0) {
        $prev = $PreviousCompanies -join " and "
        $bio += " Before this, $FullName worked at $prev."
    }

    if ($Flair -ne "") {
        $bio += " Fun fact: $Flair."
    }

    if ($Location -ne "") {
        $bio += " Based in $Location."
    }

    $firstName = $FullName.Split(" ")[0]
    $bio += " $firstName, welcome to the show."

    return $bio
}

# Load JSON
$json = Get-Content $jsonPath | ConvertFrom-Json

# Generate and save bio
$bioText = Generate-GuestBio `
    -FullName $json.full_name `
    -Role $json.role `
    -Company $json.company `
    -Achievements $json.notable_achievements `
    -Location $json.location `
    -PreviousCompanies $json.previous_companies `
    -Flair $json.flair

Write-Host "`n🎙️ Guest Intro Bio:`n" -ForegroundColor Green
Write-Host $bioText -ForegroundColor Yellow

$bioOutputPath = "C:\PodcastResearchTool\guest_intro_bio.txt"
$bioText | Out-File $bioOutputPath -Encoding UTF8
Write-Host "`n✅ guest_intro_bio.txt saved to $bioOutputPath" -ForegroundColor Cyan

Read-Host -Prompt "`nPress Enter to close"
