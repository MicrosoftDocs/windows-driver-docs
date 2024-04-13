---
title: WDI_TLV_P2P_DEVICE_ADDRESS
ms.topic: reference
description: WDI_TLV_P2P_DEVICE_ADDRESS is a TLV that contains the device address of the Group Owner.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_DEVICE_ADDRESS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DEVICE\_ADDRESS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_DEVICE\_ADDRESS is a TLV that contains the device address of the Group Owner.

## TLV Type


0x91

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) structure.

## Values


| Type                                              | Description                            |
|---------------------------------------------------|----------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | The device address of the Group Owner. |

 

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

 

