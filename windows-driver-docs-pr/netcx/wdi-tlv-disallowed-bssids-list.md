---
title: WDI_TLV_DISALLOWED_BSSIDS_LIST (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_DISALLOWED_BSSIDS_LIST is a WiFiCx TLV that contains a list of BSSIDs that are not allowed to be used for association.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_DISALLOWED_BSSIDS_LIST Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_DISALLOWED\_BSSIDS\_LIST (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_DISALLOWED\_BSSIDS\_LIST is a TLV that contains a list of BSSIDs that are not allowed to be used for association.

## TLV Type


0xC3

## Length


The size (in bytes) of the array of [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) structures. The array must contain 1 or more structures.

## Values


| Type                                                  | Description                                                                                                                                               |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)\[\] | A list of BSSIDs that are not allowed to be used for association. If this is specified, the adapter must not associate to any AP that is not in this list |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

