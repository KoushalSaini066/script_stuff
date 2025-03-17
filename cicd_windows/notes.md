## Code Build

### YALM 1

```
version: 0.2
env:
    variables:
        publish_artifact: ".\artifact\eShopOnWeb"
        zip_artifact: ".\artifact\eShopOnWeb.zip"
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
            - dotnet publish --configuration Release --output $publish_artifact
            - Get-ChildItem -Path "$publish_artifact" -Filter "web.config" -Recurse | Remove-Item -Force
            - Compress-Archive -Path $publish_artifact -DestinationPath $zip_artifact -Update
artifacts:
    files:
        - .\ProfitCalc.Web\artifact\*.zip
        - .\ProfitCalc.Web\appspec.yml
        - .\ProfitCalc.Web\scripts\**\*
```

### YALM 2

```
version: 0.0
os: windows
files:
  - source: \artifacts\_PublishedWebsites\Test.Web
    destination: D:\inetpub\wwwroot\Test\
file_exists_behavior: OVERWRITE
hooks:
  BeforeInstall:
    - location: \Scripts\stop-iis-website.ps1
  AfterInstall:
    - location: \Scripts\start-iis-website.ps1
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

### Commands ran for the scipt