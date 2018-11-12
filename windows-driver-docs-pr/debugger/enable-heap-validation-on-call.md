---
title: Enable heap validation on call
description: Enable heap validation on call
ms.assetid: 779871e0-f8b9-4eb5-9869-8df67586ffab
keywords: ["Enable heap validation on call (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable heap validation on call


## <span id="ddk_enable_heap_validation_on_call_dtools"></span><span id="DDK_ENABLE_HEAP_VALIDATION_ON_CALL_DTOOLS"></span>


The **Enable heap validation on call** flag validates the entire heap each time a heap function is called.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>hvc</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x80</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_HEAP_VALIDATE_ALL</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

To avoid the high overhead associated with this flag, use the **HeapValidate** function instead of setting this flag, especially at critical junctures, such as when the heap is destroyed. However, this flag is useful for detecting random corruption in a pool.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Enable heap parameter checking](enable-heap-parameter-checking.md)

 

 





