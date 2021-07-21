---
title: OID_WWAN_PACKET_SERVICE
description: OID_WWAN_PACKET_SERVICE is used to instruct miniport drivers to perform packet service attach/detach actions on the current registered provider’s network for both GSM-based and CDMA-based MB devices.
ms.date: 04/04/2019
keywords: 
 -OID_WWAN_PACKET_SERVICE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID\_WWAN\_PACKET\_SERVICE


OID\_WWAN\_PACKET\_SERVICE is used to instruct miniport drivers to perform packet service attach/detach actions on the current registered provider’s network for both GSM-based and CDMA-based MB devices. In addition to the packet service attach/detach status, this OID is used to determine data class availability and the currently used data class information.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_PACKET\_SERVICE**](ndis-status-wwan-packet-service.md) status notification containing an [**NDIS\_WWAN\_PACKET\_SERVICE\_STATE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_packet_service_state) structure to provide information about the current packet service state regardless of completing set or query requests.

Callers requesting to set the current packet service state provide an [**NDIS\_WWAN\_SET\_PACKET\_SERVICE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_packet_service) structure to the miniport driver with the appropriate information.

## Remarks

See [WWAN Packet Service Attach Operations](./mb-packet-service-attach-operations.md) for more information about using this OID.

Miniport drivers can access the provider network when processing query or set operations, but should not access the Subscriber Identity Module (SIM card).

CDMA-based devices should use this as an opportunity to release the network resource allocation if possible.

Some SIM cards enable the MB device to register only on the packet domain and not the circuit-switched domain. Once a data call ends, the VAN UI sends an OID\_WWAN\_PACKET\_SERVICE set request to detach packet service. This causes the MB device to detach from the packet domain. The MB device unregisters from the network and goes into a power save mode. Consequently, the device disappears from the VAN UI as a result of being unregistered, and can only be recovered by rebooting. In this scenario, miniport drivers should spoof the packet attach/detach operations by returning positive data without setting the MB device into such a mode.

For technologies that do not support packet-attach, miniport drivers should spoof an attach state to let the MB Service know that it can proceed with context activation. Miniport drivers should also spoof the set OID\_WWAN\_PACKET\_SERVICE requests in the miniport driver. Miniport drivers should send [**NDIS\_STATUS\_WWAN\_PACKET\_SERVICE**](ndis-status-wwan-packet-service.md) notifications for query operations and for unsolicited events. Miniport drivers should fail PDP activation if the device packet service state is not set to *WwanPacketServiceStateAttached*.

The MB Service shall not proceed with context activation until the packet service state has reached *WwanPacketServiceStateAttached*.

### Windows 10, version 1903

A new revision 2 for this OID is supported starting in Windows 10, version 1903. The extension enables the host to query the frequency range in which the modem is currently operating in 5G.

The host can query the extended packet service state information at any time. The response is the same as revision 1, except that revision 2 has two new fields.

If the modem is registered in a 5G domain, it returns the 5G frequency range of the carrier. If multiple 5G carriers exist, then all valid ranges are returned.

For more info about 5G data class support, see [MB 5G data class support](./mb-5g-operations-overview.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_SET\_PACKET\_SERVICE**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_packet_service)

[**NDIS\_STATUS\_WWAN\_PACKET\_SERVICE**](ndis-status-wwan-packet-service.md)

[WWAN Packet Service Attach Operations](./mb-packet-service-attach-operations.md)

