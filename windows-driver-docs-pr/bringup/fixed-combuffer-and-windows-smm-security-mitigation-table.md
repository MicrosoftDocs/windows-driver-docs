---
title: Fixed ComBuffer and Windows SMM Security Mitigation Table (WSMT)
description: Fixed ComBuffer and Windows SMM Security Mitigation Table (WSMT)
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---



# Fixed ComBuffer and Windows SMM Security Mitigation Table (WSMT)


Windows SMM Security Mitigation Table (WSMT) is a static table described in ACPI namespace that contains flags indicating that specific security features have been implemented on the system.

The Protection Flags field indicates the presence of specific BIOS security mitigations in the systems firmware. Supported versions of the Windows operating system read in the Windows SMM Security Table early during initialization, prior to start of the ACPI interpreter. Windows operating systems may elect to enable, disable, or de-feature certain security features based on the presence of these SMM Protections Flags.

Protection Flags FIXED\_COMM\_BUFFERS and COMM\_BUFFER\_NESTED\_PTR\_PROTECTION depend on the firmware vendor re-designing the System Management Interrupts (SMIs) to only read or write to an "allowed" list of regions that include MMIO and EFI-allocated memory.  It is not sufficient to check that pointers are outside of SMM, they must only be within these "safe" regions.  This prevents SMM from becoming a confused deputy which can bypass Windows flagship "Guard" features. The above-mentioned Protection Flags refer only to input validation and pointer checks and do NOT currently require enforcement via SMM page protections.

Support for the WSMT is included in the following versions of Windows:

-   Windows Server Technical Preview 2016

-   Windows 10, version 1607

-   Windows 10, version 1703

## Related resources

[Windows SMM Security Mitigations Table (WSMT)](http://www.microsoft.com/whdc/system/platform/virtual) 




--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


