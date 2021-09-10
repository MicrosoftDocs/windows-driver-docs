---
title: WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS is a WiFiCx TLV that contains parameters for sending a Wi-Fi Direct action request frame with OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_SEND_ACTION_REQUEST_FRAME_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SEND\_ACTION\_REQUEST\_FRAME\_PARAMETERS (dot11wificxtypes.hpp)


WDI\_TLV\_P2P\_SEND\_ACTION\_REQUEST\_FRAME\_PARAMETERS is a TLV that contains parameters for sending a Wi-Fi Direct action request frame with [OID\_WDI\_TASK\_P2P\_SEND\_REQUEST\_ACTION\_FRAME](./oid-wdi-task-p2p-send-request-action-frame.md).

## TLV Type


0x8B

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                    | Description                                                                                                                    |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_ACTION\_FRAME\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_p2p_action_frame_type) | The type of request to send.                                                                                                   |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)                       | The MAC address of the target peer device.                                                                                     |
| UINT8                                                                   | The Direct Dialog Token for the transaction.                                                                                   |
| UINT32                                                                  | The send timeout. The maximum time, in milliseconds, to send the action frame.                                                 |
| UINT32                                                                  | The post-ACK dwell time. The time, in milliseconds, to remain on the listen channel after the incoming packet is acknowledged. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

