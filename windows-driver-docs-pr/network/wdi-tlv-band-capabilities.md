---
title: WDI_TLV_BAND_CAPABILITIES
ms.topic: reference
description: WDI_TLV_BAND_CAPABILITIES is a TLV that contains the capabilities of a band.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BAND_CAPABILITIES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BAND\_CAPABILITIES


WDI\_TLV\_BAND\_CAPABILITIES is a TLV that contains the capabilities of a band.

## TLV Type


0x1A

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                   |
|--------|-----------------------------------------------|
| UINT32 | The identifier for the band.                  |
| UINT8  | Specifies whether the band is enabled or not. |

 

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

 

 




