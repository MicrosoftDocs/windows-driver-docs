---
title: WDI_TLV_IPV6_CHECKSUM_OFFLOAD
description: WDI_TLV_IPV6_CHECKSUM_OFFLOAD is a TLV that contains checksum offload capabilities for IPv6.
ms.assetid: 878471F5-8118-4D0A-87BC-E44DE7A713DF
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IPV6_CHECKSUM_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IPV6\_CHECKSUM\_OFFLOAD


WDI\_TLV\_IPV6\_CHECKSUM\_OFFLOAD is a TLV that contains checksum offload capabilities for IPv6.

## TLV Type


0xD0

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                 | Multiple TLV instances allowed | Optional | Description                                  |
|------------------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------|
| [**WDI\_TLV\_CHECKSUM\_OFFLOAD\_V6\_TX\_PARAMETERS**](wdi-tlv-checksum-offload-v6-tx-parameters.md) |                                |          | Parameters for Tx checksum offload for IPv6. |
| [**WDI\_TLV\_CHECKSUM\_OFFLOAD\_V6\_RX\_PARAMETERS**](wdi-tlv-checksum-offload-v6-rx-parameters.md) |                                |          | Parameters for Rx checksum offload for IPv6. |

 

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

 

 




