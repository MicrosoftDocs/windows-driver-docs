---
title: WDI_TLV_SAE_STATUS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_SAE_STATUS is a WiFix TLV that contains Simultaneous Authentication of Equals (SAE) authentication failure error status.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_STATUS Network Drivers Starting with Windows Vista
---

# WDI_TLV_SAE_STATUS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_SAE_STATUS** is a TLV that contains Simultaneous Authentication of Equals (SAE) authentication failure error status.

This TLV is used in the command parameters of [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md) and in the payload data of [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md).

## TLV Type

0x14C

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_SAE_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_status) | The SAE authentication failure error status. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
