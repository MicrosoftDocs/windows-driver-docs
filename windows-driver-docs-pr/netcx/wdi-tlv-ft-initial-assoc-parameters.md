---
title: WDI_TLV_FT_INITIAL_ASSOC_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_FT_INITIAL_ASSOC_PARAMETERS is a WiFiCx TLV that contains initial association parameters for Fast Transition.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_FT_INITIAL_ASSOC_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_FT\_INITIAL\_ASSOC\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_FT\_INITIAL\_ASSOC\_PARAMETERS is a TLV that contains initial association parameters for Fast Transition.

## TLV Type


0x105

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                        | Description                |
|---------------------------------------------|----------------------------|
| [**WDI\_TLV\_FT\_MDE**](wdi-tlv-ft-mde.md) | The MDIE of the BSS entry. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




