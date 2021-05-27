---
title: OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS
description: OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS is sent in response to NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED. It has the parameters required to send the (Re)Association request. The command is sent to the driver as a direct OID.
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WDI\_SET\_FAST\_BSS\_TRANSITION\_PARAMETERS


OID\_WDI\_SET\_FAST\_BSS\_TRANSITION\_PARAMETERS is sent in response to [NDIS\_STATUS\_WDI\_INDICATION\_FT\_ASSOC\_PARAMS\_NEEDED](ndis-status-wdi-indication-ft-assoc-params-needed.md). It has the parameters required to send the (Re)Association request. The command is sent to the driver as a direct OID.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Set property parameters


| TLV                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                    |
|------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_STATUS**](./wdi-tlv-status.md)      |                                |          | If this status is success, the rest of the fields (RSNIE, MDE, FTE) are present. This indicates that there are no problems or errors with the Authentication response (for example, MIC check failure) and the IHV can proceed with the reassociation request. |
| [**WDI\_TLV\_FT\_RSNIE**](./wdi-tlv-ft-rsnie.md) |                                | X        | The RSN IE byte blob.                                                                                                                                                                                                                                          |
| [**WDI\_TLV\_FT\_MDE**](./wdi-tlv-ft-mde.md)     |                                | X        | The MDE byte blob.                                                                                                                                                                                                                                             |
| [**WDI\_TLV\_FT\_FTE**](./wdi-tlv-ft-fte.md)     |                                | X        | The FTE byte blob.                                                                                                                                                                                                                                             |

 

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

 

