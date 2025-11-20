---
title: Legacy and Unsupported WDK versions
description: Download legacy WDK, EWDK, or WDK NuGet packages for reference or non-production use only.
keywords:
- Windows Driver Kit
- previous versions
- deprecated WDK
- unsupported driver kits
- security advisory
- WDK
ms.date: 11/13/2025
ms.topic: feature-availability
---

#  Legacy and Unsupported WDK versions

The following table lists legacy and unsupported WDK versions, their corresponding SDK and Visual Studio versions where available. If you are developing a driver for the Windows platform, use one of the supported kits listed on the [supported WDK versions](./other-wdk-downlaods.md) table.

> [!WARNING]
> **Critical Security Notice:**
Some of these releases contain components affected by [CVE-2024-29187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29187) and are **NOT safe for production driver development**. They are provided only for reference and non-production use. If you do need to access that specific kit build, then consider if you can use the matching EWDK that is not impacted by the CVE.  If EWDK is not an option, then take precautions including researching CVE, isolate your build environments, and ensure no use on production systems

| Windows Version | Build Number | Supported Visual Studio | SDK | WDK | EWDK | NuGet |Comment|
|--|--|--|--|--|--|--|--|
| Windows 11 24H2 (Ge) | 26100.4204 | VS 2022 | [SDK](https://go.microsoft.com/fwlink/?linkid=2320455) | [WDK](https://go.microsoft.com/fwlink/?linkid=2324617) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2324618) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.4204) | These kits are not impacted by CVE-2024-29187  |
| Windows 11 24H2 (Ge) | 26100.3323 | VS 2022 | [SDK](https://go.microsoft.com/fwlink/?linkid=2305205) | [WDK](https://go.microsoft.com/fwlink/?linkid=2307500) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2303317) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.3323) | These kits are not impacted by CVE-2024-29187 |
| Windows 11 24H2 (Ge) | 26100.2454 | VS 2022 | [SDK](https://download.microsoft.com/download/a/f/2/af287d69-2c0a-4320-9d0f-555d5be767b9/WinSDKSetup.exe) | [WDK](https://go.microsoft.com/fwlink/?linkid=2297653) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2297951) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.2454) | These kits are not impacted by CVE-2024-29187 |
| Windows 11 24H2 (Ge) | 26100.2161 | VS 2022 | N/A | [WDK](https://go.microsoft.com/fwlink/?linkid=2294834) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2295035) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.2161) | These kits are not impacted by CVE-2024-29187 |
| Windows 11 24H2 (Ge) | 26100.1882 | VS 2022 | N/A | [WDK](https://go.microsoft.com/fwlink/?linkid=2290025) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2290926) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1882) |These kits are not impacted by CVE-2024-29187  |
| Windows 11 24H2 (Ge) | 26100.1591 | VS 2022 | [SDK](https://go.microsoft.com/fwlink/?linkid=2286561) | [WDK](https://go.microsoft.com/fwlink/?linkid=2286137) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2286188) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1591) | These kits are not impacted by CVE-2024-29187 |
| Windows 11 24H2 (Ge) | 26100.1 | VS 2022 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2338977) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=2272234) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2271957) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1) | SDK and WDK installers are impacted by CVE-2024-29187. EWDK and WDK NuGet are not impacted
| Windows 11 23H2 (Zn) | 22621.2428 | VS 2022 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2250105) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=2249371) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2249942) | N/A |  SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted
| Windows 11 22H2 (Ni) | 22621.755 | VS 2022 | [SDK (*)](https://go.microsoft.com/fwlink/p/?linkid=2196241) | N/A | [EWDK](https://go.microsoft.com/fwlink/?linkid=2195661) | N/A | SDK installer is impacted by CVE-2024-29187. EWDK is not impacted
| Windows 11 22H2 (Ni) | 22621.382 | VS 2022 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2237387) | [WDK](https://go.microsoft.com/fwlink/?linkid=2196230) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2237475) | N/A |SDK and WDK installer are impacted by CVE-2024-29187. EWDK is not impacted
| Windows 11 21H2 (CO) | 22000.1 | VS 2019 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2173743) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=2166289) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2202360) | N/A | SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted 
| Windows Server 2022 (FE) | 20348.1| VS 2019 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2164145) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=2164149) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2163981) | N/A |  SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted
| Windows 10 2004 (VB) | 19041.685 | VS 2019 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2128856) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=2128854) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2128902) | N/A | SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted  
| Windows 10 1903 (19H1) | 18362.1 | VS 2019 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2083338) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=2085767) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2086136) | N/A |  SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted 
| Windows 10 1809 (RS5) | 17763.1 | VS 2017 | [SDK (*)](https://go.microsoft.com/fwlink/p/?LinkID=2033908) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=2026156) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2070246&clcid=0x409) | N/A |  SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted 
| Windows 10 1803 (RS4) | 17134.1 | VS 2017 | [SDK (*)](https://go.microsoft.com/fwlink/?linkid=2014198) | [WDK (*)](https://go.microsoft.com/fwlink/?linkid=873060) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2008688&clcid=0x409) | N/A |  SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted 
| Windows 10 1709 (RS3) | 16299.15 | VS 2017 | [SDK (*)](https://go.microsoft.com/fwlink/p/?linkid=864422) | [WDK (*)](https://go.microsoft.com/fwlink/p/?linkid=859232) | [EWDK](https://go.microsoft.com/fwlink/?linkid=870959) | N/A |  SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted 
| Windows 10 1703 (RS2) | 15063.0 | VS 2015 | [SDK (*)](https://go.microsoft.com/fwlink/p/?LinkId=845298) | [WDK (*)](https://go.microsoft.com/fwlink/p/?LinkID=845980) | [EWDK](https://go.microsoft.com/fwlink/p/?LinkID=846038) | N/A |  SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted  
| Windows 10 1607 (RS1) | 14393.0 | VS 2015 | [SDK (*)](https://go.microsoft.com/fwlink/p/?LinkId=838916) | [WDK (*)](https://go.microsoft.com/fwlink/p/?LinkId=526733) | [EWDK](https://go.microsoft.com/fwlink/p/?LinkID=699461) | N/A |   SDK and WDK installers are impacted by CVE-2024-29187. EWDK is not impacted |
| Windows 8 | 9200 | VS 2012 | [SDK (*)](https://go.microsoft.com/fwlink/p/?LinkId=226658) | [WDK (*)](https://go.microsoft.com/fwlink/p/?LinkID=324284) | N/A | N/A | SDK and WDK installers are impacted by CVE-2024-29187 |
| Windows 7 | 7600 | VS 2010 | [SDK (*)](https://go.microsoft.com/fwlink/?LinkID=191424) | [WDK (*)](https://www.microsoft.com/en-sg/download/details.aspx?id=11800) | N/A | N/A | SDK and WDK installers are impacted by CVE-2024-29187|

## Guidance

- **Compatibility**: Verify the required Visual Studio and SDK version before installing any WDK release.
- **Legacy usage**: **(*)** Unsupported SDK and WDK kits that are impacted by [CVE-2024-29187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29187).  
- **Contact us**: Share feedback or question through the [feedback form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR0aScSwEgKxJvzxab6T-IN5UNFlHSkFQTjBLS1lRS08wTFRZME0yRVRVVi4u) or email [wdkfeedback@microsoft.com](mailto:wdkfeedback@microsoft.com).
## See also

- [Download the latest Windows Driver Kit](download-the-wdk.md)
- [WDK NuGet documentation](install-the-wdk-using-nuget.md)
- [Windows drivers development documentation](index.yml)
