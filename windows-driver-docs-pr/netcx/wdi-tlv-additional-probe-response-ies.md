---
title: WDI_TLV_ADDITIONAL_PROBE_RESPONSE_IES (dot11wificxtypes.hpp)
description: WDI_TLV_ADDITIONAL_PROBE_RESPONSE_IES is a WiFiCx TLV that contains probe response IEs.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ADDITIONAL_PROBE_RESPONSE_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADDITIONAL\_PROBE\_RESPONSE\_IES (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_ADDITIONAL\_PROBE\_RESPONSE\_IES is a TLV that contains probe response IEs.

## TLV Type


0x93

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | The array of probe response IEs. The Wi-Fi Direct port must add these additional IEs to the probe response packets when it is acting as a Wi-Fi Direct device or Group Owner. This member is ignored when the Wi-Fi Direct port is operating in client mode. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




