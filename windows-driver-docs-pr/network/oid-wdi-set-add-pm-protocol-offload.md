---
title: OID_WDI_SET_ADD_PM_PROTOCOL_OFFLOAD
description: OID_WDI_SET_ADD_PM_PROTOCOL_OFFLOAD adds a list of one or more protocol offloads for power management.
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_ADD_PM_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_SET\_ADD\_PM\_PROTOCOL\_OFFLOAD


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

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-get-pm-protocol-offload.md)

[OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-remove-pm-protocol-offload.md)

 

