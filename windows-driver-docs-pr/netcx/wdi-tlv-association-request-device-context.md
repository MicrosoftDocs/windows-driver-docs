---
title: WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT (dot11wificxtypes.h)
description: WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT is a WiFiCx TLV that contains vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ASSOCIATION_REQUEST_DEVICE_CONTEXT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT (dot11wificxtypes.h)


WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT is a TLV that contains vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request.

## TLV Type


0x72

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                           |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | Vendor-specific information that is passed down to the port if the host decides to send a response to a incoming association request. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|


 

 




