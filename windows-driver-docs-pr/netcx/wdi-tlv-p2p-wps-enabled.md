---
title: WDI_TLV_P2P_WPS_ENABLED (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_WPS_ENABLED is a WiFiCx TLV that specifies if Wi-Fi Protected Setup is enabled.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_WPS_ENABLED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_WPS\_ENABLED (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_WPS\_ENABLED is a TLV that specifies if Wi-Fi Protected Setup is enabled.

## TLV Type


0xF7

## Length


The size (in bytes) of a UINT8.

## Values


| Type | Description |
| --- | --- |
| UINT8 | Specifies if Wi-Fi Protected Setup is enabled. Valid values are 0 (not enabled) and 1 (enabled).|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


## See also


[OID\_WDI\_SET\_P2P\_WPS\_ENABLED](./oid-wdi-set-p2p-wps-enabled.md)

 

