---
title: WDI_TLV_SAE_ANTI_CLOGGING_TOKEN
description: WDI_TLV_SAE_ANTI_CLOGGING_TOKEN is a TLV that contains the anti-clogging token for a Simultaneous Authentication of Equals (SAE) Commit request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_ANTI_CLOGGING_TOKEN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_ANTI_CLOGGING_TOKEN

**WDI_TLV_SAE_ANTI_CLOGGING_TOKEN** is a TLV that contains the anti-clogging token for a Simultaneous Authentication of Equals (SAE) Commit request.

This TLV is used in [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md).

## TLV Type

0x155

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | The anti-clogging token. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
