---
title: Error Source Discovery
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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




