---
title: ACPI_METHOD_SET_ARGUMENT_INTEGER macro
author: windows-driver-content
description: The ACPI_METHOD_SET_ARGUMENT_INTEGER macro sets the members of an ACPI_METHOD_ARGUMENT structure for a single integer value.
ms.assetid: a79f9149-0ffe-483f-a45e-427b05ff0a11
keywords: 
- ACPI_METHOD_SET_ARGUMENT_INTEGER macro ACPI Devices
ms.author: windowsdriverdev
ms.date: 07/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ACPI\_METHOD\_SET\_ARGUMENT\_INTEGER macro


The ACPI\_METHOD\_SET\_ARGUMENT\_INTEGER macro sets the members of an [**ACPI\_METHOD\_ARGUMENT**](https://msdn.microsoft.com/library/windows/hardware/ff536125) structure for a single integer value.

Syntax
------

```ManagedCPlusPlus
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

 

 




