---
title: WDI_TLV_SAE_CONFIRM_FRAME (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_SAE_CONFIRM_FRAME is a WiFiCx TLV that contains the Simultaneous Authentication of Equals (SAE) Confirm response frame.
ms.date: 07/19/2023
---

# WDI_TLV_SAE_CONFIRM_FRAME (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_SAE_CONFIRM_FRAME** is a TLV that contains the Simultaneous Authentication of Equals (SAE) Confirm response frame.

This TLV is used in the payload data of [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md).

## TLV Type

0x14E

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | The SAE Confirm response frame. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
