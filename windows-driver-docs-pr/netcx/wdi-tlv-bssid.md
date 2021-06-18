---
title: WDI_TLV_BSSID (dot11wificxtypes.h)
description: WDI_TLV_BSSID is a WiFiCx TLV that contains the BSSID of a BSS.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_BSSID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_BSSID (dot11wificxtypes.h)


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
|Minimum supported client|WIN10_NEXT|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

