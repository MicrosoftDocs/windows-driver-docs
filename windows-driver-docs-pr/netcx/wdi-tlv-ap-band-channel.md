---
title: WDI_TLV_AP_BAND_CHANNEL (dot11wificxtypes.hpp)
description: WDI_TLV_AP_BAND_CHANNEL is a WiFiCx TLV that specifies access point band and channel information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_AP_BAND_CHANNEL Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_AP\_BAND\_CHANNEL (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_AP\_BAND\_CHANNEL is a TLV that specifies access point band and channel information.

 

## TLV Type


0x127

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                               | Multiple TLV instances allowed | Optional | Description                                                |
|--------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------|
| [**WDI\_TLV\_BANDID**](wdi-tlv-bandid.md)                         |                                |          | Specifies the identifier for the band.                     |
| [**WDI\_TLV\_CHANNEL\_INFO\_LIST**](wdi-tlv-channel-info-list.md) |                                | X        | Specifies a list of channels to start the access point on. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

## See also


[OID\_WDI\_TASK\_START\_AP](./oid-wdi-task-start-ap.md)

 

