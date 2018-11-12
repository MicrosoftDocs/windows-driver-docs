---
title: owner
description: The owner extension displays the owner of a module or function.
ms.assetid: f881bd86-89cf-49fd-9bca-3ecc96123be8
keywords: ["owner Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- owner
api_type:
- NA
ms.localizationpriority: medium
---

# !owner


The **!owner** extension displays the owner of a module or function.

```dbgcmd
!owner [Module[!Symbol]]
```

## <span id="ddk__owner_dbg"></span><span id="DDK__OWNER_DBG"></span>Parameters


<span id="_______Module______"></span><span id="_______module______"></span><span id="_______MODULE______"></span> *Module*   
Specifies the module whose owner is desired. An asterisk (\*) at the end of *Module* represents any number of additional characters.

<span id="_______Symbol______"></span><span id="_______symbol______"></span><span id="_______SYMBOL______"></span> *Symbol*   
Specifies the symbol within *Module* whose owner is desired. An asterisk (\*) at the end of *Symbol* represents any number of additional characters. If *Symbol* is omitted, the owner of the entire module is displayed.

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

If no parameters are used and a fault has occurred, **!owner** will display the name of the owner of the faulting module or function.

When you pass a module or function name to the **!owner** extension, the debugger displays the word **Followup** followed by the name of owner of the specified module or function.

For this extension to display useful information, you must first create a triage.ini file containing the names of the module and function owners.

For details on the triage.ini file and an example of the **!owner** extension, see [Specifying Module and Function Owners](specifying-module-and-function-owners.md).

 

 





