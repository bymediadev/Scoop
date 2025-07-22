param (
    [string]$JsonPath = "C:\PodcastResearchTool\guest_profile.json"
)

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

# --- Load guest data from JSON ---
if (-Not (Test-Path $JsonPath)) {
    Write-Error "Guest profile not found at $JsonPath"
    exit
}

$json = Get-Content $JsonPath | ConvertFrom-Json

# --- Build the bio ---
$bioText = Generate-GuestBio `
    -FullName $json.full_name `
    -Role $json.role `
    -Company $json.company `
    -Achievements $json.notable_achievements `
    -Location $json.location `
    -PreviousCompanies $json.previous_companies `
    -Flair $json.flair

# --- Display and save ---
Write-Host "`nGenerated Guest Bio:`n" -ForegroundColor Green
Write-Host $bioText -ForegroundColor Yellow

# Save to text file
$bioText | Out-File "C:\PodcastResearchTool\guest_intro_bio.txt" -Encoding utf8

# Keep window open
Read-Host -Prompt "`nPress Enter to close"
