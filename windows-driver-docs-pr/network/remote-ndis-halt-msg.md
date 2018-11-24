---
title: 'REMOTE_NDIS_HALT_MSG'
Description: 'This message is sent by the host to terminate the network connection.'
ms.assetid: ad7802ff-20ee-4228-b236-a2ca39e8c478
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_HALT\_MSG


This message is sent by the host to terminate the network connection. Unlike the other host-initiated control messages, the device does not respond to REMOTE\_NDIS\_HALT\_MSG.

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
<td><p>Specifies the type of message being sent. Set to 0x00000003.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>MessageLength</p></td>
<td><p>Specifies in bytes the total length of this message from the beginning of the message.</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>4</p></td>
<td><p>RequestId</p></td>
<td><p>Specifies the Remote NDIS message ID value. This value is used to match messages sent by the host with device responses.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

It is optional for the device to implement REMOTE\_NDIS\_HALT\_MSG. If implemented, the device sends this message to the host through the control channel only when the device is in a state initialized by Remote NDIS. The device must terminate all communication immediately after sending this message. Sending this message causes the device to enter a state not initialized by Remote NDIS.

All outstanding requests and packets should be discarded on receipt of this message.

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

 

 




