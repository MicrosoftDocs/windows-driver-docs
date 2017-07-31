---
title: 'REMOTE\_NDIS\_KEEPALIVE\_CMPLT'
author: windows-driver-content
Description: 'A Remote NDIS device will respond to a REMOTE\_NDIS\_KEEPALIVE\_MSG message from the host by sending back a REMOTE\_NDIS\_KEEPALIVE\_CMPLT response message.'
ms.assetid: c090b781-73f1-4a7a-a0a2-60af366daa77
ms.author: windowsdriverdev
ms.date: 07/31/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>Specifies the current status of the device. If the returned <em>Status</em> is not RNDIS_STATUS_SUCCESS, the host will send an [<strong>REMOTE_NDIS_RESET_MSG</strong>](remote-ndis-reset-msg.md) message to reset the device.</p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20REMOTE_NDIS_KEEPALIVE_CMPLT%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


