---
title: WDI_TLV_PM_PROTOCOL_OFFLOAD_REMOVE
ms.topic: reference
description: WDI_TLV_PM_PROTOCOL_OFFLOAD_REMOVE is a TLV that contains the protocol offload ID to be removed with OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PM_PROTOCOL_OFFLOAD_REMOVE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_REMOVE


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_REMOVE is a TLV that contains the protocol offload ID to be removed with [OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD](./oid-wdi-set-remove-pm-protocol-offload.md).

## TLV Type


0x6C

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                        |
|--------|------------------------------------|
| UINT32 | Specifies the protocol offload ID. |

 

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

 

