---
title: Fixed ComBuffer and Windows SMM Security Mitigation Table (WSMT)
description: Windows SMM Security Mitigation Table (WSMT) is a static table described in ACPI namespace that contains flags indicating that specific security features have been implemented.
ms.date: 08/18/2021
---

# Fixed ComBuffer and Windows SMM Security Mitigation Table (WSMT)

Windows SMM Security Mitigation Table (WSMT) is a static table described in ACPI namespace that contains flags indicating that specific security features have been implemented on the system.

The Protection Flags field indicates the presence of specific BIOS security mitigations in the systems firmware. Supported versions of the Windows operating system read in the Windows SMM Security Table early during initialization, prior to start of the ACPI interpreter. Windows operating systems may elect to enable, disable, or de-feature certain security features based on the presence of these SMM Protections Flags.

Protection Flags FIXED_COMM_BUFFERS and COMM_BUFFER_NESTED_PTR_PROTECTION depend on the firmware vendor re-designing the System Management Interrupts (SMIs) to only read or write to an "allowed" list of regions that include MMIO and EFI-allocated memory.  It is not sufficient to check that pointers are outside of SMM, they must only be within these "safe" regions.  This prevents SMM from becoming a confused deputy which can bypass Windows flagship "Guard" features. The above-mentioned Protection Flags refer only to input validation and pointer checks and do NOT currently require enforcement via SMM page protections.

Support for the WSMT is included in the following versions of Windows:

- Windows Server Technical Preview 2016

- Windows 10, version 1607

- Windows 10, version 1703

## Related resources

[Windows SMM Security Mitigations Table (WSMT) (DOCX download)](https://download.microsoft.com/download/1/8/A/18A21244-EB67-4538-BAA2-1A54E0E490B6/WSMT.docx)
