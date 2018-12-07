---
title: WDI_TLV_VENDOR_SPECIFIC_IE
description: WDI_TLV_VENDOR_SPECIFIC_IE is a TLV that contains a list of vendor-specific IEs.
ms.assetid: 66995086-329A-49F1-B531-2AD2383473CF
ms.date: 07/18/2017
keywords:
 - WDI_TLV_VENDOR_SPECIFIC_IE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_VENDOR\_SPECIFIC\_IE


WDI\_TLV\_VENDOR\_SPECIFIC\_IE is a TLV that contains a list of vendor-specific IEs.

## TLV Type


0x5

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                        |
|-----------|--------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the vendor-specific IEs. |

 

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

 

 




