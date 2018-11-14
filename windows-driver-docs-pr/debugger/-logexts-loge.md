---
title: logexts.loge
description: The logexts.loge extension enables logging. If logging has not been initialized, it will be initialized and enabled.
ms.assetid: d8b621f1-19e7-4c42-a428-8572d29b666f
keywords: ["logexts.loge Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- logexts.loge
api_type:
- NA
ms.localizationpriority: medium
---

# !logexts.loge


The **!logexts.loge** extension enables logging. If logging has not been initialized, it will be initialized and enabled.

```dbgcmd
    !logexts.loge [OutputDirectory] 
```

## <span id="ddk__logexts_loge_dbg"></span><span id="DDK__LOGEXTS_LOGE_DBG"></span>Parameters


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

If Logger has not yet been injected into the target application by the [**!logexts.logi**](-logexts-logi.md) extension, the **!logexts.loge** extension will inject Logger into the target and then enable logging.

If [**!logexts.logi**](-logexts-logi.md) has already been run, you cannot include *OutputDirectory*, because the output directory will have already been set.

 

 





