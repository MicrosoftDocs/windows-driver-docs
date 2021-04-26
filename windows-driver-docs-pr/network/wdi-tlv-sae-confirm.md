---
title: WDI_TLV_SAE_CONFIRM
description: WDI_TLV_SAE_CONFIRM is a TLV that contains the Confirm field for a Simultaneous Authentication of Equals (SAE) Confirm request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_CONFIRM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_CONFIRM

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
