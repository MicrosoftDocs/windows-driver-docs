---
title: WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD (dot11wificxtypes.hpp)
description: WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD is a WiFiCx TLV that contains the unreachable detection threshold.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_UNREACHABLE\_DETECTION\_THRESHOLD (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_UNREACHABLE\_DETECTION\_THRESHOLD is a TLV that contains the unreachable detection threshold.

## TLV Type


0xB1

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                                                                                                                                                                                               |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The unreachable detection threshold. Specifies the maximum amount of time, in milliseconds, before the 802.11 station determines that it has lost connectivity to a peer device. The station must include missed beacons in making this connectivity loss determination but can also use any other heuristics it desires. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




