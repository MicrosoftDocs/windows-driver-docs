---
title: WDI_TLV_P2P_CHANNEL_NUMBER (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_CHANNEL_NUMBER is a WiFiCx TLV that contains Wi-Fi Direct channel number information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_CHANNEL_NUMBER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CHANNEL\_NUMBER (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_CHANNEL\_NUMBER is a TLV that contains Wi-Fi Direct channel number information.

## TLV Type


0x82

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                          | Description                                                                        |
|-------------------------------|------------------------------------------------------------------------------------|
| UINT8\[3\]                    | The country or region code where the operating class and channel number are valid. |
| UINT8                         | The operating class/frequency band for the channel number.                         |
| WDI\_CHANNEL\_NUMBER (UINT32) | The channel number for the Wi-Fi Direct Device or Group.                           |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




