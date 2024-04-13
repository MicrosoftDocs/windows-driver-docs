---
title: WDI_TLV_LSO_V2_CAPABILITIES
ms.topic: reference
description: WDI_TLV_LSO_V2_CAPABILITIES is a TLV that contains Large Send Offload V2 capabilities.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_LSO_V2_CAPABILITIES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_LSO\_V2\_CAPABILITIES


WDI\_TLV\_LSO\_V2\_CAPABILITIES is a TLV that contains Large Send Offload V2 capabilities.

## TLV Type


0xCD

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                   | Multiple TLV instances allowed | Optional | Description                                  |
|--------------------------------------------------------|--------------------------------|----------|----------------------------------------------|
| [**WDI\_TLV\_IPV4\_LSO\_V2**](wdi-tlv-ipv4-lso-v2.md) |                                |          | Large Send Offload V2 capabilities for IPv4. |
| [**WDI\_TLV\_IPV6\_LSO\_V2**](wdi-tlv-ipv6-lso-v2.md) |                                |          | Large Send Offload V2 capabilities for IPv6. |

 

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
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




