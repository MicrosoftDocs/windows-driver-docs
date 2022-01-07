---
title: WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST is a WiFiCx TLV that contains an array of multicast data algorithm pairs.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_MULTICAST_DATA_ALGORITHM_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST is a TLV that contains an array of multicast data algorithm pairs.

## TLV Type


0x14

## Length


The size (in bytes) of the array of WDI\_ALGO\_PAIRS elements. The array must contain 1 or more elements.

**Note**  WDI\_ALGO\_PAIRS is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                 | Description                                            |
|----------------------|--------------------------------------------------------|
| WDI\_ALGO\_PAIRS\[\] | An array of authentication and cipher algorithm pairs. |

 

WDI\_ALGO\_PAIRS consists of the following elements.

| Type  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| UINT8 | Authentication algorithm as defined in [**WDI\_AUTH\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_auth_algorithm). |
| UINT8 | Cipher algorithm as defined in [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm).     |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

