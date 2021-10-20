---
title: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT is a WiFiCx TLV that contains information about an Action Frame that was sent to a peer.
ms.date: 07/30/2021
keywords:
 - WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT is a TLV that contains information about an Action Frame that was sent to a peer.

## TLV Type


0xAF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                                              | Multiple TLV instances allowed | Optional | Description                                           |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT\_PARAMETERS**](wdi-tlv-p2p-send-action-frame-result-parameters.md) |                                |          | The Wi-Fi Direct send Action Frame result parameters. |
| [**WDI\_TLV\_P2P\_ACTION\_FRAME\_IES**](wdi-tlv-p2p-action-frame-ies.md)                                         |                                |          | The set of IEs sent to the remote device.             |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




