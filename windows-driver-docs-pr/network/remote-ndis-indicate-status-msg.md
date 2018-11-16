---
title: 'REMOTE_NDIS_INDICATE_STATUS_MSG'
Description: 'This message is sent from a Remote NDIS device to a host to indicate a change in the status of the device.'
ms.assetid: 768aad13-3da6-436c-a7ba-d420af34643e
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# REMOTE\_NDIS\_INDICATE\_STATUS\_MSG


This message is sent from a Remote NDIS device to a host to indicate a change in the status of the device. A REMOTE\_NDIS\_INDICATE\_STATUS\_MSG message can also be used to indicate an error event, such as an unrecognized message. The Remote NDIS device may send this message at any time that it is in a state initialized by Remote NDIS. There is no response to this message.

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
<td><p>Specifies the type of message being sent. Set to 0x00000007.</p></td>
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
<td><p>Specifies the current status of the host request.</p></td>
</tr>
<tr class="even">
<td><p>12</p></td>
<td><p>4</p></td>
<td><p>StatusBufferLength</p></td>
<td><p>Specifies the length of the status data, in bytes.</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>4</p></td>
<td><p>StatusBufferOffset</p></td>
<td><p>Specifies the byte offset, from the beginning of this message, at which Rndis_Diagnostic_Info status data for the device indication is located.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The most common use of REMOTE\_NDIS\_INDICATE\_STATUS\_MSG is to indicate the state of the link for an 802.3 device. A status value of RNDIS\_STATUS\_MEDIA\_CONNECT indicates a transition from disconnected (for example no 802.3 link pulse) to connected state (802.3 link pulse detected). A status value of RNDIS\_STATUS\_MEDIA\_DISCONNECT indicates a transition from connected to disconnected state. The device must send REMOTE\_NDIS\_INDICATE\_STATUS\_MSG with one of these values every time the 802.3 link state changes. No status buffer is required to return these two common indications.

In the specific case where this message is sent in response to a host message that the device could not handle, the *Status* field must be set to RNDIS\_STATUS\_INVALID\_DATA, and the Rndis\_Diagnostic\_Info status buffer is formatted as follows.

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
<td><p>DiagStatus</p></td>
<td><p>Contains status information about the error itself (for example, RNDIS_STATUS_NOT_SUPPORTED)</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>4</p></td>
<td><p>ErrorOffset</p></td>
<td><p>Specifies the zero-based byte offset in the original message at which the error was detected.</p></td>
</tr>
</tbody>
</table>

 

If the error condition was caused by an Remote NDIS message (for example, the device can't recognize a particular RNDIS message), then the device should append the original message at the end of the status message defined above.

This message is used to report an error condition only in circumstances where the device is not able to generate a response message with appropriate status. Examples of appropriate usage are:

-   On receiving a message with unsupported message type.

-   On receiving a [**REMOTE\_NDIS\_PACKET\_MSG**](remote-ndis-packet-msg.md) with unacceptable contents.

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

 

 




