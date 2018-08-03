---
title: ACPI_METHOD_ARGUMENT_LENGTH macro
author: windows-driver-content
description: The ACPI_METHOD_ARGUMENT_LENGTH macro calculates the size, in bytes, of a variable-length ACPI_METHOD_ARGUMENT structure that contains data of a specified size, in bytes.
ms.assetid: 8329c2eb-a787-4590-8de9-95078bbb85da
keywords: 
- ACPI_METHOD_ARGUMENT_LENGTH macro ACPI Devices
ms.author: windowsdriverdev
ms.date: 07/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ACPI\_METHOD\_ARGUMENT\_LENGTH macro


The ACPI\_METHOD\_ARGUMENT\_LENGTH macro calculates the size, in bytes, of a variable-length [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure that contains data of a specified size, in bytes.

Syntax
------

```ManagedCPlusPlus
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

 

 




