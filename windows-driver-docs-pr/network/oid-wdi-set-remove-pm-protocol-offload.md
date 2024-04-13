---
title: OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD
ms.topic: reference
description: OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD removes the protocol offload specified by the protocol offload ID.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD


OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD removes the protocol offload specified by the protocol offload ID.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                        | Multiple TLV instances allowed | Optional | Description          |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------|
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_REMOVE**](./wdi-tlv-pm-protocol-offload-remove.md) |                                |          | Protocol offload ID. |

 

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


[OID\_WDI\_GET\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-get-pm-protocol-offload.md)

[OID\_WDI\_SET\_ADD\_PM\_PROTOCOL\_OFFLOAD](oid-wdi-set-add-pm-protocol-offload.md)

 

