---
title: WDI_TLV_KCK_CONTENT (dot11wificxtypes.hpp)
description: WDI_TLV_KCK_CONTENT is a WiFiCx TLV that contains an IEEE 802.11 key confirmation key (KCK).
ms.date: 09/30/2021
keywords:
 - WDI_TLV_KCK_CONTENT Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_KCK\_CONTENT (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI\_TLV\_KCK\_CONTENT is a TLV that contains an IEEE 802.11 key confirmation key (KCK).

## TLV Type

0x168

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies an IEEE 802.11 key confirmation key (KCK). |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
