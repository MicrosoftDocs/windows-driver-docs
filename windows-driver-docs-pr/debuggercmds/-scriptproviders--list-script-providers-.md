---
title: .scriptproviders (List Script Providers)
description: The .scriptproviders command lists the active script providers.
keywords: [".scriptproviders (List Script Providers) Windows Debugging"]
ms.date: 02/02/2021
topic_type:
- apiref
ms.topic: reference
api_name:
- .scriptproviders (List Script Providers)
api_type:
- NA
---

# .scriptproviders (List Script Providers)


The **.scriptproviders** command lists the active script providers.

```dbgcmd
.scriptproviders 
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

The .scriptproviders command will list all the script languages which are presently understood by the debugger and the extension under which they are registered. Any file ending in ".NatVis" is understood as a NatVis script and any file ending in ".js" is understood as a JavaScript script. Either type of script can be loaded with the .scriptload command.

In the example below, the JavaScript and NatVis providers are loaded.

```dbgcmd
0:000> .scriptproviders
Available Script Providers:
    NatVis (extension '.NatVis')
    JavaScript (extension '.js')
```

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded.

## See also

[JavaScript Debugger Scripting](../debugger/javascript-debugger-scripting.md)

[**.scriptload (Load Script)**](-scriptload--load-script-.md)
