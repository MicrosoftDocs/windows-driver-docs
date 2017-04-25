---
title: Remote NDIS Control Messages
description: Remote NDIS Control Messages
ms.assetid: aefeb07c-f77e-40ca-adbd-fcc724a764aa
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Remote NDIS Control Messages


## <a href="" id="ddk-remote-ndis-control-messages-ng"></a>


Remote NDIS control messages are sent by the host to the Remote NDIS device and by the Remote NDIS device to the host. All Remote NDIS control messages indicate the type of message being sent and the total length of the message, from the beginning of the message.

The following Remote NDIS control messages must be supported by an Ethernet 802.3 connectionless device.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Message Identifier</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[REMOTE_NDIS_INITIALIZE_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570624)</p></td>
<td align="left"><p>0x00000002</p></td>
<td align="left"><p>Initialize the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[REMOTE_NDIS_INITIALIZE_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570621)</p></td>
<td align="left"><p>0x80000002</p></td>
<td align="left"><p>Device response to initialization request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[REMOTE_NDIS_HALT_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570613)</p></td>
<td align="left"><p>0x00000003</p></td>
<td align="left"><p>Halt the device. This is the only host control message that doesn't get a response.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[REMOTE_NDIS_QUERY_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570641)</p></td>
<td align="left"><p>0x00000004</p></td>
<td align="left"><p>Send a 'query' OID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[REMOTE_NDIS_QUERY_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570638)</p></td>
<td align="left"><p>0x80000004</p></td>
<td align="left"><p>Device response to 'query' OID request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[REMOTE_NDIS_SET_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570654)</p></td>
<td align="left"><p>0x00000005</p></td>
<td align="left"><p>Send a 'set' OID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[REMOTE_NDIS_SET_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570651)</p></td>
<td align="left"><p>0x80000005</p></td>
<td align="left"><p>Device response to 'set' OID request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[REMOTE_NDIS_RESET_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570648)</p></td>
<td align="left"><p>0x00000006</p></td>
<td align="left"><p>Perform a soft reset on the device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[REMOTE_NDIS_RESET_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570645)</p></td>
<td align="left"><p>0x80000006</p></td>
<td align="left"><p>Device responses to reset request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[REMOTE_NDIS_INDICATE_STATUS_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570617)</p></td>
<td align="left"><p>0x00000007</p></td>
<td align="left"><p>Indicates 802.3 link state or undefined message error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[REMOTE_NDIS_KEEPALIVE_MSG](https://msdn.microsoft.com/library/windows/hardware/ff570629)</p></td>
<td align="left"><p>0x00000008</p></td>
<td align="left"><p>During idle periods, sent every few seconds to check that the device is still responsive (may optionally also be sent by the device).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[REMOTE_NDIS_KEEPALIVE_CMPLT](https://msdn.microsoft.com/library/windows/hardware/ff570626)</p></td>
<td align="left"><p>0x80000008</p></td>
<td align="left"><p>Device response to keep alive message.</p></td>
</tr>
</tbody>
</table>

 

For more details on these messages, see [Remote NDIS Control Messages Reference](https://msdn.microsoft.com/library/windows/hardware/ff570597).

 

 





