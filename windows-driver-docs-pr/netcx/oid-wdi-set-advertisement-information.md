---
title: OID_WDI_SET_ADVERTISEMENT_INFORMATION (dot11wificxintf.h)
description: The OID_WDI_SET_ADVERTISEMENT_INFORMATION command configures the IEs and other advertisement settings to be included in the probe request, probe response, and beacons sent by the specified port.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_ADVERTISEMENT_INFORMATION Network Drivers Starting with Windows Vista
---

# OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION configures the Information Elements (IEs) and other advertisement settings to be included in the probe request, probe response, and beacons sent by the specified port. This request is only applicable to Wi-Fi Direct ports.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

When this command is received by the device, it shall update any relevant Wi-Fi Direct IEs, and append any necessary additional IEs in future outgoing messages sent by this port.

## Set property parameters


| TLV                                                                                                 | Multiple TLV instances allowed | Optional | Description                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------|
| [**WDI\_TLV\_ADDITIONAL\_IES**](./wdi-tlv-additional-ies.md)                                    |                                | X        | Additional IEs to be included.                  |
| [**WDI\_TLV\_P2P\_DEVICE\_CAPABILITY**](./wdi-tlv-p2p-device-capability.md)                     |                                | X        | Wi-Fi Direct device capabilities.               |
| [**WDI\_TLV\_P2P\_DEVICE\_INFO**](./wdi-tlv-p2p-device-info.md)                                 |                                | X        | Wi-Fi Direct device information.                |
| [**WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY**](./wdi-tlv-p2p-group-owner-capability.md)          |                                | X        | Wi-Fi Direct Group Owner capability information |
| [**WDI\_TLV\_P2P\_SECONDARY\_DEVICE\_TYPE\_LIST**](./wdi-tlv-p2p-secondary-device-type-list.md) |                                | X        | List of Wi-Fi Direct secondary device types.    |
| [**WDI\_TLV\_P2P\_ADVERTISED\_SERVICES**](./wdi-tlv-p2p-advertised-services.md)                 |                                | X        | Wi-Fi Direct advertised services.               |

 

## Set property results


No additional data. The data in the header is sufficient.
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_ACTION\_FRAME\_RECEIVED](ndis-status-wdi-indication-action-frame-received.md)

The adapter must indicate ANQP Action Frame requests for the Service Information if it receives an ANQP request (or any other unknown action frame) from a peer.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

