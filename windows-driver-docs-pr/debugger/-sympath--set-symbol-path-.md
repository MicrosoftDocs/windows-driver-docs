---
title: .sympath (Set Symbol Path)
description: The .sympath command sets or alters the symbol path. The symbol path specifies locations where the debugger looks for symbol files.
ms.assetid: 32146871-a59f-4c93-b886-137c5ecf5c99
keywords: ["Set Symbol Path (.sympath) command", "symbol files and paths, Set Symbol Path (.sympath) command", ".sympath (Set Symbol Path) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .sympath (Set Symbol Path)
api_type:
- NA
ms.localizationpriority: medium
---

# .sympath (Set Symbol Path)


The **.sympath** command sets or alters the symbol path. The symbol path specifies locations where the debugger looks for symbol files.

```dbgcmd
.sympath[+] [Path [; ...]]
```

## <span id="ddk_meta_set_symbol_path_dbg"></span><span id="DDK_META_SET_SYMBOL_PATH_DBG"></span>Parameters


<span id="______________"></span> **+**   
Specifies that the new locations will be appended to (rather than replace) the previous symbol search path.

<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
A fully qualified path or a list of fully qualified paths. Multiple paths are separated by semicolons. If *Path* is omitted, the current symbol path is displayed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details and other ways to change this path, see [Symbol Path](symbol-path.md).

Remarks
-------

New symbol information will not be loaded when the symbol path is changed. You can use the [**.reload (Reload Module)**](-reload--reload-module-.md) command to reload symbols.

 

 





