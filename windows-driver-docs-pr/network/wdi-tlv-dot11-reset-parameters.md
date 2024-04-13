---
title: WDI_TLV_DOT11_RESET_PARAMETERS
ms.topic: reference
description: WDI_TLV_DOT11_RESET_PARAMETERS is a TLV that contains parameters for OID_WDI_TASK_DOT11_RESET.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_DOT11_RESET_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_DOT11\_RESET\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_DOT11\_RESET\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_DOT11\_RESET](./oid-wdi-task-dot11-reset.md).

## TLV Type


0xA2

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                     |
|-------|-----------------------------------------------------------------------------------------------------------------|
| UINT8 | If (and only if) this is set to 1, all MIB attributes for the port being reset are set to their default values. |

 

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

 

