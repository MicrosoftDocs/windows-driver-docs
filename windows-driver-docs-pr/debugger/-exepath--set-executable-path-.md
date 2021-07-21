---
title: .exepath (Set Executable Path)
description: The .exepath command sets or displays the executable file search path.
keywords: [".exepath (Set Executable Path) Windows Debugging"]
ms.date: 05/05/2021
topic_type:
- apiref
api_name:
- .exepath (Set Executable Path)
api_type:
- NA
ms.localizationpriority: medium
---

# .exepath (Set Executable Path)


The **.exepath** command sets or displays the executable file search path.

```dbgcmd
.exepath[+] [Directory [; ...]] 
```

## Parameters


<span id="______________"></span> **+**   
Specifies that the debugger should append the new directories to the previous executable file search path (instead of replacing the path).

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies one or more directories to put in the search path. If you do not specify *Directory*, the current path is displayed. You can separate multiple directories with semicolons.

## Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
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


## Remarks

In most situations, the debugger knows the location of the executable files, so you do not have to set the path for this file.

However, there are situations when this path is required. For example, kernel-mode small memory dump files do not contain all of the executable files that exist in memory at the time of a stop error (that is, a crash). Similarly, user-mode minidump files do not contain the application binaries. If you set the path of the executable files, the debugger can find these binary files. For more information, see [Setting Symbol and Executable Image Paths in WinDbg](setting-symbol-and-source-paths-in-windbg.md).

The executable file search path can also be set using the `_NT_EXECUTABLE_IMAGE_PATH` environment variable. For more information, see [General Environment Variables](general-environment-variables.md).

## See also

[Setting Symbol and Executable Image Paths in WinDbg](setting-symbol-and-source-paths-in-windbg.md)

[General Environment Variables](general-environment-variables.md)


 

 

 





