---
title: Enable heap tagging by DLL
description: Enable heap tagging by DLL
ms.assetid: d8f8f6f6-7365-4208-834f-3f5ccacdb7b6
keywords: ["Enable heap tagging by DLL (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable heap tagging by DLL


## <span id="ddk_enable_heap_tagging_by_dll_dtools"></span><span id="DDK_ENABLE_HEAP_TAGGING_BY_DLL_DTOOLS"></span>


The **Enable heap tagging by DLL** flag assigns a unique tag to heap allocations created by the same DLL.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>htd</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x8000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAG_BY_DLL</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

You can display the tag by using the [**!heap**](-heap.md) debugger extension with the -t parameter.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Enable heap tagging](enable-heap-tagging.md)

 

 





