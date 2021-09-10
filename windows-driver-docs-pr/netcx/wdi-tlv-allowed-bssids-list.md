---
title: WDI_TLV_ALLOWED_BSSIDS_LIST (dot11wificxtypes.hpp)
description: WDI_TLV_ALLOWED_BSSIDS_LIST is a WiFiCx TLV that contains a list of BSSIDs that are allowed to be used for association.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_ALLOWED_BSSIDS_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ALLOWED\_BSSIDS\_LIST (dot11wificxtypes.hpp)


WDI\_TLV\_ALLOWED\_BSSIDS\_LIST is a TLV that contains a list of BSSIDs that are allowed to be used for association.

## TLV Type


0xC2

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                                                   |
|-------------------------------------------------------|---------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)\[\] | A list of BSSIDs that are allowed to be used for association. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

