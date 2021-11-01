---
title: WDI_TLV_SECONDARY_STA_BAND_CHANNEL (dot11wificxtypes.hpp)
description: WDI_TLV_SECONDARY_STA_BAND_CHANNEL is a WiFiCx TLV that contains a list of band IDs and channel numbers available for secondary STA connections. 
ms.date: 08/30/2021
keywords:
 - WDI_TLV_SECONDARY_STA_BAND_CHANNEL Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SECONDARY_STA_BAND_CHANNEL (dot11wificxtypes.hpp)

**WDI_TLV_SECONDARY_STA_BAND_CHANNEL** is a TLV that contains a list of band IDs and optional channel numbers available for secondary STA connections.

This TLV is used in the payload data for [NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY ](ndis-status-wdi-indication-secondary-sta-connectivity.md).

## TLV Type

0x202

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| Type                                                                                      | Multiple TLV instances allowed | Optional                                                                            | Description                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI_TLV_BANDID**](wdi-tlv-bandid.md)                                                  |                                |                                                                                     | The identifier for this band.                                                                                                                                                                                                                                          |
| [**WDI_TLV_CHANNEL_INFO_LIST**](wdi-tlv-channel-info-list.md)                  |                                |                                                                                  X  |List of channels. If this list is empty all of the bands/channels are unavailable. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

