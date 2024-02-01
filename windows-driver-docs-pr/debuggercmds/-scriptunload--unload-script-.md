---
title: .scriptunload (Unload Script)
description: The .scriptunload command unloads the specified script.
keywords: [".scriptunload (Unload Script) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .scriptunload (Unload Script)
api_type:
- NA
---

# .scriptunload (Unload Script)


The **.scriptunload** command unloads the specified script.

```dbgcmd
.scriptunload ScriptFile
```

## Parameters


<span id="_______ScriptFile______"></span><span id="_______scriptfile______"></span><span id="_______SCRIPTFILE______"></span> *ScriptFile*   
Specifies the name of the script file to unload. *ScriptFile* should include the .js file name extension. Absolute or relative paths can be used. Relative paths are relative to the directory that you started the debugger in. File paths containing spaces are not supported.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

The .scriptunload command unloads a loaded script. Use the following command syntax to unload a script

```dbgcmd
0:000:x86> .scriptunload C:\WinDbg\Scripts\TestScript.js
JavaScript script unloaded from 'C:\WinDbg\Scripts\TestScript.js'
```

If there are outstanding references to objects in a script, the contents of the script will be unlinked but the script may remain in memory until all such references are released.

For more information about working with JavaScript, see [JavaScript Debugger Scripting](../debugger/javascript-debugger-scripting.md). For more information about the debugger objects, see [Native Objects in JavaScript Extensions](../debugger/native-objects-in-javascript-extensions.md).

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider dll.

```dbgcmd
0:000> .load C:\ScriptProviders\jsprovider.dll
```

## <span id="see_also"></span>See also


[**.scriptload (Load Script)**](-scriptload--load-script-.md)

[JavaScript Debugger Scripting](../debugger/javascript-debugger-scripting.md)

 

 






