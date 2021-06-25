---
title: WDI_TLV_ASSOCIATION_PARAMETERS_REQUESTED_TYPE (dot11wificxtypes.h)
description: WDI_TLV_ASSOCIATION_PARAMETERS_REQUESTED_TYPE is a WiFiCx TLV that contains the requested Association Parameter TLV types.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_ASSOCIATION_PARAMETERS_REQUESTED_TYPE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ASSOCIATION\_PARAMETERS\_REQUESTED\_TYPE (dot11wificxtypes.h)


WDI\_TLV\_ASSOCIATION\_PARAMETERS\_REQUESTED\_TYPE is a TLV that contains the requested Association Parameter TLV types.

## TLV Type


0xBB

## Length


The size (in bytes) of the array of UINT16 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                                                                                                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16\[\] | The list of Association Parameters TLV types that are requested. Valid TLV types are [**WDI\_TLV\_PMKID**](wdi-tlv-pmkid.md) (0x9F) and [**WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES**](wdi-tlv-extra-association-request-ies.md) (0x40). |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




