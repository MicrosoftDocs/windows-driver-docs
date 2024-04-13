---
title: WDI_TLV_HESSID
ms.topic: reference
description: WDI_TLV_HESSID is a TLV that contains a list of HESSIDs.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_HESSID Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_HESSID

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_HESSID is a TLV that contains a list of HESSIDs.

## TLV Type


0xC8

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description        |
|-------------------------------------------------------|--------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address)\[\] | A list of HESSIDs. |

 

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

 

