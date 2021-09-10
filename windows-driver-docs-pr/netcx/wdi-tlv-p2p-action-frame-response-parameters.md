---
title: WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS is a WiFiCx TLV that contains Wi-Fi Direct Action Frame response parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_ACTION_FRAME_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ACTION\_FRAME\_RESPONSE\_PARAMETERS (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_ACTION\_FRAME\_RESPONSE\_PARAMETERS is a TLV that contains Wi-Fi Direct Action Frame response parameters.

## TLV Type


0xAD

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                    | Description                                                                                                                          |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_ACTION\_FRAME\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_p2p_action_frame_type) | The type of Response Frame to be sent.                                                                                               |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)                       | The device address of the target peer Wi-Fi Direct device.                                                                           |
| UINT8                                                                   | The Wi-Fi Direct Dialog Token for this transaction.                                                                                  |
| UINT32                                                                  | The send timeout. Specifies the maximum time, in milliseconds, to send this action frame.                                            |
| UINT32                                                                  | The post-ACK dwell time. Specifies the time to remain on listen channel, in milliseconds, after the incoming packet is acknowledged. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

