---
title: WDI_TLV_P2P_DEVICE_CAPABILITY (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_DEVICE_CAPABILITY is a WiFiCx TLV that contains Wi-Fi Direct device capabilities.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_DEVICE_CAPABILITY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DEVICE\_CAPABILITY (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_DEVICE\_CAPABILITY is a TLV that contains Wi-Fi Direct device capabilities.

## TLV Type


0x84

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| UINT8  | A bitmap of the Wi-Fi Direct device capabilities as defined in Table 12 of the Wi-Fi Direct technical specification.            |
| UINT8  | A bitmap of the Wi-Fi Direct capabilities in the above device capability bitmap that are currently set by the operating system. |
| UINT32 | A bitmask that indicates which WPS versions are enabled.                                                                        |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




