---
title: Windows Hardware Error Architecture Definitions
description: Windows Hardware Error Architecture Definitions
ms.assetid: 4de5ead1-aa17-4c14-9afc-bc0d9689a13e
keywords:
- Windows Hardware Error Architecture WDK , terminology
- WHEA WDK , terminology
- hardware errors WDK WHEA , terminology
- errors WDK WHEA , terminology
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Hardware Error Architecture Definitions


The following are definitions for terms related to the Windows Hardware Error Architecture (WHEA).

<a href="" id="advanced-configuration-and-power-interface--acpi-"></a>Advanced Configuration and Power Interface (ACPI)  
An industry-standard interface for operating system-directed device configuration and power management. For more information about ACPI, see the [ACPI Specification](http://go.microsoft.com/fwlink/p/?linkid=69483).

<a href="" id="baseboard-management-controller--bmc-"></a>Baseboard Management Controller (BMC)  
A set of hardware components on the motherboard that manages platform-specific functions, such as monitoring and handling certain environmental error conditions.

<a href="" id="corrected-machine-check--cmc-"></a>Corrected Machine Check (CMC)  
An error condition detected by the processor that has been corrected by the hardware or the firmware. A CMC is typically reported to the operating system either by signaling an interrupt or by setting bits in an error register that is periodically polled by the operating system. This is a nonfatal error condition.

<a href="" id="corrected-platform-error--cpe-"></a>Corrected Platform Error (CPE)  
An error condition detected by the platform hardware that has been corrected by the hardware or the firmware. A CPE is typically reported to the operating system either by signaling an interrupt or by setting bits in an error register that is periodically polled by the operating system. This is a nonfatal error condition.

<a href="" id="event-log--el-"></a>Event Log (EL)  
A Windows operating system component that tracks events that occur on system components. WHEA uses the system event log to record hardware error events.

<a href="" id="event-tracing-for-windows--etw-"></a>Event Tracing for Windows (ETW)  
ETW provides software developers the ability to start and stop event tracing sessions, instrument an application to provide trace events, and consume trace events. WHEA uses ETW to notify subscribers about the hardware error events and to record hardware error events in the system event log.

<a href="" id="extensible-firmware-interface--efi-"></a>Extensible Firmware Interface (EFI)  
The next-generation model for the interface between the operating system and the platform firmware. The interface consists of data tables that contain platform-related information, plus boot and runtime service calls that are available to the operating system and its loader. Together, these provide a standard environment for booting an operating system and running pre-boot applications. For more information about EFI, see the [Unified Extensible Firmware Interface (UEFI) Specification](http://go.microsoft.com/fwlink/p/?linkid=69484).

<a href="" id="intelligent-platform-management-interface--ipmi-"></a>Intelligent Platform Management Interface (IPMI)  
An interface that is used to monitor and manage functionality, and that is built into the hardware platform. IPMI is primarily used to monitor the health of the system hardware and to handle environmental error conditions. For more information about IPMI, see the [IPMI Specification](http://go.microsoft.com/fwlink/p/?linkid=69485).

<a href="" id="low-level-hardware-error-handler--llheh-"></a>Low Level Hardware Error Handler (LLHEH)  
The first operating system code that runs in response to a hardware error condition. An LLHEH can be an interrupt handler, exception handler, polling routine, or a callback routine that is called by the system firmware. All LLHEHs report hardware errors to the operating system through a common hardware error reporting function.

<a href="" id="machine-check-abort--mca-"></a>Machine Check Abort (MCA)  
An exception that an Itanium processor reports to the operating system to indicate that a hardware error has occurred.

<a href="" id="machine-check-architecture--mca-"></a>Machine Check Architecture (MCA)  
A hardware and software architecture used to report hardware errors to the operating system.

<a href="" id="machine-check-exception--mce-"></a>Machine Check Exception (MCE)  
An exception that an x86 or x64 processor reports to the operating system to indicate that a hardware error has occurred.

<a href="" id="machine-specific-register--msr-"></a>Machine Specific Register (MSR)  
A processor-specific register that is used by system software to implement certain functions. The operation of each MSR is specific for each processor and/or processor family.

<a href="" id="nonmaskable-interrupt--nmi-"></a>Nonmaskable Interrupt (NMI)  
An interrupt that the processor reports to the operating system regardless of the processor's current interrupt priority level. An NMI is usually signaled when the platform detects a fatal hardware error condition.

<a href="" id="pci-express-advanced-error-reporting--pcie-aer-"></a>PCI Express Advanced Error Reporting (PCIe AER)  
An optional extended capability of PCI Express that provides more robust error reporting than the standard PCI Express error reporting mechanism. For more information about PCIe AER, see the [PCI Express Specification](http://go.microsoft.com/fwlink/p/?linkid=69486).

<a href="" id="platform-specific-hardware-error-driver--pshed-"></a>Platform-Specific Hardware Error Driver (PSHED)  
A WHEA component that provides an abstraction of the hardware error reporting facilities of the underlying platform. Microsoft provides PSHEDs for each processor architecture. Platform vendors can supplement the PSHED functionality by implementing PSHED plug-ins that take advantage of platform-specific capabilities.

<a href="" id="service-control-interrupt--sci-"></a>Service Control Interrupt (SCI)  
An interrupt handled by the ACPI driver. Upon receipt of an SCI, the ACPI driver determines which device signaled the interrupt and then responds to the device accordingly.

<a href="" id="service-processor--sp-"></a>Service Processor (SP)  
A microcontroller, distinct from the main processor(s), which manages platform-specific functions such as monitoring environmental conditions and handling certain error conditions. A service processor is usually a component of the baseboard management controller hardware.

 

 




