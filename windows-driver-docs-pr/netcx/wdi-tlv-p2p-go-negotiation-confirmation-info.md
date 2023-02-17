---
title: WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_INFO (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_INFO is a WiFiCx TLV that contains Wi-Fi Direct GO Negotiation Confirmation information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_INFO is a TLV that contains Wi-Fi Direct GO Negotiation Confirmation information.

## TLV Type


0x88

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                                   | Multiple TLV instances allowed | Optional | Description                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_PARAMETERS**](wdi-tlv-p2p-go-negotiation-confirmation-parameters.md) |                                |          | The Wi-Fi Direct GO Negotiation Confirmation parameters.                                                                                |
| [**WDI\_TLV\_P2P\_GROUP\_ID**](wdi-tlv-p2p-group-id.md)                                                               |                                | X        | The Wi-Fi Direct Group ID.                                                                                                              |
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](wdi-tlv-p2p-channel-number.md)                                                   |                                | X        | The listen channel of the remote device. The GO negotiation confirmation frame must be sent on this channel whenever this is specified. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




