---
title: WDI_TLV_P2P_PERSISTENT_GROUP_ID (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_PERSISTENT_GROUP_ID is a WiFiCx TLV that contains a Group ID of a Persistent Group to be used for a connection.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_PERSISTENT_GROUP_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_PERSISTENT\_GROUP\_ID (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_PERSISTENT\_GROUP\_ID is a TLV that contains a Group ID of a Persistent Group to be used for a connection.

## TLV Type


0xF1

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                 | Multiple TLV instances allowed | Optional | Description                            |
|----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------|
| [**WDI\_TLV\_P2P\_DEVICE\_ADDRESS**](wdi-tlv-p2p-device-address.md) |                                |          | The device address of the Group Owner. |
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid.md)                               |                                |          | The Group SSID.                        |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
 

 




