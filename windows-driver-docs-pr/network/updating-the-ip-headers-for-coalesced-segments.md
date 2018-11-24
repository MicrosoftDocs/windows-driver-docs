---
title: Updating the IP headers for coalesced segments
description: This section describes how to update the IP headers for coalesced segments
ms.assetid: 18F2944A-D5A7-41BB-885F-EC183A00F7CE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating the IP Headers for Coalesced Segments


When finalizing a single coalescing unit (SCU), a receive segment coalescing (RSC)-capable miniport driver updates the fields in the IP headers as described in the following tables.

-   [Updating IPv4 header fields for coalesced segments](#updating-ipv4-header-fields-for-coalesced-segments)
-   [Updating IPv6 header fields for coalesced segments](#updating-ipv6-header-fields-for-coalesced-segments)

## Updating IPv4 header fields for coalesced segments


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Version</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Header Length</strong></p></td>
<td align="left"><p>The length of a basic IPv4 header without any IP options.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Differentiated Services</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ECN bits</strong></p></td>
<td align="left"><p>See Exception 8 in <a href="exception-conditions-that-terminate-coalescing.md" data-raw-source="[Exception Conditions that Terminate Coalescing](exception-conditions-that-terminate-coalescing.md)">Exception Conditions that Terminate Coalescing</a>. Datagrams should be coalesced if they all have the same values for the ECN bits.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Total Length</strong></p></td>
<td align="left"><p>The value of this field must be recomputed every time a new segment with non-zero TCP payload length is coalesced into an existing SCU. See <a href="exception-conditions-that-terminate-coalescing.md" data-raw-source="[Exception Conditions that Terminate Coalescing](exception-conditions-that-terminate-coalescing.md)">Exception Conditions that Terminate Coalescing</a> for special cases that arise from the value in this field.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Identification</strong></p></td>
<td align="left"><p>Must be set to the IP ID of the first coalesced segment.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Flags</strong></p></td>
<td align="left"><ul>
<li><p>Datagrams may be coalesced as long as they have the same value for the DF (Don’t Fragment) bit: either all set or all clear.</p></li>
<li><p>Segments with the MF (More Fragments) bit set must not be coalesced.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Fragment Offset</strong></p></td>
<td align="left"><p>Not applicable. Fragmented IP datagrams are not coalesced.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Time To Live</strong></p></td>
<td align="left"><p>Must be set to the minimum time to live (TTL) value of the coalesced segments.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Protocol</strong></p></td>
<td align="left"><p>Always set to 6, for TCP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Header Checksum</strong></p></td>
<td align="left"><p>The value of this field must be recomputed by the miniport driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Source Address</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Destination Address</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
</tbody>
</table>

 

## Updating IPv6 header fields for coalesced segments


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Version</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Traffic Class</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Flow Label</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Payload Length</strong></p></td>
<td align="left"><p>The value of this field must be recomputed whenever a new segment with nonzero TCP payload length is coalesced into an existing segment.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Next Header</strong></p></td>
<td align="left"><p>Always set to 6, for TCP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hop Limit</strong></p></td>
<td align="left"><p>Must be set to the minimum <strong>Hop Limit</strong> value of the coalesced segments.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Source Address</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination Address</strong></p></td>
<td align="left"><p>The value of this field must be the same for all coalesced segments.</p></td>
</tr>
</tbody>
</table>

 

 

 





