---
title: WDI_TLV_P2P_INTERFACE_ADDRESS_LIST (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_INTERFACE_ADDRESS_LIST is a WiFiCx TLV that contains an address list for a Wi-Fi Direct interface.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_P2P_INTERFACE_ADDRESS_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_INTERFACE\_ADDRESS\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_INTERFACE\_ADDRESS\_LIST is a TLV that contains an address list for a Wi-Fi Direct interface.

## TLV Type


0x18

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                      |
|-------------------------------------------------------|----------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)\[\] | An array of Wi-Fi MAC addresses. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

