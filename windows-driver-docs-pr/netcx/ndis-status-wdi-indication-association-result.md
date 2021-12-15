---
title: NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT to indicate association results.
ms.date: 06/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT to indicate association results.

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

 

