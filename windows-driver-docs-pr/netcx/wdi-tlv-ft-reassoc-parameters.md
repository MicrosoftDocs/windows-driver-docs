---
title: WDI_TLV_FT_REASSOC_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_FT_REASSOC_PARAMETERS is a WiFiCx TLV that contains reassociation parameters for Fast Transition.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_FT_REASSOC_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_FT\_REASSOC\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_FT\_REASSOC\_PARAMETERS is a TLV that contains reassociation parameters for Fast Transition.

## TLV Type


0x106

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                    | Description                                                                                                                            |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_FT\_MDE**](wdi-tlv-ft-mde.md)             | The MDIE of the BSS entry.                                                                                                             |
| [**WDI\_TLV\_FT\_PMKR0NAME**](wdi-tlv-ft-pmkr0name.md) | The PMKR0Name. This is needed during Fast Transition. The STA needs to send the PMKR0Name during the authentication request to the AP. |
| [**WDI\_TLV\_FT\_FTE**](wdi-tlv-ft-fte.md)             | The Fast Transition Element that contains the R0KHID and SNonce.                                                                       |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




