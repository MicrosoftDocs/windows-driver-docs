---
title: .scriptload (Load Script)
description: The .scriptload command will load and execute the specified script file.
ms.assetid: 1D4C9587-1491-4D34-9D09-45587B272641
keywords: [".scriptload (Load Script) Windows Debugging"]
topic_type:
- apiref
api_name:
- .scriptload (Load Script)
api_type:
- NA
---

# .scriptload (Load Script)


The **.scriptload** command will load and execute the specified script file.

``` syntax
    .scriptload ScriptFile
     
   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______ScriptFile______"></span><span id="_______scriptfile______"></span><span id="_______SCRIPTFILE______"></span> *ScriptFile*   
Specifies the name of the script file to load. *ScriptFile* should include the .js file name extension. Absolute or relative paths can be used. Relative paths are relative to the directory that you started the debugger in. File paths containing spaces are not supported.

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

The .scriptload command will load a script and execute a script. The following command shows the successful load of TestScript.js.

```
0:000> .scriptload C:\WinDbg\Scripts\TestScript.js
JavaScript script successfully loaded from &#39;C:\WinDbg\Scripts\TestScript.js&#39;
```

If there are any errors in the initial load and execution of the script, the errors will be displayed to console, including the line number and error message.

```
0:000:x86> .scriptload C:\WinDbg\Scripts\TestScript.js
0:000> "C:\WinDbg\Scripts\TestScript.js" (line 11 (@ 1)): Error (0x80004005): Syntax error
Error: Unable to execute JavaScript script &#39;C:\WinDbg\Scripts\TestScript.js&#39;
```

The .scriptload command will execute the following in a JavaScript.

-   root code
-   intializeScript function (if present in the script)

When a script is loaded using the .scriptload command, the intializeScript function and the root code of the script is executed, the names which are present in the script are bridged into the root namespace of the debugger (dx Debugger) and the script stays resident in memory until it is unloaded and all references to its objects are released.

The script can provide new functions to the debugger's expression evaluator, modify the object model of the debugger, or can act as a visualizers in much the same way that a NatVis visualizer does. For more information about NavVis and the debugger, see [**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md).

For more information about working with JavaScript, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md). For more information about the debugger objects, see [Native Objects in JavaScript Extensions](native-objects-in-javascript-extensions.md).

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

## <span id="see_also"></span>See also


[**.scriptunload (Unload Script)**](-scriptunload--unload-script-.md)

[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.scriptload%20%28Load%20Script%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





