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

# Windows Driver Kit Archive
> [!IMPORTANT]
> This Archive contains links to earlier WDK releases that are not serviced or supported by Microsoft. Some installers may be susceptible to security vulnerabilities (including [CVE-2024-29187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29187)). These are not recommended for production driver development.  
> To develop Windows drivers, always use the [latest WDK version](https://learn.microsoft.com/windows-hardware/drivers/download-the-wdk).


## Legacy WDK Releases
The following table lists legacy WDK releases, their compatibility and support status. Use these only for reference or non-production scenarios
| Windows Version         | Build Number   | Supported Visual Studio | [WDK](#) | [EWDK](#) | [NuGet](#) | [SDK](#) | WDK Susceptible to CVE-2024-29187 | Comments |
|------------------------|---------------|------------------------|----------|-----------|------------|----------|-------------------------------|----------|
| Windows 11 25H2 (Ge)   | 26100         | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.6584) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | No | This is the primary WDK recommended for driver development |
| Windows 11 26H1 (Br)   | 28000.1       | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.6584) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | No | 26H1 is not a feature update for version 25H2 and only includes platform changes to support specific silicon. For more, see [Windows Insider Blog](https://blogs.windows.com/windows-insider/) |
| Windows 11 24H2 (Ge)   | 26100.4204    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.6584) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | No | Supported but not recommended for driver development |
| Windows 11 24H2 (Ge)   | 26100.3323    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.3323) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | No | Supported but not recommended for driver development |
| Windows 11 24H2 (Ge)   | 26100.2454    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.2454) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | No | Supported but not recommended for driver development |
| Windows 11 24H2 (Ge)   | 26100.2161    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.2161) | N/A | No | Supported but not recommended for driver development |
| Windows 11 24H2 (Ge)   | 26100.1882    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1882) | N/A | No | Supported but not recommended for driver development |
| Windows 11 24H2 (Ge)   | 26100.1591    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1591) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | Yes | Supported but not recommended for driver development |
| Windows 11 24H2 (Ge)   | 26100.1       | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | Yes | Supported but not recommended for driver development |
| Windows 11 23H2 (Zn)   | 22621.2428    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2217936) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2217937) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2217938) | Yes | Supported but not recommended for driver development  |
| Windows 11 22H2 (Ni)   | 22621.5337    | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2188002) | N/A | N/A | N/A | No | Supported but not recommended for driver development |
| Windows 11 22H2 (Ni)   | 22621.755     | VS 2022                | N/A | [EWDK](https://go.microsoft.com/fwlink/?linkid=2188003) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2188004) | Yes | Supported but not recommended for driver development  |
| Windows 11 22H2 (Ni)   | 22621.382     | VS 2022                | [WDK](https://go.microsoft.com/fwlink/?linkid=2188002) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2188003) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2188004) | Yes | Supported but not recommended for driver developmen|
| Windows 11 21H2 (CO)   | 22000.832     | VS 2019                | [WDK](https://go.microsoft.com/fwlink/?linkid=2156297) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2156298) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2156299) | Yes | Supported but not recommended for driver development |
| Windows Server 2022 (FE)| 20348.1      | VS 2019                | [WDK](https://go.microsoft.com/fwlink/?linkid=2156297) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2156298) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2156299) | Yes | Supported until 10/14/2031 under LTSC license |
| Windows 10 2004 (VB)   | 19041         | VS 2019                | [WDK](https://go.microsoft.com/fwlink/?linkid=2128854) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2128855) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2128856) | Yes | Out of support |
| Windows 10 1903 (19H1) | 18362.1       | VS 2019                | [WDK](https://go.microsoft.com/fwlink/?linkid=2085767) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2085768) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2085769) | Yes | Out of support |
| Windows 10 1809 (RS5)  | 17763.1       | VS 2017                | [WDK](https://go.microsoft.com/fwlink/?linkid=2026153) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2026154) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2026155) | Yes | Supported until 01/19/2029 under LTSC license |
| Windows 10 1803 (RS4)  | 17134.1       | VS 2017                | [WDK](https://go.microsoft.com/fwlink/?linkid=2014196) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2014197) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2014198) | Yes | Out of support |
| Windows 10 1709 (RS3)  | 16299.15      | VS 2017                | [WDK](https://go.microsoft.com/fwlink/?linkid=2014193) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2014194) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2014195) | Yes | Out of support |
| Windows 10 1703 (RS2)  | 15063.0       | VS 2015                | [WDK](https://go.microsoft.com/fwlink/?linkid=2014189) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2014190) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2014191) | Yes | Out of support |
| Windows 10 1607 (RS1)  | 14393.0       | VS 2015                | [WDK](https://go.microsoft.com/fwlink/?linkid=2014186) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2014187) | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2014188) | Yes | Supported until 10/13/2026 under LTSC license |
| Windows 8              | 9200          | VS 2012                | [WDK](https://go.microsoft.com/fwlink/?linkid=2014183) | N/A | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2014184) | Yes | Supported until 01/13/2026 under Premium Assurance license |
| Windows 7              | 7600          | VS 2010                | [WDK](https://go.microsoft.com/fwlink/?linkid=2014180) | N/A | N/A | [SDK](https://go.microsoft.com/fwlink/?linkid=2014181) | Yes | Supported until 01/13/2026 under Premium Assurance license
## Additional Guidance
- **Security**: These installers may have known vulnerabilities, including [CVE-2024-29187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29187), and are not recommended for production driver development. Use at your own risk
- **Support**: Only the latest WDK and certain LTSC/Premium Assurance releases receive support.
- **Compatibility**: Check required Visual Studio and SDK version before installing any WDK release.
- **Legacy Usage**: Avoid legacy releases for new development. If required, isolate build environments and do not use on production systems.
- **Feedback & Help**: Reach out via the [feedback form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR0aScSwEgKxJvzxab6T-IN5UNFlHSkFQTjBLS1lRS08wTFRZME0yRVRVVi4u) or [wdkfeedback@microsoft.com](mailto:wdkfeedback@microsoft.com).

## See Also

- [Download the latest Windows Driver Kit](https://learn.microsoft.com/windows-hardware/drivers/download-the-wdk)
- [WDK NuGet documentation](https://learn.microsoft.com/windows-hardware/drivers/download-wdk-nuget)
- [Windows Driver Documentation](https://learn.microsoft.com/windows-hardware/drivers/)



