---
title: WDI_TLV_LINK_INFO (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_LINK_INFO is a WiFiCx TLV that contains a WDI_LINK_INFO_PARAMETERS_STRUCT that specifies link information parameters.
ms.date: 08/23/2023
---

# WDI_TLV_LINK_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_LINK_INFO contains a WDI_LINK_INFO_PARAMETERS_STRUCT that specifies link information parameters for [NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE](ndis-status-wdi-indication-link-state-change.md).

## TLV Type

0x204

## Length

The sum (in bytes) of the sizes of all contained elements.

## Values

| Type | Description |
|-----------------|-----------------|
| UINT32 | AP link ID. |
| [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Local Link MAC address. |
| [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Link MAC address of remote peer. |
| WDI_CHANNEL_NUMBER (UINT32) | Logical channel number on which the peer was discovered.  |
| WDI_BAND_ID (UINT32) | Band ID for the given BSS entry. |
| INT32 | The received signal strength indicator (RSSI) value of the beacon or probe response from the peer. This is in units of decibels referenced to 1.0 milliwatts (dBm). |
| UINT32 | Current Bandwidth in MHz. |
| UINT32 | Current Tx MCS. |
| UINT32 | Current Rx MCS. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|WIN11_NEXT|
|Header|dot11wificxtypes.hpp|
