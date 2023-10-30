---
title: WDI_TLV_BSS_SELECTION_PARAMETERS
ms.topic: reference
description: WDI_TLV_BSS_SELECTION_PARAMETERS is a TLV that contains WDI_BSS_SELECTION_FLAGS that are used by host for BSS selection.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BSS_SELECTION_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSS\_SELECTION\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BSS\_SELECTION\_PARAMETERS is a TLV that contains [**WDI\_BSS\_SELECTION\_FLAGS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_bss_selection_flags) that are used by host for BSS selection.

## TLV Type


0x10F

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------|
| UINT32 | [**WDI\_BSS\_SELECTION\_FLAGS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_bss_selection_flags) that are used by the host for BSS selection. |

 

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

 

