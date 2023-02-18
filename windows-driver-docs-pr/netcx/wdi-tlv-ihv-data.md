---
title: WDI_TLV_IHV_DATA (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_IHV_DATA is a WiFiCx TLV that contains IHV-specific information that is used by the IHV extensibility module.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_IHV_DATA Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_IHV\_DATA (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_IHV\_DATA is a TLV that contains IHV-specific information that is used by the IHV extensibility module.

## TLV Type


0xBD

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                            |
|-----------|------------------------------------------------------------------------|
| UINT8\[\] | IHV specific information that is used by the IHV extensibility module. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




