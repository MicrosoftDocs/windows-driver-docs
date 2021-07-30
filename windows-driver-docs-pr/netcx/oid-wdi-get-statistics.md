---
title: OID_WDI_GET_STATISTICS (dot11wificxintf.h)
description: The OID_WDI_GET_STATISTICS command requests that the IHV component returns MAC and PHY layer statistics.
ms.date: 07/31/2021
keywords:
 - OID_WDI_GET_STATISTICS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_GET\_STATISTICS (dot11wificxintf.h)


OID\_WDI\_GET\_STATISTICS requests that the IHV component returns MAC and PHY layer statistics.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Set not supported        | 1                               |

 

The MAC statistics must all be maintained per port. PHY statistics must also be maintained per port unless exempted. If PHY statistics cannot be maintained per port (as allowed by exemption), the statistics can be maintained per "channel" (PHY statistics for two ports operating on the same channel can be combined).

## Get property parameters


No additional parameters. The data in the header is sufficient.
## Get property results


| TLV                                                              | Multiple TLV instances allowed | Optional | Description              |
|------------------------------------------------------------------|--------------------------------|----------|--------------------------|
| [**WDI\_TLV\_MAC\_STATISTICS**](./wdi-tlv-mac-statistics.md) | X                              |          | Per-peer MAC statistics. |
| [**WDI\_TLV\_PHY\_STATISTICS**](./wdi-tlv-phy-statistics.md) | X                              |          | Per-port PHY statistics. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

