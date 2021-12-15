---
title: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT_PARAMETERS is a WiFiCx TLV that contains Wi-Fi Direct send Action Frame result parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_SEND_ACTION_FRAME_RESULT_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_SEND\_ACTION\_FRAME\_RESULT\_PARAMETERS is a TLV that contains Wi-Fi Direct send Action Frame result parameters.

## TLV Type


0xAE

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                           |
|---------------------------------------------------|-------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | The device address of the target Wi-Fi Direct device. |
| UINT8                                             | The Wi-Fi Direct Dialog Token for this transaction.   |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

