---
title: WDI_TLV_SAE_FINITE_CYCLIC_GROUP (dot11wificxtypes.hpp)
description: WDI_TLV_SAE_FINITE_CYCLIC_GROUP is a WiFiCx TLV that contains the Finite Cyclic Group used in a Commit request for SAE authentication.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_FINITE_CYCLIC_GROUP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SAE_FINITE_CYCLIC_GROUP (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_SAE_FINITE_CYCLIC_GROUP** is a TLV that contains the Finite Cyclic Group used in a Commit request for Simultaneous Authentication of Equals (SAE) authentication.

This TLV is used in [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md).

## TLV Type

0x152

## Length

The size (in bytes) of a UINT16.

## Values

| Type | Description |
| --- | --- |
| UINT16 | The Finite Cyclic Group used for SAE authentication. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
