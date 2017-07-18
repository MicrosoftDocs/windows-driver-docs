---
title: ACPI Control Method Macros
description: ACPI Control Method Macros
MS-HAID:
- 'acpi-meth-eval-ref\_1aea644b-d732-4d53-982a-e10c08cf6a69.xml'
- 'acpi.acpi\_control\_method\_macros'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5ac67a45-56ee-4a48-bc42-f6ab789313e9
---

# ACPI Control Method Macros


A driver can use the following macros to set input arguments that are used with the ACPI control method IOCTLs:

[**ACPI\_METHOD\_SET\_ARGUMENT\_INTEGER**](acpi-method-set-argument-integer.md)

[**ACPI\_METHOD\_SET\_ARGUMENT\_STRING**](acpi-method-set-argument-string.md)

[**ACPI\_METHOD\_SET\_ARGUMENT\_BUFFER**](acpi-method-set-argument-buffer.md)

A driver can use the following macros to help process an array of [**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109) structures in an [**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112) structure.

[**ACPI\_ENUM\_CHILD\_NEXT**](acpi-enum-child-next.md)

[**ACPI\_ENUM\_CHILD\_LENGTH\_FROM\_CHILD**](acpi-enum-child-length-from-child.md)

A driver can use the following macros to help process an array of [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structures in an [**ACPI\_EVAL\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536123) structure.

[**ACPI\_METHOD\_ARGUMENT\_LENGTH**](acpi-method-argument-length.md)

[**ACPI\_METHOD\_ARGUMENT\_LENGTH\_FROM\_ARGUMENT**](acpi-method-argument-length-from-argument.md)

[**ACPI\_METHOD\_NEXT\_ARGUMENT**](acpi-method-next-argument.md)

The following macro is reserved for internal use only:

[**ACPI\_MANIPULATE\_LOCK\_BUFFER**](acpi-manipulate-lock-buffer.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20ACPI%20Control%20Method%20Macros%20%20RELEASE:%20%287/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




