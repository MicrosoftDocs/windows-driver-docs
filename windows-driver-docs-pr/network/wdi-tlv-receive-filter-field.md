---
title: WDI_TLV_RECEIVE_FILTER_FIELD (0x65)
ms.topic: reference
description: WDI_TLV_RECEIVE_FILTER_FIELD is a TLV that contains a receive filter test criterion for one field in a network header.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_RECEIVE_FILTER_FIELD (0x65) Network Drivers Starting with Windows Vista
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
<li>The packet's MAC address matches the specified MAC header field test.</li>
<li>The packet either does not contain a VLAN tag or has a VLAN tag with an ID of zero.</li>
</ul></td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_frame_header" data-raw-source="[&lt;strong&gt;NDIS_FRAME_HEADER&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_frame_header)"><strong>NDIS_FRAME_HEADER</strong></a> (UINT32)</td>
<td>Frame header. Specifies the type of the frame header.</td>
</tr>
<tr class="odd">
<td><a href="/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_receive_filter_test" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_TEST&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_receive_filter_test)"><strong>NDIS_RECEIVE_FILTER_TEST</strong></a> (UINT32)</td>
<td>Receive filter test. Specifies the type of test that the receive filter performs.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>Header field. Specifies the protocol-specific header field type with the union as documented in the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_FIELD_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters)"><strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong></a>.HeaderField.</td>
</tr>
<tr class="odd">
<td>UINT8[16]</td>
<td>Field value. Specifies the value that the miniport adapter compares to the corresponding header field value in incoming packets. The location of the header field value is determined by the field type that is specified in the <em>header field</em> element. This value is in network byte order and is specified with the union as documented in the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_FIELD_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters)"><strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong></a>.FieldValue.</td>
</tr>
<tr class="even">
<td>UINT8[16]</td>
<td>Test result value. If the <em>receive filter test</em> element is set to ReceiveFilterTestMaskEqual, the network adapter first calculates a result from the value in the <em>field value</em> member and the header field value as specified by the <em>header field</em> member. The adapter then compares the calculated result with <em>result value</em>. This value is specified with the union as documented in the <a href="/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters" data-raw-source="[&lt;strong&gt;NDIS_RECEIVE_FILTER_FIELD_PARAMETERS&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_field_parameters)"><strong>NDIS_RECEIVE_FILTER_FIELD_PARAMETERS</strong></a>.ResultValue.</td>
</tr>
</tbody>
</table>

 

## Requirements

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

