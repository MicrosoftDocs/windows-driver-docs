---
title: Using AMLI Debugger Extensions
description: Using AMLI Debugger Extensions
ms.assetid: 98b9cd6e-b2e1-44bd-aff6-376b9cf2daa2
keywords: ["AMLI Debugger, AMLI Debugger extensions", "amli extension", "acpikd.amli extension"]
ms.author: domars
ms.date: 11/07/2018
ms.localizationpriority: medium
---

# Using AMLI Debugger Extensions


## <span id="ddk_using_amli_debugger_extensions_dbg"></span><span id="DDK_USING_AMLI_DEBUGGER_EXTENSIONS_DBG"></span>


The AMLI Debugger extension commands are contained in the extension module Kdexts.dll and use the following syntax:

```dbgcmd
kd> !amli command [parameters] 
```


As with any extension module, after it has been loaded you can omit the **acpikd** prefix.

If you are at the AMLI Debugger prompt, you can execute any of these extension commands by simply entering the *command* name without the **!amli** prefix:

```dbgcmd
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
<td align="left"><p><strong><a href="-amli--.md" data-raw-source="[!amli ?](-amli--.md)">!amli ?</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Set AML Breakpoint</p></td>
<td align="left"><p><strong><a href="-amli-bp.md" data-raw-source="[!amli bp](-amli-bp.md)">!amli bp</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>List AML Breakpoints</p></td>
<td align="left"><p><strong><a href="-amli-bl.md" data-raw-source="[!amli bl](-amli-bl.md)">!amli bl</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Disable AML Breakpoint</p></td>
<td align="left"><p><strong><a href="-amli-bd.md" data-raw-source="[!amli bd](-amli-bd.md)">!amli bd</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Enable AML Breakpoint</p></td>
<td align="left"><p><strong><a href="-amli-be.md" data-raw-source="[!amli be](-amli-be.md)">!amli be</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Clear AML Breakpoint</p></td>
<td align="left"><p><strong><a href="-amli-bc.md" data-raw-source="[!amli bc](-amli-bc.md)">!amli bc</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Enter AMLI Debugger</p></td>
<td align="left"><p><strong><a href="-amli-debugger.md" data-raw-source="[!amli debugger](-amli-debugger.md)">!amli debugger</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Event Log</p></td>
<td align="left"><p><strong><a href="-amli-dl.md" data-raw-source="[!amli dl](-amli-dl.md)">!amli dl</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Clear Event Log</p></td>
<td align="left"><p><strong><a href="-amli-cl.md" data-raw-source="[!amli cl](-amli-cl.md)">!amli cl</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Heap</p></td>
<td align="left"><p><strong><a href="-amli-dh.md" data-raw-source="[!amli dh](-amli-dh.md)">!amli dh</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Data Object</p></td>
<td align="left"><p><strong><a href="-amli-do.md" data-raw-source="[!amli do](-amli-do.md)">!amli do</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Display Stack</p></td>
<td align="left"><p><strong><a href="-amli-ds.md" data-raw-source="[!amli ds](-amli-ds.md)">!amli ds</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Namespace Object</p></td>
<td align="left"><p><strong><a href="-amli-dns.md" data-raw-source="[!amli dns](-amli-dns.md)">!amli dns</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Find Namespace Object</p></td>
<td align="left"><p><strong><a href="-amli-find.md" data-raw-source="[!amli find](-amli-find.md)">!amli find</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Nearest Method</p></td>
<td align="left"><p><strong><a href="-amli-ln.md" data-raw-source="[!amli ln](-amli-ln.md)">!amli ln</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>List All Contexts</p></td>
<td align="left"><p><strong><a href="-amli-lc.md" data-raw-source="[!amli lc](-amli-lc.md)">!amli lc</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Display Context Information</p></td>
<td align="left"><p><strong><a href="-amli-r.md" data-raw-source="[!amli r](-amli-r.md)">!amli r</a></strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Unassemble AML Code</p></td>
<td align="left"><p><strong><a href="-amli-u.md" data-raw-source="[!amli u](-amli-u.md)">!amli u</a></strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Set AMLI Debugger Options</p></td>
<td align="left"><p><strong><a href="-amli-set.md" data-raw-source="[!amli set](-amli-set.md)">!amli set</a></strong></p></td>
</tr>
</tbody>
</table>

## See Also

[The AMLI Debugger](the-amli-debugger.md)
