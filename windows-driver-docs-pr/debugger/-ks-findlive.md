---
title: ks.findlive
description: The ks.findlive extension searches the internal Ks.sys debug log to attempt to find live objects of a specified type.
ms.assetid: 71372144-3f39-460b-859c-ac4cba0c766d
keywords: ["ks.findlive Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.findlive
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.findlive


The **!ks.findlive** extension searches the internal Ks.sys debug log to attempt to find live objects of a specified type.

```dbgcmd
!ks.findlive Type [Entries] [Level] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the type of object for which to search. Enter one of the following as a literal value: **Queue**, **Requestor**, **Pin**, **Filter**, or **Irp**.

<span id="Entries"></span><span id="entries"></span><span id="ENTRIES"></span>Entries  
If this parameter is zero or omitted, the entire log is searched.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Specifies the level of detail to display on a 0-7 scale with progressively more information displayed for higher values. To display all available details, supply a value of 7.

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

The **!ks.findlive** command may not find all possible specified live objects.

This extension requires that the target computer be running a checked (debug) version of Ks.sys.

 

 





