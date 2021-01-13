---
title: WDI_TLV_SAE_REQUEST_TYPE
description: WDI_TLV_SAE_REQUEST_TYPE is a TLV that contains the type of Simultaneous Authentication of Equals (SAE) request frame to send to a target BSSID.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_REQUEST_TYPE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_REQUEST_TYPE

**WDI_TLV_SAE_REQUEST_TYPE** is a TLV that contains the type of Simultaneous Authentication of Equals (SAE) request frame to send to a target BSSID.

This TLV is used in the command parameters of [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md).

## TLV Type

0x14F

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_SAE_REQUEST_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_sae_request_type) | The type of SAE request frame to send to the BSSID. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
