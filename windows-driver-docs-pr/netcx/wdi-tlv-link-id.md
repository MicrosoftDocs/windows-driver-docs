---
title: WDI_TLV_LINK_ID (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_LINK_ID is a WiFiCx TLV that contains an AP's link ID .
ms.date: 07/21/2023
---

# WDI_TLV_LINK_ID (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_LINK_ID is a WiFiCx TLV that contains an AP's link ID that is used when setting or querying the link-specific keys on a multi-link connection.

## TLV Type

0x203

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
|-----------------|-----------------|
| UINT32 | An ID that identifies an AP's link. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|WIN11_NEXT|
|Header|dot11wificxtypes.hpp|
