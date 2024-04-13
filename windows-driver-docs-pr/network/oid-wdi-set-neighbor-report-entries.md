---
title: OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES
ms.topic: reference
description: OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES sends the list of neighbor reports received from the AP to the LE. This is sent as soon as the UE receives the neighbor report from the currently connected AP.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_NEIGHBOR\_REPORT\_ENTRIES

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_SET\_NEIGHBOR\_REPORT\_ENTRIES sends the list of neighbor reports received from the AP to the LE. This is sent as soon as the UE receives the neighbor report from the currently connected AP.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Set property parameters


| TLV                                                                             | Multiple TLV instances allowed | Optional | Description                   |
|---------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------|
| [**WDI\_TLV\_NEIGHBOR\_REPORT\_ENTRY**](./wdi-tlv-neighbor-report-entry.md) | X                              |          | The list of neighbor reports. |

 

## Set property results


No additional data. The data in the header is sufficient.

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

 

