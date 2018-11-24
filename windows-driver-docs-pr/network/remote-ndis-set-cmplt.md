---
title: 'REMOTE_NDIS_SET_CMPLT'
Description: 'A Remote NDIS device will respond to a REMOTE_NDIS_SET_MSG message with a REMOTE_NDIS_SET_CMPLT message.'
ms.assetid: 97436a5f-7516-46cf-b789-a6b1c8c067a2
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_SET\_CMPLT


A Remote NDIS device will respond to a [**REMOTE\_NDIS\_SET\_MSG**](remote-ndis-set-msg.md) message with a REMOTE\_NDIS\_SET\_CMPLT message. This message is used to relay the result of setting the value of a device operational parameter to the host.

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
<td><p>Specifies the type of message being sent. Set to 0x80000005.</p></td>
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
<td><p>Specifies the Remote NDIS message ID value. This value is copied from the REMOTE_NDIS_SET_MSG being responded to.</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>Status</p></td>
<td><p>Specifies the status of processing the OID set request.</p></td>
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

 

 




