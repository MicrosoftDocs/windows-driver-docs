---
title: WDI_TLV_MULTICAST_CIPHER_ALGO_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_MULTICAST_CIPHER_ALGO_LIST is a WiFiCx TLV that contains a list of multicast cipher algorithms.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_MULTICAST_CIPHER_ALGO_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_MULTICAST\_CIPHER\_ALGO\_LIST (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_MULTICAST\_CIPHER\_ALGO\_LIST is a TLV that contains a list of multicast cipher algorithms.

## TLV Type


0x3D

## Length


The size (in bytes) of the array of [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm) structures. The array must contain 1 or more elements.

## Values


| Type                                                            | Description                              |
|-----------------------------------------------------------------|------------------------------------------|
| [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm)\[\] | An array of multicast cipher algorithms. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

