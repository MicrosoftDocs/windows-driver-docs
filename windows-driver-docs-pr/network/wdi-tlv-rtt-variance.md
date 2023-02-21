---
title: WDI_TLV_RTT_VARIANCE
ms.topic: reference
description: WDI_TLV_RTT_VARIANCE is a TLV that contains the statistical variance of the measurements used to calculate roundtrip time (RTT) during a Fine Timing Measurement (FTM) request, if more than one measurement was used. 
ms.date: 02/15/2019
keywords:
 - WDI_TLV_RTT_VARIANCE Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI_TLV_RTT_VARIANCE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
