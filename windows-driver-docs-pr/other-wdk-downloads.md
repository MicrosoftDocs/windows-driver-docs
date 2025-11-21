---
title: Supported and other WDK download versions
description: Download supported WDK, EWDK, and WDK NuGet packages for Windows driver development.
keywords:
- Windows Driver Kit
- Enterprise Windows Driver Kit
- WDK NuGet package
- supported WDK versions
- driver development kits
- Windows driver tools
- EWDK download
- Windows driver development tools
ms.date: 11/19/2025
ms.topic: how-to
---

# Supported WDK versions

The following table lists the supported WDK versions, along with their usage guidance. 

| Windows Version | Build Number | Supported Visual Studio | SDK | WDK | EWDK | NuGet | Comments |
|--|--|--|--|--|--|--|--|
| Windows 11 26H1 (Br) | 28000.1 | [VS 2022](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2022-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2320455) | [WDK](https://go.microsoft.com/fwlink/?linkid=2342530) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2342427) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.28000.1) | 26H1 includes platform changes to support specific silicon. Use only if you need these changes. For details see [Announcing Windows 11 Insider Preview Build 28000](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fblogs.windows.com%2Fwindows-insider%2F2025%2F11%2F07%2Fannouncing-windows-11-insider-preview-build-28000-canary-channel%2F&data=05%7C02%7Cpauleze%40microsoft.com%7C498c0503d8c84aa195b708de2249f8c0%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638985898291940431%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=%2FYAhAgrFpJPAoPoMxaqrb%2FRoYooyRr%2FeMeCA5L7zFkg%3D&reserved=0). |
| Windows 11 25H2 (Ge) | 26100.6584 | [VS 2022](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2022-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.6584) | This version is the default supported kit for Windows driver development. |
| Windows 11 22H2 (Ni) | 22621.5193 | [VS 2022](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2022-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2311806) | [WDK](https://go.microsoft.com/fwlink/?linkid=2330411) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2249942) | N/A | Supported for Windows 10 x86/ARM32 driver development only. |
| Windows 10 2004 (VB) | 19041.5738 | [VS 2019](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2019-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2311805) | [WDK](https://go.microsoft.com/fwlink/?linkid=2342425) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2128902) | N/A | Supported for Windows 7/Windows 8/Windows 8.1 driver development only.  |

 If you are looking for unsupported WDKs, they can be found on [legacy and unsupported WDKs](./legacy-wdk-downloads.md) page. 

## Additional Guidance
- **Best Practice**: Always use the latest WDK for new driver development to ensure security and compatibility.
- **Compatibility**: Verify the required Visual Studio and SDK version before installing any WDK release.
- **Contact us**: Share feedback or questions through the [feedback form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR0aScSwEgKxJvzxab6T-IN5UNFlHSkFQTjBLS1lRS08wTFRZME0yRVRVVi4u) or email [wdkfeedback@microsoft.com](mailto:wdkfeedback@microsoft.com).


## See also

- [Download the latest Windows Driver Kit](download-the-wdk.md)
- [WDK NuGet documentation](install-the-wdk-using-nuget.md)
- [Windows drivers development documentation](index.yml)

