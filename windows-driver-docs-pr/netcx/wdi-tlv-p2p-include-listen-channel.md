---
title: WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL is a WiFiCx TLV that specifies whether the probe request should include the Listen Channel attribute during discovery.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INCLUDE\_LISTEN\_CHANNEL (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_INCLUDE\_LISTEN\_CHANNEL is a TLV that specifies whether the probe request should include the Listen Channel attribute during discovery.

 

## TLV Type


0x128

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | This parameter specifies whether the probe request should include the Listen Channel attribute during discovery. Valid values are 0 (do not include) and 1 (include). |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




