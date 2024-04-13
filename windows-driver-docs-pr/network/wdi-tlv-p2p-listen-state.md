---
title: WDI_TLV_P2P_LISTEN_STATE
ms.topic: reference
description: WDI_TLV_P2P_LISTEN_STATE is a TLV that contains a Wi-Fi Direct listen state.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_LISTEN_STATE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_LISTEN\_STATE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_LISTEN\_STATE is a TLV that contains a Wi-Fi Direct listen state.

## TLV Type


0x81

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                         | Description                            |
|--------------------------------------------------------------|----------------------------------------|
| [**WDI\_P2P\_LISTEN\_STATE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_listen_state) | The desired Wi-Fi Direct listen state. |

 

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

 

