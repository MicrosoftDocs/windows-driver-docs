---
title: WDI_TLV_SAE_INDICATION_TYPE
description: WDI_TLV_SAE_INDICATION_TYPE is a TLV that contains the type of information needed to continue SAE authentication with a target BSSID, or notification that authentication cannot continue.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_INDICATION_TYPE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_INDICATION_TYPE

[!INCLUDE[WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_SAE_INDICATION_TYPE** is a TLV that contains the type of information needed to continue SAE authentication with a target BSSID, or notification that authentication cannot continue.

This TLV is used in the payload data of [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md).

## TLV Type

0x14B

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_SAE_INDICATION_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_sae_indication_type) | The type of information needed to continue SAE authentication with a target BSSID, or notification that authentication cannot continue. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
