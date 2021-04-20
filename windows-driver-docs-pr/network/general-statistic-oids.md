---
title: General Statistic OIDs
description: General Statistic OIDs
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
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-xmit-ok" data-raw-source="[OID_GEN_XMIT_OK](./oid-gen-xmit-ok.md)">OID_GEN_XMIT_OK</a></p></td>
<td align="left"><p>Frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-rcv-ok" data-raw-source="[OID_GEN_RCV_OK](./oid-gen-rcv-ok.md)">OID_GEN_RCV_OK</a></p></td>
<td align="left"><p>Frames received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-xmit-error" data-raw-source="[OID_GEN_XMIT_ERROR](./oid-gen-xmit-error.md)">OID_GEN_XMIT_ERROR</a></p></td>
<td align="left"><p>Frames transmitted with errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-rcv-error" data-raw-source="[OID_GEN_RCV_ERROR](./oid-gen-rcv-error.md)">OID_GEN_RCV_ERROR</a></p></td>
<td align="left"><p>Frames received with errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-rcv-no-buffer" data-raw-source="[OID_GEN_RCV_NO_BUFFER](./oid-gen-rcv-no-buffer.md)">OID_GEN_RCV_NO_BUFFER</a></p></td>
<td align="left"><p>Frame missed, no buffers</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-directed-bytes-xmit" data-raw-source="[OID_GEN_DIRECTED_BYTES_XMIT](./oid-gen-directed-bytes-xmit.md)">OID_GEN_DIRECTED_BYTES_XMIT</a></p></td>
<td align="left"><p>Directed bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-directed-frames-xmit" data-raw-source="[OID_GEN_DIRECTED_FRAMES_XMIT](./oid-gen-directed-frames-xmit.md)">OID_GEN_DIRECTED_FRAMES_XMIT</a></p></td>
<td align="left"><p>Directed frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-multicast-bytes-xmit" data-raw-source="[OID_GEN_MULTICAST_BYTES_XMIT](./oid-gen-multicast-bytes-xmit.md)">OID_GEN_MULTICAST_BYTES_XMIT</a></p></td>
<td align="left"><p>Multicast bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-multicast-frames-xmit" data-raw-source="[OID_GEN_MULTICAST_FRAMES_XMIT](./oid-gen-multicast-frames-xmit.md)">OID_GEN_MULTICAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>Multicast frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-bytes-xmit" data-raw-source="[OID_GEN_BROADCAST_BYTES_XMIT](./oid-gen-broadcast-bytes-xmit.md)">OID_GEN_BROADCAST_BYTES_XMIT</a></p></td>
<td align="left"><p>Broadcast bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-frames-xmit" data-raw-source="[OID_GEN_BROADCAST_FRAMES_XMIT](./oid-gen-broadcast-frames-xmit.md)">OID_GEN_BROADCAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>Broadcast frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-directed-bytes-rcv" data-raw-source="[OID_GEN_DIRECTED_BYTES_RCV](./oid-gen-directed-bytes-rcv.md)">OID_GEN_DIRECTED_BYTES_RCV</a></p></td>
<td align="left"><p>Directed bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-directed-frames-rcv" data-raw-source="[OID_GEN_DIRECTED_FRAMES_RCV](./oid-gen-directed-frames-rcv.md)">OID_GEN_DIRECTED_FRAMES_RCV</a></p></td>
<td align="left"><p>Directed frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-multicast-bytes-rcv" data-raw-source="[OID_GEN_MULTICAST_BYTES_RCV](./oid-gen-multicast-bytes-rcv.md)">OID_GEN_MULTICAST_BYTES_RCV</a></p></td>
<td align="left"><p>Multicast bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-multicast-frames-rcv" data-raw-source="[OID_GEN_MULTICAST_FRAMES_RCV](./oid-gen-multicast-frames-rcv.md)">OID_GEN_MULTICAST_FRAMES_RCV</a></p></td>
<td align="left"><p>Multicast frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-bytes-rcv" data-raw-source="[OID_GEN_BROADCAST_BYTES_RCV](./oid-gen-broadcast-bytes-rcv.md)">OID_GEN_BROADCAST_BYTES_RCV</a></p></td>
<td align="left"><p>Broadcast bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-frames-rcv" data-raw-source="[OID_GEN_BROADCAST_FRAMES_RCV](./oid-gen-broadcast-frames-rcv.md)">OID_GEN_BROADCAST_FRAMES_RCV</a></p></td>
<td align="left"><p>Broadcast frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-rcv-crc-error" data-raw-source="[OID_GEN_RCV_CRC_ERROR](./oid-gen-rcv-crc-error.md)">OID_GEN_RCV_CRC_ERROR</a></p></td>
<td align="left"><p>Frames received with circular redundancy check (CRC) or frame check sequence (FCS) errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-transmit-queue-length" data-raw-source="[OID_GEN_TRANSMIT_QUEUE_LENGTH](./oid-gen-transmit-queue-length.md)">OID_GEN_TRANSMIT_QUEUE_LENGTH</a></p></td>
<td align="left"><p>Length of transmit queue</p></td>
</tr>
</tbody>
</table>

 

