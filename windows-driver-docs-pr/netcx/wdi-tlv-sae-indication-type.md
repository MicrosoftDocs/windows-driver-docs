---
title: WDI_TLV_SAE_INDICATION_TYPE (dot11wificxtypes.hpp)
description: WDI_TLV_SAE_INDICATION_TYPE is a WiFiCx TLV that contains the type of information needed to continue SAE authentication with a target BSSID, or notification that authentication cannot continue.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_INDICATION_TYPE Network Drivers Starting with Windows Vista
---

# WDI_TLV_SAE_INDICATION_TYPE (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_SAE_INDICATION_TYPE** is a TLV that contains the type of information needed to continue SAE authentication with a target BSSID, or notification that authentication cannot continue.

This TLV is used in the payload data of [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md).

## TLV Type

0x14B

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_SAE_INDICATION_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_indication_type) | The type of information needed to continue SAE authentication with a target BSSID, or notification that authentication cannot continue. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
