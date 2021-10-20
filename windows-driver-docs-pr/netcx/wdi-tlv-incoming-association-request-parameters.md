---
title: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS is a WiFiCx TLV that contains association request parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_INCOMING_ASSOCIATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_INCOMING\_ASSOCIATION\_REQUEST\_PARAMETERS is a TLV that contains association request parameters.

## TLV Type


0x7D

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | The MAC address of the sender.                                                                                                |
| UINT8                                             | A bit that indicates whether or not it is a reassociation request. A value of 1 indicates that it is a reassociation request. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

