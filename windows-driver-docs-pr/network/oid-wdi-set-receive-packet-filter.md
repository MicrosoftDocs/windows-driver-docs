---
title: OID_WDI_SET_RECEIVE_PACKET_FILTER
description: OID_WDI_SET_RECEIVE_PACKET_FILTER defines a bitmask filter for data packets to be indicated for a given virtualized port.
ms.assetid: 180efda5-3ca2-40f8-89d1-098a53f33844
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_RECEIVE_PACKET_FILTER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER


OID\_WDI\_SET\_RECEIVE\_PACKET\_FILTER defines a bitmask filter for data packets to be indicated for a given virtualized port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

If set, the port shall only notify the host of packets which match the provided filter. These filters are similar to the required 802.11 filters provided to [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

## Set property parameters


| TLV                                                                                   | Multiple TLV instances allowed | Optional | Description                          |
|---------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------|
| [**WDI\_TLV\_PACKET\_FILTER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898019) |                                |          | The bitmask filter for data packets. |

 

## Set property results


No additional data. The data in the header is sufficient.
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

 

 




