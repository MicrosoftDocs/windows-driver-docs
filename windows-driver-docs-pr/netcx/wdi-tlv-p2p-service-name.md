---
title: WDI_TLV_P2P_SERVICE_NAME (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_SERVICE_NAME is a WiFiCx TLV that contains the name of a service.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_P2P_SERVICE_NAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SERVICE\_NAME (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_SERVICE\_NAME is a TLV that contains the name of a service.

## TLV Type


0xEC

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                         |
|-----------|-----------------------------------------------------|
| UINT8\[\] | The name of the service, in UTF-8, up to 255 bytes. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




