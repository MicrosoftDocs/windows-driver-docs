---
title: DXGKDDI_UPDATEPAGETABLE Callback Function
description: The DxgkDdiUpdatePageTable function is reserved for system use. Do not implement it in your driver.
keywords: ["DxgkDdiUpdatePageTable callback function Display Devices", "DXGKDDI_UPDATEPAGETABLE"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DxgkDdiUpdatePageTable
api_location:
- Dispmprt.h
api_type:
- UserDefined
ms.date: 01/05/2018
---

# DXGKDDI\_UPDATEPAGETABLE callback function


\[Reserved for system use.\]

The *DxgkDdiUpdatePageTable* function is reserved for system use. Do not implement it in your driver.

## Syntax

```ManagedCPlusPlus
DXGKDDI_UPDATEPAGETABLE DxgkDdiUpdatePageTable;

NTSTATUS DxgkDdiUpdatePageTable(
   IN_CONST_HANDLE                hDevice,
   INOUT_PDXGKARG_UPDATEPAGETABLE pUpdatePageTable
)
{ ... }
```

## Parameters

*hDevice*
This parameter is reserved for system use.

*pUpdatePageTable*
This parameter is reserved for system use.

## Requirements

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
<td align="left">Dispmprt.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





