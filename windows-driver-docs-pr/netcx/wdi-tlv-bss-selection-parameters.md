---
title: WDI_TLV_BSS_SELECTION_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_BSS_SELECTION_PARAMETERS is a WiFiCx TLV that contains WDI_BSS_SELECTION_FLAGS that are used by host for BSS selection.
ms.date: 06/25/2021
keywords:
 - WDI_TLV_BSS_SELECTION_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSS\_SELECTION\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_BSS\_SELECTION\_PARAMETERS is a TLV that contains [**WDI\_BSS\_SELECTION\_FLAGS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_bss_selection_flags) that are used by host for BSS selection.

## TLV Type


0x10F

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------|
| UINT32 | [**WDI\_BSS\_SELECTION\_FLAGS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_bss_selection_flags) that are used by the host for BSS selection. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

