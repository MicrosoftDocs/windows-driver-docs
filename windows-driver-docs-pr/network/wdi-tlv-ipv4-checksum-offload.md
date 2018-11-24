---
title: WDI_TLV_IPV4_CHECKSUM_OFFLOAD
description: WDI_TLV_IPV4_CHECKSUM_OFFLOAD is a TLV that contains checksum offload capabilities for IPv4.
ms.assetid: FCC5880E-4323-4A24-98C6-CE7C84D03C16
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IPV4_CHECKSUM_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IPV4\_CHECKSUM\_OFFLOAD


WDI\_TLV\_IPV4\_CHECKSUM\_OFFLOAD is a TLV that contains checksum offload capabilities for IPv4.

## TLV Type


0xCF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                 | Multiple TLV instances allowed | Optional | Description                                  |
|------------------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------|
| [**WDI\_TLV\_CHECKSUM\_OFFLOAD\_V4\_TX\_PARAMETERS**](wdi-tlv-checksum-offload-v4-tx-parameters.md) |                                |          | Parameters for Tx checksum offload for IPv4. |
| [**WDI\_TLV\_CHECKSUM\_OFFLOAD\_V4\_RX\_PARAMETERS**](wdi-tlv-checksum-offload-v4-rx-parameters.md) |                                |          | Parameters for Rx checksum offload for IPv4. |

 

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

 

 




