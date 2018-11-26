---
title: ACPI_METHOD_SET_ARGUMENT_STRING macro
description: The ACPI_METHOD_SET_ARGUMENT_STRING macro sets the members of an ACPI_METHOD_ARGUMENT structure for a string value.
ms.assetid: e0c037a9-65b6-4d6a-9ed6-d9296c14df07
keywords: 
- ACPI_METHOD_SET_ARGUMENT_STRING macro ACPI Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ACPI\_METHOD\_SET\_ARGUMENT\_STRING macro


The ACPI\_METHOD\_SET\_ARGUMENT\_STRING macro sets the members of an [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure for a string value.

Syntax
------

```cpp
void ACPI_METHOD_SET_ARGUMENT_STRING(
    Argument,
    StrData
);
```

Parameters
----------

*Argument*   
A pointer to an ACPI\_METHOD\_ARGUMENT structure.

*StrData*   
A pointer to a NULL-terminated ASCII string.

Return value
------------

This macro does not return a value.

Remarks
-------

A driver can use this macro to set the members of an ACPI\_METHOD\_ARGUMENT structure that supplies a NULL-terminated ASCII string.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr>
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr>
<td><p>Header</p></td>
<td>Acpiioct.h (include Acpiioct.h)</td>
</tr>
</tbody>
</table>

## See also


[**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) 
