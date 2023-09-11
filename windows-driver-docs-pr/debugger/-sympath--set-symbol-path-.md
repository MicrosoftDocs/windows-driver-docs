---
title: .sympath (Set Symbol Path)
description: The .sympath command sets or alters the symbol path. The symbol path specifies locations where the debugger looks for symbol files.
keywords: ["Set Symbol Path (.sympath) command", "symbol files and paths, Set Symbol Path (.sympath) command", ".sympath (Set Symbol Path) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .sympath (Set Symbol Path)
api_type:
- NA
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

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For details and other ways to change this path, see [Symbol Path](symbol-path.md).

## Remarks

New symbol information will not be loaded when the symbol path is changed. You can use the [**.reload (Reload Module)**](-reload--reload-module-.md) command to reload symbols.

 

 





