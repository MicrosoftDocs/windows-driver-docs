---
title: Driver Rank Ranges
description: Driver Rank Ranges
ms.assetid: ea822171-c1f3-49b4-ae63-3300728666f0
keywords: ["driver rank ranges WDK device installations", "rank ranges WDK device installations", "range ranking WDK device installations"]
---

# Driver Rank Ranges


A driver rank is formatted as 0x*SSGGTHHH*, where the value of 0x*SS*000000 is the [signature score](signature-score--windows-vista-and-later-.md), the value of 0x00*GG*0000 is the [feature score](feature-score--windows-vista-and-later-.md), and the value of 0x0000*THHH* is the [identifier score](identifier-score--windows-vista-and-later-.md).

The following table lists all the valid driver rank ranges, where 0x*SS*000000 represents a valid signature score, 0x00*GG*0000 represents a valid feature score, and the range of the identifier score for each type of identifier match is shown.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver Rank</th>
<th align="left">Identifier score</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0xSS<em>GG</em>0000-0xSS<em>GG</em>0FFF</p></td>
<td align="left"><p>0x0000-0x0FFF</p></td>
<td align="left"><p>A device hardware ID matched the hardware ID in an INF <em>Models</em> section entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xSS<em>GG</em>1000-0xSS<em>GG</em>1FFF</p></td>
<td align="left"><p>0x1000-0x1FFF</p></td>
<td align="left"><p>A device hardware ID matched a compatible ID in an INF <em>Models</em> section entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xSS<em>GG</em>2000-0xSS<em>GG</em>2FFF</p></td>
<td align="left"><p>0x2000-0x2FFF</p></td>
<td align="left"><p>A device compatible ID matched the hardware ID in an INF <em>Models</em> section entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xSS<em>GG</em>3000-0xSS<em>GG</em>3FFF</p></td>
<td align="left"><p>0x3000-0x3FFF</p></td>
<td align="left"><p>A device compatible ID matched a compatible ID in an INF <em>Models</em> section entry.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Driver%20Rank%20Ranges%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




