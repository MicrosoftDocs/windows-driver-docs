---
title: WDI_TLV_LCI_REPORT_BODY
description: WDI_TLV_LCI_REPORT_BODY is a TLV that contains the Location Configuration Report (LCI) for a Fine Timing Measuremement (FTM) request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_LCI_REPORT_BODY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_LCI_REPORT_BODY

**WDI_TLV_LCI_REPORT_BODY** is a TLV that contains the Location Configuration Report (LCI) for a Fine Timing Measuremement (FTM) request.

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
