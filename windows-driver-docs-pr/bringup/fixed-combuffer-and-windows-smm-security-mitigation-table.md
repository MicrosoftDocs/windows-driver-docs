---
title: Fixed ComBuffer and Windows SMM Security Mitigation Table (WSMT)
description: Fixed ComBuffer and Windows SMM Security Mitigation Table (WSMT)
ms.date: 05/07/2018
ms.localizationpriority: medium
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

[Windows SMM Security Mitigations Table (WSMT)](http://go.microsoft.com/fwlink/p/?LinkId=786943)


