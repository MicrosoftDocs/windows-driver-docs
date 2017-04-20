---
title: Example Connectionless (802.3) Initialization Sequence
description: Example Connectionless (802.3) Initialization Sequence
ms.assetid: 9625f717-81c3-460b-83e8-c7a86aa85f36
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example Connectionless (802.3) Initialization Sequence


## <a href="" id="ddk-example-connectionless-802-3-initialization-sequence-ng"></a>


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
<td align="left"><p>[<strong>REMOTE_NDIS_INITIALIZE_MSG</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570624)</p></td>
<td align="left"></td>
<td align="left"><p>Hosts sends Remote NDIS Initialization message to device.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>[<strong>REMOTE_NDIS_INITIALIZE_CMPLT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570621)</p></td>
<td align="left"><p>Device response with Initialize Complete message.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Receiving. Successful Initialization</p></td>
<td align="left"></td>
<td align="left"><p>Host starts accepting data on incoming data channel. (Example: on USB starts doing reads on IN pipe).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>REMOTE_NDIS_QUERY_MSG</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570641)</p>
<p>AND</p>
<p>[<strong>REMOTE_NDIS_SET_MSG</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570654)</p></td>
<td align="left"><p>[<strong>REMOTE_NDIS_QUERY_CMPLT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570638)</p>
<p>OR</p>
<p>[<strong>REMOTE_NDIS_SET_CMPLT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570651)</p></td>
<td align="left"><p>Host initiates a series of sets and queries to determine state of device and to setup initial parameters. The device responses appropriately with the correct complete messages. The following NDIS OIDs may be queried: [OID_802_3_CURRENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569069), [OID_802_3_MAXIMUM_LIST_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569072), and so on.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>REMOTE_NDIS_SET_MSG</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570654)</p></td>
<td align="left"></td>
<td align="left"><p>Host sends an [OID_GEN_CURRENT_PACKET_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575) OID with a nonzero filter value to the device. At this point the device should start sending data packets on the incoming data channel. The host will also start sending data packets on the outgoing data channel.</p></td>
</tr>
</tbody>
</table>

 

 

 





