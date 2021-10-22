---
title: OID_WDI_GET_BSS_ENTRY_LIST (dot11wificxintf.h)
description: The OID_WDI_GET_BSS_ENTRY_LIST command is used to ask the adapter to indicate the list of BSS networks that have been cached by the port.
ms.date: 07/31/2021
keywords:
 - OID_WDI_GET_BSS_ENTRY_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_GET\_BSS\_ENTRY\_LIST (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_GET\_BSS\_ENTRY\_LIST is used to ask the adapter to indicate the list of BSS networks that have been cached by the port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Set not supported        | 1                               |

 

This is only used for an adapter that perform BSS list caching. When acting as a client, the port must report the BSS entry for the access point. In addition, if the port is performing background scans, it should report BSS entries that it has discovered in its scan.

When this request is received by the adapter, it must send [NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md) indications to the Microsoft component. These indications must contain the BSS entries that match the Get parameters. The adapter can send one or more NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST indications, but they must be completed before the property completes.

The Microsoft component uses the list of indicated entries to report the BSS list to the operation system. It is also used to populate parameters for roam and connect tasks.

## Get property parameters


| TLV                                         | Multiple TLV instances allowed | Optional | Description                                           |
|---------------------------------------------|--------------------------------|----------|-------------------------------------------------------|
| [**WDI\_TLV\_SSID**](./wdi-tlv-ssid.md) |                                |          | The SSID that the host needs the BSS list update for. |

 

## Get property results


No additional data. The data in the header is sufficient.
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md)

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

