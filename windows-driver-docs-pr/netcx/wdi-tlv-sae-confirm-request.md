---
title: WDI_TLV_SAE_CONFIRM_REQUEST (dot11wificxtypes.hpp)
description: WDI_TLV_SAE_CONFIRM_REQUEST is a WiFiCx TLV that contains parameters for a SAE Confirm request. 
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_CONFIRM_REQUEST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SAE_CONFIRM_REQUEST (dot11wificxtypes.hpp)

**WDI_TLV_SAE_CONFIRM_REQUEST** is a TLV that contains parameters for a Simultaneous Authentication of Equals (SAE) Confirm request. 

This TLV is used in the command parameters for [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md).

## TLV type

0x151

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_SAE_SEND_CONFIRM](wdi-tlv-sae-send-confirm.md) | UINT16 |   |   | The Send Confirm field, used as an anti-replay counter. |
| [WDI_TLV_SAE_CONFIRM](wdi-tlv-sae-confirm.md) | TLV\<LIST\<UINT8>> |  |   | The Confirm field. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
