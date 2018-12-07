---
title: 'REMOTE_NDIS_KEEPALIVE_MSG'
Description: 'The host sends this message periodically when there has been no other control or data traffic from the device to the host for the bus-defined KeepAliveTimeoutPeriod.'
ms.assetid: 7e0b329f-8ba7-488d-b99d-63e6b9bbc171
ms.date: 07/31/2017
ms.localizationpriority: medium
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

 

 




