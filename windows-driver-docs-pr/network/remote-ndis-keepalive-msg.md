---
title: 'REMOTE\_NDIS\_KEEPALIVE\_MSG'
author: windows-driver-content
Description: 'The host sends this message periodically when there has been no other control or data traffic from the device to the host for the bus-defined KeepAliveTimeoutPeriod.'
ms.assetid: 7e0b329f-8ba7-488d-b99d-63e6b9bbc171
ms.author: windowsdriverdev
ms.date: 07/31/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_KEEPALIVE\_MSG


The host sends this message periodically when there has been no other control or data traffic from the device to the host for the bus-defined *KeepAliveTimeoutPeriod*. This message is sent by the host at least every RNDIS\_KEEPALIVE\_TIMEOUT seconds, in the absence of other message traffic, to detect the state of the remote device. The remote device may use the same message in the reverse direction, but it is not required.

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
<td><p>Specifies the type of message being sent. Set to 0x00000008.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>MessageLength</p></td>
<td><p>Specifies in bytes the total length of this message, from the beginning of the message.</p></td>
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

The host will not send a REMOTE\_NDIS\_KEEPALIVE\_MSG message until RNDIS\_KEEPALIVE\_TIMEOUT seconds have elapsed since the last message received from the remote device. This avoids unnecessary exchange of keep-alive messages when the communication channel is active.

The device can optionally send this message to the host as well. For example, the device may use this message to trigger a response from the host for computing round-trip delay time. If implemented, the device must send REMOTE\_NDIS\_KEEPALIVE\_MSG through the control channel and only when the device is in a state initialized by Remote NDIS.

The host sends a **REMOTE\_NDIS\_KEEPALIVE\_MSG** message to the device through the control channel to check the health of the device. When the device is in a state initialized by Remote NDIS, the host sends this message periodically when there has been no other control or data traffic from the device to the host for the *KeepAliveTimeoutPeriod*. *KeepAliveTimeoutPeriod* is bus-dependent and is defined in the appropriate bus-mapping specifications.

Upon receiving this message, the remote device must return a response whose *Status* field indicates whether the device solicits a [**REMOTE\_NDIS\_RESET\_MSG**](remote-ndis-reset-msg.md) message from the host.

The device does not have to perform any specific action if it stops seeing **REMOTE\_NDIS\_KEEPALIVE\_MSG** messages from the host.

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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20REMOTE_NDIS_KEEPALIVE_MSG%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


