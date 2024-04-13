---
title: OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME
ms.topic: reference
description: OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME requests that the IHV component sends Response Action Frames.
ms.date: 03/02/2023
keywords:
 - OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_TASK\_SEND\_RESPONSE\_ACTION\_FRAME

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_TASK\_SEND\_RESPONSE\_ACTION\_FRAME requests that the IHV component sends Response Action Frames.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 3                                     | 5                               |

 

This task is time sensitive and must be serviced within 100 milliseconds of receiving this packet.

While the maximum timeout has not expired, the port shall retry sending the frame to the remote device on the specified channel.

The task is complete either when local device receives an acknowledgment from the remote device for the action frame that was sent, the timeout expires, or the host aborts the operation. The device may indicate task completion after the same-channel dwell time has expired.

The host may decide to abort this operation and continue/retry the action frame exchange, so it is important that the device is able to abort this operation quickly.

## Task parameters


| TLV                                                                                                               | Multiple TLV instances allowed | Optional | Description                                      |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------|
| [**WDI\_TLV\_SEND\_ACTION\_FRAME\_RESPONSE\_PARAMETERS**](./wdi-tlv-send-action-frame-response-parameters.md) |                                |          | Parameters for sending an Action Frame Response. |
| [**WDI\_TLV\_ACTION\_FRAME\_BODY**](./wdi-tlv-action-frame-body.md)                                           |                                |          | The Action Frame body.                           |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_SEND\_RESPONSE\_ACTION\_FRAME\_COMPLETE](ndis-status-wdi-indication-send-response-action-frame-complete.md)

## Requirements

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

 

