---
title: WDI_TLV_SAE_COMMIT_RESPONSE (dot11wificxtypes.h)
description: WDI_TLV_SAE_COMMIT_RESPONSE is a WiFiCx TLV that contains the Simultaneous Authentication of Equals (SAE) Commit response frame.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SAE_COMMIT_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_SAE_COMMIT_RESPONSE (dot11wificxtypes.h)

**WDI_TLV_SAE_COMMIT_RESPONSE** is a TLV that contains the Simultaneous Authentication of Equals (SAE) Commit response frame.

This TLV is used in the payload data of [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md).

## TLV Type

0x14D

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8[] | The SAE Commit response frame. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|
