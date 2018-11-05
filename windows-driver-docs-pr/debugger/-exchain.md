---
title: exchain
description: The exchain extension displays the current exception handler chain.
ms.assetid: 6e5c935b-e475-4213-83d8-94510a58fde5
keywords: ["exchain Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- exchain
api_type:
- NA
ms.localizationpriority: medium
---

# !exchain


The **!exchain** extension displays the current exception handler chain.

```dbgcmd
!exchain [Options]
```

## <span id="ddk__exchain_dbg"></span><span id="DDK__EXCHAIN_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
One of the following values:

<span id="_c"></span><span id="_C"></span>**/c**  
Displays information that is relevant for debugging a C++ **try**/**catch** exception, if such an exception is detected.

<span id="_C"></span><span id="_c"></span>**/C**  
Displays information that is relevant for debugging a C++ **try**/**catch** exception, even when such an exception has not been detected.

<span id="_f"></span><span id="_F"></span>**/f**  
Displays information that is obtained by walking the CRT function tables, even if a CRT exception handler was not detected.

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

 

The **!exchain** extension is available only for an x86-based target computer.

Remarks
-------

The **!exchain** extension displays the list of exception handlers for the current thread.

The list begins with the first handler on the chain (the one that is given the first opportunity to handle an exception) and continues on to the end. The following example shows this extension.

```dbgcmd
0:000> !exchain
0012fea8: Prymes!_except_handler3+0 (00407604)
  CRT scope  0, filter: Prymes!dzExcepError+e6 (00401576)
                func:   Prymes!dzExcepError+ec (0040157c)
0012ffb0: Prymes!_except_handler3+0 (00407604)
  CRT scope  0, filter: Prymes!mainCRTStartup+f8 (004021b8)
                func:   Prymes!mainCRTStartup+113 (004021d3)
0012ffe0: KERNEL32!GetThreadContext+1c (77ea1856)
```

 

 





