---
title: WDI_TLV_ASSOCIATION_REQUEST_FRAME
description: WDI_TLV_ASSOCIATION_REQUEST_FRAME is a TLV that contains the association request that was used for the association.
ms.assetid: C2323DFE-2B13-4E35-BF9B-4A0B5F3B2076
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ASSOCIATION_REQUEST_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME


WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME is a TLV that contains the association request that was used for the association.

## TLV Type


0x2E

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the association request that was used for the association. This does not include the 802.11 MAC header. |

 

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

 

 




