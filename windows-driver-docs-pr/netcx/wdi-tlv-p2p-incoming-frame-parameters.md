---
title: WDI_TLV_P2P_INCOMING_FRAME_PARAMETERS (dot11wificxtypes.h)
description: WDI_TLV_P2P_INCOMING_FRAME_PARAMETERS is a WiFiCx TLV that contains incoming Wi-Fi Direct action frame parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_INCOMING_FRAME_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INCOMING\_FRAME\_PARAMETERS (dot11wificxtypes.h)


WDI\_TLV\_P2P\_INCOMING\_FRAME\_PARAMETERS is a TLV that contains incoming Wi-Fi Direct action frame parameters.

## TLV Type


0x7A

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                    | Description                                        |
|-------------------------------------------------------------------------|----------------------------------------------------|
| [**WDI\_P2P\_ACTION\_FRAME\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_p2p_action_frame_type) | The type of the incoming action frame.             |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)                       | The MAC address of the remote peer.                |
| UINT8                                                                   | The Wi-Fi Direct Dialog Token for the transaction. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

