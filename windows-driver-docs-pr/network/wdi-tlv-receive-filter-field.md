---
title: WDI_TLV_RECEIVE_FILTER_FIELD (0x65)
description: WDI_TLV_RECEIVE_FILTER_FIELD is a TLV that contains a receive filter test criterion for one field in a network header.
ms.assetid: 9037CD08-742E-4A99-A37B-9969A2BC666A
ms.date: 07/18/2017
keywords:
 - WDI_TLV_RECEIVE_FILTER_FIELD (0x65) Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_RECEIVE\_FILTER\_FIELD (0x65)


WDI\_TLV\_RECEIVE\_FILTER\_FIELD is a TLV that contains a receive filter test criterion for one field in a network header.

## TLV Type


0x65

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT32</td>
<td>Specifies a bitwise OR of flags. The possible flag value is WDI_RECEIVE_FILTER_FIELD_MAC_HEADER_VLAN_UNTAGGED_OR_ZERO. If this flag is set, the network adapter must only indicate received packets that pass the following criteria:
<ul>
<li>The packet&#39;s MAC address matches the specified MAC header field test.</li>
<li>The packet either does not contain a VLAN tag or has a VLAN tag with an ID of zero.</li>
</ul></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff565581" data-raw-source="[&lt;strong&gt;NDIS_FRAME_HEADER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565581)"><strong>NDIS_FRAME_HEADER</strong></a> (UINT32)</td>
<td>Frame header. Specifies the type of the frame header.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff567183" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_TEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567183)"><strong>NDIS_RECEIVE_FILTER_TEST</strong></a> (UINT32)</td>
<td>Receive filter test. Specifies the type of test that the receive filter performs.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Header field. Specifies the protocol-specific header field type with the union as documented in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567169" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_FIELD_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567169)"><strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong></a>.HeaderField.</td>
</tr>
<tr class="odd">
<td>UINT8[16]</td>
<td>Field value. Specifies the value that the miniport adapter compares to the corresponding header field value in incoming packets. The location of the header field value is determined by the field type that is specified in the <em>header field</em> element. This value is in network byte order and is specified with the union as documented in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567169" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_FIELD_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567169)"><strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong></a>.FieldValue.</td>
</tr>
<tr class="even">
<td>UINT8[16]</td>
<td>Test result value. If the <em>receive filter test</em> element is set to ReceiveFilterTestMaskEqual, the network adapter first calculates a result from the value in the <em>field value</em> member and the header field value as specified by the <em>header field</em> member. The adapter then compares the calculated result with <em>result value</em>. This value is specified with the union as documented in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567169" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_FIELD_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567169)"><strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong></a>.ResultValue.</td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




