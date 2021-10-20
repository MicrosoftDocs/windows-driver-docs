---
title: WDI_TLV_P2P_GROUP_BSSID (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_GROUP_BSSID is a WiFiCx TLV that contains the Group BSSID for local Wi-Fi Direct GO.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GROUP_BSSID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GROUP\_BSSID (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GROUP\_BSSID is a TLV that contains the Group BSSID for local Wi-Fi Direct GO.

## TLV Type


0x73

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structure.

## Values


| Type                                              | Description                                          |
|---------------------------------------------------|------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Specifies the Group BSSID for local Wi-Fi Direct GO. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

