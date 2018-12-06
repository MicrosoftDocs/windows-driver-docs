---
title: Input Buffer Order Example 2
description: Input Buffer Order Example 2
ms.assetid: e480bd93-4ae2-4a6c-b669-69c44c0154d0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Input Buffer Order Example 2


## <span id="ddk_input_buffer_order_example_2_gg"></span><span id="DDK_INPUT_BUFFER_ORDER_EXAMPLE_2_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The VMR initiates a call to the driver's [**DeinterlaceBltEx**](https://msdn.microsoft.com/library/windows/hardware/ff563927) function to use the device in [Input Buffer Order Example 1](input-buffer-order-example-1.md) to combine 2 video substreams with an interlaced video stream. The sequence of surfaces in the **lpBufferInfo** array are:

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
</tbody>
</table>

 

 

 





