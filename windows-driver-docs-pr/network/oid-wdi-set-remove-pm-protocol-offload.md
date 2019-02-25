---
title: OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD
description: OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD removes the protocol offload specified by the protocol offload ID.
ms.assetid: 47850c43-4d10-48f5-b2e9-1f94f23eabf2
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_REMOVE_PM_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD


OID\_WDI\_SET\_REMOVE\_PM\_PROTOCOL\_OFFLOAD removes the protocol offload specified by the protocol offload ID.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                        | Multiple TLV instances allowed | Optional | Description          |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------|
| [**WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_REMOVE**](https://msdn.microsoft.com/library/windows/hardware/dn898037) |                                |          | Protocol offload ID. |

 

## Set property results


No additional parameters. The data in the header is sufficient.
Requirements
------------

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

 

 




