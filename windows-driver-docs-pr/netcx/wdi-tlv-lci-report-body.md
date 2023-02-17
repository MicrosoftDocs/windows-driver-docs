---
title: WDI_TLV_LCI_REPORT_BODY (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_LCI_REPORT_BODY is a WiFiCx TLV that contains the Location Configuration Report (LCI) for a Fine Timing Measuremement (FTM) request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_LCI_REPORT_BODY Network Drivers Starting with Windows Vista
---

# WDI_TLV_LCI_REPORT_BODY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_LCI_REPORT_BODY** is a TLV that contains the Location Configuration Report (LCI) for a Fine Timing Measurement (FTM) request.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x160

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | The LCI report. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
