---
title: WDI_TLV_UNICAST_ALGORITHM_LIST
description: WDI_TLV_UNICAST_ALGORITHM_LIST is a TLV that contains an array of unicast data algorithm pairs.
ms.assetid: E216BE6A-5425-498F-ABDE-1229170DA5DB
ms.date: 07/18/2017
keywords:
 - WDI_TLV_UNICAST_ALGORITHM_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_UNICAST\_ALGORITHM\_LIST


WDI\_TLV\_UNICAST\_ALGORITHM\_LIST is a TLV that contains an array of unicast data algorithm pairs.

## TLV Type


0x13

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
| UINT8 | Authentication algorithm as defined in [**WDI\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897792). |
| UINT8 | Cipher algorithm as defined in [**WDI\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/dn897802).     |

 

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

 

 




