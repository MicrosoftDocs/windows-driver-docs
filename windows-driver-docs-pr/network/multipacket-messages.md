---
title: Multipacket Messages
description: Multipacket Messages
ms.assetid: 58979799-4618-43b9-a6dc-0635f6ade9b3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multipacket Messages





Multiple [**REMOTE\_NDIS\_PACKET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570635) messages may be sent in a single transfer, in either direction. A multipacket message is formed by concatenating multiple **REMOTE\_NDIS\_PACKET\_MSG** elements. The maximum length of such a transfer is governed by the *MaxTransferSize* parameter passed in the [**REMOTE\_NDIS\_INITIALIZE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570624) and response messages. The host will also limit the number of messages it bundles into a single transfer to the *MaxPacketsPerMessage* parameter returned by the device in the [**REMOTE\_NDIS\_INITIALIZE\_CMPLT**](https://msdn.microsoft.com/library/windows/hardware/ff570621) response message.

The difference from the single-packet message case is that the *MessageLength* field in each [**REMOTE\_NDIS\_PACKET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570635) header includes some additional padding bytes. These padding bytes are added to all but the last **REMOTE\_NDIS\_PACKET\_MSG** such that the succeeding REMOTE\_NDIS\_PACKET\_MSG starts at an appropriate byte boundary. For messages sent from the device to the host, this padding should result in each REMOTE\_NDIS\_PACKET\_MSG starting at a byte offset that is a multiple of 8 bytes starting from the beginning of the multipacket message. When the host sends a multipacket message to the device, it will adhere to the *PacketAlignmentFactor* specified by the device in the [**REMOTE\_NDIS\_INITIALIZE\_CMPLT**](https://msdn.microsoft.com/library/windows/hardware/ff570621) response message.

Note that neither the combined length of a multipacket message nor the number of [**REMOTE\_NDIS\_PACKET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570635) elements in a combined message is given explicitly in any Remote NDIS defined field. The combined length is implicit in the bus-specific transfer mechanism, and the host or device must walk the *MessageLength* fields of the combined message to determine the number of combined messages.

The following table is an example of a multipacket message that is made up of two REMOTE\_NDIS\_PACKET\_MSGs, sent from the host to the device. During the [**REMOTE\_NDIS\_INITIALIZE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570624) exchange, the device requested a *PacketAlignmentFactor* of 3 (an alignment along an 8-byte boundary).

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset</th>
<th align="left">Size</th>
<th align="left">Field</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>MessageType</p></td>
<td align="left"><p>0x1</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>MessageLength</p></td>
<td align="left"><p>72 (includes 2 padding bytes; see below)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>8</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>DataOffset</p></td>
<td align="left"><p>36</p></td>
</tr>
<tr class="even">
<td align="left"><p>12</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>DataLength</p></td>
<td align="left"><p>26</p></td>
</tr>
<tr class="odd">
<td align="left"><p>16</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>OOBDataOffset</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>20</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>OOBDataLength</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>24</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>NumOOBDataElements</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>28</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>PerPacketInfoOffset</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>32</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>PerPacketInfoLength</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>36</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>VcHandle</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>40</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>44</p></td>
<td align="left"><p>26</p></td>
<td align="left"><p>Payload (data)</p></td>
<td align="left"><p>Some network data of 26 bytes in length</p></td>
</tr>
<tr class="odd">
<td align="left"><p>70</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>Padding</p></td>
<td align="left"><p>Doesn&#39;t matter - unused</p></td>
</tr>
<tr class="even">
<td align="left"><p>72</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>MessageType (start of second <a href="https://msdn.microsoft.com/library/windows/hardware/ff570635" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_PACKET_MSG&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570635)"><strong>REMOTE_NDIS_PACKET_MSG</strong></a>)</p></td>
<td align="left"><p>0x1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>76</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>MessageLength</p></td>
<td align="left"><p>60</p></td>
</tr>
<tr class="even">
<td align="left"><p>80</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>DataOffset</p></td>
<td align="left"><p>36</p></td>
</tr>
<tr class="odd">
<td align="left"><p>84</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>DataLength</p></td>
<td align="left"><p>16</p></td>
</tr>
<tr class="even">
<td align="left"><p>88</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>OOBDataOffset</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>92</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>OOBDataLength</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>96</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>NumOOBDataElements</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>100</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>PerPacketInfoOffset</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>104</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>PerPacketInfoLength</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>108</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>VcHandle</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>112</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>116</p></td>
<td align="left"><p>16</p></td>
<td align="left"><p>Payload (data)</p></td>
<td align="left"><p>Some network data of 16 bytes in length</p></td>
</tr>
</tbody>
</table>

 

 

 





