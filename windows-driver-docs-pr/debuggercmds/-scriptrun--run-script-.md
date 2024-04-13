---
title: ".scriptrun (Run Script)"
description: "The .scriptrun command will load and run a JavaScript."
keywords: [".scriptrun (Run Script) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .scriptrun (Run Script)
api_type:
- NA
---

# .scriptrun (Run Script)


The .scriptrun command will load and run a JavaScript.

```dbgcmd
.scriptrun ScriptFile  
```

## Parameters


<span id="_______ScriptFile______"></span><span id="_______scriptfile______"></span><span id="_______SCRIPTFILE______"></span> *ScriptFile*   
Specifies the name of the script file to load and execute. *ScriptFile* should include the .js file name extension. Absolute or relative paths can be used. Relative paths are relative to the directory that you started the debugger in. File paths containing spaces are not supported.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |



## Additional Information

The .scriptrun command will load a script and, execute the following code.

-   root
-   intializeScript
-   invokeScript

A confirmation message is displayed when the code is loaded and executed.

```dbgcmd
0:000> .scriptrun C:\WinDbg\Scripts\helloWorld.js
JavaScript script successfully loaded from 'C:\WinDbg\Scripts\helloWorld.js'
Hello World!  We are in JavaScript!
```

Any object model manipulations made by the script will stay in place until the script is subsequently unloaded or is run again with different content.

This table summarizes which functions are executed by .scriptload and .scriptrun.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"></td>
<td align="left"><strong><a href="-scriptload--load-script-.md" data-raw-source="[.scriptload](-scriptload--load-script-.md)">.scriptload</a></strong></td>
<td align="left"><strong>.scriptrun</strong></td>
</tr>
<tr class="even">
<td align="left">root</td>
<td align="left">yes</td>
<td align="left">yes</td>
</tr>
<tr class="odd">
<td align="left">initializeScript</td>
<td align="left">yes</td>
<td align="left">yes</td>
</tr>
<tr class="even">
<td align="left">invokeScript</td>
<td align="left"></td>
<td align="left">yes</td>
</tr>
<tr class="odd">
<td align="left">uninitializeScript</td>
<td align="left"></td>
<td align="left"></td>
</tr>
</tbody>
</table>



You can use this code to see which functions are called with the .script run command.

```dbgcmd
// Root of Script
host.diagnostics.debugLog("***>; Code at the very top (root) of the script is always run \n");


function initializeScript()
{
    // Add code here that you want to run every time the script is loaded. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***>; initializeScript was called \n");
}

function invokeScript()
{
    // Add code here that you want to run every time the script is executed. 
    // We will just send a message to indicate that function was called.
    host.diagnostics.debugLog("***>; invokeScript was called \n");
}
```

For more information about working with JavaScript, see [JavaScript Debugger Scripting](../debugger/javascript-debugger-scripting.md). For more information about the debugger objects, see [Native Objects in JavaScript Extensions](../debugger/native-objects-in-javascript-extensions.md).

### Requirements

Before using any of the .script commands, a scripting provider needs to be loaded. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider dll.

```dbgcmd
0:000> .load C:\ScriptProviders\jsprovider.dll
```

## See also


[**.scriptload (Load Script)**](-scriptload--load-script-.md)

[JavaScript Debugger Scripting](../debugger/javascript-debugger-scripting.md)



