---
title: WDI_TLV_CONFIGURED_MAC_ADDRESS (dot11wificxtypes.hpp)
description: WDI_TLV_CONFIGURED_MAC_ADDRESS is a WiFiCx TLV that contains a custom MAC address.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CONFIGURED_MAC_ADDRESS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CONFIGURED\_MAC\_ADDRESS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CONFIGURED\_MAC\_ADDRESS is a TLV that contains a custom MAC address.

## TLV Type


0x99

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structure.

## Values


| Type                                              | Description                                       |
|---------------------------------------------------|---------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | The MAC address that should be used for the port. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 

