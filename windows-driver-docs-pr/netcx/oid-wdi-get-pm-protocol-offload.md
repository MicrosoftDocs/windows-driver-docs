---
title: OID_WDI_GET_PM_PROTOCOL_OFFLOAD (dot11wificxintf.h)
ms.topic: reference
description: OID_WDI_GET_PM_PROTOCOL_OFFLOAD requests a list of protocol offloads for power management.
ms.date: 08/23/2023
---

# OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD requests a list of protocol offloads for power management.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Not applicable           | 1                               |

 

## Get property parameters


| TLV                                                                                  | Multiple TLV instances allowed | Optional | Description          |
|--------------------------------------------------------------------------------------|--------------------------------|----------|----------------------|
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_GET**](./wdi-tlv-pm-protocol-offload-get.md) |                                |          | Protocol offload ID. |

 

## Get property results


| TLV                                                                                                         | Multiple TLV instances allowed | Optional | Description                            |
|-------------------------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------|
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv4ARP**](./wdi-tlv-pm-protocol-offload-ipv4arp.md)                |                                | X        | IPv4 ARP protocol offload parameters.  |
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS**](./wdi-tlv-pm-protocol-offload-ipv6ns.md)                  |                                | X        | IPv6 NS protocol offload parameters.   |
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY**](./wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) |                                | X        | RSN Rekey protocol offload parameters. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_SET\_ADD\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-add-pm-protocol-offload.md)

[OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-remove-pm-protocol-offload.md)

 

