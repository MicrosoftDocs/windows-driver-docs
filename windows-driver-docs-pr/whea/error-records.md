---
title: Error Records
description: Error Records
ms.assetid: 080da29a-b5cb-45a5-848d-048d9612ee2a
keywords:
- Windows Hardware Error Architecture WDK , error records
- WHEA WDK , error records
- errors WDK WHEA , error records
- error records WDK WHEA
- error record format WDK WHEA
- error record header WDK WHEA
- error record section WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Records


The Windows Hardware Error Architecture (WHEA) uses a standard error record format to represent all platform hardware errors. As a result, the system firmware, the Windows operating system, and user-mode applications can design hardware error reporting and recovery mechanisms that are all based on the same error record format.

The format of the error records that are used by WHEA are based on the *Common Platform Error Record* as described in Appendix N of version 2.2 of the [Unified Extensible Firmware Interface (UEFI) Specification](http://go.microsoft.com/fwlink/p/?linkid=69484).

The following diagram shows the general format of an error record.

![diagram illustrating the general format of an error record](images/whearecord.png)

An error record consists of an error record header followed by one or more fixed-length error record section descriptors. For each error record section descriptor there is an associated variable-length error record section that contains either error data or informational data. An error record must contain at least one error record section.

An error record can include extra buffer space for the dynamic addition of error record sections and section descriptors. The extra buffer space can also be used to dynamically increase the size of existing error record sections.

An error record is described by a [**WHEA\_ERROR\_RECORD**](https://msdn.microsoft.com/library/windows/hardware/ff560483) structure, the error record header is described by a [**WHEA\_ERROR\_RECORD\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff560487) structure, and the error record section descriptors are each described by a [**WHEA\_ERROR\_RECORD\_SECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff560496) structure.

Each error record section can be one of the following section types:

<a href="" id="hardware-error-packet"></a>Hardware Error Packet  
This error record section contains the hardware error packet that was passed to the operating system by the low-level hardware error handler (LLHEH) that reported the error. The data that is contained in this section is described by the [WHEA\_ERROR\_PACKET](https://msdn.microsoft.com/library/windows/hardware/ff560465) structure.

<a href="" id="generic-processor-error"></a>Generic Processor Error  
This error record section contains processor error data that is not specific to a particular processor architecture. The data that is contained in this section is described by the [**WHEA\_PROCESSOR\_GENERIC\_ERROR\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff560607) structure.

<a href="" id="x86-x64-processor-error"></a>x86/x64 Processor Error  
This error record section contains processor error data that is specific to the x86 or x64 processor architecture. The data that is contained in this section is described by the [**WHEA\_XPF\_PROCESSOR\_ERROR\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff560655) structure. The following diagram shows how the data structures that contain the processor error data are stored in the VariableInfo member. 

![Processor error data](images/wheaxpfsection.gif)

<a href="" id="itanium-processor-error"></a>Itanium Processor Error  
This error record section contains processor error data that is specific to the Itanium processor architecture. For more information about the format of the error data that is contained in this error record section, see the [Intel Itanium Processor Family System Abstraction Layer Specification](http://go.microsoft.com/fwlink/p/?linkid=72212).

<a href="" id="itanium-processor-firmware-error-record-reference"></a>Itanium Processor Firmware Error Record Reference  
This error record section contains a reference to a firmware error record that is specific to the Itanium processor architecture. This error record section is described by a [**WHEA\_FIRMWARE\_ERROR\_RECORD\_REFERENCE**](https://msdn.microsoft.com/library/windows/hardware/ff560520) structure.

<a href="" id="platform-memory-error"></a>Platform Memory Error  
This error record section contains platform memory error data. The data that is contained in this section is described by the [**WHEA\_MEMORY\_ERROR\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff560565) structure.

<a href="" id="nonmaskable-interrupt"></a>Nonmaskable Interrupt  
This error record section contains nonmaskable interrupt (NMI) data. The data that is contained in this section is described by the [**WHEA\_NMI\_ERROR\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff560571) structure.

<a href="" id="pci-express-error"></a>PCI Express Error  
This error record section contains PCI Express error data. The data that is contained in this section is described by the [**WHEA\_PCIEXPRESS\_ERROR\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff560576) structure.

<a href="" id="pci-pci-x-bus-error"></a>PCI/PCI-X Bus Error  
This error record section contains PCI/PCI-X bus error data. The data that is contained in this section is described by the [**WHEA\_PCIXBUS\_ERROR\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff560583) structure.

<a href="" id="pci-pci-x-device-error"></a>PCI/PCI-X Device Error  
This error record section contains PCI/PCI-X device error data. The data that is contained in this section is described by the [**WHEA\_PCIXDEVICE\_ERROR\_SECTION**](https://msdn.microsoft.com/library/windows/hardware/ff560589) structure.

For additional hardware error data that does not fit into one of the section types in the previous list, a platform-specific error record section can be defined to contain the data. For each type of platform-specific error record section that is defined, a corresponding GUID that identifies the type of the error record section must be defined. This GUID is specified in the **SectionType** member of any [**WHEA\_ERROR\_RECORD\_SECTION\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff560496) structure that describes that type of error record section.

If there is additional hardware error data that does not fit into one of the section types in the previous list or into a defined platform-specific error record section, a generic error record section is used to contain the data.

 

 




