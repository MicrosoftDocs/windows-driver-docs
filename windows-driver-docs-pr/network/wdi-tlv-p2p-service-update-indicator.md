---
title: WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR
ms.topic: reference
description: WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR is a TLV that contains a Wi-Fi Direct service update indicator.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_SERVICE\_UPDATE\_INDICATOR

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_SERVICE\_UPDATE\_INDICATOR is a TLV that contains a Wi-Fi Direct service update indicator.

## TLV Type


0x115

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16 | The service update indicator to include in ANQP responses if the driver supports responding to service information discovery ANQP requests. |

 

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

 

 




