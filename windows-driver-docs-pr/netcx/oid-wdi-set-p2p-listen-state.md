---
title: OID_WDI_SET_P2P_LISTEN_STATE (dot11wificxintf.h)
description: The OID_WDI_SET_P2P_LISTEN_STATE command sets the Wi-Fi Direct listen state on the port.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_P2P_LISTEN_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_P2P\_LISTEN\_STATE (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_P2P\_LISTEN\_STATE sets the Wi-Fi Direct listen state on the port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

There are different levels of listen state, and the port is expected to adhere to concurrency requirements across ports.

This property is only applicable to virtualized Wi-Fi Direct Adapter Port interfaces.

When the listen state is active, the port is expected to park the radio on a social channel for a certain period of time.

If the adapter has a virtualized port operating on a non-social channel, the port may become discoverable on that channel. If this behavior is used, the port must be very highly available to allow other adapters to quickly discover it when in the scan phase of Wi-Fi Direct discovery. This is provided as a trade-off to avoid channel hopping in low latency scenarios.

**Note**  This property specifies a radio time slice requirement to the port, which may cause conflicts with other properties or tasks issued to the port.

 


## Set property parameters


| TLV                                                                         | Multiple TLV instances allowed | Optional | Description                                                                                                                                                      |
|-----------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_LISTEN\_STATE**](./wdi-tlv-p2p-listen-state.md)       |                                |          | Desired listen state.                                                                                                                                            |
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](./wdi-tlv-p2p-channel-number.md)   |                                | X        | The host’s desired listen channel when enabling the Wi-Fi Direct listen state. If this option is not specified, the port may select a listen channel on its own. |
| [**WDI\_TLV\_P2P\_LISTEN\_DURATION**](./wdi-tlv-p2p-listen-duration.md) |                                |          | Cycle duration and listen time.                                                                                                                                  |


 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


 

