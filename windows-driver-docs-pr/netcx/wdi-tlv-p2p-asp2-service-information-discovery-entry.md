---
title: WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY is a WiFiCx TLV that contains an ASP2 Service Information Discovery Entry.
ms.date: 06/30/2021
keywords:
 - WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_ASP2\_SERVICE\_INFORMATION\_DISCOVERY\_ENTRY is a TLV that contains an ASP2 Service Information Discovery Entry.

 

## TLV Type


0x12D

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                         |
|-------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_TYPE**](wdi-tlv-p2p-service-type.md)                          |                                |          | Name of the service (UTF-8), up to 21 bytes.                                                                        |
| [**WDI\_TLV\_P2P\_INSTANCE\_NAME**](wdi-tlv-p2p-instance-name.md)                        |                                |          | Instance name of the service (UTF-8), up to 63 bytes.                                                               |
| [**WDI\_TLV\_P2P\_SERVICE\_UPDATE\_INDICATOR**](wdi-tlv-p2p-service-update-indicator.md) |                                | X        | Service Update indicator to be used for the ANQP query request.                                                     |
| [**WDI\_TLV\_P2P\_SERVICE\_TRANSACTION\_ID**](wdi-tlv-p2p-service-transaction-id.md)     |                                | X        | Service transaction ID to be used for the ANQP query request.                                                       |
| [**WDI\_TLV\_P2P\_SERVICE\_INFORMATION**](wdi-tlv-p2p-service-information.md)            |                                | X        | Request service information to be used for the ANQP query request to download service information for this Service. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




