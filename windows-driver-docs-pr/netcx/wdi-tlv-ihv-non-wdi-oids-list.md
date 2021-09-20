---
title: WDI_TLV_IHV_NON_WDI_OIDS_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_IHV_NON_WDI_OIDS_LIST is a WiFiCx TLV that contains a list of non-WDI OIDs that the adapter wants to advertise to the operating system.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_IHV_NON_WDI_OIDS_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IHV\_NON\_WDI\_OIDS\_LIST (dot11wificxtypes.hpp)


WDI\_TLV\_IHV\_NON\_WDI\_OIDS\_LIST is a TLV that contains a list of non-WDI OIDs that the adapter wants to advertise to the operating system.

## TLV Type


0x104

## Length


The size (in bytes) of the array of UINT32 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                                                                                                                                                                       |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32\[\] | A list of non-WDI OIDs that the adapter wants to advertise to the operating system. The adapter should not assume that the operating system has already filtered non-WDI OIDs to match this list. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




