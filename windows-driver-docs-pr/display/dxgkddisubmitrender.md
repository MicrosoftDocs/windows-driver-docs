---
title: DXGKDDI\_SUBMITRENDER callback function
description: The DxgkDdiSubmitRender function is reserved for system use. Do not implement it in your driver.
ms.assetid: a409f737-72e9-43b0-be81-c373b151f5d9
keywords: ["DxgkDdiSubmitRender callback function Display Devices", "DXGKDDI_SUBMITRENDER"]
topic_type:
- apiref
api_name:
- DxgkDdiSubmitRender
api_location:
- Dispmprt.h
api_type:
- UserDefined
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGKDDI\_SUBMITRENDER callback function


\[Reserved for system use.\]

The *DxgkDdiSubmitRender* function is reserved for system use. Do not implement it in your driver.

Syntax
------

```ManagedCPlusPlus
DXGKDDI_SUBMITRENDER DxgkDdiSubmitRender;

NTSTATUS DxgkDdiSubmitRender(
   IN_CONST_HANDLE             hContext,
   INOUT_PDXGKARG_SUBMITRENDER pSubmitRender
)
{ ... }
```

Parameters
----------

*hContext*
This parameter is reserved for system use.

*pSubmitRender*
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
<td align="left">Dispmprt.h</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





