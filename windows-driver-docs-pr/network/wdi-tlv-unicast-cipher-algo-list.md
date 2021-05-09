---
title: WDI_TLV_UNICAST_CIPHER_ALGO_LIST
description: WDI_TLV_UNICAST_CIPHER_ALGO_LIST is a TLV that contains a list of unicast cipher algorithms.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_UNICAST_CIPHER_ALGO_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_UNICAST\_CIPHER\_ALGO\_LIST


WDI\_TLV\_UNICAST\_CIPHER\_ALGO\_LIST is a TLV that contains a list of unicast cipher algorithms.

## TLV Type


0x3E

## Length


The size (in bytes) of the array of [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm) structures. The array must contain 1 or more elements.

## Values


| Type                                                            | Description                            |
|-----------------------------------------------------------------|----------------------------------------|
| [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm)\[\] | An array of unicast cipher algorithms. |

 

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

 

