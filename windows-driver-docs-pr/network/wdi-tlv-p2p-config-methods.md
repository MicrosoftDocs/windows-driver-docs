---
title: WDI_TLV_P2P_CONFIG_METHODS
ms.topic: reference
description: WDI_TLV_P2P_CONFIG_METHODS is a TLV that contains Wi-Fi Direct configuration methods.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_CONFIG_METHODS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_CONFIG\_METHODS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_CONFIG\_METHODS is a TLV that contains Wi-Fi Direct configuration methods.

## TLV Type


0xEB

## Length


The size (in bytes) of a UINT16.

## Values


| Type   | Description                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16 | Configuration methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_wps_configuration_method). Only PIN display, PIN keypad, and WFDS are applicable. |

 

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

 

