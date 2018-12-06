---
title: 'REMOTE_NDIS_KEEPALIVE_CMPLT'
Description: 'A Remote NDIS device will respond to a REMOTE_NDIS_KEEPALIVE_MSG message from the host by sending back a REMOTE_NDIS_KEEPALIVE_CMPLT response message.'
ms.assetid: c090b781-73f1-4a7a-a0a2-60af366daa77
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_KEEPALIVE\_CMPLT


A Remote NDIS device will respond to a [**REMOTE\_NDIS\_KEEPALIVE\_MSG**](remote-ndis-keepalive-msg.md) message from the host by sending back a REMOTE\_NDIS\_KEEPALIVE\_CMPLT response message. If the returned Status is not RNDIS\_STATUS\_SUCCESS, the host will send [**REMOTE\_NDIS\_RESET\_MSG**](remote-ndis-reset-msg.md) to reset the device.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Offset</th>
<th>Size</th>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>4</p></td>
<td><p>MessageType</p></td>
<td><p>Specifies the type of message being sent. Set to 0x80000008.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>MessageLength</p></td>
<td><p>Specifies, in bytes, the total length of this message, from the beginning of the message.</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>4</p></td>
<td><p>RequestId</p></td>
<td><p>Specifies the Remote NDIS message ID value. This value is used to match messages sent by the host with device responses.</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>Status</p></td>
<td><p>Specifies the current status of the device. If the returned <em>Status</em> is not RNDIS_STATUS_SUCCESS, the host will send an <a href="remote-ndis-reset-msg.md" data-raw-source="[&lt;strong&gt;REMOTE_NDIS_RESET_MSG&lt;/strong&gt;](remote-ndis-reset-msg.md)"><strong>REMOTE_NDIS_RESET_MSG</strong></a> message to reset the device.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If the device implements the option of sending [**REMOTE\_NDIS\_KEEPALIVE\_MSG**](remote-ndis-keepalive-msg.md), the host will respond with REMOTE\_NDIS\_KEEPALIVE\_CMPLT through the control channel.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Microsoft Windows XP and later versions of the Windows operating systems. Also available in Windows 2000 as redistributable binaries.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Rndis.h (include Rndis.h)</td>
</tr>
</tbody>
</table>

 

 




