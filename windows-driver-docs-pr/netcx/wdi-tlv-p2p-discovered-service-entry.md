---
title: WDI_TLV_P2P_DISCOVERED_SERVICE_ENTRY  (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_DISCOVERED_SERVICE_ENTRY is a WiFix TLV that contains a discovered service entry.
ms.date: 06/17/2021
keywords:
 - WDI_TLV_P2P_DISCOVERED_SERVICE_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_DISCOVERED\_SERVICE\_ENTRY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_DISCOVERED\_SERVICE\_ENTRY is a TLV that contains a discovered service entry.

## TLV Type


0x112

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                           | Multiple TLV instances allowed | Optional | Description                                                                                                                                                               |
|--------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_NAME**](wdi-tlv-p2p-service-name.md)               |                                |          | The name of the service, in UTF-8, up to 255 bytes.                                                                                                                       |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md) |                                | X        | The Service Information for the service.                                                                                                                                  |
| [**WDI\_TLV\_P2P\_SERVICE\_STATUS**](wdi-tlv-p2p-service-status.md)           |                                |          | The Service Status of the service, if ANQP service discovery was performed. Otherwise this value may default to **one**.                                                                                          |
| [**WDI\_TLV\_P2P\_ADVERTISEMENT\_ID**](wdi-tlv-p2p-advertisement-id.md)       |                                |          | An ID that uniquely identifies the service instance.                                                                                                                      |
| [**WDI\_TLV\_P2P\_CONFIG\_METHODS**](wdi-tlv-p2p-config-methods.md)           |                                |          | The Configuration Methods as defined in [**WDI\_WPS\_CONFIGURATION\_METHOD**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_wps_configuration_method). Only PinDisplay, PinKeypad and WFDS are applicable. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

