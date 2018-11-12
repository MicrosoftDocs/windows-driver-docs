---
title: loadermemorylist
description: The loadermemorylist extension displays the memory allocation list that the Windows boot loader passes to Windows.
ms.assetid: 3e5dff7a-ea8f-4029-93e3-7c160487e968
keywords: ["OSLOADER", "loadermemorylist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- loadermemorylist
api_type:
- NA
ms.localizationpriority: medium
---

# !loadermemorylist


The **!loadermemorylist** extension displays the memory allocation list that the Windows boot loader passes to Windows.

```dbgcmd
!loadermemorylist ListHeadAddress
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______ListHeadAddress______"></span><span id="_______listheadaddress______"></span><span id="_______LISTHEADADDRESS______"></span> *ListHeadAddress*   
Specifies the address of a list header.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP</strong></p>
<p><strong>Windows Server 2003</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows Vista and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This extension is designed to be used at the beginning of the system boot process while Ntldr is running. It displays a memory allocation list that includes the start, end, and type of each page range.

You can stop execution at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





