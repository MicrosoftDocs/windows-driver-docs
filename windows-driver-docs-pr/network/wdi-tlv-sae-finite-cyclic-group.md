---
title: WDI_TLV_SAE_FINITE_CYCLIC_GROUP
description: WDI_TLV_SAE_FINITE_CYCLIC_GROUP is a TLV that contains the Finite Cyclic Group used in a Commit request for Simultaneous Authentication of Equals (SAE) authentication.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_FINITE_CYCLIC_GROUP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_SAE_FINITE_CYCLIC_GROUP

[!INCLUDE[WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_SAE_FINITE_CYCLIC_GROUP** is a TLV that contains the Finite Cyclic Group used in a Commit request for Simultaneous Authentication of Equals (SAE) authentication.

This TLV is used in [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md).

## TLV Type

0x152

## Length

The size (in bytes) of a UINT16.

## Values

| Type | Description |
| --- | --- |
| UINT16 | The Finite Cyclic Group used for SAE authentication. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
