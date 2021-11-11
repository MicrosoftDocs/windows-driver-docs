---
title: WDI_TLV_P2P_INSTANCE_NAME_HASH (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_INSTANCE_NAME_HASH is a WiFiCx TLV that contains the hash of "Instance Name, Service Type".
ms.date: 09/30/2021
keywords:
 - WDI_TLV_P2P_INSTANCE_NAME_HASH Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INSTANCE\_NAME\_HASH (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_INSTANCE\_NAME\_HASH is a TLV that contains the hash of "Instance Name, Service Type".

 

## TLV Type


0x12C

## Length


The size (in bytes) of a [**WDI\_P2P\_SERVICE\_NAME\_HASH**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_p2p_service_name_hash) structure.

## Values


| Type                                                                    | Description                                |
|-------------------------------------------------------------------------|--------------------------------------------|
| [**WDI\_P2P\_SERVICE\_NAME\_HASH**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_p2p_service_name_hash) | The hash of "Instance Name, Service Type". |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

