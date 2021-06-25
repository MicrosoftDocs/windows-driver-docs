---
title: WDI_TLV_BSS_ENTRY_DEVICE_CONTEXT (dot11wificxtypes.h)
description: WDI_TLV_BSS_ENTRY_DEVICE_CONTEXT is a WiFiCx TLV that contains device context for the BSS entry.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_BSS_ENTRY_DEVICE_CONTEXT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BSS\_ENTRY\_DEVICE\_CONTEXT (dot11wificxtypes.h)


WDI\_TLV\_BSS\_ENTRY\_DEVICE\_CONTEXT is a TLV that contains device context for the BSS entry.

## TLV Type


0xD

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                                                                                                                                                                                |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the context data. This context is provided by the IHV component and can be used to store per-BSS entry state that the IHV component wants to maintain. To avoid lifetime management issues, the IHV component must not use pointers in this TLV. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




