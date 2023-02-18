---
title: WDI_TLV_P2P_DEVICE_ADDRESS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_DEVICE_ADDRESS is a WiFiCx TLV that contains the device address of the Group Owner.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_DEVICE_ADDRESS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DEVICE\_ADDRESS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_DEVICE\_ADDRESS is a TLV that contains the device address of the Group Owner.

## TLV Type


0x91

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structure.

## Values


| Type                                              | Description                            |
|---------------------------------------------------|----------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | The device address of the Group Owner. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

