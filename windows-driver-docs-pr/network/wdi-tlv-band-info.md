---
title: WDI_TLV_BAND_INFO
description: WDI_TLV_BAND_INFO is a TLV that contains band information.
ms.assetid: 37F1CE39-5471-489A-8DA2-F058B631B31F
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BAND_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BAND\_INFO


WDI\_TLV\_BAND\_INFO is a TLV that contains band information.

## TLV Type


0x27

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                 | Multiple TLV instances allowed | Optional | Description                                   |
|----------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------|
| [**WDI\_TLV\_BAND\_CAPABILITIES**](wdi-tlv-band-capabilities.md)    |                                |          | The capabilities of the band.                 |
| [**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md)           |                                |          | A list of valid PHY types in this band.       |
| [**WDI\_TLV\_CHANNEL\_LIST**](wdi-tlv-channel-list.md)              |                                |          | A list of valid channel numbers in this band. |
| [**WDI\_TLV\_CHANNEL\_WIDTH\_LIST**](wdi-tlv-channel-width-list.md) |                                |          | A list of channel widths in MHz               |

 

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

 

 




