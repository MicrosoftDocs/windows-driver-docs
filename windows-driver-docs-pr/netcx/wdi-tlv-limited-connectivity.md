---
title: WDI_TLV_LIMITED_CONNECTIVITY (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_LIMITED_CONNECTIVITY is a WiFiCx TLV that specifies  whether the WiFiCx driver can maintain a secondary STA connection.
ms.date: 08/31/2021
keywords:
 - WDI_TLV_LIMITED_CONNECTIVITY Network Drivers Starting with Windows Vista
---

# WDI_TLV_LIMITED_CONNECTIVITY (dot11wificxtypes.hpp)

**WDI_TLV_LIMITED_CONNECTIVITY** is a TLV that specifies whether the WiFiCx driver can maintain a secondary STA connection. 

This TLV is used in [NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY](ndis-status-wdi-indication-secondary-sta-connectivity.md).

## TLV Type

0x201

## Length

The size (in bytes) of a UINT8.

## Values

| Type | Description |
| --- | --- |
| UINT8 | If this value is **1**, the driver cannot maintain a secondary STA connection. Otherwise this value is **0**. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

