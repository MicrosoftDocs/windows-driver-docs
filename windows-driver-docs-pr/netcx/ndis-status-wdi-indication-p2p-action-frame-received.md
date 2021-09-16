---
title: NDIS_STATUS_WDI_INDICATION_P2P_ACTION_FRAME_RECEIVED (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_P2P_ACTION_FRAME_RECEIVED to indicate that a Wi-Fi Direct Action Frame has been received.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_ACTION_FRAME_RECEIVED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_ACTION\_FRAME\_RECEIVED (dot11wificxintf.h)


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_ACTION\_FRAME\_RECEIVED to indicate that a Wi-Fi Direct Action Frame has been received.

| Object |
|--------|
| Port   |

 

The host may issue an [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md) for this request.

The port must indicate these packets in any of the following situations:

-   The port is in listen state.
-   The port has a GO in operational state.
-   The port is dwelling on a remote listen channel when an [OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](oid-wdi-task-p2p-send-request-action-frame.md) or [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md) has been recently issued.

## Payload data


| Type                                                                                               | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_INCOMING\_FRAME\_INFORMATION**](./wdi-tlv-p2p-incoming-frame-information.md) |                                |          | The incoming Wi-Fi Direct Action Frame information. This information is forwarded back to the port when the host issues [OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md). |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](oid-wdi-task-p2p-send-request-action-frame.md)

[OID\_WDI\_TASK\_P2P\_SEND\_RESPONSE\_ACTION\_FRAME](oid-wdi-task-p2p-send-response-action-frame.md)

 

