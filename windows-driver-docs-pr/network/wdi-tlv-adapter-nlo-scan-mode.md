---
title: WDI_TLV_ADAPTER_NLO_SCAN_MODE
ms.topic: reference
description: WDI_TLV_ADAPTER_NLO_SCAN_MODE is a TLV that indicates whether scans should be performed in active or passive mode.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ADAPTER_NLO_SCAN_MODE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ADAPTER\_NLO\_SCAN\_MODE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_ADAPTER\_NLO\_SCAN\_MODE is a TLV that indicates whether scans should be performed in active or passive mode.

## TLV Type


0x125

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | [**WDI\_SCAN\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_scan_type) value that indicates whether scans should be performed in active or passive mode. |

 

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

 

