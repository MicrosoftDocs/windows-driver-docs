---
title: NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE  (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE to indicate link speed or quality changes.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_LINK\_STATE\_CHANGE (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_LINK\_STATE\_CHANGE to indicate any of the following situations:

-   The link speed changed.
-   The link quality changed by more than a threshold value. The threshold is 1 if the connection quality hint is set to WDI\_CONNECTION\_QUALITY\_LOW\_LATENCY (defined in [**WDI\_CONNECTION\_QUALITY\_HINT**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_connection_quality_hint)). Otherwise, the threshold is 5.

| Object |
|--------|
| Port   |

 

This information from this indication is used by the host to keep track of metadata about the current link, and it may be propagated to the user.

In Station and P2P Client cases, the Peer MAC Address is set to the BSSID of the connected network. In AP/P2P GO cases, the Peer MAC Address is set to the MAC address of a given connected device.

## Payload data


| Type                                                                                           | Multiple TLV instances allowed | Optional | Description                       |
|------------------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------|
| [**WDI\_TLV\_LINK\_STATE\_CHANGE\_PARAMETERS**](./wdi-tlv-link-state-change-parameters.md) | | |The link state change parameters. |
| [**WDI_TLV_BSS_ENTRY_CHANNEL_INFO**](wdi-tlv-bss-entry-channel-info.md) |                                |     X     | Channel number and Band ID of the current connection. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


 

