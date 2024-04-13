---
title: WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_PARAMETERS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_PARAMETERS is a WiFiCx TLV that contains Wi-Fi Provision Discovery Request parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_PROVISION_DISCOVERY_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_REQUEST\_PARAMETERS is a TLV that contains Wi-Fi Provision Discovery Request parameters.

## TLV Type


0x85

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi Direct technical specification. |
| UINT8 | The bits in the Group capability bitmap above that are set by the operating system.                                                                                  |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




