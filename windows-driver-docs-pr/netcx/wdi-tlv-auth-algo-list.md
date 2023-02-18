---
title: WDI_TLV_AUTH_ALGO_LIST (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_AUTH_ALGO_LIST is a WiFiCx TLV that contains a list of authentication algorithms.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_AUTH_ALGO_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_AUTH\_ALGO\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_AUTH\_ALGO\_LIST is a TLV that contains a list of authentication algorithms.

## TLV Type


0x3C

## Length


The size (in bytes) of the array of [**WDI\_AUTH\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_auth_algorithm) structures. The array must contain 1 or more elements.

## Values


| Type                                                        | Description                            |
|-------------------------------------------------------------|----------------------------------------|
| [**WDI\_AUTH\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_auth_algorithm)\[\] | An array of authentication algorithms. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

