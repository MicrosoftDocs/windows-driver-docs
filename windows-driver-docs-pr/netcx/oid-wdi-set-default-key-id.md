---
title: OID_WDI_SET_DEFAULT_KEY_ID (dot11wificxintf.h)
description: The OID_WDI_SET_DEFAULT_KEY_ID command sets the default key ID for packet transmission on a port.
ms.date: 07/21/2021
keywords:
 - OID_WDI_SET_DEFAULT_KEY_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_DEFAULT\_KEY\_ID (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_DEFAULT\_KEY\_ID sets the default key ID for packet transmission on a port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                             | Multiple TLV instances allowed | Optional | Description                                             |
|-------------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------|
| [**WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS**](./wdi-tlv-default-tx-key-id-parameters.md) |                                |          | The default key ID for packet transmission on the port. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

