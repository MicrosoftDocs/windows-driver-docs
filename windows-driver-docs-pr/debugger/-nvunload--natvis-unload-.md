---
title: .nvunload (NatVis Unload)
description: The .nvunload command unloads a NatVis file from the debugger environment.
keywords: [".nvunload (NatVis Unload) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .nvunload (NatVis Unload)
api_type:
- NA
ms.localizationpriority: medium
---

# .nvunload (NatVis Unload)

The .nvunload command unloads a NatVis file from the debugger environment.

```dbgcmd
.nvunload FileName|ModuleName  
```

*FileName | ModuleName*

Specifies the NatVis file name or module name to unload.

The **FileName** is the explicit name of a .natvis file to unload. A fully qualified path can be used.

The **ModuleName** is the name of a module in the target process being debugged. All NatVis files which are embedded within the symbol file (PDB) of the named module name are unloaded.

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

## Additional Information

For more information, see [Create Custom Views of Native Objects](/visualstudio/debugger/create-custom-views-of-native-objects).

## See also

[**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md)
