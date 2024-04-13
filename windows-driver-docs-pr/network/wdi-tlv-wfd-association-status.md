---
title: WDI_TLV_WFD_ASSOCIATION_STATUS
ms.topic: reference
description: WDI_TLV_WFD_ASSOCIATION_STATUS is a TLV that contains the status code to be set when an association request is denied.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_WFD_ASSOCIATION_STATUS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_WFD\_ASSOCIATION\_STATUS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_WFD\_ASSOCIATION\_STATUS is a TLV that contains the status code to be set when an association request is denied.

## TLV Type


0x126

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                   |
|-------|-------------------------------------------------------------------------------|
| UINT8 | The DOT11\_WFD\_STATUS\_CODE to be set when an association request is denied. |

 

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

 

 




