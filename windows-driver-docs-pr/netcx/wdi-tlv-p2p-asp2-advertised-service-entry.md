---
title: WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY is a WiFiCx TLV that contains an ASP2 Advertised Service Entry.
ms.date: 09/30/2021
keywords:
 - WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ASP2\_ADVERTISED\_SERVICE\_ENTRY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_ASP2\_ADVERTISED\_SERVICE\_ENTRY is a TLV that contains an ASP2 Advertised Service Entry.

 

## TLV Type


0x12E

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                           | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_TYPE**](wdi-tlv-p2p-service-type.md)               |                                |          | Service Type of the service (UTF-8), up to 21 bytes.                                                                                                                                                                                                                                     |
| [**WDI\_TLV\_P2P\_SERVICE\_TYPE\_HASH**](wdi-tlv-p2p-service-type-hash.md)    |                                |          | Hash of Service Type.                                                                                                                                                                                                                                                                    |
| [**WDI\_TLV\_P2P\_INSTANCE\_NAME**](wdi-tlv-p2p-instance-name.md)             |                                |          | Instance Type of the service (UTF-8), up to 63 bytes.                                                                                                                                                                                                                                    |
| [**WDI\_TLV\_P2P\_INSTANCE\_NAME\_HASH**](wdi-tlv-p2p-instance-name-hash.md)  |                                |          | Hash of "Instance Name, Service Type".                                                                                                                                                                                                                                                   |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md) |                                | X        | Service Information for the service.                                                                                                                                                                                                                                                     |
| [**WDI\_TLV\_P2P\_SERVICE\_STATUS**](wdi-tlv-p2p-service-status.md)           |                                |          | Service Status of the service.                                                                                                                                                                                                                                                           |
| [**WDI\_TLV\_P2P\_ADVERTISEMENT\_ID**](wdi-tlv-p2p-advertisement-id.md)       |                                |          | An ID that uniquely identifies the service instance.                                                                                                                                                                                                                                     |
| [**WDI\_TLV\_P2P\_CONFIG\_METHODS**](wdi-tlv-p2p-config-methods.md)           |                                |          | Configuration methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_wps_configuration_method). Only **WDI\_WPS\_CONFIGURATION\_METHOD\_DISPLAY**, **WDI\_WPS\_CONFIGURATION\_METHOD\_KEYPAD**, and **WDI\_WPS\_CONFIGURATION\_METHOD\_WFDS\_DEFAULT** are applicable. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

