---
title: rtlavl
description: The rtlavl extension displays the entries of an RTL_AVL_TABLE structure.
ms.assetid: b1e19b13-8bb6-4f40-8d51-368fafc38ebc
keywords: ["avl tables", "rtlavl Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- rtlavl
api_type:
- NA
ms.localizationpriority: medium
---

# !rtlavl


The **!rtlavl** extension displays the entries of an RTL\_AVL\_TABLE structure.

```dbgcmd
!rtlavl Address [Module!Type]
!rtlavl -?
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the RTL\_AVL\_TABLE to display.

<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the module in which the data structure is defined.

<span id="_______Type______"></span><span id="_______type______"></span><span id="_______TYPE______"></span> *Type*   
Specifies the name of a data structure.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Debugger Command window.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

Use the [**!gentable**](-gentable.md) extension to display AVL tables.

Remarks
-------

Including the <em>Module</em>**!**<em>Type</em> option causes each entry in the table to be interpreted as having the given type.

The display can be interrupted at any time by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD or CDB).

 

 





