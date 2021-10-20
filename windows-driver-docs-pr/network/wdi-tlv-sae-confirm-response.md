---
title: WDI_TLV_SAE_CONFIRM_RESPONSE
description: WDI_TLV_SAE_CONFIRM_RESPONSE is a TLV that contains the Simultaneous Authentication of Equals (SAE) Confirm response frame.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_CONFIRM_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_CONFIRM_RESPONSE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_SAE_CONFIRM_RESPONSE** is a TLV that contains the Simultaneous Authentication of Equals (SAE) Confirm response frame.

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
