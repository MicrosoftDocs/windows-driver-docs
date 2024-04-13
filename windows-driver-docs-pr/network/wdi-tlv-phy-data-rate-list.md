---
title: WDI_TLV_PHY_DATA_RATE_LIST
ms.topic: reference
description: WDI_TLV_PHY_DATA_RATE_LIST is a TLV that contains a list of data rates.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PHY_DATA_RATE_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PHY\_DATA\_RATE\_LIST


WDI\_TLV\_PHY\_DATA\_RATE\_LIST is a TLV that contains a list of data rates.

## TLV Type


0x13

## Length


The size (in bytes) of the array of WDI\_DATA\_RATE\_LIST elements. The array must contain 1 or more elements.

**Note**  WDI\_DATA\_RATE\_LIST is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                      | Description                                                                                             |
|---------------------------|---------------------------------------------------------------------------------------------------------|
| WDI\_DATA\_RATE\_LIST\[\] | An array of data rates. Each data rate in the array must contain data rate flags and a data rate value. |

 

WDI\_DATA\_RATE\_LIST consists of the following elements.

| Type   | Description                                                                                   |
|--------|-----------------------------------------------------------------------------------------------|
| UINT8  | The data rate flags as defined in [**WDI\_DATA\_RATE\_FLAGS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_data_rate_flags). |
| UINT16 | The data rate value.                                                                          |

 

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

 

