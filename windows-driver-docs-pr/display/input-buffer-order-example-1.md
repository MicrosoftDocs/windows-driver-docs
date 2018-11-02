---
title: Input Buffer Order Example 1
description: Input Buffer Order Example 1
ms.assetid: 1fd5f181-8bf7-4b16-adc9-ed751f9ad664
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Input Buffer Order Example 1


## <span id="ddk_input_buffer_order_example_1_gg"></span><span id="DDK_INPUT_BUFFER_ORDER_EXAMPLE_1_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

Consider a device that does not require any previous output reference frames or previous or future input reference frames to perform its deinterlacing operation (for example, the [bob deinterlacer](bob-deinterlacing.md)). The sequence of surfaces in the **lpBufferInfo** array for this device are:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Index position</th>
<th align="left">Surface type</th>
<th align="left">Temporal location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>lpBufferInfo[0]</p></td>
<td align="left"><p>Destination</p></td>
<td align="left"><p>T</p></td>
</tr>
<tr class="even">
<td align="left"><p>lpBufferInfo[1]</p></td>
<td align="left"><p>Interlaced input</p></td>
<td align="left"><p>T</p></td>
</tr>
</tbody>
</table>

 

 

 





