---
title: DXGKDDISETPOWERPSTATE callback function
description: Learn about the DXGKDDISETPOWERPSTATE callback function, which is reserved for system use. Do not use it in your driver.
keywords: ["DxgkDdiSetPowerPState callback function Display Devices", "DXGKDDISETPOWERPSTATE"]
topic_type:
- apiref
api_name:
- DxgkDdiSetPowerPState
api_location:
- D3dkmddi.h
api_type:
- UserDefined
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGKDDISETPOWERPSTATE callback function


Reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
DXGKDDISETPOWERPSTATE DxgkDdiSetPowerPState;

NTSTATUS APIENTRY DxgkDdiSetPowerPState(
  _In_ const HANDLE DriverContext,
  _In_       UINT   ComponentIndex,
  _In_       UINT   RequestedComponentPState
)
{ ... }
```

## Parameters

*DriverContext* \[in\]

*ComponentIndex* \[in\]

*RequestedComponentPState* \[in\]

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8.1</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012 R2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





