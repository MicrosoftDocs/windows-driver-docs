---
title: ACPI_ENUM_CHILD_NEXT macro
description: The ACPI_ENUM_CHILD_NEXT macro calculates a pointer to the next ACPI_ENUM_CHILD structure in an array of variable length ACPI_ENUM_CHILD structures.
ms.assetid: 1ff37770-b0ea-4275-9568-611ec125a0b6
keywords: 
- ACPI_ENUM_CHILD_NEXT macro ACPI Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ACPI\_ENUM\_CHILD\_NEXT macro


The ACPI\_ENUM\_CHILD\_NEXT macro calculates a pointer to the next [**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109) structure in an array of variable length ACPI\_ENUM\_CHILD structures.

Syntax
------

```cpp
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


[**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109)

[**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112)

[**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147)

 

 




