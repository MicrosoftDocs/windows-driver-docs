---
title: ACPI_METHOD_ARGUMENT_LENGTH_FROM_ARGUMENT macro
author: windows-driver-content
description: The ACPI_METHOD_ARGUMENT_LENGTH_FROM_ARGUMENT macro calculates the size, in bytes, of the data that is contained in the Data array of an ACPI_METHOD_ARGUMENT structure.
ms.assetid: 46fe0382-1496-49eb-988d-2007885d2210
keywords: 
- ACPI_METHOD_ARGUMENT_LENGTH_FROM_ARGUMENT macro ACPI Devices
ms.author: windowsdriverdev
ms.date: 07/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ACPI\_METHOD\_ARGUMENT\_LENGTH\_FROM\_ARGUMENT macro


The ACPI\_METHOD\_ARGUMENT\_LENGTH\_FROM\_ARGUMENT macro calculates the size, in bytes, of the data that is contained in the Data array of an [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure.

Syntax
------

```ManagedCPlusPlus
void ACPI_METHOD_ARGUMENT_LENGTH_FROM_ARGUMENT(
    Argument
);
```

Parameters
----------

*Argument*   
A pointer to an ACPI\_METHOD\_ARGUMENT structure.

Return value
------------

The size, in bytes, of the data that is contained in the **Data** array of the ACPI\_METHOD\_ARGUMENT structure that *Argument* points to.

Remarks
-------

A driver can use this macro to determine the size, in bytes, of the data in the **Data** array of an ACPI\_METHOD\_ARGUMENT structure.

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

 

 




