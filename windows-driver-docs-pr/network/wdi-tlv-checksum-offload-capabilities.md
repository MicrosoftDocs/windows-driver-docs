---
title: WDI_TLV_CHECKSUM_OFFLOAD_CAPABILITIES
description: WDI_TLV_CHECKSUM_OFFLOAD_CAPABILITIES is a TLV that contains checksum offload capabilities for IPv4 and IPv6.
ms.assetid: 400D532F-CAAA-40F9-8001-EE460D4C89F9
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CHECKSUM_OFFLOAD_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CHECKSUM\_OFFLOAD\_CAPABILITIES


WDI\_TLV\_CHECKSUM\_OFFLOAD\_CAPABILITIES is a TLV that contains checksum offload capabilities for IPv4 and IPv6.

## TLV Type


0xCB

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                       | Multiple TLV instances allowed | Optional | Description                           |
|----------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------|
| [**WDI\_TLV\_IPV4\_CHECKSUM\_OFFLOAD**](wdi-tlv-ipv4-checksum-offload.md) |                                |          | Parameters for IPv4 checksum offload. |
| [**WDI\_TLV\_IPV6\_CHECKSUM\_OFFLOAD**](wdi-tlv-ipv6-checksum-offload.md) |                                |          | Parameters for IPv6 checksum offload. |

 

Requirements
------------

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

 

 




