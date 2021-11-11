---
title: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_INFO (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_INFO is a WiFiCx TLV that contains Wi-Fi Direct Group Owner negotiation response information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_INFO is a TLV that contains Wi-Fi Direct Group Owner negotiation response information.

## TLV Type


0x6F

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                           | Multiple TLV instances allowed | Optional | Description                                                             |
|----------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_PARAMETERS**](wdi-tlv-p2p-go-negotiation-response-parameters.md) |                                |          | Specifies the Wi-Fi Direct Group Owner negotiation response parameters. |
| [**WDI\_TLV\_P2P\_GROUP\_ID**](wdi-tlv-p2p-group-id.md)                                                       |                                | X        | Specifies the Group ID for local Wi-Fi Direct GO.                       |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




