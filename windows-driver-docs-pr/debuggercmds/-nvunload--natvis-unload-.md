---
title: .nvunload (NatVis Unload)
description: The .nvunload command unloads a NatVis file from the debugger environment.
keywords: [".nvunload (NatVis Unload) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .nvunload (NatVis Unload)
api_type:
- NA
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

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

For more information, see [Create Custom Views of Native Objects](/visualstudio/debugger/create-custom-views-of-native-objects).

## See also

[**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md)
