---
title: ACPI_METHOD_SET_ARGUMENT_INTEGER macro
description: The ACPI_METHOD_SET_ARGUMENT_INTEGER macro sets the members of an ACPI_METHOD_ARGUMENT structure for a single integer value.
ms.assetid: a79f9149-0ffe-483f-a45e-427b05ff0a11
keywords: 
- ACPI_METHOD_SET_ARGUMENT_INTEGER macro ACPI Devices
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# ACPI\_METHOD\_SET\_ARGUMENT\_INTEGER macro


The ACPI\_METHOD\_SET\_ARGUMENT\_INTEGER macro sets the members of an [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure for a single integer value.

Syntax
------

```cpp
void ACPI_METHOD_SET_ARGUMENT_INTEGER(
    MethodArgument,
    IntData
);
```

Parameters
----------

*MethodArgument*   
A pointer to an ACPI\_METHOD\_ARGUMENT structure.

*IntData*   
An integer value of type ULONG.

Return value
------------

This macro does not return a value.

Remarks
-------

A driver can use this macro to set the members of an ACPI\_METHOD\_ARGUMENT structure that supplies a single integer value of type ULONG.

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
