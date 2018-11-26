---
title: WDI_TLV_PHY_INFO
description: WDI_TLV_PHY_INFO is a TLV that contains PHY information.
ms.assetid: 3A363FDC-FE79-42C4-AD19-A6B960857CBD
ms.date: 07/18/2017
keywords:
 - WDI_TLV_PHY_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




