---
title: ks.topology
description: The ks.topology extension displays a sorted graph of the internal topology of the filter closest to Object.
ms.assetid: 04ef6920-c022-4136-a42a-800679fe7ff4
keywords: ["ks.topology Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.topology
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.topology


The **!ks.topology** extension displays a sorted graph of the internal topology of the filter closest to *Object*.

```dbgcmd
!ks.topology Object [Level] [Flags] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
Specifies a pointer to the object to use as a base for the graph. Can be a pointer to a file object, IRP, pin, filter, or other KS object.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Specifies the level of detail to display on a 0-7 scale with progressively more information displayed for higher values. To display all available details, supply a value of 7.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Not currently available.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

For help, issue a **!ks.topology** command with no arguments.

Note that this command may take a few moments to execute.

 

 





