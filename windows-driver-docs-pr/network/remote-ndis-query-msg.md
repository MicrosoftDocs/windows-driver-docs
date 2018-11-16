---
title: 'REMOTE_NDIS_QUERY_MSG'
Description: 'This message is sent to a Remote NDIS device from a host when it needs to query the device for its characteristics, statistics information, or status.'
ms.assetid: 9cf79495-a115-49ce-a0cf-fa4fa2183a8a
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_QUERY\_MSG


This message is sent to a Remote NDIS device from a host when it needs to query the device for its characteristics, statistics information, or status. The parameter or statistics counter being queried for is identified by means of an NDIS Object Identifier (OID). The host may send REMOTE\_NDIS\_QUERY\_MSG to the device through the control channel at any time that the device is in either a state initialized by Remote NDIS. The Remote NDIS device will respond to this message by sending a REMOTE\_NDIS\_QUERY\_CMPLT to the host.

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
<td><p>Specifies the type of message being sent. Set to 0x00000004.</p></td>
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
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>Oid</p></td>
<td><p>Specifies the NDIS OID that identifies the parameter being queried.</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>4</p></td>
<td><p>InformationBufferLength</p></td>
<td><p>Specifies in bytes the length of the input data for the query. Set to zero when there is no OID input buffer.</p></td>
</tr>
<tr class="even">
<td><p>20</p></td>
<td><p>4</p></td>
<td><p>InformationBufferOffset</p></td>
<td><p>Specifies the byte offset, from the beginning of the <em>RequestId</em> field, at which input data for the query is located. Set to zero if there is no OID input buffer.</p></td>
</tr>
<tr class="odd">
<td><p>24</p></td>
<td><p>4</p></td>
<td><p>DeviceVcHandle</p></td>
<td><p>Reserved for connection-oriented devices. Set to zero.</p></td>
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

 

 




