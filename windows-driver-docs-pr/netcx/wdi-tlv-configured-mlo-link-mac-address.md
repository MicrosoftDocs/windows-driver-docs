---
title: WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS is a WiFiCx TLV that contains a custom MLO link MAC address.
ms.date: 08/18/2023
keywords:
 - WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS Network Drivers Starting with Windows Vista
---

# WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS is a TLV that contains a custom Multi-Link Operation (MLO) link MAC address.

## TLV Type

0x207

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structure.

## Values


| Type                                              | Description                                       |
|---------------------------------------------------|---------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | The MAC address that should be used for the port. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|WIN11_NEXT|
|Header|dot11wificxtypes.hpp|

 

 

