---
title: lse (Launch Source Editor)
description: The lse command opens an editor for the current source file.
ms.assetid: 2f66b5c3-1cd6-4641-8dea-5e3a11c87db0
keywords: ["lse (Launch Source Editor) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- lse (Launch Source Editor)
api_type:
- NA
ms.localizationpriority: medium
---

# lse (Launch Source Editor)


The **lse** command opens an editor for the current source file.

```dbgcmd
lse 
```

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User-mode, kernel-mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **lse** command opens an editor for the current source file. This command is equivalent to clicking **Edit this file** in the shortcut menu of the [Source window](source-window.md) in WinDbg.

The editor is opened on the computer that the target is running on, so you cannot use the **lse** command from a remote client.

The WinDiff editor registry information or the value of the WINDBG\_INVOKE\_EDITOR environment variable determine which editor is opened. For example, consider the following value of WINDBG\_INVOKE\_EDITOR.

```reg
c:\my\path\myeditor.exe -file %f -line %l
```

This value indicates that Myeditor.exe opens to the one-based line number of the current source file. The **%l** option indicates that line numbers should be read as one-based, and **%f** indicates that the current source file should be used. You could also include **%L** to indicate that line numbers are zero-based or **%p** to indicate that the current source file should be used.

 

 





