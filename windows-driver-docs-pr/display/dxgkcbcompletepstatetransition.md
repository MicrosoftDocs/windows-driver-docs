---
title: DXGKCB_COMPLETEPSTATETRANSITION Callback Function
description: Learn about the DXGKCB\_COMPLETEPSTATETRANSITION callback function, which is reserved for system use. Do not use it in your driver.
keywords: ["DxgkCbCompletePStateTransition callback function Display Devices", "DXGKCB_COMPLETEPSTATETRANSITION"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DxgkCbCompletePStateTransition
api_location:
- D3dkmddi.h
api_type:
- UserDefined
ms.date: 01/05/2018
---

# DXGKCB\_COMPLETEPSTATETRANSITION callback function


Reserved for system use. Do not use it in your driver.

## Syntax

```ManagedCPlusPlus
DXGKCB_COMPLETEPSTATETRANSITION DxgkCbCompletePStateTransition;

VOID APIENTRY CALLBACK* DxgkCbCompletePStateTransition(
  _In_ const HANDLE hAdapter,
  _In_       UINT   ComponentIndex,
  _In_       UINT   CompletedPState
)
{ ... }
```

## Parameters

*hAdapter* \[in\]

*ComponentIndex* \[in\]

*CompletedPState* \[in\]

## Return value

This callback function does not return a value.

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
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





