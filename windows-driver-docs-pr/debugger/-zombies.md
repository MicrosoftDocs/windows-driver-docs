---
title: zombies
description: The zombies extension displays all dead ("zombie") processes or threads.
ms.assetid: f7fbce79-456a-4643-ad31-8cb2e6449ecf
keywords: ["zombies Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- zombies
api_type:
- NA
ms.localizationpriority: medium
---

# !zombies


The **!zombies** extension displays all dead ("zombie") processes or threads.

```dbgcmd
!zombies [Flags [RestartAddress]]
```

## <span id="ddk__zombies_dbg"></span><span id="DDK__ZOMBIES_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what will be displayed. Possible values include:

<span id="1"></span>1  
Displays all zombie processes. (This is the default.)

<span id="2"></span>2  
Displays all zombie threads.

<span id="_______RestartAddress______"></span><span id="_______restartaddress______"></span><span id="_______RESTARTADDRESS______"></span> *RestartAddress*   
Specifies the hexadecimal address at which to begin the search. This is useful if the previous search was terminated prematurely. The default is zero.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

To see a list of all processes and threads, use the [**!process**](-process.md) extension.

For general information about processes and threads in kernel mode, see [Changing Contexts](changing-contexts.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

Zombie processes are dead processes that have not yet been removed from the process list. Zombie threads are analogous.

This extension is available only for Windows 2000.

 

 





