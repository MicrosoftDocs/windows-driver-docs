---
title: OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME
description: OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME is issued to the IHV component to send a Wi-Fi Direct Public Action Frame Request to a peer.
ms.assetid: 5cb57f20-ef9d-4e79-9b4b-8cf939221d47
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME


OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME is issued to the IHV component to send a Wi-Fi Direct Public Action Frame Request to a peer.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 3                                     | 5                               |

 

When port receives an acknowledgment for a request frame, it shall dwell on the same channel for 100ms and indicate any Wi-Fi Direct Public Action Frames it receives to the host.

This task is time sensitive. The Wi-Fi Direct specification requires that sending Wi-Fi Direct action responses are only serviced within 100 milliseconds of receiving this packet.

While the maximum timeout has not expired, the port shall retry sending the Wi-Fi Direct to the remote device on the appropriate channel as defined by the following table. The table defines the explicit channel requirements for where to send the packets when the command is issued. The general rule is that the response packet shall be sent out on the same channel as the prior request.

| Response Action Frame Type   | Target Transmit Channel                               |
|------------------------------|-------------------------------------------------------|
| GO Negotiation Response      | Local Listen Channel                                  |
| GO Negotiation Confirmation  | Remote Listen Channel                                 |
| Invitation Response          | Local Listen or Local GO Operational Channel          |
| Provision Discovery Response | Local Listen Channel or Remote GO Operational Channel |

 

The task is complete either when local device receives an acknowledgment from the remote device for the action frame that was sent, the timeout expires, or the host aborts the operation. The device may indicate task completion after the same-channel dwell time has expired.

The host may decide to abort this operation and continue/retry the Wi-Fi Direct action frame exchange, so it is important that the device is able to abort this operation quickly.

## Task parameters


| TLV                                                                                                               | Multiple TLV instances allowed | Optional | Description                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_ACTION\_FRAME\_RESPONSE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn897859)   |                                |          | Parameters such as action frame type, device address of target peer adapter, and dialog token.                                                 |
| [**WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn897942)           |                                | X        | GO Negotiation Response Parameters. The port shall only examine this structure if wfdRequestFrameType is a GO Negotiation Response.            |
| [**WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn897880)   |                                | X        | GO Negotiation Confirmation Parameters. The port shall only examine this structure if wfdRequestFrameType is a GO Negotiation Confirmation.    |
| [**WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn897968)                    |                                | X        | Invitation Response Parameters. The port shall only examine this structure if wfdRequestFrameType is an Invitation Response.                   |
| [**WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn897983) |                                | X        | Provision Discovery Response Parameters. The port shall only examine this structure if wfdRequestFrameType is an Provision Discovery Response. |
| [**WDI\_TLV\_P2P\_INCOMING\_FRAME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/dn897957)                |                                |          | Information that was indicated from the previously received P2P Action Frame. The received indication is provided back to the port.            |
| [**WDI\_TLV\_VENDOR\_SPECIFIC\_IE**](https://msdn.microsoft.com/library/windows/hardware/dn898076)                                         |                                | X        | One or more IEs that must be included in the frame sent by the port.                                                                           |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME\_COMPLETE](ndis-status-wdi-indication-p2p-send-response-action-frame-complete.md)
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

 

 




