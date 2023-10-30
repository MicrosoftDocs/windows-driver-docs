---
title: WDI_TLV_BAND_CHANNEL (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_BAND_CHANNEL is a WiFiCx TLV that contains the channels to scan for a specified band.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_BAND_CHANNEL Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BAND\_CHANNEL (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_BAND\_CHANNEL is a TLV that contains the channels to scan for a specified band.

## TLV Type


0x2C

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                               | Multiple TLV instances allowed | Optional | Description                                                                                     |
|--------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BANDID**](wdi-tlv-bandid.md)                         |                                |          | Specifies the identifier for the band.                                                          |
| [**WDI\_TLV\_CHANNEL\_INFO\_LIST**](wdi-tlv-channel-info-list.md) |                                |          | Specifies a list of channels to scan. If the list is empty, the port must scan on all channels. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




