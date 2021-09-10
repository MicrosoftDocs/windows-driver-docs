---
title: WDI_TLV_P2P_INCOMING_FRAME_INFORMATION (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_INCOMING_FRAME_INFORMATION is a WiFiCx TLV that contains incoming Wi-Fi Direct action frame information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_INCOMING_FRAME_INFORMATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INCOMING\_FRAME\_INFORMATION (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_INCOMING\_FRAME\_INFORMATION is a TLV that contains incoming Wi-Fi Direct action frame information.

## TLV Type


0x79

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                        | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_INCOMING\_FRAME\_PARAMETERS**](wdi-tlv-p2p-incoming-frame-parameters.md) |                                |          | Specifies the incoming frame parameters.                                                                                                                                                                                        |
| [**WDI\_TLV\_P2P\_ACTION\_FRAME\_IES**](wdi-tlv-p2p-action-frame-ies.md)                   |                                |          | Specifies the IEs section of the received public action frame.                                                                                                                                                                  |
| [**WDI\_TLV\_ACTION\_FRAME\_DEVICE\_CONTEXT**](wdi-tlv-action-frame-device-context.md)     |                                | X        | Specifies the vendor-specific information that is passed back down if the host decides to send a response to this incoming message. To avoid lifetime management issues, the IHV component must not use pointers in this field. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




