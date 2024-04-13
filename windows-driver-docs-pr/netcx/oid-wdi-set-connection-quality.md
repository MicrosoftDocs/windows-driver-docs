---
title: OID_WDI_SET_CONNECTION_QUALITY (dot11wificxintf.h)
ms.topic: reference
description: The OID_WDI_SET_CONNECTION_QUALITY command provides a hint to the IHV component to enforce connection quality for a given virtualized port. This hint allows the port to optimize channel usage in different scenarios.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_CONNECTION_QUALITY Network Drivers Starting with Windows Vista
---

# OID\_WDI\_SET\_CONNECTION\_QUALITY (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_CONNECTION\_QUALITY provides a hint to the IHV component to enforce connection quality for a given virtualized port. This hint allows the port to optimize channel usage in different scenarios.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

**Note**  This property specifies data path quality of service hints, which may cause conflicts with other properties or tasks that are issued to the adapter.

 

## Set property parameters


| TLV                                                                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_CONNECTION\_QUALITY\_PARAMETERS**](./wdi-tlv-connection-quality-parameters.md)                           |                                |          | The desired Wi-Fi connection quality hint.                                                                                                                                                     |
| [**WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS**](./wdi-tlv-low-latency-connection-quality-parameters.md) |                                | X        | The behavior for low latency connection quality. This is only required if the connection quality is set to [**WDI\_CONNECTION\_QUALITY\_LOW\_LATENCY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_connection_quality_hint). |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

