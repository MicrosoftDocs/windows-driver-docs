---
title: WDI_TLV_SEND_ACTION_FRAME_REQUEST_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_SEND_ACTION_FRAME_REQUEST_PARAMETERS is a WiFiCx TLV that contains parameters for OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SEND_ACTION_FRAME_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SEND\_ACTION\_FRAME\_REQUEST\_PARAMETERS (dot11wificxtypes.hpp)


WDI\_TLV\_SEND\_ACTION\_FRAME\_REQUEST\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_SEND\_REQUEST\_ACTION\_FRAME](./oid-wdi-task-send-request-action-frame.md).

## TLV Type


0xBF

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| WDI\_CHANNEL\_NUMBER (UINT32)                     | The channel on which to send the action frame and also to linger on as specified in the post-ACK dwell time.                                    |
| WDI\_BAND\_ID (UINT32)                            | The ID of the band on which to send the action frame.                                                                                           |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | The MAC address of the target access point or peer adapter.                                                                                     |
| UINT32                                            | The send timeout. Specifies the maximum time (in milliseconds) to send this Action Frame.                                                       |
| UINT32                                            | The post-acknowledgment dwell time. Specifies the time (in milliseconds) to remain on listen channel after the incoming packet is acknowledged. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

