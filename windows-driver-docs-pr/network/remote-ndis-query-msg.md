---
title: 'REMOTE\_NDIS\_QUERY\_MSG'
author: windows-driver-content
Description: 'This message is sent to a Remote NDIS device from a host when it needs to query the device for its characteristics, statistics information, or status.'
ms.assetid: 9cf79495-a115-49ce-a0cf-fa4fa2183a8a
ms.author: windowsdriverdev
ms.date: 07/31/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20REMOTE_NDIS_QUERY_MSG%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


