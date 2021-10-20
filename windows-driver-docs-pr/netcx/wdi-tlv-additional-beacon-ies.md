---
title: WDI_TLV_ADDITIONAL_BEACON_IES (dot11wificxtypes.hpp)
description: WDI_TLV_ADDITIONAL_BEACON_IES is a WiFiCx TLV that contains additional beacon IEs.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ADDITIONAL_BEACON_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADDITIONAL\_BEACON\_IES (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_ADDITIONAL\_BEACON\_IES is a TLV that contains additional beacon IEs.

## TLV Type


0x98

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | The array of beacon IEs. The Wi-Fi Direct port must add these additional IEs to the beacon packets when it is acting as a Group Owner. These are ignored when the Wi-Fi Direct port is operating in device or client mode. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




