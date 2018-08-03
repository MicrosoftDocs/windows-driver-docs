---
title: ACPI_METHOD_SET_ARGUMENT_BUFFER macro
author: windows-driver-content
description: The ACPI_METHOD_SET_ARGUMENT_BUFFER macro sets the members of an ACPI_METHOD_ARGUMENT structure for custom data that is supplied in a data buffer.
ms.assetid: 1f335814-fa9f-45c6-b970-10884e971ec1
keywords: 
- ACPI_METHOD_SET_ARGUMENT_BUFFER macro ACPI Devices
ms.author: windowsdriverdev
ms.date: 07/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ACPI\_METHOD\_SET\_ARGUMENT\_BUFFER macro


The ACPI\_METHOD\_SET\_ARGUMENT\_BUFFER macro sets the members of an [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure for custom data that is supplied in a data buffer.

Syntax
------

```ManagedCPlusPlus
void ACPI_METHOD_SET_ARGUMENT_BUFFER(
    Argument,
    BuffData,
    BuffLength
);
```

Parameters
----------

*Argument*   
A pointer to an ACPI\_METHOD\_ARGUMENT structure.

*BuffData*   
A pointer to a data buffer that contains custom data.

*BuffLength*   
The size, in bytes, of the custom data.

Return value
------------

This macro does not return a value.

Remarks
-------

A driver can use this macro to set the members of an ACPI\_METHOD\_ARGUMENT structure that supplies custom data.

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

 

 




