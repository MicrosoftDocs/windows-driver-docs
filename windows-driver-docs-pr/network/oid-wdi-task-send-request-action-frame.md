---
title: OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME
description: OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME requests that the device sends an Action Frame Request to another device.
ms.assetid: CAC86B50-BE85-4650-B6D3-738B4E960587
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_SEND\_REQUEST\_ACTION\_FRAME


OID\_WDI\_TASK\_SEND\_REQUEST\_ACTION\_FRAME requests that the device sends an Action Frame Request to another device.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 3                                     | 5                               |

 

This command is different from [OID\_WDI\_TASK\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-send-response-action-frame.md), which is a significantly more time-sensitive operation.

When the device receives an acknowledgment for a request frame, it shall dwell on the same channel for the Post-ACK Dwell time as specified in the Task Parameters, and shall indicate to the host any Action Frames it receives and doesn’t handle itself.

As long as the maximum timeout has not expired, the device shall retry sending the Public Action frame to the remote device on the remote device’s listen channel.

The task is complete either when local device receives an acknowledgment from the remote device for the action frame that was sent, the timeout expires, or the host aborts the operation. The device may indicate task completion after the same-channel dwell time has expired.

The host may decide to abort this operation and continue/retry the public action frame exchange, so it is important that the device is able to abort this operation quickly.

## Task parameters


| TLV                                                                                                             | Multiple TLV instances allowed | Optional | Description                                     |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------|
| [**WDI\_TLV\_SEND\_ACTION\_FRAME\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898053) |                                |          | Parameters for sending an Action Frame Request. |
| [**WDI\_TLV\_ACTION\_FRAME\_BODY**](https://msdn.microsoft.com/library/windows/hardware/dn926118)                                         |                                |          | The Action Frame body.                          |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_SEND\_REQUEST\_ACTION\_FRAME\_COMPLETE](ndis-status-wdi-indication-send-request-action-frame-complete.md)
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

 

 




