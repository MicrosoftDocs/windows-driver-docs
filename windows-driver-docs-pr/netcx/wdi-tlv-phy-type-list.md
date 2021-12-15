---
title: WDI_TLV_PHY_TYPE_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_PHY_TYPE_LIST is a WiFiCx TLV that contains an array of PHY types.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_PHY_TYPE_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PHY\_TYPE\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_PHY\_TYPE\_LIST is a TLV that contains an array of PHY types.

## TLV Type


0x19

## Length


The size (in bytes) of the array of [**WDI\_PHY\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_phy_type) values. The array must contain 1 or more values.

## Values


| Type                                            | Description                  |
|-------------------------------------------------|------------------------------|
| [**WDI\_PHY\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_phy_type)\[\] | An array of PHY type values. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

