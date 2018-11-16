---
title: WDI_TLV_WAKE_PACKET_BITMAP_PATTERN
description: WDI_TLV_WAKE_PACKET_BITMAP_PATTERN is a TLV that contains a wake-on-LAN pattern.
ms.assetid: 5BE0F668-A3B4-4ECF-B963-EC4DD1B1A8AE
ms.date: 07/18/2017
keywords:
 - WDI_TLV_WAKE_PACKET_BITMAP_PATTERN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_WAKE\_PACKET\_BITMAP\_PATTERN


WDI\_TLV\_WAKE\_PACKET\_BITMAP\_PATTERN is a TLV that contains a wake-on-LAN pattern.

## TLV Type


0x5B

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                         | Multiple TLV instances allowed | Optional | Description                                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------|
| [**WDI\_TLV\_WAKE\_PACKET\_BITMAP\_PATTERN\_ID**](wdi-tlv-wake-packet-bitmap-pattern-id.md) |                                |          | Specifies the wake-on-LAN pattern ID.                                        |
| [**WDI\_TLV\_BITMAP\_PATTERN**](wdi-tlv-bitmap-pattern.md)                                  |                                |          | Specifies the wake-on-LAN pattern.                                           |
| [**WDI\_TLV\_BITMAP\_PATTERN\_MASK**](wdi-tlv-bitmap-pattern-mask.md)                       |                                |          | Specifies the wake-on-LAN pattern mask. The length is (PatternLength + 7)/8. |

 

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

 

 




