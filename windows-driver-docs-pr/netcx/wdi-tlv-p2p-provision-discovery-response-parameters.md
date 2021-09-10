---
title: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_PARAMETERS is a WiFiCx TLV that contains provision discovery response parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS is a TLV that contains provision discovery response parameters.

## TLV Type


0x113

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | The Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi P2P technical specification. |
| UINT8 | The bits set by the operating system in the above Group capability bitmap.                                                                                            |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




