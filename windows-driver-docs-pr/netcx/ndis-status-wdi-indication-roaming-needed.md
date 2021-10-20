---
title: NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED to indicate that the host should try to find a better peer to connect to.
ms.date: 06/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED to indicate that the host should try to find a better peer to connect to. This notification is used when the link quality with the currently connected peer falls below a certain threshold. On sending this notification, the host may trigger a roam scan and/or a roam operation. The Microsoft component does not perform a disconnect before it starts the roam operation.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                    | Multiple TLV instances allowed | Optional | Description                                                                                                                         |
|-----------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ROAMING\_NEEDED\_PARAMETERS**](./wdi-tlv-roaming-needed-parameters.md) |                                |          | The reason for the roam trigger. When a [OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md) is triggered, this reason is forwarded to it. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_TASK\_ROAM](oid-wdi-task-roam.md)

 

