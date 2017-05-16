---
title: Secure Boot
description: Secure Boot
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Secure Boot


Secure Boot is a security standard developed by members of the PC industry to help make sure that your PC boots using only software that is trusted by the PC manufacturer.

When the PC starts, the firmware checks the signature of each piece of boot software, including firmware drivers (Option ROMs) and the operating system. If the signatures are good, the PC boots, and the firmware gives control to the operating system.

Secure Boot is required for Windows operating systems; Windows 8, 8.1, and 10, and is also part of UEFI Specification docs. See section [27.1 Secure Boot](http://www.uefi.org/sites/default/files/resources/UEFI_2_3_1_C.pdf) in the UEFI specification document for additional information.

For more information regarding Windows requirements for Secure boot, see **System.Fundamentals.Firmware.UEFISecureBoot** in the **Hardware Compatibility Specification for Systems for Windows 10, version 1607** topic link below.

## Related resources

[Hardware Security Testability Specification](https://msdn.microsoft.com/en-us/library/windows/hardware/mt712332)                                         |

[Hardware Compatibility Specification for Systems for Windows 10, version 1607](https://msdn.microsoft.com/en-us/windows/hardware/commercialize/design/compatibility/systems) 

[Secured Boot and Measured Boot: Hardening Early Boot Components Against Malware](https://msdn.microsoft.com/en-us/library/windows/hardware/dn653311)           

[Windows 8.1 Secure Boot Key Creation and Management Guidance](https://technet.microsoft.com/en-us/library/dn747883)          



--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


