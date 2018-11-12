---
title: Enable heap tagging
description: Enable heap tagging
ms.assetid: be877811-075c-4019-81dd-73a134d5fb81
keywords: ["Enable heap tagging (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable heap tagging


## <span id="ddk_enable_heap_tagging_dtools"></span><span id="DDK_ENABLE_HEAP_TAGGING_DTOOLS"></span>


The **Enable heap tagging** flag assigns unique tags to heap allocations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>htg</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x800</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_HEAP_ENABLE_TAGGING</p></td>
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

[Enable heap tagging by DLL](enable-heap-tagging-by-dll.md)

 

 





