---
title: WDI_TLV_RTT (dot11wificxtypes.hpp)
description: WDI_TLV_RTT is a WiFiCx TLV that contains the measured roundtrip time (RTT), in picoseconds, for a Fine Timing Measurement (FTM) request. 
ms.date: 07/31/2021
keywords:
 - WDI_TLV_RTT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_RTT (dot11wificxtypes.hpp)

**WDI_TLV_RTT** is a TLV that contains the measured roundtrip time (RTT), in picoseconds, for a Fine Timing Measurement (FTM) request. 

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15C

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| UINT32 | The RTT. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

