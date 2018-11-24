---
title: Control Method Macros
description: Control Method Macros
ms.assetid: cffcfb7a-c949-4bc9-a92f-349f5637ab84
keywords:
- ACPI control methods WDK , macros
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control Method Macros


A driver can use the following macros to set input arguments that are used with the ACPI IOCTLs that [evaluate control methods](evaluating-acpi-control-methods.md):

[**ACPI\_METHOD\_SET\_ARGUMENT\_INTEGER**](acpi-method-set-argument-integer.md)

[**ACPI\_METHOD\_SET\_ARGUMENT\_STRING**](acpi-method-set-argument-string.md)

[**ACPI\_METHOD\_SET\_ARGUMENT\_BUFFER**](acpi-method-set-argument-buffer.md)

The ACPI IOCTLs that evaluate control methods return output arguments in the **Argument** member of an [**ACPI\_EVAL\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536123) structure, where the **Argument** member is an array of [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structures. A driver can use the following macros to help process an array of ACPI\_METHOD\_ARGUMENT structures:

[**ACPI\_METHOD\_ARGUMENT\_LENGTH**](acpi-method-argument-length.md)

[**ACPI\_METHOD\_ARGUMENT\_LENGTH\_FROM\_ARGUMENT**](acpi-method-argument-length-from-argument.md)

[**ACPI\_METHOD\_NEXT\_ARGUMENT**](acpi-method-next-argument.md)

An [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request retrieves the path and name of child objects in the namespace of the device to which the request is sent. The ACPI driver returns the full path and name of the enumerated object beginning with the root of the ACPI namespace. The path and name of the child objects are returned in the **Children** member of an [**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112) structure, where the **Children** member is an array of [**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109) structures. A driver can use the following macros to help process an array of ACPI\_ENUM\_CHILD structures:

[**ACPI\_ENUM\_CHILD\_NEXT**](acpi-enum-child-next.md)

[**ACPI\_ENUM\_CHILD\_LENGTH\_FROM\_CHILD**](acpi-enum-child-length-from-child.md)

 

 




