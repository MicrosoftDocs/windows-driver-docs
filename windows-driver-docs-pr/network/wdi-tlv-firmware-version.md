---
title: WDI_TLV_FIRMWARE_VERSION
ms.topic: reference
description: WDI_TLV_FIRMWARE_VERSION is a TLV that contains the firmware version.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_FIRMWARE_VERSION Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_FIRMWARE\_VERSION

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_FIRMWARE\_VERSION is a TLV that contains the firmware version.

## TLV Type


0xF4

## Length


The size (in bytes) of the array of char elements. The array must contain 1 or more elements.

## Values


| Type     | Description                                                     |
|----------|-----------------------------------------------------------------|
| char\[\] | The firmware version, stored as a null-terminated ASCII string. |

 

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

 

 




