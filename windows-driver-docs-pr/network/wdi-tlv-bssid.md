---
title: WDI_TLV_BSSID
ms.topic: reference
description: WDI_TLV_BSSID is a TLV that contains the BSSID of a BSS.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BSSID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSSID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BSSID is a TLV that contains the BSSID of a BSS.

## TLV Type


0x2

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) structure.

## Values


| Type                                              | Description                                 |
|---------------------------------------------------|---------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) | A Wi-Fi MAC address that specifies a BSSID. |

 

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

 

