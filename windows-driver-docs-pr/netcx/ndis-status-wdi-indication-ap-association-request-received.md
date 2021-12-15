---
title: NDIS_STATUS_WDI_INDICATION_AP_ASSOCIATION_REQUEST_RECEIVED (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_AP_ASSOCIATION_REQUEST_RECEIVED to indicate that a Wi-Fi Association Request Frame has been received for an operational Wi-Fi Direct Group Owner.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_AP_ASSOCIATION_REQUEST_RECEIVED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_AP\_ASSOCIATION\_REQUEST\_RECEIVED (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_AP\_ASSOCIATION\_REQUEST\_RECEIVED to indicate that a Wi-Fi Association Request Frame has been received for an operational Wi-Fi Direct Group Owner. The host may issue an [OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE](oid-wdi-task-send-ap-association-response.md) for this request.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                                     | Multiple TLV instances allowed | Optional | Description                                   |
|----------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------|
| [**WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO**](./wdi-tlv-incoming-association-request-info.md) |                                |          | The incoming Association Request information. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|
 

