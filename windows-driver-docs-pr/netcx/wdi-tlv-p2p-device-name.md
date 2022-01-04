---
title: WDI_TLV_P2P_DEVICE_NAME (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_DEVICE_NAME is a WiFiCx TLV that contains a device name.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_DEVICE_NAME Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DEVICE\_NAME (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_DEVICE\_NAME is a TLV that contains a device name.

## TLV Type


0x92

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                               |
|-----------|---------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the device name for the device. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
 

 




