---
title: WDI_TLV_SAE_REJECTED_GROUPS (dot11wificxtypes.hpp)
description: WDI_TLV_SAE_REJECTED_GROUPS is a WiFiCx TLV that contains the anti-clogging token for a SAE Commit request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_REJECTED_GROUPS Network Drivers Starting with Windows Vista
---

# WDI_TLV_SAE_REJECTED_GROUPS (dot11wificxtypes.hpp)

**WDI_TLV_SAE_REJECTED_GROUPS** is a TLV that contains any rejected Finite Cyclic Groups used in a Commit request for Simultaneous Authentication of Equals (SAE) authentication.

This TLV is used in [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md).

## TLV Type

0x16F

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | An array of UINT8 elements that contains the rejected groups. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
