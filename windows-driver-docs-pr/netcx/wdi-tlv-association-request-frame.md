---
title: WDI_TLV_ASSOCIATION_REQUEST_FRAME (dot11wificxtypes.h)
description: WDI_TLV_ASSOCIATION_REQUEST_FRAME is a WiFiCx TLV that contains the association request that was used for the association.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_ASSOCIATION_REQUEST_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME (dot11wificxtypes.h)


WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME is a TLV that contains the association request that was used for the association.

## TLV Type


0x2E

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                       |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the association request that was used for the association. This does not include the 802.11 MAC header. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




