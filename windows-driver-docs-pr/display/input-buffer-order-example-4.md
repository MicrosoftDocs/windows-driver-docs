---
title: Input Buffer Order Example 4
description: Input Buffer Order Example 4
ms.assetid: 56370370-4786-44e4-9447-3937e4595e27
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Input Buffer Order Example 4


## <span id="ddk_input_buffer_order_example_4_gg"></span><span id="DDK_INPUT_BUFFER_ORDER_EXAMPLE_4_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

Consider a more sophisticated deinterlacing device that requires a single backward reference sample, a single future reference sample, and the current sample to perform its deinterlace operation. Two video substreams are also combined with the deinterlace operation. The sequence of surfaces in the **lpBufferInfo** array are:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Index position</th>
<th align="left">Surface type</th>
<th align="left">Temporal location</th>
<th align="left">Layer location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>lpBufferInfo[0]</p></td>
<td align="left"><p>Destination</p></td>
<td align="left"><p>T</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>lpBufferInfo[1]</p></td>
<td align="left"><p>Interlaced input</p></td>
<td align="left"><p>T - 1</p></td>
<td align="left"><p>Z</p></td>
</tr>
<tr class="odd">
<td align="left"><p>lpBufferInfo[2]</p></td>
<td align="left"><p>Interlaced input</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>Z</p></td>
</tr>
<tr class="even">
<td align="left"><p>lpBufferInfo[3]</p></td>
<td align="left"><p>Interlaced input</p></td>
<td align="left"><p>T + 1</p></td>
<td align="left"><p>Z</p></td>
</tr>
<tr class="odd">
<td align="left"><p>lpBufferInfo[4]</p></td>
<td align="left"><p>Substream</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Z + 1</p></td>
</tr>
<tr class="even">
<td align="left"><p>lpBufferInfo[5]</p></td>
<td align="left"><p>Substream</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Z + 2</p></td>
</tr>
</tbody>
</table>

 

 

 





