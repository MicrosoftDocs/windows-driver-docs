---
title: 'REMOTE_NDIS_PACKET_MSG'
Description: 'REMOTE_NDIS_PACKET_MSG encapsulates NDIS data packets to form a single data message.'
ms.assetid: cc4efe94-6e2c-4201-b251-10e76cf5a553
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_PACKET\_MSG


REMOTE\_NDIS\_PACKET\_MSG encapsulates NDIS data packets to form a single data message.

Concatenating multiple REMOTE\_NDIS\_PACKET\_MSG elements forms a multipacket message. Each individual REMOTE\_NDIS\_PACKET\_MSG component is constructed as described below. The difference from the single-packet message is that the *MessageLength* field in each REMOTE\_NDIS\_PACKET\_MSG header includes some additional padding bytes. These padding bytes are appended to all but the last REMOTE\_NDIS\_PACKET\_MSG so that the succeeding REMOTE\_NDIS\_PACKET\_MSG starts at an appropriate byte boundary. For messages sent from the device to the host, this padding should result in each REMOTE\_NDIS\_PACKET\_MSG starting at a byte offset that is a multiple of 8 bytes starting from the beginning of the multipacket message. When the host sends a multipacket message to the device, it will adhere to the *PacketAlignmentFactor* that the device specifies.

The REMOTE\_NDIS\_PACKET\_MSG format is defined in the following table.

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
<td><p>Specifies the type of message being sent. Set to 0x1.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>MessageLength</p></td>
<td><p>Message length in bytes, including appended packet data, OOB data, per-packet information data, and both internal and external padding.</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>4</p></td>
<td><p>DataOffset</p></td>
<td><p>Specifies the offset in bytes from the start of the DataOffset field of this message to the start of the data. This is an integer multiple of 4.</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>DataLength</p></td>
<td><p>Specifies the number of bytes in the data content of this message.</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>4</p></td>
<td><p>OOBDataOffset</p></td>
<td><p>Specifies the offset in bytes of the first OOB data record from the start of the <em>DataOffset</em> field of this message. Set to zero if there is no OOB data. Otherwise, this is an integer multiple of 4.</p></td>
</tr>
<tr class="even">
<td><p>20</p></td>
<td><p>4</p></td>
<td><p>OOBDataLength</p></td>
<td><p>Specifies in bytes the total length of the OOB data.</p></td>
</tr>
<tr class="odd">
<td><p>24</p></td>
<td><p>4</p></td>
<td><p>NumOOBDataElements</p></td>
<td><p>Specifies the number of OOB records in this message.</p></td>
</tr>
<tr class="even">
<td><p>28</p></td>
<td><p>4</p></td>
<td><p>PerPacketInfoOffset</p></td>
<td><p>Specifies in bytes the offset from the beginning of the <em>DataOffset</em> field in the REMOTE_NDIS_PACKET_MSG data message to the start of the first per-packet information data record. Set to zero if there is no per-packet data. Otherwise, this is an integer multiple of 4.</p></td>
</tr>
<tr class="odd">
<td><p>32</p></td>
<td><p>4</p></td>
<td><p>PerPacketInfoLength</p></td>
<td><p>Specifies in bytes the total length of the per-packet information contained in this message.</p></td>
</tr>
<tr class="even">
<td><p>36</p></td>
<td><p>4</p></td>
<td><p>VcHandle</p></td>
<td><p>Reserved for connection-oriented devices. Set to zero.</p></td>
</tr>
<tr class="odd">
<td><p>40</p></td>
<td><p>4</p></td>
<td><p>Reserved</p></td>
<td><p>Reserved. Set to zero.</p></td>
</tr>
</tbody>
</table>

 

The format of a single OOB data record is indicated in the following table.

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
<td><p>Size</p></td>
<td><p>Length in bytes of this OOB header and appended OOB data and padding. This is an integer multiple of 4.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>Type</p></td>
<td><p>None defined for 802.3 devices.</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>4</p></td>
<td><p>ClassInformationOffset</p></td>
<td><p>The byte offset from the beginning of this OOB data record to the beginning of the OOB data.</p></td>
</tr>
<tr class="even">
<td><p>(N)</p></td>
<td><p>...</p></td>
<td><p>OOB Data</p></td>
<td><p>OOB Data; consult Microsoft Windows Driver Development Kit (DDK) documentation for more information.</p></td>
</tr>
</tbody>
</table>

 

**Note**  
(N) is equal to the value of *ClassInformationOffset*.

 

The following table defines the format of a per-packet information data record.

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
<td><p>Size</p></td>
<td><p>Length in bytes of this per-packet header and appended per-packet data and padding. This value is an integer multiple of 4.</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>Type</p></td>
<td><p>Set to one of the legal values for NDIS_PER_PACKET_INFO_FROM_PACKET, as described in the Windows 2000 Driver Development Kit (DDK).</p></td>
</tr>
<tr class="odd">
<td><p>8</p></td>
<td><p>4</p></td>
<td><p>PerPacketInformationOffset</p></td>
<td><p>The byte offset from the beginning of this per-packet information data record to the beginning of the per-packet information data.</p></td>
</tr>
<tr class="even">
<td><p>(N)</p></td>
<td><p>...</p></td>
<td><p>Per-Packet Data</p></td>
<td><p>Per-Packet Data; consult Windows 2000 DDK documentation for more information.</p></td>
</tr>
</tbody>
</table>

 

**Note**  
(N) is equal to the value of *PerPacketInformationOffset*.

 

Remarks
-------

Each REMOTE\_NDIS\_PACKET\_MSG may contain one or more OOB data records. *NumOOBDataElements* indicates the number of OOB data records in this message. The OOB data records must appear in sequence. The *OOBDataLength* field indicates the length in bytes of the entire OOB data block. The *OOBDataOffset* field indicates the byte offset from the beginning of the *DataOffset* field to the beginning of the OOB data block. For more information about OOB packet data, see the NDIS specification in the Windows 2000 DDK.

If multiple OOB data blocks are attached to a REMOTE\_NDIS\_PACKET\_MSG message, each subsequent OOB data record must immediately follow the previous OOB record's data.

No OOB information is currently defined for 802.3 devices.

Each REMOTE\_NDIS\_PACKET\_MSG may contain one or more per-packet-info data records. Per-packet-info is used to convey packet metadata, such as TCP checksum. The *PerPacketInfoOffset* field indicates the byte offset from the beginning of the *DataOffset* field to the beginning of the per-packet information data record. The *OOBDataLength* field indicates the byte length of the per-packet information data record. For more information about per-packet information data, see the Windows 2000 DDK.

If there are multiple per-packet information data blocks, each subsequent per-packet information data record must immediately follow the previous per-packet information record's data.

A Remote NDIS device must send and receive data through NDIS data packets. The bus that the device uses determines how these packets are passed from host to device and device to host. It could be shared memory or, in the case of USB, Isoch and Bulk pipes. NDIS packets may also contain out-of-band (OOB) data as well as the data that goes across the network.

A Remote NDIS device transfers NDIS packets, encapsulated as **REMOTE\_NDIS\_PACKET\_MSG** across the data channel. Both connectionless (such as 802.3) and connection-oriented (such as ATM) devices use the same packet message structure to facilitate common code for packet processing. Each **REMOTE\_NDIS\_PACKET\_MSG** message contains information about a single network data unit (such s an Ethernet 802.3 frame).

For more information about out-of-band packet data or per-packet-info data, see the Windows 2000 DDK NDIS sections.

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

 

 




