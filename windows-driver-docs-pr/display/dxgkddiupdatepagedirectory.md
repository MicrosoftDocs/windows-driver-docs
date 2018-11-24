---
title: DxgkDdiUpdatePageDirectory function
description: The DxgkDdiUpdatePageDirectory function is reserved for system use. Do not implement it in your driver.
ms.assetid: 91f81165-a63c-44bb-8898-9cc85c2a6e45
keywords: ["DxgkDdiUpdatePageDirectory function Display Devices"]
topic_type:
- apiref
api_name:
- DxgkDdiUpdatePageDirectory
api_location:
- Dispmprt.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DxgkDdiUpdatePageDirectory function


\[Reserved for system use.\]

The *DxgkDdiUpdatePageDirectory* function is reserved for system use. Do not implement it in your driver.

Syntax
------

```ManagedCPlusPlus
NTSTATUS APIENTRY DxgkDdiUpdatePageDirectory(
   IN_CONST_HANDLE                    hDevice,
   INOUT_PDXGKARG_UPDATEPAGEDIRECTORY pUpdatePageDirectory
);
```

Parameters
----------

*hDevice*
This parameter is reserved for system use.

*pUpdatePageDirectory*
This parameter is reserved for system use.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Dispmprt.h (include Dispmprt.h)</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





