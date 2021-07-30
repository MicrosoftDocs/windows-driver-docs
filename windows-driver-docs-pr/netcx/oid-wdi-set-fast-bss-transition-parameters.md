---
title: OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS (dot11wificxintf.h)
description: The OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS command is sent in response to NDIS_STATUS_WDI_INDICATION_FT_ASSOC_PARAMS_NEEDED. It has the parameters required to send the (Re)Association request. The command is sent to the driver as a direct OID.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_FAST_BSS_TRANSITION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_FAST\_BSS\_TRANSITION\_PARAMETERS (dot11wificxintf.h)


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

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

