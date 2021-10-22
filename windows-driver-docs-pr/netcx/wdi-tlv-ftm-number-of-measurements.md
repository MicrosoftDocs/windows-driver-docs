---
title: WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS (dot11wificxtypes.hpp)
description: WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS is a WiFiCx TLV that contains the number of measurements used to provide the round trip time (RTT) for a Fine Timing Measurement (FTM) request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS** is a TLV that contains the number of measurements used to provide the round trip time (RTT) for a Fine Timing Measurement (FTM) request.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15B

## Length

The size (in bytes) of a UINT16.

## Values

| Type | Description |
| --- | --- |
| UINT16 | The number of measurements used to provide the RTT. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
