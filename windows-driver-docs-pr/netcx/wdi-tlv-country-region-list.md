---
title: WDI_TLV_COUNTRY_REGION_LIST (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_COUNTRY_REGION_LIST is a WiFiCx TLV that contains a list of country or region codes.
ms.date: 08/30/2021
keywords:
 - WDI_TLV_COUNTRY_REGION_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_COUNTRY\_REGION\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_COUNTRY\_REGION\_LIST is a TLV that contains a list of country or region codes.

## TLV Type


0x12

## Length


The size (in bytes) of the array of WDI\_COUNTRY\_REGION\_LIST elements. The array must contain 1 or more elements.

**Note**  WDI\_COUNTRY\_REGION\_LIST is not a WDI structure. It is defined in the WDI TLV parser generator, and is used for documentation purposes only.

 

## Values


| Type                           | Description                          |
|--------------------------------|--------------------------------------|
| WDI\_COUNTRY\_REGION\_LIST\[\] | An array of country or region codes. |

 

WDI\_COUNTRY\_REGION\_LIST consists of the following elements.

| Type       | Description               |
|------------|---------------------------|
| UINT8\[3\] | A country or region code. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
 

 




