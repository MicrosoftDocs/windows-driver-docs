---
title: .scriptlist (List Loaded Scripts)
description: The .scriptlist command lists the loaded scripts.
keywords: [".scriptlist (List Loaded Scripts) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .scriptlist (List Loaded Scripts)
api_type:
- NA
---

# .scriptlist (List Loaded Scripts)


The **.scriptlist** command lists the loaded scripts.

```dbgcmd
.scriptlist 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______________"></span>    
None

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

The .scriptlist command will list any scripts which have been loaded via the .scriptload command.

If the TestScript was successfully loaded using .scriptload, the .scriptlist command would display the name of the loaded script.

```dbgcmd
0:000> .scriptlist
Command Loaded Scripts:
    JavaScript script from 'C:\WinDbg\Scripts\TestScript.js'
```

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded.

## <span id="see_also"></span>See also


[JavaScript Debugger Scripting](../debugger/javascript-debugger-scripting.md)

[**.scriptload (Load Script)**](-scriptload--load-script-.md)

 

 






