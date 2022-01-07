---
title: WDI_TLV_BSSID (dot11wificxtypes.hpp)
description: WDI_TLV_BSSID is a WiFiCx TLV that contains the BSSID of a BSS.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_BSSID Network Drivers Starting with Windows Vista
---

# WDI_TLV_BSSID (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_BSSID is a TLV that contains the BSSID of a BSS.

## TLV Type


0x2

## Length


The size (in bytes) of a [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structure.

## Values


| Type                                              | Description                                 |
|---------------------------------------------------|---------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | A Wi-Fi MAC address that specifies a BSSID. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

