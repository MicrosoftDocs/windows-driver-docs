---
title: WDI_TLV_PROTOCOL_OFFLOAD_ID (dot11wificxtypes.hpp)
description: WDI_TLV_PROTOCOL_OFFLOAD_ID is a WiFiCx TLV that contains the protocol offload identifier.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_PROTOCOL_OFFLOAD_ID Network Drivers Starting with Windows 10, Version 2004
ms.localizationpriority: medium
---

# WDI\_TLV\_PROTOCOL\_OFFLOAD\_ID (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI\_TLV\_PROTOCOL\_OFFLOAD\_ID is a TLV that contains the protocol offload identifier.

## TLV Type

0x166

## Length

The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values

| Type | Description |
| --- | --- |
| UINT8\[\] | Specifies the the protocol offload identifier. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
