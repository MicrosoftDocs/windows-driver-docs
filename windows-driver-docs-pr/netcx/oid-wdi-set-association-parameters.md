---
title: OID_WDI_SET_ASSOCIATION_PARAMETERS (dot11wificxintf.h)
description: The OID_WDI_SET_ASSOCIATION_PARAMETERS command specifies parameters that the adapter can use during association to a set of BSSIDs.
ms.date: 06/30/2021
keywords:
 - OID_WDI_SET_ASSOCIATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS specifies parameters that the adapter can use during association to a set of BSSIDs.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

This command replaces the previously configured list of BSSID-specific association parameters.

## Set property parameters


| TLV                                                                     | Multiple TLV instances allowed | Optional | Description                     |
|-------------------------------------------------------------------------|--------------------------------|----------|---------------------------------|
| [**WDI\_TLV\_CONNECT\_BSS\_ENTRY**](./wdi-tlv-connect-bss-entry.md) | X                              |          | The BSS entries and parameters. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|
 

