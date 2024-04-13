---
title: WDI_TLV_RETRY_AFTER (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_RETRY_AFTER is a WiFiCx TLV that contains the duration, in seconds, that should pass before trying to request a new Fine Timing Measurement (FTM) from a target BSS.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_RETRY_AFTER Network Drivers Starting with Windows Vista
---

# WDI_TLV_RETRY_AFTER  (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_RETRY_AFTER** is a TLV that contains the duration, in seconds, that should pass before trying to request a new Fine Timing Measurement (FTM) from a target BSS.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15A

## Length

The size (in bytes) of a UINT16.

## Values

| Type | Description |
| --- | --- |
| UINT16 | The duration, in seconds, that should pass before trying to request a new Fine Timing Measurement (FTM) from the target BSS. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
