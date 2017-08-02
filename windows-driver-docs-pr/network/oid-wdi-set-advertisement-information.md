---
title: OID_WDI_SET_ADVERTISEMENT_INFORMATION
author: windows-driver-content
description: OID_WDI_SET_ADVERTISEMENT_INFORMATION configures the Information Elements (IEs) and other advertisement settings to be included in the probe request, probe response, and beacons sent by the specified port.
ms.assetid: efa1fc93-2cc8-4d14-be5f-d099ef3c371e
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - OID_WDI_SET_ADVERTISEMENT_INFORMATION Network Drivers Starting with Windows Vista
---

# OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION


OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION configures the Information Elements (IEs) and other advertisement settings to be included in the probe request, probe response, and beacons sent by the specified port. This request is only applicable to Wi-Fi Direct ports.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

When this command is received by the device, it shall update any relevant Wi-Fi Direct IEs, and append any necessary additional IEs in future outgoing messages sent by this port.

## Set property parameters


WDI can provide a pre-configured set of prefix hashes for the advertised services. If a peer sends a hash, the driver first tries to match with a service name hash as defined in [**WDI\_TLV\_P2P\_ADVERTISED\_PREFIX\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt269134). If a match is found from the prefix hashes, the driver searches for the service(s) in [**WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn897861) that have the prefix and responds with those. If a match is not found, the driver tries to match the requested service name hash in [**WDI\_TLV\_P2P\_ADVERTISED\_SERVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn897861).

| TLV                                                                                                 | Multiple TLV instances allowed | Optional | Description                                     |
|-----------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------|
| [**WDI\_TLV\_ADDITIONAL\_IES**](https://msdn.microsoft.com/library/windows/hardware/dn926122)                                    |                                | X        | Additional IEs to be included.                  |
| [**WDI\_TLV\_P2P\_DEVICE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn897875)                                 |                                | X        | Wi-Fi Direct device information.                |
| [**WDI\_TLV\_P2P\_DEVICE\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/dn897872)                     |                                | X        | Wi-Fi Direct device capabilities.               |
| [**WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/dn897954)          |                                | X        | Wi-Fi Direct Group Owner capability information |
| [**WDI\_TLV\_P2P\_SECONDARY\_DEVICE\_TYPE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn897991) |                                | X        | List of Wi-Fi Direct secondary device types.    |
| [**WDI\_TLV\_P2P\_ADVERTISED\_SERVICES**](https://msdn.microsoft.com/library/windows/hardware/dn897860)                 |                                | X        | Wi-Fi Direct advertised services.               |

 

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WDI_SET_ADVERTISEMENT_INFORMATION%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


