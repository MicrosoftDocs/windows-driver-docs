---
title: Previous WDK versions and other downloads
description: Install versions of the Windows Driver Kit (WDK), the Enterprise Windows Driver Kit (EWDK), and WDK NuGet.
keywords:
- Windows Driver Kit
- previous versions
- WDK
ms.date: 11/11/2025
ms.topic: feature-availability
---
# Previous WDK versions and other Downloads
This page contains links to earlier WDK releases some of which are no longer serviced or supported by Microsoft. To develop Windows drivers, always use the [latest WDK version](download-the-wdk.md)
> [!IMPORTANT]
> Some installers might be susceptible to security vulnerabilities (including [CVE-2024-29187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29187)). These versions of the WDK are not recommended for production driver development.

## Current WDK Releases

The following table lists the current and recommended WDK versions, along with their compatibility and support status. Version 25H2 is the latest WDK for general driver development. Use 26H1 only if you are developing drivers for specialized silicon

| Windows Version         | Build Number   | Supported Visual Studio | SDK | WDK | EWDK | NuGet | WDK Susceptible to CVE-2024-29187 | Comments |
|--------------------------|---------------|--------------------------|-----|-----|------|-------|------------------------------------|----------|
| Windows 11 26H1 (Br)    | 28000.1    | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2320455) | [WDK](https://go.microsoft.com/fwlink/?linkid=2324617) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2324618) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.4204) | No | 26H1 is not a feature update for 25H2 and only includes platform changes to support specific silicon. Use only if you need these changes. For details see [Announcing Windows 11 Insider Preview Build 28000](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fblogs.windows.com%2Fwindows-insider%2F2025%2F11%2F07%2Fannouncing-windows-11-insider-preview-build-28000-canary-channel%2F&data=05%7C02%7Cpauleze%40microsoft.com%7C498c0503d8c84aa195b708de2249f8c0%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638985898291940431%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=%2FYAhAgrFpJPAoPoMxaqrb%2FRoYooyRr%2FeMeCA5L7zFkg%3D&reserved=0) |
| Windows 11 25H2 (Ge)    | 26100.6584   | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.6584) | No | This is the default recommended kit for Windows driver development |

## Legacy WDK Releases

The following table lists legacy WDK releases, their compatibility, and support status. We recommend these to be used only for reference or nonproduction purposes.

