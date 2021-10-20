---
title: WDI_TLV_CONNECTION_QUALITY_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_CONNECTION_QUALITY_PARAMETERS is a WiFiCx TLV that contains the desired Wi-Fi Connection Quality Hint.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CONNECTION_QUALITY_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CONNECTION\_QUALITY\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CONNECTION\_QUALITY\_PARAMETERS is a TLV that contains the desired Wi-Fi Connection Quality Hint.

## TLV Type


0xA3

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The desired Wi-Fi Connection Quality Hint, as defined in [**WDI\_CONNECTION\_QUALITY\_HINT**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_connection_quality_hint). |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
 

