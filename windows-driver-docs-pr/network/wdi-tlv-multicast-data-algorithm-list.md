---
title: WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST
ms.topic: reference
description: WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST is a TLV that contains an array of multicast data algorithm pairs.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST is a TLV that contains an array of multicast data algorithm pairs.

## TLV Type


0x14

## Length


The size (in bytes) of the array of WDI\_ALGO\_PAIRS elements. The array must contain 1 or more elements.

**Note**  WDI\_ALGO\_PAIRS is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                 | Description                                            |
|----------------------|--------------------------------------------------------|
| WDI\_ALGO\_PAIRS\[\] | An array of authentication and cipher algorithm pairs. |

 

WDI\_ALGO\_PAIRS consists of the following elements.

| Type  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| UINT8 | Authentication algorithm as defined in [**WDI\_AUTH\_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_auth_algorithm). |
| UINT8 | Cipher algorithm as defined in [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm).     |

 

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

 