| Windows Version         | Build Number   | Supported Visual Studio | SDK | WDK | EWDK | NuGet | WDK Susceptible to CVE-2024-29187 | Comments |
|--------------------------|---------------|--------------------------|-----|-----|------|-------|------------------------------------|----------|
| Windows 11 24H2 (Ge)    | 26100.4204    | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2320455) | [WDK](https://go.microsoft.com/fwlink/?linkid=2324617) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2324618) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.4204) | No |  |
| Windows 11 24H2 (Ge)    | 26100.3323    | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2305205) | [WDK](https://go.microsoft.com/fwlink/?linkid=2307500) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2303317) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.3323) | No |  |
| Windows 11 24H2 (Ge)    | 26100.2454    | VS 2022                | [SDK](https://download.microsoft.com/download/a/f/2/af287d69-2c0a-4320-9d0f-555d5be767b9/WinSDKSetup.exe) | [WDK](https://go.microsoft.com/fwlink/?linkid=2297653) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2297951) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.2454) | No |  |
| Windows 11 24H2 (Ge)    | 26100.2161    | VS 2022                | N/A | [WDK](https://go.microsoft.com/fwlink/?linkid=2294834) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2295035) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.2161) | No |  |
| Windows 11 24H2 (Ge)    | 26100.1882    | VS 2022                | N/A | [WDK](https://go.microsoft.com/fwlink/?linkid=2290025) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2290926) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1882) | No |  |
| Windows 11 24H2 (Ge)    | 26100.1591    | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2286561) | [WDK](https://go.microsoft.com/fwlink/?linkid=2286137) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2286188) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1591) | Yes |  |
| Windows 11 24H2 (Ge)    | 26100.1       | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | [WDK](https://go.microsoft.com/fwlink/?linkid=2272234) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2271957) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1) | Yes |  |
| Windows 11 22H2 (Ni)    | 22621.5337    | VS 2022                | N/A | [WDK](https://go.microsoft.com/fwlink/?linkid=2330411) | N/A | N/A | No | Only recommended for x86/arm32 driver development |
| Windows 11 23H2 (Zn)    | 22621.2428    | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2250105) | [WDK](https://go.microsoft.com/fwlink/?linkid=2249371) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2249942) | N/A | Yes |  |
| Windows 11 22H2 (Ni)    | 22621.755     | VS 2022                | [SDK](https://go.microsoft.com/fwlink/p/?linkid=2196241) | N/A | [EWDK](https://go.microsoft.com/fwlink/?linkid=2195661) | N/A | Yes |  |
| Windows 11 22H2 (Ni)    | 22621.382     | VS 2022                | [SDK](https://go.microsoft.com/fwlink/?linkid=2237387) | [WDK](https://go.microsoft.com/fwlink/?linkid=2196230) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2237475) | N/A | Yes |  |
| Windows 11 21H2 (CO)    | 22000.1     | VS 2019                | [SDK](https://go.microsoft.com/fwlink/?linkid=2173743) | [WDK](https://go.microsoft.com/fwlink/?linkid=2166289) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2202360) | N/A | Yes | Only recommended for Windows 7/Windows 8/Windows 8.1 driver development. |
| Windows Server 2022 (FE)| 20348.1       | VS 2019                | [SDK](https://go.microsoft.com/fwlink/?linkid=2164145) | [WDK](https://go.microsoft.com/fwlink/?linkid=2164149) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2163981) | N/A | Yes | OS Supported until 10/14/2031 under LTSC license. |
| Windows 10 2004 (VB)    | 19041.685     | VS 2019                | [SDK](https://go.microsoft.com/fwlink/?linkid=2128856) | [WDK](https://go.microsoft.com/fwlink/?linkid=2128854) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2128902) | N/A | Yes | Out of support. |
| Windows 10 1903 (19H1)  | 18362.1       | VS 2019                | [SDK](https://go.microsoft.com/fwlink/?linkid=2083338) | [WDK](https://go.microsoft.com/fwlink/?linkid=2085767) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2086136) | N/A | Yes | Out of support. |
| Windows 10 1809 (RS5)   | 17763.1       | VS 2017                | [SDK](https://go.microsoft.com/fwlink/p/?LinkID=2033908) | [WDK](https://go.microsoft.com/fwlink/?linkid=2026156) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2070246&clcid=0x409) | N/A | Yes | OS Supported until 01/19/2029 under LTSC license |
| Windows 10 1803 (RS4)   | 17134.1       | VS 2017                | [SDK](https://go.microsoft.com/fwlink/?linkid=2014198) | [WDK](https://go.microsoft.com/fwlink/?linkid=873060) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2008688&clcid=0x409) | N/A | Yes | Out of support. |
| Windows 10 1709 (RS3)   | 16299.15      | VS 2017                | [SDK](https://go.microsoft.com/fwlink/p/?linkid=864422) | [WDK](https://go.microsoft.com/fwlink/p/?linkid=859232) | [EWDK](https://go.microsoft.com/fwlink/?linkid=870959) | N/A | Yes | Out of support. |
| Windows 10 1703 (RS2)   | 15063.0       | VS 2015                | [SDK](https://go.microsoft.com/fwlink/p/?LinkId=845298) | [WDK](https://go.microsoft.com/fwlink/p/?LinkID=845980) | [EWDK](https://go.microsoft.com/fwlink/p/?LinkID=846038) | N/A | Yes | Out of support. |
| Windows 10 1607 (RS1)   | 14393.0       | VS 2015                | [SDK](https://go.microsoft.com/fwlink/p/?LinkId=838916) | [WDK](https://go.microsoft.com/fwlink/p/?LinkId=526733) | [EWDK](https://go.microsoft.com/fwlink/p/?LinkID=699461) | N/A | Yes | OS Supported until 10/13/2026 under LTSC license |
| Windows 8               | 9200          | VS 2012                | [SDK](https://go.microsoft.com/fwlink/p/?LinkId=226658) | [WDK](https://go.microsoft.com/fwlink/p/?LinkID=324284) | N/A | N/A | Yes | OS Supported until 01/13/2026 under Premium Assurance license. |
| Windows 7               | 7600          | VS 2010                | [SDK](https://go.microsoft.com/fwlink/?LinkID=191424) | [WDK](https://www.microsoft.com/en-sg/download/details.aspx?id=11800) | N/A | N/A | Yes | OS Supported until 01/13/2026 under Premium Assurance license. |


## Guidance

- **Security**: These installers might have known vulnerabilities, including [CVE-2024-29187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29187), and aren't recommended for production driver development. Use at your own risk
> [!Note]
> The referenced CVE impacts to only WDK MSI. The EWDK and WDK NuGet is not impacted.
- **Support**: Only the latest WDK and certain LTSC/Premium Assurance releases receive support.
- **Compatibility**: Check required Visual Studio and SDK version before installing any WDK release.
- **Legacy Usage**: Avoid legacy releases for new development. If necessary, isolate build environments and don't use on production systems.
- **Contact Us**: Reach out via the [feedback form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR0aScSwEgKxJvzxab6T-IN5UNFlHSkFQTjBLS1lRS08wTFRZME0yRVRVVi4u) or email [wdkfeedback@microsoft.com](mailto:wdkfeedback@microsoft.com).

## See Also

- [Download the latest Windows Driver Kit](download-the-wdk.md)
- [WDK NuGet documentation](install-the-wdk-using-nuget.md)
- [Windows Driver Documentation](index.yml)
