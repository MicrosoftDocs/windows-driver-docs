---
title: WDI_TLV_P2P_ACTION_FRAME_IES (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_ACTION_FRAME_IES is a WiFiCx TLV that contains action frame IEs.
ms.date: 07/30/2021
keywords:
 - WDI_TLV_P2P_ACTION_FRAME_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ACTION\_FRAME\_IES (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_ACTION\_FRAME\_IES is a TLV that contains action frame IEs.

## TLV Type


0x90

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                  |
|-----------|----------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the set of IEs that are sent to the remote device. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




