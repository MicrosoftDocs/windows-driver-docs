---
title: Control Method Macros
description: Control Method Macros
MS-HAID:
- 'acpi-meth-eval-dg\_69965f04-c94a-462f-970e-f91257f614a3.xml'
- 'acpi.control\_method\_macros'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cffcfb7a-c949-4bc9-a92f-349f5637ab84
keywords: ["ACPI control methods WDK , macros"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Control%20Method%20Macros%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




