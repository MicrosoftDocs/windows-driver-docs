---
title: WDI_TLV_PM_PROTOCOL_OFFLOAD_GET
ms.topic: reference
description: WDI_TLV_PM_PROTOCOL_OFFLOAD_GET is a TLV that contains a protocol offload ID for OID_WDI_GET_PM_PROTOCOL_OFFLOAD.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_PM_PROTOCOL_OFFLOAD_GET Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_GET


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_GET is a TLV that contains a protocol offload ID for [OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD](./oid-wdi-get-pm-protocol-offload.md).

## TLV Type


0xA8

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | Specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter. |

 

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

 

