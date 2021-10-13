---
title: Secure Boot
description: Secure Boot
ms.date: 08/13/2021
ms.localizationpriority: medium
---

# Secure Boot

Secure Boot is a process to ensure that your PC boots using only software that is trusted by the PC manufacturer. Secure Boot is not exclusive to Microsoft and is defined in UEFI specification documents, though Microsoft does have specific requirements defined in the links included below.

When the PC starts, the firmware checks the signature of each piece of boot software, including firmware drivers (Option ROMs) and the operating system. If the signatures are good, the PC boots, and the firmware gives control to the operating system.

Secure Boot is required for Windows operating systems; Windows 8, 8.1, and 10, and is also part of UEFI Specification docs. See section [27.1 Secure Boot](https://uefi.org/sites/default/files/resources/UEFI_2_3_1_C.pdf) in the UEFI specification document for additional information.

For more information regarding Windows requirements for Secure boot, see **System.Fundamentals.Firmware.UEFISecureBoot** in the **WHCP-Systems-Specification-1607** link below.

## Related resources

[Hardware Security Testability Specification](/windows-hardware/test/hlk/testref/hardware-security-testability-specification)

[Windows Hardware Compatibility Program Specifications and Policies](/windows-hardware/design/compatibility/whcp-specifications-policies)

[WHCP-Systems-Specification-1607 (ZIP download)](https://download.microsoft.com/download/D/3/C/D3CAA04D-0EE6-415B-9E94-FA7BDE37C2B4/WHCP-Documents-1607.zip)

[Secured Boot and Measured Boot: Hardening Early Boot Components Against Malware](/previous-versions/windows/hardware/design/dn653311(v=vs.85))

[Windows 8.1 Secure Boot Key Creation and Management Guidance](/previous-versions/windows/it-pro/windows-8.1-and-8/dn747883(v=win.10))
