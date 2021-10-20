---
title: WDI_TLV_NETWORK_LIST_OFFLOAD_CONFIG (dot11wificxtypes.hpp)
description: WDI_TLV_NETWORK_LIST_OFFLOAD_CONFIG is a WiFiCx TLV that contains Network List Offload (NLO) configuration.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_NETWORK_LIST_OFFLOAD_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_CONFIG (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_CONFIG is a TLV that contains Network List Offload (NLO) configuration.

## TLV Type


0xDA

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------|
| UINT32 | Reserved field.                                                                                                       |
| UINT32 | The delay (in seconds) before the scan schedule starts.                                                               |
| UINT32 | The period (in seconds) to scan in the first phase.                                                                   |
| UINT32 | The number of iterations in the fast scan phase.                                                                      |
| UINT32 | The period (in seconds) to scan in the slow scan phase. This phase lasts indefinitely until a new NLO command is set. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




