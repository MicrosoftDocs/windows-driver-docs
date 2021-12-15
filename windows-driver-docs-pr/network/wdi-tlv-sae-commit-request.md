---
title: WDI_TLV_SAE_COMMIT_REQUEST
description: WDI_TLV_SAE_COMMIT_REQUEST is a TLV that contains parameters for a Simultaneous Authentication of Equals (SAE) Commit request. 
ms.date: 02/14/2019
keywords:
 - WDI_TLV_SAE_COMMIT_REQUEST Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI_TLV_SAE_COMMIT_REQUEST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_SAE_COMMIT_REQUEST** is a TLV that contains parameters for a Simultaneous Authentication of Equals (SAE) Commit request. 

This TLV is used in the command parameters for [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md).

## TLV type

0x150

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_SAE_FINITE_CYCLIC_GROUP](wdi-tlv-sae-finite-cyclic-group.md) | UINT16 |   |   | The Finite Cyclic Group used for SAE authentication. |
| [WDI_TLV_SAE_SCALAR](wdi-tlv-sae-scalar.md) | TLV\<LIST\<UINT8>> |   |   | The Finite Field Element (FFE). |
| [WDI_TLV_SAE_ELEMENT](wdi-tlv-sae-element.md) | TLV\<LIST\<UINT8>> |   |   | The Encoded Field Element (EFE). |
| [WDI_TLV_SAE_ANTI_CLOGGING_TOKEN](wdi-tlv-sae-anti-clogging-token.md) | TLV\<LIST\<UINT8>> |   |   | The anti-clogging token as requested by the BSSID. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
