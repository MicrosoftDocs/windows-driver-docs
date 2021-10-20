---
title: WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY is a WiFiCx TLV that contains an advertised service entry.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY is a TLV that contains an advertised service entry.

## TLV Type


0xFC

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                           | Multiple TLV instances allowed | Optional | Description                                                                                                                                                              |
|--------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_NAME**](wdi-tlv-p2p-service-name.md)               |                                |          | Name of the service, in UTF-8, up to 255 bytes.                                                                                                                          |
| [**WDI\_TLV\_P2P\_SERVICE\_NAME\_HASH**](wdi-tlv-p2p-service-name-hash.md)    |                                |          | Hash of Service Name.                                                                                                                                                    |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md) |                                | X        | Service Information for this service.                                                                                                                                    |
| [**WDI\_TLV\_P2P\_SERVICE\_STATUS**](wdi-tlv-p2p-service-status.md)           |                                |          | Service Status of this service.                                                                                                                                          |
| [**WDI\_TLV\_P2P\_ADVERTISEMENT\_ID**](wdi-tlv-p2p-advertisement-id.md)       |                                |          | An ID that uniquely identifies the service instance.                                                                                                                     |
| [**WDI\_TLV\_P2P\_CONFIG\_METHODS**](wdi-tlv-p2p-config-methods.md)           |                                |          | Configuration methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_wps_configuration_method). Only PIN display, PIN keypad, and WFDS are applicable. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

