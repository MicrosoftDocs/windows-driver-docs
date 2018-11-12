---
title: .setdll (Set Default Extension DLL)
description: The .setdll command changes the default extension DLL for the debugger.
ms.assetid: 9dc5cd9e-d4f2-4112-bf3d-f7061c786ddf
keywords: ["Set Default Extension DLL (.setdll) command", "extension commands ( commands), Set Default Extension DLL (.setdll) command", ".setdll (Set Default Extension DLL) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .setdll (Set Default Extension DLL)
api_type:
- NA
ms.localizationpriority: medium
---

# .setdll (Set Default Extension DLL)


The **.setdll** command changes the default extension DLL for the debugger.

```dbgcmd
.setdll DLLName 
!DLLName.setdll 
```

## <span id="ddk_meta_set_default_extension_dll_dbg"></span><span id="DDK_META_SET_DEFAULT_EXTENSION_DLL_DBG"></span>Parameters


<span id="_______DLLName______"></span><span id="_______dllname______"></span><span id="_______DLLNAME______"></span> *DLLName*   
The name and path of the extension DLL. If the full path was specified when the DLL was loaded, it needs to be given in full here as well.

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

For details on loading, unloading, and controlling extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md). For details on executing extension commands, see [Using Debugger Extension Commands](using-debugger-extension-commands.md).

Remarks
-------

The debugger maintains a default extension DLL that is implicitly loaded when the debugger is started. This allows the user to specify an extension command without first having to load an extension DLL. This command allows modification of which DLL is loaded as the default DLL.

When a command is issued, the debugger looks for it in the default extension first. If a match is not found, all other loaded extension DLLs are searched in the order they were loaded.

 

 





