---
title: OID_WDI_SET_ADD_PM_PROTOCOL_OFFLOAD (dot11wificxintf.h)
ms.topic: reference
description: OID_WDI_SET_ADD_PM_PROTOCOL_OFFLOAD adds a list of one or more protocol offloads for power management.
ms.date: 08/23/2023
---

# OID\_WDI\_SET\_ADD\_PM\_PROTOCOL\_OFFLOAD (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_ADD\_PM\_PROTOCOL\_OFFLOAD adds a list of one or more protocol offloads for power management.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

This property provides information to enable the device/firmware to implement these protocols while the main CPU is asleep. In this state, the firmware and device handles the offloaded tasks without waking up the host.

## Set property parameters


| TLV                                                                                                         | Multiple TLV instances allowed | Optional | Description                            |
|-------------------------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------|
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv4ARP**](./wdi-tlv-pm-protocol-offload-ipv4arp.md)                |                                | X        | IPv4 ARP protocol offload parameters.  |
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_IPv6NS**](./wdi-tlv-pm-protocol-offload-ipv6ns.md)                  |                                | X        | IPv6 NS protocol offload parameters.   |
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY**](./wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) |                                | X        | RSN Rekey protocol offload parameters. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-get-pm-protocol-offload.md)

[OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-remove-pm-protocol-offload.md)

 

