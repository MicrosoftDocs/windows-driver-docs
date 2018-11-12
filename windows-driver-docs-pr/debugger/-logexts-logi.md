---
title: logexts.logi
description: The logexts.logi extension initializes logging by injecting Logger into the target application.
ms.assetid: c02d2799-c83a-455d-90c0-401244062365
keywords: ["logexts.logi Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- logexts.logi
api_type:
- NA
ms.localizationpriority: medium
---

# !logexts.logi


The **!logexts.logi** extension initializes logging by injecting Logger into the target application.

```dbgcmd
    !logexts.logi [OutputDirectory] 
```

## <span id="ddk__logexts_logi_dbg"></span><span id="DDK__LOGEXTS_LOGI_DBG"></span>Parameters


<span id="_______OutputDirectory______"></span><span id="_______outputdirectory______"></span><span id="_______OUTPUTDIRECTORY______"></span> *OutputDirectory*   
Specifies the directory to use for output. If *OutputDirectory* is specified, it must exist -- the debugger will not create it. If a relative path is specified, it will be relative to the directory from which the debugger was started. If *OutputDirectory* is omitted, the path to the Desktop will be used. The debugger will create a LogExts subdirectory of *OutputDirectory*, and all Logger output will be placed in this subdirectory.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Logexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Logexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Logger and LogViewer](logger-and-logviewer.md).

Remarks
-------

This command initializes logging, but does not actually enable it. Logging can be enabled with the [**!logexts.loge**](-logexts-loge.md) command.

 

 





