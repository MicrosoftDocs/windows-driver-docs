---
title: WDI_TLV_P2P_GROUP_ID (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_GROUP_ID is a WiFiCx TLV that contains the Group ID for Wi-Fi Direct GO.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GROUP_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GROUP\_ID (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_GROUP\_ID is a TLV that contains the Group ID for Wi-Fi Direct GO.

## TLV Type


0x75

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                 | Multiple TLV instances allowed | Optional | Description                                          |
|----------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------|
| [**WDI\_TLV\_P2P\_DEVICE\_ADDRESS**](wdi-tlv-p2p-device-address.md) |                                |          | Specifies the device address of the Wi-Fi Direct GO. |
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid.md)                          |                                |          | Specifies the Group SSID.                            |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




