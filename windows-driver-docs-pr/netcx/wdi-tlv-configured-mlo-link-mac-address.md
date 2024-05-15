---
title: WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS is a WiFiCx TLV that contains a list of custom Multi-Link Operation (MLO) link MAC addresses.
ms.date: 02/07/2024
---

# WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS is a TLV that contains a list of custom Multi-Link Operation (MLO) link MAC addresses.

## TLV Type

0x207

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structures.

## Values


| Type | Description |
|---|---|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)[] | An array of MLO link MAC addresses. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11, version 24H2|
|Header|dot11wificxtypes.hpp|

 

 

