---
title: WDI_TLV_SAE_ANTI_CLOGGING_TOKEN
ms.topic: reference
description: WDI_TLV_SAE_ANTI_CLOGGING_TOKEN is a TLV that contains the anti-clogging token for a Simultaneous Authentication of Equals (SAE) Commit request.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_SAE_ANTI_CLOGGING_TOKEN Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI_TLV_SAE_ANTI_CLOGGING_TOKEN

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

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
