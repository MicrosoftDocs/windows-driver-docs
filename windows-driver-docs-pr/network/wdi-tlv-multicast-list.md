---
title: WDI_TLV_MULTICAST_LIST
ms.topic: reference
description: WDI_TLV_MULTICAST_LIST is a TLV that contains an array of multicast MAC addresses.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_MULTICAST_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_MULTICAST\_LIST


WDI\_TLV\_MULTICAST\_LIST is a TLV that contains an array of multicast MAC addresses.

## TLV Type


0x6A

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                          |
|-------------------------------------------------------|--------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address)\[\] | An array of multicast MAC addresses. |

 

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

 

