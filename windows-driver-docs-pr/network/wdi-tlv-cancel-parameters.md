---
title: WDI_TLV_CANCEL_PARAMETERS
ms.topic: reference
description: WDI_TLV_CANCEL_PARAMETERS is a TLV that contains parameters for OID_WDI_ABORT_TASK.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_CANCEL_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CANCEL\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_CANCEL\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_ABORT\_TASK](./oid-wdi-abort-task.md).

## TLV Type


0x2B

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                   | Description                                             |
|------------------------|---------------------------------------------------------|
| NDIS\_OID              | Specifies the OID from the original task being aborted. |
| UINT32                 | Specifies the transaction ID from the original task.    |
| WDI\_PORT\_ID (UINT16) | Specifies the port ID from the original task.           |

 

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

 

