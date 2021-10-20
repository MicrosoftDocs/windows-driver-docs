---
title: OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES (dot11wificxintf.h)
description: The OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES command sends the list of neighbor reports received from the AP to the LE.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_NEIGHBOR_REPORT_ENTRIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_NEIGHBOR\_REPORT\_ENTRIES (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


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

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

