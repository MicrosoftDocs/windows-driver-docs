---
title: WDI_TLV_P2P_BACKGROUND_DISCOVER_MODE (dot11wificxtypes.h)
description: WDI_TLV_P2P_BACKGROUND_DISCOVER_MODE is a WiFiCx TLV that contains Wi-Fi Direct Background Discover Mode parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_BACKGROUND_DISCOVER_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_BACKGROUND\_DISCOVER\_MODE (dot11wificxtypes.h)


WDI\_TLV\_P2P\_BACKGROUND\_DISCOVER\_MODE is a TLV that contains Wi-Fi Direct Background Discover Mode parameters.

## TLV Type


0xC4

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|[**WDI_P2P_DISCOVER_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_p2p_discover_type)|The type of discovery to be performed by the port.|
|[**WDI_P2P_SERVICE_DISCOVERY_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_p2p_service_discovery_type)|The type of Service Discovery to be performed by the port. The only valid values are **WDI_P2P_SERVICE_DISCOVERY_TYPE_NO_SERVICE_DISCOVERY** and **WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_NAME_ONLY**.|
|UINT32|The device visibility timeout. Specifies the maximum timeout (in milliseconds) for reporting a device entry. This is required for background scan only.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

