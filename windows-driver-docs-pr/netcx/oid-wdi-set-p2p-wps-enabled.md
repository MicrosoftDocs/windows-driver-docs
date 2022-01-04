---
title: OID_WDI_SET_P2P_WPS_ENABLED (dot11wificxintf.h)
description: The OID_WDI_SET_P2P_WPS_ENABLED command requests that the adapter enables or disables Wi-Fi Protected Setup (WPS) on the NIC.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_P2P_WPS_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_WDI\_SET\_P2P\_WPS\_ENABLED (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_P2P\_WPS\_ENABLED requests that the adapter enables or disables Wi-Fi Protected Setup (WPS) on the NIC.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                 | Multiple TLV instances allowed | Optional | Description                                 |
|---------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------|
| [**WDI\_TLV\_P2P\_WPS\_ENABLED**](./wdi-tlv-p2p-wps-enabled.md) |                                |          | Specifies whether to enable or disable WPS. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

