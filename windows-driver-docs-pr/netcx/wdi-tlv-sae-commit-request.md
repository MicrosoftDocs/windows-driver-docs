---
title: WDI_TLV_SAE_COMMIT_REQUEST (dot11wificxtypes.hpp)
description: WDI_TLV_SAE_COMMIT_REQUEST is a WiFiCx TLV that contains parameters for a Simultaneous Authentication of Equals (SAE) Commit request. 
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_COMMIT_REQUEST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SAE_COMMIT_REQUEST (dot11wificxtypes.hpp)

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
| [WDI_TLV_SAE_ANTI_CLOGGING_TOKEN](wdi-tlv-sae-anti-clogging-token.md) | TLV\<LIST\<UINT8>> |   |  X | The anti-clogging token as requested by the BSSID. |
| [WDI_TLV_SAE_REJECTED_GROUPS](wdi-tlv-sae-rejected-groups.md) | TLV\<LIST\<UINT8>> |   | X  | Any rejected groups. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|