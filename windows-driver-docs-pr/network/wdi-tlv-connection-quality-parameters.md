---
title: WDI_TLV_CONNECTION_QUALITY_PARAMETERS
description: WDI_TLV_CONNECTION_QUALITY_PARAMETERS is a TLV that contains the desired Wi-Fi Connection Quality Hint.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CONNECTION_QUALITY_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CONNECTION\_QUALITY\_PARAMETERS


WDI\_TLV\_CONNECTION\_QUALITY\_PARAMETERS is a TLV that contains the desired Wi-Fi Connection Quality Hint.

## TLV Type


0xA3

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The desired Wi-Fi Connection Quality Hint, as defined in [**WDI\_CONNECTION\_QUALITY\_HINT**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_connection_quality_hint). |

 

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

 

