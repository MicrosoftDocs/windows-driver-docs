---
title: WDI_TLV_VENDOR_SPECIFIC_IE (dot11wificxtypes.h)
description: WDI_TLV_VENDOR_SPECIFIC_IE is a WiFiCx TLV that contains a list of vendor-specific IEs.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_VENDOR_SPECIFIC_IE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_VENDOR\_SPECIFIC\_IE (dot11wificxtypes.h)


WDI\_TLV\_VENDOR\_SPECIFIC\_IE is a TLV that contains a list of vendor-specific IEs.

## TLV Type


0x5

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                        |
|-----------|--------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that specifies the vendor-specific IEs. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




