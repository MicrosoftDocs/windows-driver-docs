---
title: WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS
description: WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS is a TLV that contains the number of measurements used to provide the round trip time (RTT) for a Fine Timing Measurement (FTM) request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
