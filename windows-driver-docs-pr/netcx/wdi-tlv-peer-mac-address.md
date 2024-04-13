---
title: WDI_TLV_PEER_MAC_ADDRESS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_PEER_MAC_ADDRESS is a WiFiCx TLV that contains the MAC address of the peer.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_PEER_MAC_ADDRESS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PEER\_MAC\_ADDRESS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_PEER\_MAC\_ADDRESS is a TLV that contains the MAC address of the peer.

## TLV Type


0x4C

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structure.

## Values


| Type                                              | Description                                  |
|---------------------------------------------------|----------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)| Specifies the Wi-Fi MAC address of the peer. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

