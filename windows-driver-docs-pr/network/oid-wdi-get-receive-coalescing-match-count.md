---
title: OID_WDI_GET_RECEIVE_COALESCING_MATCH_COUNT
description: OID_WDI_GET_RECEIVE_COALESCING_MATCH_COUNT requests the number of packets that have matched receive filters on the network port.
ms.assetid: 45b68057-d62a-4b77-9634-dfbed2817f23
ms.date: 07/18/2017
keywords:
 - OID_WDI_GET_RECEIVE_COALESCING_MATCH_COUNT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_GET\_RECEIVE\_COALESCING\_MATCH\_COUNT


OID\_WDI\_GET\_RECEIVE\_COALESCING\_MATCH\_COUNT requests the number of packets that have matched receive filters on the network port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                                                              | Multiple TLV instances allowed | Optional | Description                                                                  |
|--------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------|
| [**WDI\_TLV\_COALESCING\_FILTER\_MATCH\_COUNT**](https://msdn.microsoft.com/library/windows/hardware/dn926252) |                                |          | The number of packets that have matched receive filters on the network port. |

 

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

 

 




