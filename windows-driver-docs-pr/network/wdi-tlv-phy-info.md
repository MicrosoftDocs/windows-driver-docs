---
title: WDI_TLV_PHY_INFO
ms.topic: reference
description: WDI_TLV_PHY_INFO is a TLV that contains PHY information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PHY_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PHY\_INFO


WDI\_TLV\_PHY\_INFO is a TLV that contains PHY information.

## TLV Type


0x26

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                             | Multiple TLV instances allowed | Optional | Description                |
|----------------------------------------------------------------------------------|--------------------------------|----------|----------------------------|
| [**WDI\_TLV\_PHY\_CAPABILITIES**](wdi-tlv-phy-capabilities.md)                  |                                |          | The phy capabilities.      |
| [**WDI\_TLV\_PHY\_TX\_POWER\_LEVEL\_LIST**](wdi-tlv-phy-tx-power-level-list.md) |                                |          | A list of TX power levels. |
| [**WDI\_TLV\_PHY\_DATA\_RATE\_LIST**](wdi-tlv-phy-data-rate-list.md)            |                                |          | A list of data rates.      |

 

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

 

 




