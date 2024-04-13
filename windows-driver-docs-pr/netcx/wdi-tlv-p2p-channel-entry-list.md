---
title: WDI_TLV_P2P_CHANNEL_ENTRY_LIST (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_CHANNEL_ENTRY_LIST is a WiFiCx TLV that contains a channel number list.
ms.date: 08/31/2021
keywords:
 - WDI_TLV_P2P_CHANNEL_ENTRY_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_CHANNEL\_ENTRY\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_CHANNEL\_ENTRY\_LIST is a TLV that contains a channel number list.

## TLV Type


0xF9

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                               | Multiple TLV instances allowed | Optional | Description                          |
|--------------------------------------------------------------------|--------------------------------|----------|--------------------------------------|
| [**WDI\_TLV\_OPERATING\_CLASS**](wdi-tlv-operating-class.md)      |                                |          | The frequency band for the channels. |
| [**WDI\_TLV\_CHANNEL\_INFO\_LIST**](wdi-tlv-channel-info-list.md) |                                |          | The channel number list.             |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




