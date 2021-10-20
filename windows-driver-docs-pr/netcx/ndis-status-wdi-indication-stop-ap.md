---
title: NDIS_STATUS_WDI_INDICATION_STOP_AP (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_STOP_AP to indicate that the adapter cannot sustain 802.11 AP functionality on any of the PHYs.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_STOP_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP to indicate that the adapter cannot sustain 802.11 Access Point (AP) functionality on any of the PHYs. The adapter should send this indication only after the NIC has stopped any APs that are operating on the available PHYs. The host blocks all [OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md) requests until the adapter sends [NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP](ndis-status-wdi-indication-can-sustain-ap.md).

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                      | Multiple TLV instances allowed | Optional | Description                                                                       |
|---------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------|
| [**WDI\_TLV\_INDICATION\_STOP\_AP**](./wdi-tlv-indication-stop-ap.md) |                                |          | The reason the adapter cannot sustain 802.11 AP functionality on any of the PHYs. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md)

[NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP](ndis-status-wdi-indication-can-sustain-ap.md)

 

