---
title: WDI_TLV_INDICATION_CAN_SUSTAIN_AP
description: WDI_TLV_INDICATION_CAN_SUSTAIN_AP is a TLV that contains the reason for a Can Sustain AP indication.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_INDICATION_CAN_SUSTAIN_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INDICATION\_CAN\_SUSTAIN\_AP


WDI\_TLV\_INDICATION\_CAN\_SUSTAIN\_AP is a TLV that contains the reason for a Can Sustain AP indication.

## TLV Type


0xE7

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The Can Sustain AP reason. See [**WDI\_CAN\_SUSTAIN\_AP\_REASON**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_can_sustain_ap_reason) for possible reason values. |

 

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


[NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP](./ndis-status-wdi-indication-can-sustain-ap.md)

 

