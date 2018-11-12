---
title: elog_str
description: The elog_str extension adds a string to the event log.
ms.assetid: 142ef480-8095-428e-9b7d-f4c8bfb78075
keywords: ["event log", "elog_str Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- elog_str
api_type:
- NA
ms.localizationpriority: medium
---

# !elog\_str


The **!elog\_str** extension adds a string to the event log.

```dbgcmd
!elog_str String
```

## <span id="ddk__elog_str_dbg"></span><span id="DDK__ELOG_STR_DBG"></span>Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the string to add to the event log.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Because a registered event source does not send *String*, the string appears in the event log with a warning that no event ID was determined.

 

 





