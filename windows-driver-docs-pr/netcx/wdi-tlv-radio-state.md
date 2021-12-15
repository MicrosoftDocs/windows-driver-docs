---
title: WDI_TLV_RADIO_STATE (dot11wificxtypes.hpp)
description: WDI_TLV_RADIO_STATE is a WiFiCx TLV that contains the state of the radio in hardware and software.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_RADIO_STATE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_RADIO\_STATE (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_RADIO\_STATE is a TLV that contains the state of the radio in hardware and software.

## TLV Type


0xA1

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|UINT8|The current state of the radio in hardware. Valid values are 0 and 1.|
|UINT8|The current state of the radio in software. Valid values are 0 and 1.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




