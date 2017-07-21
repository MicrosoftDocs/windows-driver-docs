---
title: OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME
author: windows-driver-content
description: OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME is issued to the device to send a Wi-Fi Direct Public Action Frame Request.
ms.assetid: bd8a746e-7d47-44c1-ad05-a452ce00749f
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME Network Drivers Starting with Windows Vista
---

# OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME


OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME is issued to the device to send a Wi-Fi Direct Public Action Frame Request.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 3                                     | 5                               |

 

This command is different than [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md), which is a significantly more time-sensitive operation.

When the device receives an acknowledgment for a request frame, it shall dwell on the same channel for 100ms and indicate any Wi-Fi Direct Public Action Frames it receives to the host.

While the maximum timeout has not expired, the device shall retry sending the Wi-Fi Direct Public Action frame to the remote device on the remote device’s listen channel.

The task is complete either when the local device receives an acknowledgment from the remote device for the action frame that was sent, the timeout expires, or the host aborts the operation. The device may indicate task completion after the same-channel dwell time has expired.

The host may decide to abort this operation and continue/retry the Wi-Fi Direct action frame exchange, so it is important that the device is able to abort this operation quickly.

## Task parameters


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>TLV</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>WDI_TLV_P2P_SEND_ACTION_ REQUEST_FRAME_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898001)</td>
<td></td>
<td></td>
<td>Parameters such as action frame type, device address of target peer adapter, and dialog token.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_P2P_GO_ NEGOTIATION_REQUEST_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897937)</td>
<td></td>
<td>X</td>
<td>GO Negotiation Request Parameters. THe port shall only examine this structure if wfdRequestFrameType is a GO Negotiation request.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_P2P_INVITATION_REQUEST_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897963)</td>
<td></td>
<td>X</td>
<td>Invitation Request Parameters. The port shall only examine this structure if wfdRequestFrameType is an Invitation request.</td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_P2P_PROVISION_ DISCOVERY_REQUEST_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/dn897980)</td>
<td></td>
<td>X</td>
<td>Provision Discovery Request Parameters. The port shall only examine this structure if wfdRequestFrameType is an Provision Discovery request.</td>
</tr>
<tr class="odd">
<td>[<strong>WDI_TLV_BSS_ENTRY</strong>](https://msdn.microsoft.com/library/windows/hardware/dn926162)</td>
<td></td>
<td></td>
<td><p>The device discovery entry as returned by the Wi-Fi Direct Discovery task from the port.</p>
<p>This is provided so the port does not need to remember its discovery database in order to send Wi-Fi Direct Action Frame Requests to remote Wi-Fi Direct devices without requiring a discovery.</p></td>
</tr>
<tr class="even">
<td>[<strong>WDI_TLV_VENDOR_SPECIFIC_IE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn898076)</td>
<td></td>
<td>X</td>
<td>One or more IEs that must be included in the frame sent by the port.</td>
</tr>
</tbody>
</table>

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_REQUEST\_ACTION\_FRAME\_COMPLETE](ndis-status-wdi-indication-p2p-send-request-action-frame-complete.md)
Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


