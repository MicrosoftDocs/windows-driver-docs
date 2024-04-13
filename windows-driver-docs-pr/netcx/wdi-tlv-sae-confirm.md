---
title: WDI_TLV_SAE_CONFIRM (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_SAE_CONFIRM is a WiFiCx TLV that contains the Confirm field for a SAE Confirm request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_CONFIRM Network Drivers Starting with Windows Vista
---

# WDI_TLV_SAE_CONFIRM (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_SAE_CONFIRM** is a TLV that contains the Confirm field for a Simultaneous Authentication of Equals (SAE) Confirm request.

This TLV is used in [WDI_TLV_SAE_CONFIRM_REQUEST](wdi-tlv-sae-confirm-request.md).

## TLV Type

0x157

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | The Confirm field. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
