---
title: rebase
description: The rebase extension searches in a rebase.log file for a specified address or symbol.
ms.assetid: 811e7ab8-301f-433a-bfc4-8a4e5f002b30
keywords: ["rebase Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rebase
api_type:
- NA
ms.localizationpriority: medium
---

# !rebase


The **!rebase** extension searches in a rebase.log file for a specified address or symbol.

```dbgcmd
!rebase [-r] Address [Path]
!rebase Symbol [Path]
!rebase -stack [Path]
!rebase -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-r______"></span><span id="_______-R______"></span> **-r**   
Attempts to load any module found in rebase.log.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies an address in standard hexadecimal format. The extension will search for DLLs near this address.

<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
Specifies the file path to the rebase.log. If *Path* is not specified, then the extension tries to guess the path to the rebase.log or, failing that, tries to read a rebase.log file from the current working directory.

<span id="_______Symbol______"></span><span id="_______symbol______"></span><span id="_______SYMBOL______"></span> *Symbol*   
Specifies the symbol or image name. The extension will search for DLLs that contain this substring.

<span id="_______-stack______"></span><span id="_______-STACK______"></span> **-stack**   
Displays all modules in the current stack.

<span id="_______-_______"></span> **-?**   
Displays a brief help text for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

 

 





