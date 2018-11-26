---
title: 'REMOTE_NDIS_INITIALIZE_CMPLT'
ms.assetid: e1e057bf-aa92-4b90-b993-a82cc260ff7f
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_INITIALIZE\_CMPLT


The REMOTE\_NDIS\_INITIALIZE\_CMPLT message is sent by the Remote NDIS device to the host in response to a [**REMOTE\_NDIS\_INITIALIZE\_MSG**](remote-ndis-initialize-msg.md) message. In the REMOTE\_NDIS\_INITIALIZE\_CMPLT message, the device reports its medium type, Remote NDIS version numbers, and its type (connectionless or connection-oriented or both).

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
<td><p>Specifies the type of message being sent. Set to 0x80000002.</p></td>
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
<td><p>Status</p></td>
<td><p>Specifies RNDIS_STATUS_SUCCESS if the device initialized successfully; otherwise, it specifies an error code that indicates the failure.</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>4</p></td>
<td><p>MajorVersion</p></td>
<td><p>Specifies the highest Remote NDIS major protocol version supported by the device.</p></td>
</tr>
<tr class="even">
<td><p>20</p></td>
<td><p>4</p></td>
<td><p>MinorVersion</p></td>
<td><p>Specifies the highest Remote NDIS minor protocol version supported by the device.</p></td>
</tr>
<tr class="odd">
<td><p>24</p></td>
<td><p>4</p></td>
<td><p>DeviceFlags</p></td>
<td><p>Specifies the miniport driver type as either connectionless or connection-oriented. This value can be one of the following:</p>
<p>RNDIS_DF_CONNECTIONLESS 0x00000001</p>
<p>RNDIS_DF_CONNECTION_ORIENTED 0x00000002</p></td>
</tr>
<tr class="even">
<td><p>28</p></td>
<td><p>4</p></td>
<td><p>Medium</p></td>
<td><p>Specifies the medium supported by the device. Set to RNDIS_MEDIUM_802_3 (0x00000000)</p></td>
</tr>
<tr class="odd">
<td><p>32</p></td>
<td><p>4</p></td>
<td><p>MaxPacketsPerMessage</p></td>
<td><p>Specifies the maximum number of Remote NDIS data messages that the device can handle in a single transfer to it. This value should be at least one.</p></td>
</tr>
<tr class="even">
<td><p>36</p></td>
<td><p>4</p></td>
<td><p>MaxTransferSize</p></td>
<td><p>Specifies the maximum size in bytes of any single bus data transfer that the device expects to receive from the host.</p></td>
</tr>
<tr class="odd">
<td><p>40</p></td>
<td><p>4</p></td>
<td><p>PacketAlignmentFactor</p></td>
<td><p>Specifies the byte alignment that the device expects for each Remote NDIS message that is part of a multimessage transfer to it. This value is specified in powers of 2. For example, this value is set to three to indicate 8-byte alignment. This value has a maximum setting of seven, which specifies 128-byte alignment.</p></td>
</tr>
<tr class="even">
<td><p>44</p></td>
<td><p>4</p></td>
<td><p>AFListOffset</p></td>
<td><p>Reserved for connection-oriented devices. Set value to zero.</p></td>
</tr>
<tr class="odd">
<td><p>48</p></td>
<td><p>4</p></td>
<td><p>AFListSize</p></td>
<td><p>Reserved for connection-oriented devices. Set value to zero.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The *Status* field should be set to RNDIS\_STATUS\_SUCCESS if the device initialized successfully; otherwise, it is set to an error code that indicates the failure. The device should return the highest Remote NDIS protocol version that it can support, in *MajorVersion* and *MinorVersion*--the combined version number should be less than or equal to the version number the host specified in the [**REMOTE\_NDIS\_INITIALIZE\_MSG**](remote-ndis-initialize-msg.md) message.

The *AFListSize* and *AFListOffset* fields are relevant only for connection-oriented devices that include a call manager. Connectionless devices should set these fields to zero.

In this message, the Remote NDIS device indicates the following:

-   Highest Remote NDIS protocol version number that the device can support. The combined version number should be less than or equal to the version number that the host specifies in the [**REMOTE\_NDIS\_INITIALIZE\_MSG**](remote-ndis-initialize-msg.md) message. This allows the device to fall back to a compatibility mode when the host implements a Remote NDIS protocol version that is lower than that supported by the device.

-   Maximum size in bytes of a single data transfer that the device expects to receive from the host. The device can specify the byte alignment it expects for each Remote NDIS message that is part of a multimessage transfer to it. This alignment value is specified in terms of powers of two. For example, this value is set to 3 to indicate 8-byte alignment.

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

 

 




