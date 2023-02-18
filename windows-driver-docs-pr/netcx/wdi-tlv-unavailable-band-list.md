---
title: WDI_TLV_UNAVAILABLE_BAND_LIST (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_UNAVAILABLE_BAND_LIST is a WiFiCx TLV that contains the list of bands on which the driver should not connect.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_UNAVAILABLE_BAND_LIST Network Drivers Starting with Windows Vista
---

# WDI_TLV_UNAVAILABLE_BAND_LIST (dot11wificxtypes.hpp)


WDI_TLV_UNAVAILABLE_BAND_LIST is a TLV that contains the list of bands on which the driver should not connect as they are used for Primary Sta connectivity. 

## TLV Type


0x200

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                               | Multiple TLV instances allowed | Optional | Description                                                                                     |
|--------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BANDID**](wdi-tlv-bandid.md)                         |              X                  |          | Specifies the identifier for the band.                                                          |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
