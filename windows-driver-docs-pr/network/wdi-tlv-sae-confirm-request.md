---
title: WDI_TLV_SAE_CONFIRM_REQUEST
ms.topic: reference
description: WDI_TLV_SAE_CONFIRM_REQUEST is a TLV that contains parameters for a Simultaneous Authentication of Equals (SAE) Confirm request. 
ms.date: 02/15/2019
keywords:
 - WDI_TLV_SAE_CONFIRM_REQUEST Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI_TLV_SAE_CONFIRM_REQUEST

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

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

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
