---
title: WDI_TLV_LINK_STATE_CHANGE_PARAMETERS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_LINK_STATE_CHANGE_PARAMETERS is a WiFiCx TLV that contains link state change parameters for NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE.
ms.date: 08/30/2021
keywords:
 - WDI_TLV_LINK_STATE_CHANGE_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_LINK\_STATE\_CHANGE\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_LINK\_STATE\_CHANGE\_PARAMETERS is a TLV that contains link state change parameters for [NDIS\_STATUS\_WDI\_INDICATION\_LINK\_STATE\_CHANGE](./ndis-status-wdi-indication-link-state-change.md).

## TLV Type


0x56

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Specifies the MAC address of the remote peer.                                                                                                                                   |
| UINT32                                            | Specifies the current TX link speed. This is a value, in kilobits per second, that is the current TX link speed for this virtualized port. The conversion is 1 kbps = 1000 bps. |
| UINT32                                            | Specifies the current RX link speed. This is a value, in kilobits per second, that is the current RX link speed for this virtualized port. The conversion is 1 kbps = 1000 bps. |
| UINT8                                             | Specifies the current link quality. This is a value between 0 and 100 that is the current link quality for this virtualized port.                                               |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

