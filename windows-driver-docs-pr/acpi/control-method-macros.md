---
title: Control Method Macros
author: windows-driver-content
description: Control Method Macros
ms.assetid: cffcfb7a-c949-4bc9-a92f-349f5637ab84
keywords:
- ACPI control methods WDK , macros
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Control Method Macros


A driver can use the following macros to set input arguments that are used with the ACPI IOCTLs that [evaluate control methods](evaluating-acpi-control-methods.md):

[**ACPI\_METHOD\_SET\_ARGUMENT\_INTEGER**](https://msdn.microsoft.com/library/windows/hardware/ff536130)

[**ACPI\_METHOD\_SET\_ARGUMENT\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff536131)

[**ACPI\_METHOD\_SET\_ARGUMENT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536129)

The ACPI IOCTLs that evaluate control methods return output arguments in the **Argument** member of an [**ACPI\_EVAL\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536123) structure, where the **Argument** member is an array of [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structures. A driver can use the following macros to help process an array of ACPI\_METHOD\_ARGUMENT structures:

[**ACPI\_METHOD\_ARGUMENT\_LENGTH**](https://msdn.microsoft.com/library/windows/hardware/ff536126)

[**ACPI\_METHOD\_ARGUMENT\_LENGTH\_FROM\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536127)

[**ACPI\_METHOD\_NEXT\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536128)

An [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request retrieves the path and name of child objects in the namespace of the device to which the request is sent. The ACPI driver returns the full path and name of the enumerated object beginning with the root of the ACPI namespace. The path and name of the child objects are returned in the **Children** member of an [**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112) structure, where the **Children** member is an array of [**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109) structures. A driver can use the following macros to help process an array of ACPI\_ENUM\_CHILD structures:

[**ACPI\_ENUM\_CHILD\_NEXT**](https://msdn.microsoft.com/library/windows/hardware/ff536114)

[**ACPI\_ENUM\_CHILD\_LENGTH\_FROM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536113)

 

 


--------------------


