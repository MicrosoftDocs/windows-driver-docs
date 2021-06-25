---
title: WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS (dot11wificxtypes.h)
description: WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS is a WiFiCx TLV that contains Wi-Fi Direct discovery channel settings.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_P2P_DISCOVERY_CHANNEL_SETTINGS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DISCOVERY\_CHANNEL\_SETTINGS (dot11wificxtypes.h)


WDI\_TLV\_P2P\_DISCOVERY\_CHANNEL\_SETTINGS is a TLV that contains Wi-Fi Direct discovery channel settings.

## TLV Type


0xE8

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                   | Multiple TLV instances allowed | Optional | Description                         |
|------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------|
| [**WDI\_TLV\_P2P\_LISTEN\_DURATION**](wdi-tlv-p2p-listen-duration.md) |                                |          | The cycle duration and listen time. |
| [**WDI\_TLV\_BAND\_CHANNEL**](wdi-tlv-band-channel.md)                | X                              |          | The list of channels to scan.       |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




