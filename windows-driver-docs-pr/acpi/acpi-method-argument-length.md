---
title: ACPI_METHOD_ARGUMENT_LENGTH macro
description: The ACPI_METHOD_ARGUMENT_LENGTH macro calculates the size, in bytes, of a variable-length ACPI_METHOD_ARGUMENT structure that contains data of a specified size, in bytes.
ms.assetid: 8329c2eb-a787-4590-8de9-95078bbb85da
keywords: 
- ACPI_METHOD_ARGUMENT_LENGTH macro ACPI Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ACPI\_METHOD\_ARGUMENT\_LENGTH macro


The ACPI\_METHOD\_ARGUMENT\_LENGTH macro calculates the size, in bytes, of a variable-length [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure that contains data of a specified size, in bytes.

Syntax
------

```cpp
void ACPI_METHOD_ARGUMENT_LENGTH(
    DataLength
);
```

Parameters
----------

*DataLength*   
The size, in bytes, of data in the **Data** array of an ACPI\_METHOD\_ARGUMENT structure.

Return value
------------

The size, in bytes, of a variable-length ACPI\_METHOD\_ARGUMENT structure that can contains a **Data** array whose size, in bytes, is *DataLength*.

Remarks
-------

A driver can use this macro to calculate the required size, in bytes, of a variable-length ACPI\_METHOD\_ARGUMENT structure that can contain a **Data** array of a specified size, in bytes.

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

 

 




