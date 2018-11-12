---
title: Input Buffer Order Example 3
description: Input Buffer Order Example 3
ms.assetid: 627102bb-e7a8-4b6d-9a52-f8bf4b9727d6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Input Buffer Order Example 3


## <span id="ddk_input_buffer_order_example_3_gg"></span><span id="DDK_INPUT_BUFFER_ORDER_EXAMPLE_3_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR initiates a call to the driver's *DeinterlaceBltEx* function to use the device in [Input Buffer Order Example 1](input-buffer-order-example-1.md) and [Input Buffer Order Example 2](input-buffer-order-example-2.md) to instead combine 3 video substreams with a progressive video stream. The sequence of surfaces in the **lpBufferInfo** array are:

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
<td align="left"><p>Progressive input</p></td>
<td align="left"><p>T</p></td>
<td align="left"><p>Z</p></td>
</tr>
<tr class="odd">
<td align="left"><p>lpBufferInfo[2]</p></td>
<td align="left"><p>Substream</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Z + 1</p></td>
</tr>
<tr class="even">
<td align="left"><p>lpBufferInfo[3]</p></td>
<td align="left"><p>Substream</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Z + 2</p></td>
</tr>
<tr class="odd">
<td align="left"><p>lpBufferInfo[4]</p></td>
<td align="left"><p>Substream</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Z + 3</p></td>
</tr>
</tbody>
</table>

 

In the change from example 2 to 3, the video stream changed from interlaced to progressive and an additional video substream became active.

 

 





