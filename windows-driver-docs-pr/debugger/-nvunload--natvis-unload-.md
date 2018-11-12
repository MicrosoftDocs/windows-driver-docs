---
title: .nvunload (NatVis Unload)
description: The .nvunload command unloads a NatVis file from the debugger environment.
ms.assetid: E63BE2B5-291B-4F78-98FF-C1D7663A184E
keywords: [".nvunload (NatVis Unload) Windows Debugging"]
ms.author: domars
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

<span id="_______FileName___ModuleName______"></span><span id="_______filename___modulename______"></span><span id="_______FILENAME___MODULENAME______"></span> *FileName | ModuleName*   
Specifies the NatVis file name or module name to unload.

The **FileName** is the explicit name of a .natvis file to unload. A fully qualified path can be used.

The **ModuleName** is the name of a module in the target process being debugged. All NatVis files which are embedded within the symbol file (PDB) of the named module name are unloaded.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Writing debugger type visualizers for C++ using .natvis files](https://code.msdn.microsoft.com/windowsdesktop/Writing-type-visualizers-2eae77a2).

## <span id="see_also"></span>See also


[**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md)

 

 






