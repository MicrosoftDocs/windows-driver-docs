---
title: WDI_TLV_FIRMWARE_VERSION
description: WDI_TLV_FIRMWARE_VERSION is a TLV that contains the firmware version.
ms.assetid: 31E61ACA-AF2F-4E5D-9448-363630A27E39
ms.date: 07/18/2017
keywords:
 - WDI_TLV_FIRMWARE_VERSION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_FIRMWARE\_VERSION


WDI\_TLV\_FIRMWARE\_VERSION is a TLV that contains the firmware version.

## TLV Type


0xF4

## Length


The size (in bytes) of the array of char elements. The array must contain 1 or more elements.

## Values


| Type     | Description                                                     |
|----------|-----------------------------------------------------------------|
| char\[\] | The firmware version, stored as a null-terminated ASCII string. |

 

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

 

 




