---
title: WDI_TLV_PMKID
ms.topic: reference
description: WDI_TLV_PMKID is a TLV that contains a PMKID value.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PMKID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PMKID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_PMKID is a TLV that contains a PMKID value.

## TLV Type


0x9F

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description            |
|-----------|------------------------|
| UINT8\[\] | A 16-byte PMKID value. |

 

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

 

 




