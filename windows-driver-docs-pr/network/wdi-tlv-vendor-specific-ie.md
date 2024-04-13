---
title: WDI_TLV_VENDOR_SPECIFIC_IE
ms.topic: reference
description: WDI_TLV_VENDOR_SPECIFIC_IE is a TLV that contains a list of vendor-specific IEs.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_VENDOR_SPECIFIC_IE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_VENDOR\_SPECIFIC\_IE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_VENDOR\_SPECIFIC\_IE is a TLV that contains a list of vendor-specific IEs.

## TLV Type


0x5

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                        |
|-----------|--------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the vendor-specific IEs. |

 

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

 

 




