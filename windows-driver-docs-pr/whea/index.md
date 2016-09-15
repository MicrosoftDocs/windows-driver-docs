---
title: Windows Hardware Error Architecture (WHEA) design guide
author: windows-driver-content
description: Windows Hardware Error Architecture (WHEA) design guide
MS-HAID:
- 'whea\_85a09f70-65b3-4897-a74f-92c112271bb7.xml'
- 'whea.design\_guide'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7a42bacd-cafe-48e0-8568-402738fd6e7c
keywords: ["Windows Hardware Error Architecture WDK", "WHEA WDK", "hardware errors WDK WHEA", "errors WDK WHEA", "detecting hardware errors WDK", "reporting hardware errors WDK", "recovering from hardware errors WDK WHEA"]
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
[Windows Hardware Error Architecture ACPI Table Specification](http://msdn.microsoft.com/windows/hardware/gg463511)  
[Hardware Management and Security](https://msdn.microsoft.com/library/windows/hardware/dn614601)  
[**Bug Check 0x124: WHEA\_UNCORRECTABLE\_ERROR (Windows Debuggers)**](https://msdn.microsoft.com/library/windows/hardware/ff557321)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Windows%20Hardware%20Error%20Architecture%20%28WHEA%29%20design%20guide%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


