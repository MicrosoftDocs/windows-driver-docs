---
title: WDI_TLV_REQUEST_LCI_REPORT (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_REQUEST_LCI_REPORT is a WiFiCx TLV that contains information for whether a Location Configuration Information (LCI) report should be requested from a target BSS during a Fine Timing Measurement (FTM) request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_REQUEST_LCI_REPORT Network Drivers Starting with Windows Vista
---

# WDI_TLV_REQUEST_LCI_REPORT (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

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

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
