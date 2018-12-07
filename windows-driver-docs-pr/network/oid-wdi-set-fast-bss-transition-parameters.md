---
title: OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS
description: OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS is sent in response to NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED. It has the parameters required to send the (Re)Association request. The command is sent to the driver as a direct OID.
ms.assetid: D769E49D-C565-41CD-9C91-195B1223AE66
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_FAST\_BSS\_TRANSITION\_PARAMETERS


OID\_WDI\_SET\_FAST\_BSS\_TRANSITION\_PARAMETERS is sent in response to [NDIS\_STATUS\_WDI\_INDICATION\_FT\_ASSOC\_PARAMS\_NEEDED](ndis-status-wdi-indication-ft-assoc-params-needed.md). It has the parameters required to send the (Re)Association request. The command is sent to the driver as a direct OID.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Set property parameters


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                    |
|------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/dn898068)      |                                |          | If this status is success, the rest of the fields (RSNIE, MDE, FTE) are present. This indicates that there are no problems or errors with the Authentication response (for example, MIC check failure) and the IHV can proceed with the reassociation request. |
| [**WDI\_TLV\_FT\_RSNIE**](https://msdn.microsoft.com/library/windows/hardware/mt269125) |                                | X        | The RSN IE byte blob.                                                                                                                                                                                                                                          |
| [**WDI\_TLV\_FT\_MDE**](https://msdn.microsoft.com/library/windows/hardware/mt269120)     |                                | X        | The MDE byte blob.                                                                                                                                                                                                                                             |
| [**WDI\_TLV\_FT\_FTE**](https://msdn.microsoft.com/library/windows/hardware/mt269118)     |                                | X        | The FTE byte blob.                                                                                                                                                                                                                                             |

 

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

 

 




