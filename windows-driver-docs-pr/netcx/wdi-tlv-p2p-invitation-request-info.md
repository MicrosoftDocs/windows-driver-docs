---
title: WDI_TLV_P2P_INVITATION_REQUEST_INFO (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_INVITATION_REQUEST_INFO is a WiFiCx TLV that contains Wi-Fi Direct Invitation Request information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_INVITATION_REQUEST_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_INVITATION\_REQUEST\_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_INVITATION\_REQUEST\_INFO is a TLV that contains Wi-Fi Direct Invitation Request information.

## TLV Type


0x7B

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                | Multiple TLV instances allowed | Optional | Description                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------|
| [**WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS**](wdi-tlv-p2p-invitation-request-parameters.md) |                                |          | The Wi-Fi Direct Invitation Request parameters. |
| [**WDI\_TLV\_P2P\_GROUP\_BSSID**](wdi-tlv-p2p-group-bssid.md)                                      |                                | X        | The Group BSSID.                                |
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](wdi-tlv-p2p-channel-number.md)                                |                                | X        | The operating channel for Wi-Fi Direct GO.      |
| [**WDI\_TLV\_P2P\_GROUP\_ID**](wdi-tlv-p2p-group-id.md)                                            |                                |          | The Group ID for target Wi-Fi Direct GO.        |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




