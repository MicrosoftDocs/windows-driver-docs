---
title: WDI_TLV_WFD_ASSOCIATION_STATUS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_WFD_ASSOCIATION_STATUS is a WiFiCx TLV that contains the status code to be set when an association request is denied.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_WFD_ASSOCIATION_STATUS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_WFD\_ASSOCIATION\_STATUS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_WFD\_ASSOCIATION\_STATUS is a TLV that contains the status code to be set when an association request is denied.

## TLV Type


0x126

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                   |
|-------|-------------------------------------------------------------------------------|
| UINT8 | The DOT11\_WFD\_STATUS\_CODE to be set when an association request is denied. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




