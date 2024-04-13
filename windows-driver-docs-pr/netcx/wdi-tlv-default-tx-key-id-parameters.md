---
title: WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS is a WiFiCx TLV that contains the default key ID for packet transmission on a port for OID_WDI_SET_DEFAULT_KEY_ID.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS is a TLV that contains the default key ID for packet transmission on a port for [OID\_WDI\_SET\_DEFAULT\_KEY\_ID](./oid-wdi-set-default-key-id.md).

## TLV Type


0x54

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                     |
|--------|-----------------------------------------------------------------|
| UINT32 | Specifies the default key ID for packet transmission on a port. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

