---
title: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_INFO (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_INFO is a WiFiCx TLV that contains Wi-Fi Direct Group Owner negotiation request information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_REQUEST_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_INFO is a TLV that contains Wi-Fi Direct Group Owner negotiation request information.

## TLV Type


0x6D

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                         | Multiple TLV instances allowed | Optional | Description                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_GO\_NEGOTIATION\_REQUEST\_PARAMETERS**](wdi-tlv-p2p-go-negotiation-request-parameters.md) |                                |          | The Wi-Fi Direct Group Owner negotiation request parameters.                                                                        |
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](wdi-tlv-p2p-channel-number.md)                                         |                                | X        | The listen channel of the remote device. Whenever this is specified, the GO negotiation request frame must be sent on this channel. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




