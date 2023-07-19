---
title: WDI_TLV_SAE_ANTI_CLOGGING_TOKEN (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_SAE_ANTI_CLOGGING_TOKEN is a WiFiCx TLV that contains the anti-clogging token for a SAE Commit request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_ANTI_CLOGGING_TOKEN Network Drivers Starting with Windows Vista
---

# WDI_TLV_SAE_ANTI_CLOGGING_TOKEN (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_SAE_ANTI_CLOGGING_TOKEN** is a TLV that contains the anti-clogging token for a Simultaneous Authentication of Equals (SAE) Commit request.

This TLV is used in [WDI_TLV_SAE_COMMIT_PARAMS](wdi-tlv-sae-commit-params.md).

## TLV Type

0x155

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | The anti-clogging token. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
