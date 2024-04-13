---
title: WDI_TLV_P2P_LISTEN_DURATION
ms.topic: reference
description: WDI_TLV_P2P_LISTEN_DURATION is a TLV that contains Wi-Fi Direct listen duration information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_LISTEN_DURATION Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_LISTEN\_DURATION

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_LISTEN\_DURATION is a TLV that contains Wi-Fi Direct listen duration information.

## TLV Type


0xE9

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                    |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The duration, in milliseconds, of the listen cycle. The adapter is in listen state during this time.                                                           |
| UINT32 | The duration, in milliseconds, that the adapter is expected to actively listen during the listen cycle. This duration must be less than listen cycle duration. |

 

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

 

 




