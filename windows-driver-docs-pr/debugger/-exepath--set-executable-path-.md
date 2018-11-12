---
title: .exepath (Set Executable Path)
description: The .exepath command sets or displays the executable file search path.
ms.assetid: 09f8c2f6-4df7-4039-bb92-66d42015c3dc
keywords: [".exepath (Set Executable Path) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
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

## <span id="ddk_meta_set_executable_path_dbg"></span><span id="DDK_META_SET_EXECUTABLE_PATH_DBG"></span>Parameters


<span id="______________"></span> **+**   
Specifies that the debugger should append the new directories to the previous executable file search path (instead of replacing the path).

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies one or more directories to put in the search path. If you do not specify *Directory*, the current path is displayed. You can separate multiple directories with semicolons.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

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

 

 

 





