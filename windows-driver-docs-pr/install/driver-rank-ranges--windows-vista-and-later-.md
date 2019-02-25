---
title: Driver Rank Ranges
description: Driver Rank Ranges
ms.assetid: ea822171-c1f3-49b4-ae63-3300728666f0
keywords:
- driver rank ranges WDK device installations
- rank ranges WDK device installations
- range ranking WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 





