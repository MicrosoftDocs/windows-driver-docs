---
title: WDI_TLV_SSID
ms.topic: reference
description: WDI_TLV_SSID is a TLV that contains an SSID.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_SSID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_SSID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_SSID is a TLV that contains an SSID.

## TLV Type


0x3B

## Length


The size (in bytes) of the array of UINT8 elements. An array length of 0 is allowed.

## Values


| Type      | Description                                        |
|-----------|----------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies an SSID. |

 

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

 

 




