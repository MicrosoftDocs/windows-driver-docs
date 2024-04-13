---
title: WDI_TLV_BEACON_PROBE_RESPONSE (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_BEACON_PROBE_RESPONSE is a WiFiCx TLV that contains the latest beacon or probe response frame received by the port.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_BEACON_PROBE_RESPONSE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BEACON\_PROBE\_RESPONSE (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_BEACON\_PROBE\_RESPONSE is a TLV that contains the latest beacon or probe response frame received by the port.

## TLV Type


0x30

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the latest beacon or probe response frame received by the port. This does not include the 802.11 MAC header. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




