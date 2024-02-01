---
title: .extpath (Set Extension Path)
description: The .extpath command sets or displays the extension DLL search path.
keywords: [".extpath (Set Extension Path) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .extpath (Set Extension Path)
api_type:
- NA
---

# .extpath (Set Extension Path)


The **.extpath** command sets or displays the extension DLL search path.

```dbgcmd
.extpath[+] [Directory[;...]]
```

## Parameters


<span id="______________"></span> +   
Signifies that the debugger should append new directories to the previous extension DLL search path (instead of replacing the path).

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies one or more directories to put in the search path. If you do not specify *Directory*, the current path is displayed. You can separate multiple directories with semicolons.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode, kernel mode|
|Targets|Live, crash dump|
|Platforms|All|

 

### Additional Information

For more information about the extension search path and loading extension DLLs, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

## Remarks

The extension DLL search path is reset to its default value at the start of each debugging session.

During live kernel-mode debugging, a reboot of the target computer results in the start of a new debugging session. So any changes that you make to the extension DLL search path during kernel-mode debugging will not persist across a reboot of the target computer.

The default value of the extension DLL search path contains all the extension paths known to the debugger and all the paths in the %PATH% environment variable. For example, suppose your %PATH% environment variable has a value of `C:\Windows\system32;C:\Windows`. Then the default value of the DLL extension search path might look like this.

```dbgcmd
0:000> .extpath
Extension search path is: C:\Program Files\Debugging Tools for Windows (x64)\WINXP;C:\Program Files\
Debugging Tools for Windows (x64)\winext;C:\Program Files\Debugging Tools for Windows (x64)\winext\
arcade;C:\Program Files\Debugging Tools for Windows (x64);C:\Program Files\Debugging Tools for 
Windows (x64)\winext\arcade;C:\Windows\system32;C:\Windows
```

 

 





