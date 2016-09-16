---
title: Hardware Errors and Error Sources
author: windows-driver-content
description: Hardware Errors and Error Sources
MS-HAID:
- 'whea\_f10c4c8e-8024-4612-b617-1240c7edbe81.xml'
- 'whea.hardware\_errors\_and\_error\_sources'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 047e5d6d-a7c6-4c20-bfb2-c1d686ec0b7b
keywords: ["Windows Hardware Error Architecture WDK , hardware errors", "WHEA WDK , hardware errors", "hardware errors WDK WHEA , about hardware errors", "errors WDK WHEA , hardware errors", "Windows Hardware Error Architecture WDK , error sources", "WHEA WDK , error sources", "hardware errors WDK WHEA , error sources", "errors WDK WHEA , error sources", "corrected errors WDK WHEA", "uncorrected errors WDK WHEA", "error sources WDK WHEA", "fatal hardware errors WDK WHEA", "non-fatal hardware errors WDK WHEA", "hardware error sources WDK WHEA"]
---

# Hardware Errors and Error Sources


A *hardware error* is a malfunction of a hardware component in a computer system. The hardware components contain error detection mechanisms that can detect when a hardware error condition exists. Hardware errors can be classified as either *corrected errors*, or *uncorrected errors*.

-   A corrected error is a hardware error condition that has been corrected by the hardware or the firmware by the time that the operating system is notified about the presence of the error condition.

-   An uncorrected error is a hardware error condition that cannot be corrected by the hardware or the firmware. Uncorrected errors are classified as either *fatal* or *nonfatal*.
    -   A fatal hardware error is an uncorrected or uncontained error condition that is determined to be unrecoverable by the hardware. When a fatal uncorrected error occurs, the operating system generates a bug check to contain the error.
    -   A nonfatal hardware error is an uncorrected error condition from which the operating system can attempt recovery by trying to correct the error. If the operating system cannot correct the error, it generates a bug check to contain the error.

The notion of a hardware *error source* is a fundamental concept of the Windows Hardware Error Architecture (WHEA). A hardware error source is any hardware unit that alerts the operating system to the presence of an error condition. Examples of hardware error sources include the following:

-   Processor machine check exception (for example, MC#)

-   Chipset error signals (for example, SCI, SMI, SERR\#, MCERR\#)

-   I/O bus error reporting (for example, PCI Express root port error interrupt)

-   I/O device errors

A single hardware error source might handle the error reporting for more than one type of hardware error condition. For example, a processor's machine check exception typically reports processor errors, cache and memory errors, and system bus errors.

**Note**   The system management interrupt (SMI) is handled by the firmware, not by the operating system.

 

A hardware error source is typically represented by the following:

-   One or more hardware error status registers

-   One or more hardware error configuration or control registers

-   A signaling mechanism to alert the operating system that a hardware error condition exists

In some situations, there is not an explicit signaling mechanism and the operating system must poll the error status registers to test for an error condition. However, polling can only be used for corrected error conditions because uncorrected errors require immediate attention by the operating system.

Starting with Windows Vista, the operating system maintains a list of all of the hardware error sources that can be discovered on a particular hardware platform. WHEA uses a discovery mechanism when the operating system starts to determine which of these hardware error sources exist on a particular system. The means by which this information is exposed to the operating system is platform-specific. The operating system collects this information from a combination of ACPI tables, firmware interactions, and other platform-specific mechanisms.

**Note**   Windows Vista does not collect hardware error source information from ACPI tables. However, starting with Windows Server 2008 and Windows Vista SP1, the operating system uses ACPI tables to collect hardware error source information.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Hardware%20Errors%20and%20Error%20Sources%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


