---
title: WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR is a WiFiCx TLV that contains a Wi-Fi Direct service update indicator.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_SERVICE\_UPDATE\_INDICATOR (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_SERVICE\_UPDATE\_INDICATOR is a TLV that contains a Wi-Fi Direct service update indicator.

## TLV Type


0x115

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16 | The service update indicator to include in ANQP responses if the driver supports responding to service information discovery ANQP requests. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




