---
title: WDI_TLV_P2P_GROUP_OWNER_CAPABILITY (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_GROUP_OWNER_CAPABILITY is a WiFiCx TLV that contains Wi-Fi Direct Group Owner capability information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GROUP_OWNER_CAPABILITY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY is a TLV that contains Wi-Fi Direct Group Owner capability information.

## TLV Type


0x77

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8  | Specifies the Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi P2P technical specification. |
| UINT8  | Specifies the bits set by the operating system in the Group capability bitmap above.                                                                                            |
| UINT32 | Maximum client count for this Group Owner.                                                                                                                                      |

 

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




