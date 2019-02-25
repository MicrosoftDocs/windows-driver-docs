---
title: WDI_TLV_BAND_CAPABILITIES
description: WDI_TLV_BAND_CAPABILITIES is a TLV that contains the capabilities of a band.
ms.assetid: ABD198FE-8E81-4AF3-BB3D-D78AEB75782F
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BAND_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




