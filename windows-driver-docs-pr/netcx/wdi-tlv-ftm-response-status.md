---
title: WDI_TLV_FTM_RESPONSE_STATUS (dot11wificxtypes.hpp) 
description: WDI_TLV_FTM_RESPONSE_STATUS is a WiFiCx TLV that contains the Fine Timing Measurement (FTM) response status from a target BSS.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_FTM_RESPONSE_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_FTM_RESPONSE_STATUS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_FTM_RESPONSE_STATUS** is a TLV that contains the Fine Timing Measurement (FTM) response status from a target BSS.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x159

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_FTM_RESPONSE_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_ftm_response_status) | The FTM response status. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
