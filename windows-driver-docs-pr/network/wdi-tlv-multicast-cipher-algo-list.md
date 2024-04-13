---
title: WDI_TLV_MULTICAST_CIPHER_ALGO_LIST
ms.topic: reference
description: WDI_TLV_MULTICAST_CIPHER_ALGO_LIST is a TLV that contains a list of multicast cipher algorithms.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_MULTICAST_CIPHER_ALGO_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_MULTICAST\_CIPHER\_ALGO\_LIST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_MULTICAST\_CIPHER\_ALGO\_LIST is a TLV that contains a list of multicast cipher algorithms.

## TLV Type


0x3D

## Length


The size (in bytes) of the array of [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm) structures. The array must contain 1 or more elements.

## Values


| Type                                                            | Description                              |
|-----------------------------------------------------------------|------------------------------------------|
| [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm)\[\] | An array of multicast cipher algorithms. |

 

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

 

