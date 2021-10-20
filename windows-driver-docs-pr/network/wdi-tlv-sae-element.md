---
title: WDI_TLV_SAE_ELEMENT
description: WDI_TLV_SAE_ELEMENT is a TLV that contains the Encoded Field Element (EFE) for a Simultaneous Authentication of Equals (SAE) Commit request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_ELEMENT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_ELEMENT

[!INCLUDE[WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_SAE_ELEMENT** is a TLV that contains the Encoded Field Element (EFE) for a Simultaneous Authentication of Equals (SAE) Commit request.

This TLV is used in [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md).

## TLV Type

0x154

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | A part of the EFE. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
