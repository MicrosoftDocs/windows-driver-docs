---
title: WDI_TLV_SAE_SEND_CONFIRM (dot11wificxtypes.hpp)
description: WDI_TLV_SAE_SEND_CONFIRM is a WiFiCx TLV that contains the Send Confirm field for a SAE Confirm request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_SEND_CONFIRM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SAE_SEND_CONFIRM (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_SAE_SEND_CONFIRM** is a TLV that contains the Send Confirm field for a Simultaneous Authentication of Equals (SAE) Confirm request. The Send Confirm field is used as an anti-replay counter.

This TLV is used in [WDI_TLV_SAE_CONFIRM_REQUEST](wdi-tlv-sae-confirm-request.md).

## TLV Type

0x156

## Length

The size (in bytes) of a UINT16.

## Values

| Type | Description |
| --- | --- |
| UINT16 | The Send Confirm field. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
