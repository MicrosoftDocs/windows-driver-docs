---
title: Secure Boot
description: Secure Boot
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/07/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Secure Boot


Secure Boot is a process to ensure that your PC boots using only software that is trusted by the PC manufacturer. Secure Boot is not exclusive to Microsoft and is defined in UEFI specification documents, though Microsoft does have specific requirements defined in the links included below. 

When the PC starts, the firmware checks the signature of each piece of boot software, including firmware drivers (Option ROMs) and the operating system. If the signatures are good, the PC boots, and the firmware gives control to the operating system.

Secure Boot is required for Windows operating systems; Windows 8, 8.1, and 10, and is also part of UEFI Specification docs. See section [27.1 Secure Boot](http://www.uefi.org/sites/default/files/resources/UEFI_2_3_1_C.pdf) in the UEFI specification document for additional information.

For more information regarding Windows requirements for Secure boot, see **System.Fundamentals.Firmware.UEFISecureBoot** in the **Hardware Compatibility Specification for Systems for Windows 10, version 1607** topic link below.

## Related resources

[Hardware Security Testability Specification](https://msdn.microsoft.com/en-us/library/windows/hardware/mt712332)                                         |

[Hardware Compatibility Specification for Systems for Windows 10, version 1607](https://msdn.microsoft.com/en-us/windows/hardware/commercialize/design/compatibility/systems) 

[Secured Boot and Measured Boot: Hardening Early Boot Components Against Malware](https://msdn.microsoft.com/en-us/library/windows/hardware/dn653311)           

[Windows 8.1 Secure Boot Key Creation and Management Guidance](https://technet.microsoft.com/en-us/library/dn747883)          



