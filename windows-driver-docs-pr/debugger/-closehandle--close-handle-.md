---
title: .closehandle (Close Handle)
description: The .closehandle command closes a handle owned by the target application.
ms.assetid: 1513cbdd-327f-447a-8267-633cb123d17d
keywords: [".closehandle (Close Handle) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .closehandle (Close Handle)
api_type:
- NA
ms.localizationpriority: medium
---

# .closehandle (Close Handle)


The **.closehandle** command closes a handle owned by the target application.

```dbgsyntax
.closehandle Handle 
.closehandle -a 
```

## <span id="ddk_meta_close_handle_dbg"></span><span id="DDK_META_CLOSE_HANDLE_DBG"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
Specifies the handle to be closed.

<span id="_______-a______"></span><span id="_______-A______"></span> **-a**   
Causes all handles owned by the target application to be closed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can use the [**!handle**](-handle.md) extension to display the existing handles.

 

 





