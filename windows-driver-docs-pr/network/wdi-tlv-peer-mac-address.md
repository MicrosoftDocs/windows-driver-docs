---
title: WDI_TLV_PEER_MAC_ADDRESS
ms.topic: reference
description: WDI_TLV_PEER_MAC_ADDRESS is a TLV that contains the MAC address of the peer.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PEER_MAC_ADDRESS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PEER\_MAC\_ADDRESS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_PEER\_MAC\_ADDRESS is a TLV that contains the MAC address of the peer.

## TLV Type


0x4C

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) structure.

## Values


| Type                                              | Description                                  |
|---------------------------------------------------|----------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | Specifies the Wi-Fi MAC address of the peer. |

 

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

 

