---
title: WDI_TLV_P2P_INSTANCE_NAME (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_INSTANCE_NAME is a WiFiCx TLV that contains the Instance Name of the service.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_P2P_INSTANCE_NAME Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_INSTANCE\_NAME (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_INSTANCE\_NAME is a TLV that contains the Instance Name of the service.

 

## TLV Type


0x12B

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                     |
|-----------|-----------------------------------------------------------------|
| UINT8\[\] | The Instance Name of the service in UTF-8, up to 63 bytes long. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




