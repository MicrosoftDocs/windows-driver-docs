---
title: OID_WDI_SET_ADVERTISEMENT_INFORMATION
description: OID_WDI_SET_ADVERTISEMENT_INFORMATION configures the Information Elements (IEs) and other advertisement settings to be included in the probe request, probe response, and beacons sent by the specified port.
ms.assetid: efa1fc93-2cc8-4d14-be5f-d099ef3c371e
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_ADVERTISEMENT_INFORMATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION


OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION configures the Information Elements (IEs) and other advertisement settings to be included in the probe request, probe response, and beacons sent by the specified port. This request is only applicable to Wi-Fi Direct ports.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

When this command is received by the device, it shall update any relevant Wi-Fi Direct IEs, and append any necessary additional IEs in future outgoing messages sent by this port.

## Set property parameters


WDI can provide a pre-configured set of prefix hashes for the advertised services. If a peer sends a hash, the driver first tries to match with a service name hash as defined in [**WDI\_TLV\_P2P\_ADVERTISED\_PREFIX\_ENTRY**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-advertised-prefix-entry). If a match is found from the prefix hashes, the driver searches for the service(s) in [**WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-advertised-service-entry) that have the prefix and responds with those. If a match is not found, the driver tries to match the requested service name hash in [**WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-advertised-service-entry).

| TLV                                                                                                 | Multiple TLV instances allowed | Optional | Description                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------|
| [**WDI\_TLV\_ADDITIONAL\_IES**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-additional-ies)                                    |                                | X        | Additional IEs to be included.                  |
| [**WDI\_TLV\_P2P\_DEVICE\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-device-info)                                 |                                | X        | Wi-Fi Direct device information.                |
| [**WDI\_TLV\_P2P\_DEVICE\_CAPABILITY**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-device-capability)                     |                                | X        | Wi-Fi Direct device capabilities.               |
| [**WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-group-owner-capability)          |                                | X        | Wi-Fi Direct Group Owner capability information |
| [**WDI\_TLV\_P2P\_SECONDARY\_DEVICE\_TYPE\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-secondary-device-type-list) |                                | X        | List of Wi-Fi Direct secondary device types.    |
| [**WDI\_TLV\_P2P\_ADVERTISED\_SERVICES**](https://docs.microsoft.com/windows-hardware/drivers/network/wdi-tlv-p2p-advertised-services)                 |                                | X        | Wi-Fi Direct advertised services.               |

 

## Set property results


No additional data. The data in the header is sufficient.
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_ACTION\_FRAME\_RECEIVED](ndis-status-wdi-indication-action-frame-received.md)
The adapter must indicate ANQP Action Frame requests for the Service Information if it receives an ANQP request (or any other unknown action frame) from a peer.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




