---
title: ACPI\_ENUM\_CHILD\_NEXT macro
description: The ACPI\_ENUM\_CHILD\_NEXT macro calculates a pointer to the next ACPI\_ENUM\_CHILD structure in an array of variable length ACPI\_ENUM\_CHILD structures.
MS-HAID:
- 'acpi-meth-eval-ref\_4dae4b10-50af-4378-b9bf-4eb092128861.xml'
- 'acpi.acpi\_enum\_child\_next'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1ff37770-b0ea-4275-9568-611ec125a0b6
keywords: ["ACPI_ENUM_CHILD_NEXT macro ACPI Devices"]
topic_type:
- apiref
api_name:
- ACPI_ENUM_CHILD_NEXT
api_location:
- Acpiioct.h
api_type:
- HeaderDef
---

# ACPI\_ENUM\_CHILD\_NEXT macro


The ACPI\_ENUM\_CHILD\_NEXT macro calculates a pointer to the next [**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109) structure in an array of variable length ACPI\_ENUM\_CHILD structures.

Syntax
------

```ManagedCPlusPlus
void ACPI_ENUM_CHILD_NEXT(
    Child
);
```

Parameters
----------

*Child*   
A pointer to a variable of type ACPI\_ENUM\_CHILD for which to return a nonaligned pointer to the next ACPI\_ENUM\_CHILD structure in an array of variable-length ACPI\_ENUM\_CHILD structures.

Return value
------------

A pointer to the next ACPI\_ENUM\_CHILD structure in an array of variable-length ACPI\_ENUM\_CHILD structures.

Remarks
-------

After a driver uses an [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request to retrieve an array of child device names in an [**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112) request, the driver can use this macro to determine a sequence of pointers to the variable-length ACPI\_ENUM\_CHILD structures in the **Children** array that the output buffer contains.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Acpiioct.h (include Acpiioct.h)</td>
</tr>
</tbody>
</table>

## See also


[**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109)

[**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112)

[**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20ACPI_ENUM_CHILD_NEXT%20macro%20%20RELEASE:%20%287/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





