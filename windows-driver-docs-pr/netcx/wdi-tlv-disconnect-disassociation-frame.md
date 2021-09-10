---
title: WDI_TLV_DISCONNECT_DISASSOCIATION_FRAME (dot11wificxtypes.hpp)
description: WDI_TLV_DISCONNECT_DISASSOCIATION_FRAME is a WiFiCx TLV that contains the received disassociation frame.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_DISCONNECT_DISASSOCIATION_FRAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DISCONNECT\_DISASSOCIATION\_FRAME (dot11wificxtypes.hpp)


WDI\_TLV\_DISCONNECT\_DISASSOCIATION\_FRAME is a TLV that contains the received disassociation frame.

## TLV Type


0x38

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | An array of UINT8 elements that contains the received disassociation frame. This does not include the 802.11 MAC header. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




