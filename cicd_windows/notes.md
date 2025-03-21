## Code Build

### YALM 1

```yaml
version: 0.2
env:
    shell: powershell.exe 
phases:
    install:
        commands:
            - Start-BitsTransfer -Source "https://builds.dotnet.microsoft.com/dotnet/Sdk/6.0.428/dotnet-sdk-6.0.428-win-x64.exe" -Destination ".\dotnet-sdk-6.0.428-win-x64.exe"
            - Start-Process -FilePath ".\dotnet-sdk-6.0.428-win-x64.exe" -ArgumentList "/quiet" -NoNewWindow -Wait
    build:
        commands:
            - cd ProfitCalc.Web
            - dotnet restore
            - dotnet build --configuration Release
            - $publish_artifact=".\artifact\eShopOnWeb"
            - $zip_artifact=".\artifact\eShopOnWeb.zip"
            - dotnet publish --configuration Release --output $publish_artifact
            - Get-ChildItem -Path "$publish_artifact" -Filter "web.config" -Recurse | Remove-Item -Force
            - Compress-Archive -Path $publish_artifact -DestinationPath $zip_artifact -Update
artifacts:
    files:
        - .\ProfitCalc.Web\artifact\*.zip
        - .\ProfitCalc.Web\appspec.yml
        - .\ProfitCalc.Web\scripts\**\*
    discard-paths: yes

```

### YALM 2

```yaml
version: 0.0
os: windows
files:
  - source: \
    destination: C:\inetpub\deployment\eShopOnWeb
file_exists_behavior: OVERWRITE
hooks:
  BeforeInstall:
    - location: \scripts\stop-iis-website.ps1
  AfterInstall:
    - location: \scripts\start-iis-website.ps1
```

### \scripts\stop-iis-website.ps1

```

```

### Powershell to install WinGet


Install winget
```
$progressPreference = 'silentlyContinue'
Install-PackageProvider -Name NuGet -Force | Out-Null
Install-Module -Name Microsoft.WinGet.Client -Force -Repository PSGallery | Out-Null
Repair-WinGetPackageManager
Write-Host "Installed Winget to Windows."
```

SDK Installation - Available options for the winget to work with supports only .8 and .9 versions
  - Microsoft.DotNet.Runtime.9—.NET Runtime 9.0
  - Microsoft.DotNet.AspNetCore.9—ASP.NET Core Runtime 9.0
  - Microsoft.DotNet.DesktopRuntime.9—.NET Desktop Runtime 9.0
  - Microsoft.DotNet.SDK.9—.NET SDK 9.0
  - Microsoft.DotNet.Runtime.8—.NET Runtime 8.0
  - Microsoft.DotNet.AspNetCore.8—ASP.NET Core Runtime 8.0
  - Microsoft.DotNet.DesktopRuntime.8—.NET Desktop Runtime 8.0
  - Microsoft.DotNet.SDK.8—.NET SDK 8.0

Command to install SDK using WinGet.
```
winget install Microsoft.DotNet.SDK.9
```

Steps to handle dependencies:

Create a scirpt for the deps and put it in the git only.

### Downloading Packages

```powershell
# Download the Package
Start-BitsTransfer -Source "https://download.visualstudio.microsoft.com/download/pr/e91a9a25-ec83-4a12-8c15-0b65081b59f5/4e21a057218b753a437bf7bebb7dcbab/dotnet-sdk-9.0.201-win-x64.exe" -Destination ".\dotnet-sdk-9.0.201-win-x64.exe"
# Install the msixbundle
Start-Process -FilePath ".\dotnet-sdk-9.0.201-win-x64.exe" -ArgumentList "/quiet" -NoNewWindow -Wait
```