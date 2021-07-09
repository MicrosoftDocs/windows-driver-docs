---
title: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO (dot11wificxtypes.h)
description: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO is a WiFiCx TLV that contains information about the incoming association request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_INCOMING_ASSOCIATION_REQUEST_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO (dot11wificxtypes.h)


WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_INFO is a TLV that contains information about the incoming association request.

## TLV Type


0x8F

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                            | Multiple TLV instances allowed | Optional | Description                                                      |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------|
| [**WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS**](wdi-tlv-incoming-association-request-parameters.md) |                                |          | The parameters for the incoming association request.             |
| [**WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME**](wdi-tlv-association-request-frame.md)                              |                                |          | The association request frame.                                   |
| [**WDI\_TLV\_ASSOCIATION\_REQUEST\_DEVICE\_CONTEXT**](wdi-tlv-association-request-device-context.md)           |                                | X        | The vendor-specific information that is passed down to the port. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




