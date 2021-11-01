---
title: WDI_TLV_REQUEST_LCI_REPORT
description: WDI_TLV_REQUEST_LCI_REPORT is a TLV that contains information for whether a Location Configuration Information (LCI) report should be requested from a target BSS during a Fine Timing Measurement (FTM) request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_REQUEST_LCI_REPORT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_REQUEST_LCI_REPORT

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_REQUEST_LCI_REPORT** is a TLV that contains information for whether a Location Configuration Information (LCI) report should be requested from a target BSS during a Fine Timing Measurement (FTM) request.

This TLV is used in [WDI_TLV_FTM_TARGET_BSS_ENTRY](wdi-tlv-ftm-target-bss-entry.md).

## TLV Type

0x158

## Length

The size (in bytes) of a UINT8.

## Values

| Type | Description |
| --- | --- |
| UINT8 | Possible values: <ul><li>0: LCI report not needed.</li><li>1: LCI report should be requested.</li></ul> |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
