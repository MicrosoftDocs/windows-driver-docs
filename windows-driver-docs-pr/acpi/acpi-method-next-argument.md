---
title: ACPI\_METHOD\_NEXT\_ARGUMENT macro
description: The ACPI\_METHOD\_NEXT\_ARGUMENT structure returns a pointer to the next ACPI\_METHOD\_ARGUMENT structure in an array of ACPI\_METHOD\_ARGUMENT structures.
MS-HAID:
- 'acpi-meth-eval-ref\_5b098ba4-dfab-4796-bdfb-ad5335f173c1.xml'
- 'acpi.acpi\_method\_next\_argument'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c723b11b-1657-4a78-a6a1-26bd916604a4
keywords: ["ACPI_METHOD_NEXT_ARGUMENT macro ACPI Devices"]
topic_type:
- apiref
api_name:
- ACPI_METHOD_NEXT_ARGUMENT
api_location:
- Acpiioct.h
api_type:
- HeaderDef
---

# ACPI\_METHOD\_NEXT\_ARGUMENT macro


The ACPI\_METHOD\_NEXT\_ARGUMENT structure returns a pointer to the next [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure in an array of ACPI\_METHOD\_ARGUMENT structures.

Syntax
------

```ManagedCPlusPlus
 ACPI_METHOD_NEXT_ARGUMENT(
    Argument
);
```

Parameters
----------

*Argument*   
A pointer to an ACPI\_METHOD\_ARGUMENT structure in an array of ACPI\_METHOD\_ARGUMENT structures.

Return value
------------

A pointer to the next ACPI\_METHOD\_ARGUMENT structure in an array of ACPI\_METHOD\_ARGUMENT structures.

Remarks
-------

Given a pointer to an ACPI\_METHOD\_ARGUMENT structure in an array of such structures, a driver can use this macro to calculate a pointer to the next structure in the array, if one exists.

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
<td><p>Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Acpiioct.h (include Acpiioct.h)</td>
</tr>
</tbody>
</table>

## See also


[**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20ACPI_METHOD_NEXT_ARGUMENT%20macro%20%20RELEASE:%20%287/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





