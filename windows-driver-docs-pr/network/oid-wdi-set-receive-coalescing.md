---
title: OID_WDI_SET_RECEIVE_COALESCING
ms.topic: reference
description: OID_WDI_SET_RECEIVE_COALESCING is used by the host to add a packet filter for packet coalescing.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_RECEIVE_COALESCING Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_RECEIVE\_COALESCING


OID\_WDI\_SET\_RECEIVE\_COALESCING is used by the host to add a packet filter for packet coalescing.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

When the host receives a request from the OS to set packet coalescing filters, it uses this command to add a packet filter for packet coalescing. To clear a packet filter for packet coalescing, see [OID\_WDI\_SET\_CLEAR\_RECEIVE\_COALESCING](oid-wdi-set-clear-receive-coalescing.md).

## Set property parameters


| TLV                                                                               | Multiple TLV instances allowed | Optional | Description                                 |
|-----------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------|
| [**WDI\_TLV\_SET\_RECEIVE\_COALESCING**](./wdi-tlv-set-receive-coalescing.md) |                                |          | The packet coalescing parameters to be set. |

 

## Set property results


No additional parameters. The data in the header is sufficient.

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WDI\_SET\_CLEAR\_RECEIVE\_COALESCING](oid-wdi-set-clear-receive-coalescing.md)

 

