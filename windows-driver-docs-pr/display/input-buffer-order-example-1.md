---
title: Input Buffer Order Example 1
description: Input Buffer Order Example 1
ms.assetid: 1fd5f181-8bf7-4b16-adc9-ed751f9ad664
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Input%20Buffer%20Order%20Example%201%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




