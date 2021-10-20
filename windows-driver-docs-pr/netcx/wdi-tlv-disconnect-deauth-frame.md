---
title: WDI_TLV_DISCONNECT_DEAUTH_FRAME (dot11wificxtypes.hpp)
description: WDI_TLV_DISCONNECT_DEAUTH_FRAME is a WiFiCx TLV that contains the received deauthentication frame.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DISCONNECT_DEAUTH_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DISCONNECT\_DEAUTH\_FRAME (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_DISCONNECT\_DEAUTH\_FRAME is a TLV that contains the received deauthentication frame.

## TLV Type


0x37

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                   |
|-----------|-------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the received deauthentication frame. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




