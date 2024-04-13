---
title: OID_WDI_SET_REMOVE_WOL_PATTERN
ms.topic: reference
description: OID_WDI_SET_REMOVE_WOL_PATTERN removes a wake-on-LAN (WOL) pattern from the firmware.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_REMOVE_WOL_PATTERN Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_REMOVE\_WOL\_PATTERN


OID\_WDI\_SET\_REMOVE\_WOL\_PATTERN removes a wake-on-LAN (WOL) pattern from the firmware.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                        | Multiple TLV instances allowed | Optional | Description     |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------|
| [**WDI\_TLV\_WAKE\_PACKET\_PATTERN\_REMOVE**](./wdi-tlv-wake-packet-pattern-remove.md) |                                |          | WOL pattern ID. |

 

## Set property results


No additional parameters. The data in the header is sufficient.

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


[OID\_WDI\_SET\_ADD\_WOL\_PATTERN](oid-wdi-set-add-wol-pattern.md)

 

