---
title: NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT (dot11wificxintf.h)
ms.topic: reference
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT to indicate association results.
ms.date: 08/25/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT to indicate association results.

For association using Wi-Fi 7 MLO, the driver must:

  - Set the **BSSID** ([WDI_TLV_BSSID](wdi-tlv-bssid.md)) in [WDI_TLV_ASSOCIATION_RESULT](./wdi-tlv-association-result.md) to the AP's Link MAC address. 
  - Set the **LocalLinkBssId** ([WDI_TLV_MLO_LINK_BSSID](wdi-tlv-mlo-link-bssid.md)) in WDI_TLV_ASSOCIATION_RESULT to the local Link MAC address.

If the **LocalLinkBssId** is not set, Windows will not be able to use MLO for the connection. See [WiFiCx Wi-Fi 7 feature requirements](wificx-wi-fi-7.md) for more information.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                     | Multiple TLV instances allowed | Optional | Description                    |
|--------------------------------------------------------------------------|--------------------------------|----------|--------------------------------|
| [**WDI\_TLV\_ASSOCIATION\_RESULT**](./wdi-tlv-association-result.md) | X                              |          | A list of association results. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_TASK\_CONNECT](oid-wdi-task-connect.md)

[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

