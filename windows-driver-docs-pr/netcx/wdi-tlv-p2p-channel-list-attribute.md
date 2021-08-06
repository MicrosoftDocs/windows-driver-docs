---
title: WDI_TLV_P2P_CHANNEL_LIST_ATTRIBUTE (dot11wificxtypes.h)
description: WDI_TLV_P2P_CHANNEL_LIST_ATTRIBUTE is a WiFiCx TLV that contains channel list attributes.
ms.date: 08/30/2021
keywords:
 - WDI_TLV_P2P_CHANNEL_LIST_ATTRIBUTE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CHANNEL\_LIST\_ATTRIBUTE (dot11wificxtypes.h)


WDI\_TLV\_P2P\_CHANNEL\_LIST\_ATTRIBUTE is a TLV that contains channel list attributes.

## TLV Type


0xD5

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                          | Multiple TLV instances allowed | Optional | Description              |
|-------------------------------------------------------------------------------|--------------------------------|----------|--------------------------|
| [**WDI\_TLV\_COUNTRY\_REGION\_LIST**](wdi-tlv-country-region-list.md)        |                                |          | The country/region list. |
| [**WDI\_TLV\_P2P\_CHANNEL\_ENTRY\_LIST**](wdi-tlv-p2p-channel-entry-list.md) | X                              |          | The list of channels.    |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




