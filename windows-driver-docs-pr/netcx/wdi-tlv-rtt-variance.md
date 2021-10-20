---
title: WDI_TLV_RTT_VARIANCE (dot11wificxtypes.hpp)
description: WDI_TLV_RTT_VARIANCE is a WiFiCx TLV that contains the statistical variance of the measurements used to calculate roundtrip time (RTT) during a Fine Timing Measurement (FTM) request, if more than one measurement was used. 
ms.date: 07/31/2021
keywords:
 - WDI_TLV_RTT_VARIANCE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_RTT_VARIANCE (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_RTT_VARIANCE** is a TLV that contains the statistical variance of the measurements used to calculate roundtrip time (RTT) during a Fine Timing Measurement (FTM) request, if more than one measurement was used. 

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15E

## Length

The size (in bytes) of a UINT64.

## Values

| Type | Description |
| --- | --- |
| UINT64 | The statistical variance of the measurements used to calculate the RTT. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
