---
title: NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST (dot11wificxintf.h)
ms.topic: reference
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST to inform the host about updates to the BSS entries. This is an unsolicited indication and can be sent at any time.
ms.date: 06/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST to inform the host about updates to the BSS entries. This is an unsolicited indication and can be sent at any time.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                   | Multiple TLV instances allowed | Optional | Description                 |
|--------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_BSS\_ENTRY**](./wdi-tlv-bss-entry.md) | X                              | X        | The list of updated BSSIDs. |

 

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID_WDI_TASK_SCAN](oid-wdi-task-scan.md)

[OID_WDI_TASK_P2P_DISCOVER](oid-wdi-task-p2p-discover.md)

[OID_WDI_SET_P2P_START_BACKGROUND_DISCOVERY](oid-wdi-set-p2p-start-background-discovery.md)

 

