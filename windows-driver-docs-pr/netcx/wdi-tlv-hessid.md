---
title: WDI_TLV_HESSID (dot11wificxtypes.hpp)
description: WDI_TLV_HESSID is a WiFiCx TLV that contains a list of HESSIDs.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_HESSID, WiFiCx
ms.localizationpriority: medium
---

# WDI_TLV_HESSID (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI_TLV_HESSID is a TLV that contains a list of HESSIDs.

## TLV Type


0xC8

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description        |
|-------------------------------------------------------|--------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)\[\] | A list of HESSIDs. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

