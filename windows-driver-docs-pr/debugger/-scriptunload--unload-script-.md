---
title: .scriptunload (Unload Script)
description: The .scriptunload command unloads the specified script.
ms.assetid: 015703C2-31E2-46B4-8F89-1EA52DB7E6FC
keywords: [".scriptunload (Unload Script) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .scriptunload (Unload Script)
api_type:
- NA
ms.localizationpriority: medium
---

# .scriptunload (Unload Script)


The **.scriptunload** command unloads the specified script.

```dbgcmd
.scriptunload ScriptFile
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______ScriptFile______"></span><span id="_______scriptfile______"></span><span id="_______SCRIPTFILE______"></span> *ScriptFile*   
Specifies the name of the script file to unload. *ScriptFile* should include the .js file name extension. Absolute or relative paths can be used. Relative paths are relative to the directory that you started the debugger in. File paths containing spaces are not supported.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

The .scriptunload command unloads a loaded script. Use the following command syntax to unload a script

```dbgcmd
0:000:x86> .scriptunload C:\WinDbg\Scripts\TestScript.js
JavaScript script unloaded from 'C:\WinDbg\Scripts\TestScript.js'
```

If there are outstanding references to objects in a script, the contents of the script will be unlinked but the script may remain in memory until all such references are released.

For more information about working with JavaScript, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md). For more information about the debugger objects, see [Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md).

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider dll.

```dbgcmd
0:000> .load C:\ScriptProviders\jsprovider.dll
```

## <span id="see_also"></span>See also


[**.scriptload (Load Script)**](-scriptload--load-script-.md)

[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

 

 






