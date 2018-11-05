---
title: chksym
description: The chksym extension tests the validity of a module against a symbol file.
ms.assetid: 52ea75cb-44a2-4c84-a3af-b3fc027348f4
keywords: ["chksym Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- chksym
api_type:
- NA
ms.localizationpriority: medium
---

# !chksym


The **!chksym** extension tests the validity of a module against a symbol file.

```dbgsyntax
    !chksym Module [Symbol] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the name of the module by its name or base address.

<span id="_______Symbol______"></span><span id="_______symbol______"></span><span id="_______SYMBOL______"></span> *Symbol*   
Specifies the name of a symbol file.

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
<td align="left"><p><strong>Windows XP</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows Vista and later</strong></p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If you do not specify a symbol filed, the loaded symbol is tested. Otherwise, if you specify a .pdb or .dbg symbol file path, the loaded symbol is tested against the loaded module.

 

 





