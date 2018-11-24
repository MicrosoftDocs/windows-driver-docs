---
title: OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES
description: OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES sends the list of neighbor reports received from the AP to the LE. This is sent as soon as the UE receives the neighbor report from the currently connected AP.
ms.assetid: F77FDA4A-3029-4F6E-A82E-B318543484FF
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_NEIGHBOR\_REPORT\_ENTRIES


OID\_WDI\_SET\_NEIGHBOR\_REPORT\_ENTRIES sends the list of neighbor reports received from the AP to the LE. This is sent as soon as the UE receives the neighbor report from the currently connected AP.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Set property parameters


| TLV                                                                             | Multiple TLV instances allowed | Optional | Description                   |
|---------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------|
| [**WDI\_TLV\_NEIGHBOR\_REPORT\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt269133) | X                              |          | The list of neighbor reports. |

 

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

 

 




