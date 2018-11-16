---
title: Windows Hardware Error Architecture (WHEA) design guide
description: Windows Hardware Error Architecture (WHEA) design guide
ms.assetid: 7a42bacd-cafe-48e0-8568-402738fd6e7c
keywords:
- Windows Hardware Error Architecture WDK
- WHEA WDK
- hardware errors WDK WHEA
- errors WDK WHEA
- detecting hardware errors WDK
- reporting hardware errors WDK
- recovering from hardware errors WDK WHEA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Hardware Error Architecture (WHEA) design guide


This section describes the Windows Hardware Error Architecture (WHEA), which provides support for hardware error reporting and recovery. In this section, the following information is provided:

-   An overview of WHEA and its components. For more information, see [Windows Hardware Error Architecture Overview](windows-hardware-error-architecture-overview.md).

-   How to develop and distribute platform-specific hardware error driver (PSHED) plug-ins. For more information, see [Platform-Specific Hardware Error Driver Plug-Ins](platform-specific-hardware-error-driver-plug-ins2.md).

-   How user-mode applications can communicate with the WHEA platform. For more information, see [Windows Hardware Error Architecture-Aware User-Mode Applications](windows-hardware-error-architecture-aware-user-mode-applications.md).

For more detailed information about WHEA and how to implement WHEA on a hardware platform, see the WHEA Platform Design Guide. Platform vendors can obtain this design guide by sending email to <wheafb@microsoft.com>.

**Note**   WHEA is supported in Windows Vista, Windows Server 2008, and later versions of the Windows operating system. For hardware error reporting that is supported on versions of Microsoft Windows prior to Windows Vista, see [Machine Check Architecture (MCA)](https://msdn.microsoft.com/library/windows/hardware/ff540685).

 

## In this section


This section includes the following topics:

[Introduction to the Windows Hardware Error Architecture](introduction-to-the-windows-hardware-error-architecture.md)

[New Information for Windows Hardware Error Architecture](new-information-for-windows-hardware-error-architecture.md)

[Windows Hardware Error Architecture Definitions](windows-hardware-error-architecture-definitions.md)

[Windows Hardware Error Architecture Overview](windows-hardware-error-architecture-overview.md)

[Platform-Specific Hardware Error Driver Plug-Ins](platform-specific-hardware-error-driver-plug-ins2.md)

[Windows Hardware Error Architecture-Aware User-Mode Applications](windows-hardware-error-architecture-aware-user-mode-applications.md)

[Windows Hardware Error Architecture Debugger Extensions](windows-hardware-error-architecture-debugger-extensions.md)

## Related topics
[Windows Hardware Error Architecture ACPI Table Specification](https://msdn.microsoft.com/windows/hardware/gg463511)  
[Hardware Management and Security](https://msdn.microsoft.com/library/windows/hardware/dn614601)  
[**Bug Check 0x124: WHEA\_UNCORRECTABLE\_ERROR (Windows Debuggers)**](https://msdn.microsoft.com/library/windows/hardware/ff557321)  





