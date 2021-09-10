---
title: WDI_TLV_CHANNEL_INFO_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_CHANNEL_INFO_LIST is a WiFiCx TLV that contains a list of channels.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_CHANNEL_INFO_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CHANNEL\_INFO\_LIST (dot11wificxtypes.hpp)


WDI\_TLV\_CHANNEL\_INFO\_LIST is a TLV that contains a list of channels.

## TLV Type


0x41

## Length


The size (in bytes) of the array of WDI\_CHANNEL\_NUMBER (UINT32) structures. The array must contain 1 or more elements.

## Values


| Type       | Description                 |
|------------|-----------------------------|
| UINT32\[\] | An array of Wi-Fi channels. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




