---
title: Legacy and Unsupported WDK Versions
description: Install versions of the Windows Driver Kit (WDK), the Enterprise Windows Driver Kit (EWDK), and WDK NuGet.
keywords:
- Windows Driver Kit
- previous versions
- WDK
ms.date: 11/13/2025
ms.topic: feature-availability
---

#  Legacy and Unsupported WDK versions

> [!WARNING]
> **Critical Security Notice:**
The following table lists legacy WDK releases, their corresponding SDK and Visual Studio versions. These releases contains compoenents affected by [CVE-2024-29187](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29187) and are **NOT safe for production driver development** and are provided only for reference or nonproduction use. For developing Windows drivers, always use the latest WDK version to ensure security and compatibility.

> [!NOTE]
> The referenced CVE impacts WDK and MSIs. The EWDK and WDK NuGet is not impacted.

| Windows Version | Build Number | Supported Visual Studio | SDK | WDK | EWDK | NuGet |
|--|--|--|--|--|--|--|
| Windows 11 24H2 (Ge) | 26100.1 | VS 2022 | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | [WDK](https://go.microsoft.com/fwlink/?linkid=2272234) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2271957) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.1) |
| Windows 11 23H2 (Zn) | 22621.2428 | VS 2022 | [SDK](https://go.microsoft.com/fwlink/?linkid=2250105) | [WDK](https://go.microsoft.com/fwlink/?linkid=2249371) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2249942) | N/A |  
| Windows 11 22H2 (Ni) | 22621.755 | VS 2022 | [SDK](https://go.microsoft.com/fwlink/p/?linkid=2196241) | N/A | [EWDK](https://go.microsoft.com/fwlink/?linkid=2195661) | N/A | 
| Windows 11 22H2 (Ni) | 22621.382 | VS 2022 | [SDK](https://go.microsoft.com/fwlink/?linkid=2237387) | [WDK](https://go.microsoft.com/fwlink/?linkid=2196230) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2237475) | N/A |
| Windows 11 21H2 (CO) | 22000.1 | VS 2019 | [SDK](https://go.microsoft.com/fwlink/?linkid=2173743) | [WDK](https://go.microsoft.com/fwlink/?linkid=2166289) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2202360) | N/A |  
| Windows Server 2022 (FE) | 20348.3567 | VS 2019 | [SDK](https://go.microsoft.com/fwlink/?linkid=2164145) | [WDK](https://go.microsoft.com/fwlink/?linkid=2164149) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2163981) | N/A |  
| Windows 10 2004 (VB) | 19041.685 | VS 2019 | [SDK](https://go.microsoft.com/fwlink/?linkid=2128856) | [WDK](https://go.microsoft.com/fwlink/?linkid=2128854) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2128902) | N/A |   
| Windows 10 1903 (19H1) | 18362.1 | VS 2019 | [SDK](https://go.microsoft.com/fwlink/?linkid=2083338) | [WDK](https://go.microsoft.com/fwlink/?linkid=2085767) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2086136) | N/A |   
| Windows 10 1809 (RS5) | 17763.1 | VS 2017 | [SDK](https://go.microsoft.com/fwlink/p/?LinkID=2033908) | [WDK](https://go.microsoft.com/fwlink/?linkid=2026156) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2070246&clcid=0x409) | N/A |   
| Windows 10 1803 (RS4) | 17134.1 | VS 2017 | [SDK](https://go.microsoft.com/fwlink/?linkid=2014198) | [WDK](https://go.microsoft.com/fwlink/?linkid=873060) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2008688&clcid=0x409) | N/A |   
| Windows 10 1709 (RS3) | 16299.15 | VS 2017 | [SDK](https://go.microsoft.com/fwlink/p/?linkid=864422) | [WDK](https://go.microsoft.com/fwlink/p/?linkid=859232) | [EWDK](https://go.microsoft.com/fwlink/?linkid=870959) | N/A |   
| Windows 10 1703 (RS2) | 15063.0 | VS 2015 | [SDK](https://go.microsoft.com/fwlink/p/?LinkId=845298) | [WDK](https://go.microsoft.com/fwlink/p/?LinkID=845980) | [EWDK](https://go.microsoft.com/fwlink/p/?LinkID=846038) | N/A |   
| Windows 10 1607 (RS1) | 14393.0 | VS 2015 | [SDK](https://go.microsoft.com/fwlink/p/?LinkId=838916) | [WDK](https://go.microsoft.com/fwlink/p/?LinkId=526733) | [EWDK](https://go.microsoft.com/fwlink/p/?LinkID=699461) | N/A |   
| Windows 8 | 9200 | VS 2012 | [SDK](https://go.microsoft.com/fwlink/p/?LinkId=226658) | [WDK](https://go.microsoft.com/fwlink/p/?LinkID=324284) | N/A | N/A |  |
| Windows 7 | 7600 | VS 2010 | [SDK](https://go.microsoft.com/fwlink/?LinkID=191424) | [WDK](https://www.microsoft.com/en-sg/download/details.aspx?id=11800) | N/A | N/A | 

## Guidance

- **Compatibility**: Verify the required Visual Studio and SDK version before installing any WDK release.
- **Legacy usage**: Don't use legacy releases for new development. If unavoidable, isolate build environments and ensure they aren't deployed on production systems
- **Contact us**: Share feedback or question through the [feedback form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR0aScSwEgKxJvzxab6T-IN5UNFlHSkFQTjBLS1lRS08wTFRZME0yRVRVVi4u) or email [wdkfeedback@microsoft.com](mailto:wdkfeedback@microsoft.com).
## See also

- [Download the latest Windows Driver Kit](download-the-wdk.md)
- [WDK NuGet documentation](install-the-wdk-using-nuget.md)
- [Windows drivers development documentation](index.yml)
