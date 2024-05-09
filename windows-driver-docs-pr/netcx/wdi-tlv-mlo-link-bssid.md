---
title: WDI_TLV_MLO_LINK_BSSID (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_MLO_LINK_BSSID is a WiFiCx TLV that contains the BSSID of a Multi-Link Operation (MLO) link.
ms.date: 08/18/2023
---

# WDI_TLV_MLO_LINK_BSSID (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_MLO_LINK_BSSID is a WiFiCx TLV that contains the BSSID of a Multi-Link Operation (MLO) link.

## TLV Type

0x206

## Length

The size (in bytes) of a [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structure.

## Values

| Type | Description |
|-----------------|-----------------|
| [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | A Wi-Fi MAC address that specifies a BSSID of an MLO link. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|WIN11_NEXT|
|Header|dot11wificxtypes.hpp|
