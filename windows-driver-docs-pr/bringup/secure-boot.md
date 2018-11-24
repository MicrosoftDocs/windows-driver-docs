---
title: Secure Boot
description: Secure Boot
ms.date: 08/06/2018
ms.localizationpriority: medium
---


# Secure Boot


Secure Boot is a process to ensure that your PC boots using only software that is trusted by the PC manufacturer. Secure Boot is not exclusive to Microsoft and is defined in UEFI specification documents, though Microsoft does have specific requirements defined in the links included below.

When the PC starts, the firmware checks the signature of each piece of boot software, including firmware drivers (Option ROMs) and the operating system. If the signatures are good, the PC boots, and the firmware gives control to the operating system.

Secure Boot is required for Windows operating systems; Windows 8, 8.1, and 10, and is also part of UEFI Specification docs. See section [27.1 Secure Boot](https://www.uefi.org/sites/default/files/resources/UEFI_2_3_1_C.pdf) in the UEFI specification document for additional information.

For more information regarding Windows requirements for Secure boot, see **System.Fundamentals.Firmware.UEFISecureBoot** in the **WHCP-Systems-Specification-1607** link below.

## Related resources

[Hardware Security Testability Specification](https://docs.microsoft.com/windows-hardware/test/hlk/testref/hardware-security-testability-specification)

[Windows Hardware Compatibility Program Specifications and Policies](https://docs.microsoft.com/windows-hardware/design/compatibility/whcp-specifications-policies)

[WHCP-Systems-Specification-1607](https://go.microsoft.com/fwlink/?linkid=866948)

[Secured Boot and Measured Boot: Hardening Early Boot Components Against Malware](https://msdn.microsoft.com/library/windows/hardware/dn653311)

[Windows 8.1 Secure Boot Key Creation and Management Guidance](https://technet.microsoft.com/library/dn747883)



