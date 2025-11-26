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
| Windows 11 25H2 (Ge) | 26100.6584 | [VS 2022](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2022-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2338977) | [WDK](https://go.microsoft.com/fwlink/?linkid=2335869) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2335681) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.26100.6584) | This version is the default supported kit for Windows driver development. |
| Windows 11 26H1 (Br) | 28000.1 | [VS 2022](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2022-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2342535) | [WDK](https://go.microsoft.com/fwlink/?linkid=2342530) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2342427) | [NuGet](https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/10.0.28000.1-RTM) | 26H1 includes platform changes to support specific silicon. Use only if you need these changes. For details see [Announcing Windows 11 Insider Preview Build 28000](https://blogs.windows.com/windows-insider/2025/11/07/announcing-windows-11-insider-preview-build-28000-canary-channel/). |
| Windows 11 22H2 (Ni) | 22621.5193 | [VS 2022](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2022-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2311806) | [WDK](https://go.microsoft.com/fwlink/?linkid=2330411) | [EWDK](https://go.microsoft.com/fwlink/?linkid=2249942) | N/A | Supported for Windows 10 x86/ARM32 driver development only. |
| Windows 10 2004 (VB) | 19041.5738 | [VS 2019](https://visualstudio.microsoft.com/vs/older-downloads/#visual-studio-2019-and-other-products) | [SDK](https://go.microsoft.com/fwlink/?linkid=2311805) | [WDK](https://go.microsoft.com/fwlink/?linkid=2342425) | [EWDK](https://go.microsoft.com/fwlink/p/?linkid=2128902) | N/A | Supported for Windows 7/Windows 8/Windows 8.1 driver development only.  |

 If you are looking for legacy or unsupported WDKs, they can be found on the [unsupported WDK versions](./legacy-wdk-downloads.md) page. 

## Additional Guidance
- **Best Practice**: Always use the latest WDK for new driver development to ensure security and compatibility.
- **Compatibility**: Verify the required Visual Studio and SDK version before installing any WDK release.
- **Contact us**: Share feedback or questions through the [feedback form](https://forms.microsoft.com/r/c2eHwWrE1Z) or email [wdkfeedback@microsoft.com](mailto:wdkfeedback@microsoft.com).


## See also

- [Download the latest Windows Driver Kit](download-the-wdk.md)
- [WDK NuGet documentation](install-the-wdk-using-nuget.md)
- [Windows drivers development documentation](index.yml)

