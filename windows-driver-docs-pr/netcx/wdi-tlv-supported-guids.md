---
title: WDI_TLV_SUPPORTED_GUIDS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_SUPPORTED_GUIDS is a WiFiCx TLV that contains a supported NDIS GUID.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_SUPPORTED_GUIDS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_SUPPORTED\_GUIDS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_SUPPORTED\_GUIDS is a TLV that contains a supported NDIS GUID.

 

## TLV Type


0x130

## Length


The size (in bytes) of a [NDIS\_GUID](../network/filling-in-an-ndis-guid-structure.md) structure.

## Values


| Type       | Description            |
|------------|------------------------|
| NDIS\_GUID | A supported NDIS GUID. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

