---
title: ".setdll (Set Default Extension DLL)"
description: "The .setdll command changes the default extension DLL for the debugger."
keywords: ["Set Default Extension DLL (.setdll) command", "extension commands ( commands), Set Default Extension DLL (.setdll) command", ".setdll (Set Default Extension DLL) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .setdll (Set Default Extension DLL)
api_type:
- NA
---

# .setdll (Set Default Extension DLL)

The **.setdll** command changes the default extension DLL for the debugger.

```dbgcmd
.setdll DLLName 
!DLLName.setdll 
```

## Parameters

<span id="_______DLLName______"></span><span id="_______dllname______"></span><span id="_______DLLNAME______"></span> *DLLName*   
The name and path of the extension DLL. If the full path was specified when the DLL was loaded, it needs to be given in full here as well.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

For details on loading, unloading, and controlling extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md). For details on executing extension commands, see [Using Debugger Extension Commands](using-debugger-extension-commands.md).

## Remarks

The debugger maintains a default extension DLL that is implicitly loaded when the debugger is started. This allows the user to specify an extension command without first having to load an extension DLL. This command allows modification of which DLL is loaded as the default DLL.

When a command is issued, the debugger looks for it in the default extension first. If a match is not found, all other loaded extension DLLs are searched in the order they were loaded.
