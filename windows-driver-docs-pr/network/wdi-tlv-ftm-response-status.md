---
title: WDI_TLV_FTM_RESPONSE_STATUS
ms.topic: reference
description: WDI_TLV_FTM_RESPONSE_STATUS is a TLV that contains the Fine Timing Measurement (FTM) response status from a target BSS.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_FTM_RESPONSE_STATUS Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI_TLV_FTM_RESPONSE_STATUS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_FTM_RESPONSE_STATUS** is a TLV that contains the Fine Timing Measurement (FTM) response status from a target BSS.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x159

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_FTM_RESPONSE_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_ftm_response_status) | The FTM response status. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
