---
title: General Statistic OIDs
description: General Statistic OIDs
ms.assetid: ebdd5723-d913-4c1a-8b1f-f70e4b0080ad
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Statistic OIDs





The following table lists the general statistic OIDs for Remote NDIS Ethernet devices.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Support</th>
<th align="left">OID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-ok" data-raw-source="[OID_GEN_XMIT_OK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-ok)">OID_GEN_XMIT_OK</a></p></td>
<td align="left"><p>Frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-ok" data-raw-source="[OID_GEN_RCV_OK](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-ok)">OID_GEN_RCV_OK</a></p></td>
<td align="left"><p>Frames received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-error" data-raw-source="[OID_GEN_XMIT_ERROR](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-xmit-error)">OID_GEN_XMIT_ERROR</a></p></td>
<td align="left"><p>Frames transmitted with errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-error" data-raw-source="[OID_GEN_RCV_ERROR](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-error)">OID_GEN_RCV_ERROR</a></p></td>
<td align="left"><p>Frames received with errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-no-buffer" data-raw-source="[OID_GEN_RCV_NO_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-no-buffer)">OID_GEN_RCV_NO_BUFFER</a></p></td>
<td align="left"><p>Frame missed, no buffers</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-bytes-xmit" data-raw-source="[OID_GEN_DIRECTED_BYTES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-bytes-xmit)">OID_GEN_DIRECTED_BYTES_XMIT</a></p></td>
<td align="left"><p>Directed bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-frames-xmit" data-raw-source="[OID_GEN_DIRECTED_FRAMES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-frames-xmit)">OID_GEN_DIRECTED_FRAMES_XMIT</a></p></td>
<td align="left"><p>Directed frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-bytes-xmit" data-raw-source="[OID_GEN_MULTICAST_BYTES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-bytes-xmit)">OID_GEN_MULTICAST_BYTES_XMIT</a></p></td>
<td align="left"><p>Multicast bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-frames-xmit" data-raw-source="[OID_GEN_MULTICAST_FRAMES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-frames-xmit)">OID_GEN_MULTICAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>Multicast frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-bytes-xmit" data-raw-source="[OID_GEN_BROADCAST_BYTES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-bytes-xmit)">OID_GEN_BROADCAST_BYTES_XMIT</a></p></td>
<td align="left"><p>Broadcast bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-frames-xmit" data-raw-source="[OID_GEN_BROADCAST_FRAMES_XMIT](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-frames-xmit)">OID_GEN_BROADCAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>Broadcast frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-bytes-rcv" data-raw-source="[OID_GEN_DIRECTED_BYTES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-bytes-rcv)">OID_GEN_DIRECTED_BYTES_RCV</a></p></td>
<td align="left"><p>Directed bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-frames-rcv" data-raw-source="[OID_GEN_DIRECTED_FRAMES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-directed-frames-rcv)">OID_GEN_DIRECTED_FRAMES_RCV</a></p></td>
<td align="left"><p>Directed frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-bytes-rcv" data-raw-source="[OID_GEN_MULTICAST_BYTES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-bytes-rcv)">OID_GEN_MULTICAST_BYTES_RCV</a></p></td>
<td align="left"><p>Multicast bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-frames-rcv" data-raw-source="[OID_GEN_MULTICAST_FRAMES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-multicast-frames-rcv)">OID_GEN_MULTICAST_FRAMES_RCV</a></p></td>
<td align="left"><p>Multicast frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-bytes-rcv" data-raw-source="[OID_GEN_BROADCAST_BYTES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-bytes-rcv)">OID_GEN_BROADCAST_BYTES_RCV</a></p></td>
<td align="left"><p>Broadcast bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-frames-rcv" data-raw-source="[OID_GEN_BROADCAST_FRAMES_RCV](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-broadcast-frames-rcv)">OID_GEN_BROADCAST_FRAMES_RCV</a></p></td>
<td align="left"><p>Broadcast frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-crc-error" data-raw-source="[OID_GEN_RCV_CRC_ERROR](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-rcv-crc-error)">OID_GEN_RCV_CRC_ERROR</a></p></td>
<td align="left"><p>Frames received with circular redundancy check (CRC) or frame check sequence (FCS) errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-transmit-queue-length" data-raw-source="[OID_GEN_TRANSMIT_QUEUE_LENGTH](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-transmit-queue-length)">OID_GEN_TRANSMIT_QUEUE_LENGTH</a></p></td>
<td align="left"><p>Length of transmit queue</p></td>
</tr>
</tbody>
</table>

 

 

 





