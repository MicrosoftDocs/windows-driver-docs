---
title: WDI_TLV_RETRY_AFTER
description: WDI_TLV_RETRY_AFTER is a TLV that contains the duration, in seconds, that should pass before trying to request a new Fine Timing Measurement (FTM) from a target BSS.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_RETRY_AFTER Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI_TLV_RETRY_AFTER

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
