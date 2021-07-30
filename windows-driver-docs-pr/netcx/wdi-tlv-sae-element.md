---
title: WDI_TLV_SAE_ELEMENT (dot11wificxtypes.h)
description: WDI_TLV_SAE_ELEMENT is a WiFiCx TLV that contains the EFE for a SAE Commit request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_ELEMENT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SAE_ELEMENT (dot11wificxtypes.h)

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

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|
