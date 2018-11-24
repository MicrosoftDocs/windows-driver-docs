---
title: DXGKCB\_PRESENT\_DISPLAYONLY\_PROGRESS callback function
description: Reserved for system use. Do not use it in your driver.
ms.assetid: 8970246b-b46f-464f-93b2-973cc351ed07
keywords: ["pfnPresentDisplayOnlyProgress callback function Display Devices", "DXGKCB_PRESENT_DISPLAYONLY_PROGRESS"]
topic_type:
- apiref
api_name:
- pfnPresentDisplayOnlyProgress
api_location:
- D3dkmddi.h
api_type:
- UserDefined
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# DXGKCB\_PRESENT\_DISPLAYONLY\_PROGRESS callback function


Reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
DXGKCB_PRESENT_DISPLAYONLY_PROGRESS pfnPresentDisplayOnlyProgress;

void APIENTRY CALLBACK* pfnPresentDisplayOnlyProgress(
  _In_ const HANDLE                                 hAdapter,
  _In_ const DXGKARGCB_PRESENT_DISPLAYONLY_PROGRESS *pProgress
)
{ ... }
```

Parameters
----------

*hAdapter* \[in\]

*pProgress* \[in\]

Return value
------------

This callback function does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h</td>
</tr>
</tbody>
</table>

 

 





