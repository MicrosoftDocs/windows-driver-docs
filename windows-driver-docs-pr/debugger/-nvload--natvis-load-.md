---
title: .nvload (NatVis Load)
description: The .nvload command loads a NatVis file into the debugger environment. After the visualization is loaded, it will be used to render data defined in the visualization.
keywords: [".nvload (NatVis Load) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .nvload (NatVis Load)
api_type:
- NA
---

# .nvload (NatVis Load)


The .nvload command loads a NatVis file into the debugger environment. After the visualization is loaded, it will be used to render data defined in the visualization.

```dbgcmd
.nvload FileName|ModuleName
```

## Parameters

*FileName | ModuleName*

Specifies the NatVis file name or module name to load.

The **FileName** is the explicit name of a .natvis file to load. A fully qualified path can be used.

The **ModuleName** is the name of a module in the target process being debugged. All NatVis files which are embedded within the symbol file (PDB) of the named module name are loaded, if there are any available.

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
