---
title: logexts.logd
description: The logexts.logd extension disables logging.
ms.assetid: d3c3403d-f86b-4f2a-a261-c00eb0b2b756
keywords: ["logexts.logd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- logexts.logd
api_type:
- NA
ms.localizationpriority: medium
---

# !logexts.logd


The **!logexts.logd** extension disables logging.

```dbgcmd
    !logexts.logd 
```

## <span id="ddk__logexts_logd_dbg"></span><span id="DDK__LOGEXTS_LOGD_DBG"></span>


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

This will cause all API hooks to be removed in an effort to allow the program to run freely. COM hooks are not removed, because they cannot be re-enabled at will.

 

 





