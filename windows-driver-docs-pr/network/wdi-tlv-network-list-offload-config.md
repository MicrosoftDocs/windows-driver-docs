---
title: WDI_TLV_NETWORK_LIST_OFFLOAD_CONFIG
ms.topic: reference
description: WDI_TLV_NETWORK_LIST_OFFLOAD_CONFIG is a TLV that contains Network List Offload (NLO) configuration.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_NETWORK_LIST_OFFLOAD_CONFIG Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_CONFIG

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_CONFIG is a TLV that contains Network List Offload (NLO) configuration.

## TLV Type


0xDA

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------|
| UINT32 | Reserved field.                                                                                                       |
| UINT32 | The delay (in seconds) before the scan schedule starts.                                                               |
| UINT32 | The period (in seconds) to scan in the first phase.                                                                   |
| UINT32 | The number of iterations in the fast scan phase.                                                                      |
| UINT32 | The period (in seconds) to scan in the slow scan phase. This phase lasts indefinitely until a new NLO command is set. |

 

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

 

 




