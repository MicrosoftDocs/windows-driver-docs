---
title: NDIS_STATUS_WDI_INDICATION_P2P_SEND_REQUEST_ACTION_FRAME_COMPLETE (dot11wificxintf.h)
ms.topic: reference
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_P2P_SEND_REQUEST_ACTION_FRAME_COMPLETE to indicate information about the Request Action frame sent by OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME.
ms.date: 07/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_SEND_REQUEST_ACTION_FRAME_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_REQUEST\_ACTION\_FRAME\_COMPLETE (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_SEND\_REQUEST\_ACTION\_FRAME\_COMPLETE to indicate information about the Request Action frame sent by [OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](oid-wdi-task-p2p-send-request-action-frame.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                                       | Multiple TLV instances allowed | Optional                                            | Description                                                           |
|------------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT**](./wdi-tlv-p2p-send-action-frame-result.md) |                                | This TLV is only required if the status is success. | Information about the Request Action frame that was sent to the peer. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

