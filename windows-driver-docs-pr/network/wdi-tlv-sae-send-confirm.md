---
title: WDI_TLV_SAE_SEND_CONFIRM
description: WDI_TLV_SAE_SEND_CONFIRM is a TLV that contains the Send Confirm field for a Simultaneous Authentication of Equals (SAE) Confirm request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_SEND_CONFIRM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_SEND_CONFIRM

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
