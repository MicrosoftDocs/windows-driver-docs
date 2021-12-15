---
title: WDI_TLV_P2P_LISTEN_DURATION (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_LISTEN_DURATION is a WiFiCx TLV that contains Wi-Fi Direct listen duration information.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_P2P_LISTEN_DURATION Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_LISTEN\_DURATION (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_LISTEN\_DURATION is a TLV that contains Wi-Fi Direct listen duration information.

## TLV Type


0xE9

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                    |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The duration, in milliseconds, of the listen cycle. The adapter is in listen state during this time.                                                           |
| UINT32 | The duration, in milliseconds, that the adapter is expected to actively listen during the listen cycle. This duration must be less than listen cycle duration. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




