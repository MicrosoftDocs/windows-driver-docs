---
title: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_INFO (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_INFO is a WiFiCx TLV that contains Wi-Fi Direct Provision Discovery Response information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_PROVISION_DISCOVERY_RESPONSE_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_INFO is a TLV that contains Wi-Fi Direct Provision Discovery Response information.

## TLV Type


0x87

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                                     | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_PROVISION\_DISCOVERY\_RESPONSE\_PARAMETERS**](wdi-tlv-p2p-provision-discovery-response-parameters.md) |                                |          | The provision discovery response parameters.                                                                                                                                                                                            |
| [**WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES**](wdi-tlv-p2p-provision-service-attributes.md)                        |                                | X        | The Provision Service attributes.                                                                                                                                                                                                       |
| [**WDI\_TLV\_P2P\_GROUP\_ID**](wdi-tlv-p2p-group-id.md)                                                                 |                                | X        | The Group ID if Wi-Fi Direct Service is supported.                                                                                                                                                                                      |
| [**WDI\_TLV\_P2P\_PERSISTENT\_GROUP\_ID**](wdi-tlv-p2p-persistent-group-id.md)                                          |                                | X        | The Group IP for the Persistent Group to be used for the connection. This field is valid if the Persistent Group flag in [**WDI\_TLV\_P2P\_PROVISION\_SERVICE\_ATTRIBUTES**](wdi-tlv-p2p-provision-service-attributes.md) is set to 1. |
| [**WDI\_TLV\_P2P\_SERVICE\_SESSION\_INFO**](wdi-tlv-p2p-service-session-info.md)                                        |                                | X        | The Service Session information.                                                                                                                                                                                                        |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




