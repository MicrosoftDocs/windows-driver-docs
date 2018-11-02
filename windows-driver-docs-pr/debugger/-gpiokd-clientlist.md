---
title: gpiokd.clientlist
description: The gpiokd.clientlist command displays all registered GPIO controllers.
ms.assetid: 4951C2D2-FA98-4600-A98D-1BC98080D2EB
keywords: ["gpiokd.clientlist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gpiokd.clientlist
api_type:
- NA
ms.localizationpriority: medium
---

# !gpiokd.clientlist


The **!gpiokd.clientlist** command displays all registered GPIO controllers.

```dbgcmd
!gpiokd.clientlist [Flags] 
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Flags that specify which information is displayed. This parameter is a bitwise OR of one or more of the following flags.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="0x1"></span><span id="0X1"></span>0x1</p></td>
<td align="left"><p>For each controller, displays detailed information including all of its banks.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="0x2"></span><span id="0X2"></span>0x2</p></td>
<td align="left"><p>If bit 0 (0x1) is set and this flag (0x2) is set, displays the Enable and Mask registers for each bank.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="0x4"></span><span id="0X4"></span>0x4</p></td>
<td align="left"><p>If bit 0 (0x1) is set and this flag (0x4) is set, the display includes unconfigured pins.</p></td>
</tr>
</tbody>
</table>

 

## <span id="DLL"></span><span id="dll"></span>DLL


Gpiokd.dll

## <span id="see_also"></span>See also


[GPIO Extensions](gpio-extensions.md)

 

 






