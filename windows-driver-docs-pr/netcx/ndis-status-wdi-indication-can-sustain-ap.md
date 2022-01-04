---
title: NDIS_STATUS_WDI_INDICATION_CAN_SUSTAIN_AP (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_CAN_SUSTAIN_AP to indicate that the port is ready to receive a OID_WDI_TASK_START_AP request, after previously indicating NDIS_STATUS_WDI_INDICATION_STOP_AP.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_CAN_SUSTAIN_AP Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP to indicate that the port is ready to receive a [OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md) request, after previously indicating [NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP](ndis-status-wdi-indication-stop-ap.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                     | Multiple TLV instances allowed | Optional | Description                                                     |
|------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------|
| [**WDI\_TLV\_INDICATION\_CAN\_SUSTAIN\_AP**](./wdi-tlv-indication-can-sustain-ap.md) |                                |          | The reason the adapter can now sustain 802.11 AP functionality. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

