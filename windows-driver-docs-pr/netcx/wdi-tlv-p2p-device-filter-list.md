---
title: WDI_TLV_P2P_DEVICE_FILTER_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_DEVICE_FILTER_LIST is a WiFiCx TLV that contains a list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_DEVICE_FILTER_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_DEVICE\_FILTER\_LIST (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_DEVICE\_FILTER\_LIST is a TLV that contains a list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery.

## TLV Type


0xC5

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                                                                                         |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)\[\] | A list of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discovery. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

