---
title: .unload (Unload Extension DLL)
description: The .unload command unloads an extension DLL from the debugger.
ms.assetid: 8399e4a8-0265-4690-b35f-973b69fe2764
keywords: ["Unload Extension DLL (.unload) command", "extension commands ( commands), Unload Extension DLL (.unload) command", ".unload (Unload Extension DLL) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .unload (Unload Extension DLL)
api_type:
- NA
ms.localizationpriority: medium
---

# .unload (Unload Extension DLL)


The **.unload** command unloads an extension DLL from the debugger.

```dbgcmd
.unload DLLName 
!DLLName.unload
```

## <span id="ddk_meta_unload_extension_dll_dbg"></span><span id="DDK_META_UNLOAD_EXTENSION_DLL_DBG"></span>Parameters


<span id="_______DLLName______"></span><span id="_______dllname______"></span><span id="_______DLLNAME______"></span> *DLLName*   
Specifies the file name of the debugger extension DLL to be unloaded. If the full path was specified when the DLL was loaded, it needs to be given in full here as well. If *DLLName* is omitted, the current extension DLL is unloaded.

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

For more details on loading, unloading, and controlling extensions, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

Remarks
-------

This command is useful when testing an extension you are creating. When the extension is recompiled, you must unload and then load the new DLL.

 

 





