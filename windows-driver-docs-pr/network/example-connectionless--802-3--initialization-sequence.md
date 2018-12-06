---
title: Example Connectionless (802.3) Initialization Sequence
description: Example Connectionless (802.3) Initialization Sequence
ms.assetid: 9625f717-81c3-460b-83e8-c7a86aa85f36
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example Connectionless (802.3) Initialization Sequence





This section describes the general order of events that a device can expect upon startup as a Remote NDIS connectionless device. Because the basic operation of Remote NDIS is the same, regardless of the underlying bus, the require bus enumeration and start up process has been left out of the example.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Host</th>
<th align="left">Device</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570624" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_INITIALIZE_MSG&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570624)"><strong>REMOTE_NDIS_INITIALIZE_MSG</strong></a></p></td>
<td align="left"></td>
<td align="left"><p>Hosts sends Remote NDIS Initialization message to device.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570621" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_INITIALIZE_CMPLT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570621)"><strong>REMOTE_NDIS_INITIALIZE_CMPLT</strong></a></p></td>
<td align="left"><p>Device response with Initialize Complete message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Receiving. Successful Initialization</p></td>
<td align="left"></td>
<td align="left"><p>Host starts accepting data on incoming data channel. (Example: on USB starts doing reads on IN pipe).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570641" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_QUERY_MSG&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570641)"><strong>REMOTE_NDIS_QUERY_MSG</strong></a></p>
<p>AND</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570654" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_SET_MSG&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570654)"><strong>REMOTE_NDIS_SET_MSG</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570638" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_QUERY_CMPLT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570638)"><strong>REMOTE_NDIS_QUERY_CMPLT</strong></a></p>
<p>OR</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570651" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_SET_CMPLT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570651)"><strong>REMOTE_NDIS_SET_CMPLT</strong></a></p></td>
<td align="left"><p>Host initiates a series of sets and queries to determine state of device and to setup initial parameters. The device responses appropriately with the correct complete messages. The following NDIS OIDs may be queried: <a href="https://msdn.microsoft.com/library/windows/hardware/ff569069" data-raw-source="[OID_802_3_CURRENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569069)">OID_802_3_CURRENT_ADDRESS</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff569072" data-raw-source="[OID_802_3_MAXIMUM_LIST_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569072)">OID_802_3_MAXIMUM_LIST_SIZE</a>, and so on.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570654" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_SET_MSG&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570654)"><strong>REMOTE_NDIS_SET_MSG</strong></a></p></td>
<td align="left"></td>
<td align="left"><p>Host sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff569575" data-raw-source="[OID_GEN_CURRENT_PACKET_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575)">OID_GEN_CURRENT_PACKET_FILTER</a> OID with a nonzero filter value to the device. At this point the device should start sending data packets on the incoming data channel. The host will also start sending data packets on the outgoing data channel.</p></td>
</tr>
</tbody>
</table>

 

 

 





