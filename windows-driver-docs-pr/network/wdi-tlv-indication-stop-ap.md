---
title: WDI_TLV_INDICATION_STOP_AP
ms.topic: reference
description: WDI_TLV_INDICATION_STOP_AP is a TLV that contains the reason for a Stop AP indication.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_INDICATION_STOP_AP Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_INDICATION\_STOP\_AP

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_INDICATION\_STOP\_AP is a TLV that contains the reason for a Stop AP indication.

## TLV Type


0xE6

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------|
| UINT32 | The Stop AP reason. See [**WDI\_STOP\_AP\_REASON**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_stop_ap_reason) for possible reason values. |

 

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

## See also


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP](./ndis-status-wdi-indication-stop-ap.md)

 

