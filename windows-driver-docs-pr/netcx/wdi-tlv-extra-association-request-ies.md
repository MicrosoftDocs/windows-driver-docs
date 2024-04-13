---
title: WDI_TLV_EXTRA_ASSOCIATION_REQUEST_IES (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_EXTRA_ASSOCIATION_REQUEST_IES is a WiFiCx TLV that contains Information Elements (IEs) that must be included in association requests sent by the port.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_EXTRA_ASSOCIATION_REQUEST_IES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES is a TLV that contains Information Elements (IEs) that must be included in association requests sent by the port.

## TLV Type


0x40

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the IEs that must be included in association requests sent by the port. These are applicable to any BSSID that the device associates with. They should be used in addition to the common and BSSID specific IEs. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




