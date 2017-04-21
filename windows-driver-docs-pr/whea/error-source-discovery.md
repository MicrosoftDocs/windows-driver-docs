---
title: Error Source Discovery
author: windows-driver-content
description: Error Source Discovery
ms.assetid: 58b7501d-b51a-436f-ac29-8d03161d0956
keywords:
- Windows Hardware Error Architecture WDK , error source discovery
- WHEA WDK , error source discovery
- hardware errors WDK WHEA , error source discovery
- errors WDK WHEA , error source discovery
- platform-specific hardware error driver plug-ins WDK WHEA , error source discovery
- PSHED plug-ins WDK WHEA , error source discovery
- error source discovery WDK WHEA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Error Source Discovery


During initialization of the operating system, the Windows kernel queries the PSHED for a list of all of the [error sources](hardware-errors-and-error-sources.md) that are implemented by the hardware platform. The PSHED returns a list of [**WHEA\_ERROR\_SOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff560505) structures that describe each of the error sources that the hardware platform supports. The operating system uses this information to enable the necessary low-level hardware error handlers (LLHEHs) that are responsible for processing error notifications from the hardware platform.

The following is the minimum set of error sources that is discovered by the PSHED.

<a href="" id="x86-based-and-x64-based-hardware-platforms"></a>**x86-based and x64-based hardware platforms**  
-   Machine Check Exception (MCE)

-   Corrected Machine Check (CMC)

-   Nonmaskable Interrupt (NMI)

-   BOOT Errors

<a href="" id="itanium-based-hardware-platforms"></a>**Itanium-based hardware platforms**  
-   Machine Check Abort (MCA)

-   Corrected Machine Check (CMC)

-   Corrected Platform Error (CPE)

-   INIT Errors

For PCI Express (PCIe) advanced error reporting (AER), the PCI bus driver discovers the error sources instead of the PSHED. Therefore, the PSHED does not include any PCIe AER error sources in the initial list of error sources that it returns to the Windows kernel. Instead, the PCI bus driver reports these error sources to the operating system. When such an error source is reported to the operating system, the Windows kernel calls into the PSHED to allow the PSHED to provide any additional details about the error source.

A PSHED plug-in can also participate in error source discovery to modify the error source information that is reported by the PSHED and to report additional error sources that were not discovered by the PSHED. If a PSHED plug-in is implemented that participates in error source discovery and reports additional error sources to the operating system that the PSHED does not support, the PSHED plug-in must also participate in [error source control](error-source-control.md) and [error information retrieval](error-information-retrieval.md) to support the error source control and error information retrieval operations for these additional error sources. For more information about how to implement a PSHED plug-in that participates in error source discovery, see [Participating in Error Source Discovery](participating-in-error-source-discovery.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Error%20Source%20Discovery%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


