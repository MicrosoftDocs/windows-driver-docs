---
title: WDI_TLV_AUTHENTICATION_RESPONSE_FRAME (dot11wificxtypes.hpp)
description: WDI_TLV_ASSOCIATION_RESPONSE_FRAME is a WiFiCx TLV that contains an authentication response frame.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_AUTHENTICATION_RESPONSE_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_AUTHENTICATION\_RESPONSE\_FRAME (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_RESPONSE\_FRAME is a TLV that contains an authentication response frame.

## TLV Type


0x124

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the authentication response that was received with a failure code. This does not include the 802.11 MAC header. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
