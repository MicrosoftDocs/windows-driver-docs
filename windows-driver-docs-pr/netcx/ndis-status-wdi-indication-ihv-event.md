---
title: NDIS_STATUS_WDI_INDICATION_IHV_EVENT (dot11wificxintf.h)
ms.topic: reference
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_IHV_EVENT to pass IHV specific information to the IHV extensibility module.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_IHV_EVENT Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_IHV\_EVENT (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_IHV\_EVENT to pass IHV specific information to the IHV extensibility module.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                 | Multiple TLV instances allowed | Optional | Description                                           |
|------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------|
| [**WDI\_TLV\_IHV\_DATA**](./wdi-tlv-ihv-data.md) |                                | X        | The event to be sent to the IHV extensibility module. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

