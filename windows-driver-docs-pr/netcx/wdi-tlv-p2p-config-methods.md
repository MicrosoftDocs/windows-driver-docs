---
title: WDI_TLV_P2P_CONFIG_METHODS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_CONFIG_METHODS is a WiFiCx TLV that contains Wi-Fi Direct configuration methods.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_P2P_CONFIG_METHODS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_CONFIG\_METHODS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_CONFIG\_METHODS is a TLV that contains Wi-Fi Direct configuration methods.

## TLV Type


0xEB

## Length


The size (in bytes) of a UINT16.

## Values


| Type   | Description                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16 | Configuration methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_wps_configuration_method). Only PIN display, PIN keypad, and WFDS are applicable. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

