---
title: ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro
author: windows-driver-content
description: The ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro calculates the size, in bytes, of a variable-length ACPI_ENUM_CHILD structure.
ms.assetid: 62be7cb5-4b71-4b8e-bad5-807623cd812a
keywords: 
- ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro ACPI Devices
ms.author: windowsdriverdev
ms.date: 07/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ACPI\_ENUM\_CHILD\_LENGTH\_FROM\_CHILD macro


The ACPI\_ENUM\_CHILD\_LENGTH\_FROM\_CHILD macro calculates the size, in bytes, of a variable-length [**ACPI\_ENUM\_CHILD**](https://msdn.microsoft.com/library/windows/hardware/ff536109) structure.

Syntax
------

```ManagedCPlusPlus
void ACPI_ENUM_CHILD_LENGTH_FROM_CHILD(
    Child
);
```

Parameters
----------

*Child*   
A pointer to a structure of type ACPI\_ENUM\_CHILD for which to calculate the size, in bytes, of the structure.

Return value
------------

The size, in bytes, of the ACPI\_ENUM\_CHILD structure that *Child* points to.

Remarks
-------

A driver can use this macro to calculate the size, in bytes, of the ACPI\_ENUM\_CHILD structures in an [**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff536112) structure.

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

 

 




