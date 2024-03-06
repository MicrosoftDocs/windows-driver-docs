---
title: .unload (Unload Extension DLL)
description: The .unload command unloads an extension DLL from the debugger.
keywords: ["Unload Extension DLL (.unload) command", "extension commands ( commands), Unload Extension DLL (.unload) command", ".unload (Unload Extension DLL) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .unload (Unload Extension DLL)
api_type:
- NA
---

# .unload (Unload Extension DLL)


The **.unload** command unloads an extension DLL from the debugger.

```dbgcmd
.unload DLLName 
!DLLName.unload
```

## <span id="ddk_meta_unload_extension_dll_dbg"></span><span id="DDK_META_UNLOAD_EXTENSION_DLL_DBG"></span>Parameters


<span id="_______DLLName______"></span><span id="_______dllname______"></span><span id="_______DLLNAME______"></span> *DLLName*   
Specifies the file name of the debugger extension DLL to be unloaded. If the full path was specified when the DLL was loaded, it needs to be given in full here as well. If *DLLName* is omitted, the current extension DLL is unloaded.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more details on loading, unloading, and controlling extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

## Remarks

This command is useful when testing an extension you are creating. When the extension is recompiled, you must unload and then load the new DLL.

 

 





