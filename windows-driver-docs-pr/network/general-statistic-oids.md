---
title: General Statistic OIDs
description: General Statistic OIDs
ms.assetid: ebdd5723-d913-4c1a-8b1f-f70e4b0080ad
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# General Statistic OIDs


## <a href="" id="ddk-general-statistic-oids-ng"></a>


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
<td align="left"><p>[OID_GEN_XMIT_OK](https://msdn.microsoft.com/library/windows/hardware/ff569656)</p></td>
<td align="left"><p>Frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_RCV_OK](https://msdn.microsoft.com/library/windows/hardware/ff569632)</p></td>
<td align="left"><p>Frames received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_XMIT_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569654)</p></td>
<td align="left"><p>Frames transmitted with errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_RCV_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569629)</p></td>
<td align="left"><p>Frames received with errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Required</p></td>
<td align="left"><p>[OID_GEN_RCV_NO_BUFFER](https://msdn.microsoft.com/library/windows/hardware/ff569631)</p></td>
<td align="left"><p>Frame missed, no buffers</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_DIRECTED_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569578)</p></td>
<td align="left"><p>Directed bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_DIRECTED_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569580)</p></td>
<td align="left"><p>Directed frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_MULTICAST_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569612)</p></td>
<td align="left"><p>Multicast bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_MULTICAST_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569614)</p></td>
<td align="left"><p>Multicast frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_BROADCAST_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569440)</p></td>
<td align="left"><p>Broadcast bytes transmitted without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_BROADCAST_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569442)</p></td>
<td align="left"><p>Broadcast frames transmitted without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_DIRECTED_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569577)</p></td>
<td align="left"><p>Directed bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_DIRECTED_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569579)</p></td>
<td align="left"><p>Directed frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_MULTICAST_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569611)</p></td>
<td align="left"><p>Multicast bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_MULTICAST_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569613)</p></td>
<td align="left"><p>Multicast frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_BROADCAST_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569439)</p></td>
<td align="left"><p>Broadcast bytes received without errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_BROADCAST_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569441)</p></td>
<td align="left"><p>Broadcast frames received without errors</p></td>
</tr>
<tr class="even">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_RCV_CRC_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569627)</p></td>
<td align="left"><p>Frames received with circular redundancy check (CRC) or frame check sequence (FCS) errors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Optional</p></td>
<td align="left"><p>[OID_GEN_TRANSMIT_QUEUE_LENGTH](https://msdn.microsoft.com/library/windows/hardware/ff569646)</p></td>
<td align="left"><p>Length of transmit queue</p></td>
</tr>
</tbody>
</table>

 

 

 





