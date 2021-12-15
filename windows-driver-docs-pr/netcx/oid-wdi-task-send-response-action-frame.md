---
title: OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME (dot11wificxintf.h)
description: The OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME command requests that the IHV component sends Response Action Frames.
ms.date: 07/31/2021
keywords:
 - OID_WDI_TASK_SEND_RESPONSE_ACTION_FRAME Network Drivers Starting with Windows Vista
---

# OID\_WDI\_TASK\_SEND\_RESPONSE\_ACTION\_FRAME (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


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

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

