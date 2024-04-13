---
title: DXGKDDI_CREATEALLOCATION2 Callback Function
description: The DxgkDdiCreateAllocation2 function is reserved for system use. Do not implement it in your driver.
keywords: ["DxgkDdiCreateAllocation2 callback function Display Devices", "DXGKDDI_CREATEALLOCATION2"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DxgkDdiCreateAllocation2
api_location:
- Dispmprt.h
api_type:
- UserDefined
ms.date: 01/05/2018
---

# DXGKDDI\_CREATEALLOCATION2 callback function


\[Reserved for system use.\]

The *DxgkDdiCreateAllocation2* function is reserved for system use. Do not implement it in your driver.

## Syntax

```ManagedCPlusPlus
DXGKDDI_CREATEALLOCATION2 DxgkDdiCreateAllocation2;

NTSTATUS DxgkDdiCreateAllocation2(
   IN_CONST_HANDLE                  hAdapter,
   INOUT_PDXGKARG_CREATEALLOCATION2 pCreateAllocation
)
{ ... }
```

## Parameters

*hAdapter*
This parameter is reserved for system use.

*pCreateAllocation*
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
<td align="left">Dispmprt.h (include D3dkmddi.h)</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





