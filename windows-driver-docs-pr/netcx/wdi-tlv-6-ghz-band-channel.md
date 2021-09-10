---
title: WDI_TLV_6_GHZ_BAND_CHANNEL (dot11wificxtypes.hpp)
description: WDI_TLV_6_GHZ_BAND_CHANNEL is a WiFiCx TLV that contains the channels to scan in the 6 GHz band.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_BSS_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_6_GHZ_BAND_CHANNEL (dot11wificxtypes.hpp)


WDI_TLV_6_GHZ_BAND_CHANNEL is a TLV that contains the channels to scan in the 6 GHz band.

## TLV Type


0x8

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                      | Multiple TLV instances allowed | Optional                                                                            | Description                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](wdi-tlv-bssid.md)                                                  |                                |                                                                                     | The BSSID of the AP.                                                                                                                                                                                                                                             |
| [**WDI_TLV_CHANNEL_NUMBER**](wdi-tlv-channel-number.md)                  |                                                                                                                  | | The channel on which the AP is parked.        |
| [**WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO**](wdi-tlv-bss-entry-channel-info.md)             |                                |     X                                                                                | The  channel number and band ID on which the colocated AP was seen.                                                                                                                                                                                                         |


 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




