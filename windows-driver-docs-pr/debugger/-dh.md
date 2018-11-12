---
title: dh
description: The dh extension displays the headers for the specified image.
ms.assetid: 1b4f94ae-42cc-4381-a2d1-c2f248e4d5a6
keywords: ["NTFS file object", "dh Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dh
api_type:
- NA
ms.localizationpriority: medium
---

# !dh


The **!dh** extension displays the headers for the specified image.

```dbgcmd
!dh [Options] Address 
!dh -h
```

## <span id="ddk__dh_dbg"></span><span id="DDK__DH_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any one of the following options:

<span id="-f"></span><span id="-F"></span>**-f**  
Displays file headers.

<span id="-s"></span><span id="-S"></span>**-s**  
Displays section headers.

<span id="-a"></span><span id="-A"></span>**-a**  
Displays all header information.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the image.

<span id="_______-h______"></span><span id="_______-H______"></span> **-h**   
Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Dbghelp.dll
Kdextx86.dll
Ntsdexts.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The [**!lmi**](-lmi.md) extension extracts the most important information from the image header and displays it in a concise summary format. That extension is frequently more useful than **!dh**.

 

 





