---
title: Using AMLI Debugger Extensions
description: Using AMLI Debugger Extensions
ms.assetid: 98b9cd6e-b2e1-44bd-aff6-376b9cf2daa2
keywords: ["AMLI Debugger, AMLI Debugger extensions", "amli extension", "acpikd.amli extension"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using AMLI Debugger Extensions


## <span id="ddk_using_amli_debugger_extensions_dbg"></span><span id="DDK_USING_AMLI_DEBUGGER_EXTENSIONS_DBG"></span>


In Windows XP and later versions of Windows, AMLI Debugger extension commands are contained in the extension module Kdexts.dll and use the following syntax:

```
kd> !amli command [parameters] 
```

In Windows 2000, these extension commands are contained in Acpikd.dll and use the following syntax:

```
kd> !acpikd.amli command [parameters] 
```

As with any extension module, after it has been loaded you can omit the **acpikd** prefix.

If you are at the AMLI Debugger prompt, you can execute any of these extension commands by simply entering the *command* name without the **!amli** prefix:

```
AMLI(? for help)-> command [parameters] 
```

When you are at this prompt, the **!amli debugger** command is not available (because it would be meaningless). Also, the help command ( **?** ) at this prompt shows all AMLI Debugger extensions and commands, while the **!amli ?** extension only displays help on actual extensions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Action</th>
<th align="left">Extension Command</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Display Help</p></td>
<td align="left"><p><strong>[!amli ?](-amli--.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Set AML Breakpoint</p></td>
<td align="left"><p><strong>[!amli bp](-amli-bp.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>List AML Breakpoints</p></td>
<td align="left"><p><strong>[!amli bl](-amli-bl.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Disable AML Breakpoint</p></td>
<td align="left"><p><strong>[!amli bd](-amli-bd.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Enable AML Breakpoint</p></td>
<td align="left"><p><strong>[!amli be](-amli-be.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Clear AML Breakpoint</p></td>
<td align="left"><p><strong>[!amli bc](-amli-bc.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Enter AMLI Debugger</p></td>
<td align="left"><p><strong>[!amli debugger](-amli-debugger.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Event Log</p></td>
<td align="left"><p><strong>[!amli dl](-amli-dl.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Clear Event Log</p></td>
<td align="left"><p><strong>[!amli cl](-amli-cl.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Heap</p></td>
<td align="left"><p><strong>[!amli dh](-amli-dh.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Data Object</p></td>
<td align="left"><p><strong>[!amli do](-amli-do.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Stack</p></td>
<td align="left"><p><strong>[!amli ds](-amli-ds.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Namespace Object</p></td>
<td align="left"><p><strong>[!amli dns](-amli-dns.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Find Namespace Object</p></td>
<td align="left"><p><strong>[!amli find](-amli-find.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Nearest Method</p></td>
<td align="left"><p><strong>[!amli ln](-amli-ln.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>List All Contexts</p></td>
<td align="left"><p><strong>[!amli lc](-amli-lc.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Context Information</p></td>
<td align="left"><p><strong>[!amli r](-amli-r.md)</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Unassemble AML Code</p></td>
<td align="left"><p><strong>[!amli u](-amli-u.md)</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Set AMLI Debugger Options</p></td>
<td align="left"><p><strong>[!amli set](-amli-set.md)</strong></p></td>
</tr>
</tbody>
</table>

 

 

 





