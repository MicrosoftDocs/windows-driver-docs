---
title: WDI_TLV_RECEIVE_COALESCING_CONFIG
ms.topic: reference
description: WDI_TLV_RECEIVE_COALESCING_CONFIG is a TLV that contains receive coalescing configuration.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_RECEIVE_COALESCING_CONFIG Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_RECEIVE\_COALESCING\_CONFIG


WDI\_TLV\_RECEIVE\_COALESCING\_CONFIG is a TLV that contains receive coalescing configuration.

## TLV Type


0xDB

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                         |
|--------|---------------------------------------------------------------------|
| UINT32 | A unique queue ID to queue packets matching this filter.            |
| UINT32 | A filter ID with a value from 1 to the number of filters supported. |
| UINT32 | The maximum coalescing delay in milliseconds.                       |

 

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

## See also


[OID\_WDI\_SET\_RECEIVE\_COALESCING](./oid-wdi-set-receive-coalescing.md)

 

