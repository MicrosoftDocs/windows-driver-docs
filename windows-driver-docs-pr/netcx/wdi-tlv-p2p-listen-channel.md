---
title: WDI_TLV_P2P_LISTEN_CHANNEL (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_LISTEN_CHANNEL is a WiFiCx TLV that contains Wi-Fi Direct channel information.
ms.date: 08/30/2021
keywords:
 - WDI_TLV_P2P_LISTEN_CHANNEL Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_LISTEN\_CHANNEL (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_LISTEN\_CHANNEL is a TLV that contains Wi-Fi Direct channel information.

## TLV Type


0x114

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

 

 




