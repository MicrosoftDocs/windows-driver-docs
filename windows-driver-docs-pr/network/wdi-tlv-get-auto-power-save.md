---
title: WDI_TLV_GET_AUTO_POWER_SAVE
ms.topic: reference
description: WDI_TLV_GET_AUTO_POWER_SAVE is a TLV that contains auto power save information for OID_WDI_GET_AUTO_POWER_SAVE.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_GET_AUTO_POWER_SAVE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_GET\_AUTO\_POWER\_SAVE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_GET\_AUTO\_POWER\_SAVE is a TLV that contains auto power save information for [OID\_WDI\_GET\_AUTO\_POWER\_SAVE](./oid-wdi-get-auto-power-save.md).

## TLV Type


0xB3

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                               | Description                                                                                                        |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| UINT8                                                                              | The firmware current AutoPSM state.                                                                                |
| UINT8                                                                              | Reserved.                                                                                                          |
| UINT16                                                                             | Reserved.                                                                                                          |
| UINT16                                                                             | The beacon interval in milliseconds.                                                                               |
| UINT8                                                                              | The listen interval, in the unit of the beacon interval (for example, 1).                                          |
| UINT8                                                                              | The listen interval in the last low power state (for example, 5). If there is no last low power state, set to 255. |
| [**WDI\_POWER\_SAVE\_LEVEL**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_power_save_level) (UINT32)              | The power mode.                                                                                                    |
| [**WDI\_POWER\_SAVE\_LEVEL**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_power_save_level) (UINT32)              | The power mode in Dx.                                                                                              |
| [**WDI\_POWER\_MODE\_REASON\_CODE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_power_mode_reason_code) (UINT32) | The reason for entering the Power Save state and listen interval.                                                  |
| UINT64                                                                             | Milliseconds since start.                                                                                          |
| UINT64                                                                             | Milliseconds in power save mode.                                                                                   |
| UINT64                                                                             | Number of received multicast packets, including broadcast.                                                         |
| UINT64                                                                             | Number of sent multicast packets, including broadcast.                                                             |
| UINT64                                                                             | Number of received unicast packets.                                                                                |
| UINT64                                                                             | Number of sent unicast packets.                                                                                    |

 

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

 

