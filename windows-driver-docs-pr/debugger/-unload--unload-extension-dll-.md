---
title: .unload (Unload Extension DLL)
description: The .unload command unloads an extension DLL from the debugger.
ms.assetid: 8399e4a8-0265-4690-b35f-973b69fe2764
keywords: ["Unload Extension DLL (.unload) command", "extension commands ( commands), Unload Extension DLL (.unload) command", ".unload (Unload Extension DLL) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .unload (Unload Extension DLL)
api_type:
- NA
---

# .unload (Unload Extension DLL)


The **.unload** command unloads an extension DLL from the debugger.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.unload%20%28Unload%20Extension%20DLL%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




