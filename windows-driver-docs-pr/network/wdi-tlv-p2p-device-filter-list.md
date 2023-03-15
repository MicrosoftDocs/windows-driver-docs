---
title: WDI_TLV_P2P_DEVICE_FILTER_LIST
ms.topic: reference
description: WDI_TLV_P2P_DEVICE_FILTER_LIST is a TLV that contains a list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_DEVICE_FILTER_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DEVICE\_FILTER\_LIST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_DEVICE\_FILTER\_LIST is a TLV that contains a list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery.

## TLV Type


0xCE

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                                                                                         |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address)\[\] | A list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery. |

 

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

 

