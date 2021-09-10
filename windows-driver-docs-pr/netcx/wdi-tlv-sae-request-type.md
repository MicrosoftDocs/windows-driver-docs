---
title: WDI_TLV_SAE_REQUEST_TYPE (dot11wificxtypes.hpp)
description: WDI_TLV_SAE_REQUEST_TYPE is a WiFiCx TLV that contains the type of Simultaneous Authentication of Equals (SAE) request frame to send to a target BSSID.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_REQUEST_TYPE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SAE_REQUEST_TYPE (dot11wificxtypes.hpp)

**WDI_TLV_SAE_REQUEST_TYPE** is a TLV that contains the type of Simultaneous Authentication of Equals (SAE) request frame to send to a target BSSID.

This TLV is used in the command parameters of [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md).

## TLV Type

0x14F

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_SAE_REQUEST_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_request_type) | The type of SAE request frame to send to the BSSID. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
