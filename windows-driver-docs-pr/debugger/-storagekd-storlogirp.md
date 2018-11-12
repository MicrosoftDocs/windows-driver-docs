---
title: storagekd.storlogirp
description: The storagekd.storlogirp extension displays the Storport’s internal log entries for the adapter filtered for the IRP provided.
ms.assetid: EE2325CC-CDC0-4963-A0E8-B8EAB9A633BE
keywords: ["storagekd.storlogirp Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- storagekd.storlogirp
api_type:
- NA
ms.localizationpriority: medium
---

# !storagekd.storlogirp


The **!storagekd.storlogirp** extension displays the Storport’s internal log entries for the adapter filtered for the IRP provided.

```dbgcmd
!storagekd.storlogirp <Address> <irp> [<starting_entry> [<ending_entry>]] [L <count>]  
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a Storport adapter device extension or device object.

<span id="_______irp______"></span><span id="_______IRP______"></span> *irp*   
The IRP to locate.

<span id="_______starting_entry______"></span><span id="_______STARTING_ENTRY______"></span> *starting\_entry*   
The beginning entry in the range to display. If not specified, the last *count* entries will be displayed.

<span id="_______ending_entry______"></span><span id="_______ENDING_ENTRY______"></span> *ending\_entry*   
The ending entry in the range to display. If not specified, *count* entries will be displayed, beginning with the item specified by *starting\_entry*.

<span id="_______count______"></span><span id="_______COUNT______"></span> *count*   
Count of entries to be displayed. If not specified, a value of 50 is used.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 8 and later</strong></p></td>
<td align="left"><p>Storagekd.dll</p></td>
</tr>
</tbody>
</table>

 

 

 





