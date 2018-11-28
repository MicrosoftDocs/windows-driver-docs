---
title: 'REMOTE_NDIS_RESET_CMPLT'
Description: 'A Remote NDIS device will respond to a REMOTE_NDIS_RESET_MSG message from the host by resetting the device and returning the status of the request in the REMOTE_NDIS_RESET_CMPLT message.'
ms.assetid: 80ab998f-9690-49d3-bb47-1937c832d13e
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_RESET\_CMPLT


A Remote NDIS device will respond to a [**REMOTE\_NDIS\_RESET\_MSG**](remote-ndis-reset-msg.md) message from the host by resetting the device and returning the status of the request in the REMOTE\_NDIS\_RESET\_CMPLT message.

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
<td><p>Specifies the type of message being sent. Set to 0x80000006.</p></td>
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
<td><p>Status</p></td>
<td><p>Specifies the status of processing the Reset request.</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>AddressingReset</p></td>
<td><p>Indicates if addressing information (multicast address list, packet filter) has been lost during the concluded reset operation. If the device requires the host to resend addressing information, set this field to one; otherwise set it to zero.</p></td>
</tr>
</tbody>
</table>

 

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

 

 




