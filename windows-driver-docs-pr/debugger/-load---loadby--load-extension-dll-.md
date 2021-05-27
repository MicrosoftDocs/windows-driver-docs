---
title: .load, .loadby (Load Extension DLL)
description: The .load and .loadby commands load a new extension DLL into the debugger.
keywords: [".load (Load Extension DLL) command", "loadby (Load Extension DLL) command", "Load Extension DLL (.load - .loadby) command", "extension commands ( commands), Load Extension DLL (.load - .loadby) command", ".load, .loadby (Load Extension DLL) Windows Debugging"]
ms.date: 01/30/2020
topic_type:
- apiref
api_name:
- .load, .loadby (Load Extension DLL)
api_type:
- NA
ms.localizationpriority: medium
---

# .load, .loadby (Load Extension DLL)

The **.load** and **.loadby** commands load a new extension DLL into the debugger.

```dbgcmd
.load DLLName  
!DLLName.load 
.loadby DLLName ModuleName
```

## <span id="ddk_meta_load_extension_dll_dbg"></span><span id="DDK_META_LOAD_EXTENSION_DLL_DBG"></span>Parameters


<span id="_______DLLName______"></span><span id="_______dllname______"></span><span id="_______DLLNAME______"></span> *DLLName*   
Specifies the debugger extension DLL to load. If you use the **.load** command, *DLLName* should include the full path. If you use the **.loadby** command, *DLLName* should include only the file name.

<span id="_______ModuleName______"></span><span id="_______modulename______"></span><span id="_______MODULENAME______"></span> *ModuleName*   
Specifies the module name of a module that is located in the same directory as the extension DLL that *DLLName* specifies.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to load, unload, and control extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

## Remarks

When you use the **.load** command, you must specify the full path.

When you use the **.loadby** command, you do not specify the path. Instead, the debugger finds the module that the *ModuleName* parameter specifies, determines the path of that module, and then uses that path when the debugger loads the extension DLL. If the debugger cannot find the module or if it cannot find the extension DLL, you receive an error message that specifies the problem. There does not have to be any relationship between the specified module and the extension DLL. Using the **.loadby** command is therefore simply a way to avoid typing a long path.

After the **.load** or **.loadby** command has been completed, you can access the commands that are stored in the loaded extension.

To load an extension DLL, you can do one of the following:

- Use the **.load** or **.loadby** command.

- Execute an extension by issuing the full **!**<em>DLLName</em>**.**<em>ExtensionCommand</em> syntax. If the debugger has not yet loaded *DLLName*.dll, it loads the DLL at this point if it is located in the current DLL search path.

Use the [.chain](-chain--list-debugger-extensions-.md) command to display information about what has been loaded and the current DLL search path.

```dbgcmd
0:000> .chain
Extension DLL search Path:
    C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\WINXP;C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\winext;C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\winext\arcade;C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\pri;C:\Program Files (x86)\Windows Kits\10\Debuggers\x64;
Extension DLL chain:
    C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SOS.dll: image 4.8.4084.0, API 1.0.0, built Sun Nov 24 00:38:52 2019
```

For example, the managed code SOS.dll is not in search path for DLLs shown above, so use the .load command with a complete path to load that dll.  

```dbgcmd
0:000> .load C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SOS.dll
```
