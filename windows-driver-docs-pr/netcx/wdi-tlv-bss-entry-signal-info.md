---
title: WDI_TLV_BSS_ENTRY_SIGNAL_INFO (dot11wificxtypes.hpp)
description: WDI_TLV_BSS_ENTRY_SIGNAL_INFO is a WiFiCx TLV that contains signal information for a BSS entry.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_BSS_ENTRY_SIGNAL_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BSS\_ENTRY\_SIGNAL\_INFO (dot11wificxtypes.hpp)


WDI\_TLV\_BSS\_ENTRY\_SIGNAL\_INFO is a TLV that contains signal information for a BSS entry.

## TLV Type


0xB

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                                                                                                                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INT32  | The received signal strength indicator (RSSI) value of the beacon or probe response from the peer. This value is specified in units of decibels referenced to 1.0 milliwatts (dBm) |
| UINT32 | The link quality specified by a value from 0 to 100. A value of 100 specifies the highest link quality.                                                                            |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




