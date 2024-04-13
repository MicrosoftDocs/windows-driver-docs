---
title: OID_PM_ADD_PROTOCOL_OFFLOAD
ms.topic: reference
description: As a set, NDIS protocol drivers use the OID_PM_ADD_PROTOCOL_OFFLOAD OID to add a protocol offload for power management to a network adapter.
ms.date: 08/08/2017
keywords: 
 -OID_PM_ADD_PROTOCOL_OFFLOAD Network Drivers Starting with Windows Vista
---

# OID\_PM\_ADD\_PROTOCOL\_OFFLOAD


As a set, NDIS protocol drivers use the OID\_PM\_ADD\_PROTOCOL\_OFFLOAD OID to add a protocol offload for power management to a network adapter. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_protocol_offload) structure.

## Remarks

NDIS 6.20 and later protocol drivers use OID\_PM\_ADD\_PROTOCOL\_OFFLOAD OID to add a protocol offload for power management to a network adapter. If the request is successful, the network adapter must generate and transmit the necessary response packets for the offloaded protocol when the network adapter is in a low power state.

A protocol driver can offload a protocol after it successfully binds to an underlying network adapter and as soon as it has the necessary data (such as the IP address of the interface) to offload the protocol. The protocol driver can also offload a protocol in response to some other power management event notifications, such as the rejection of a previously added WOL pattern or an offloaded protocol.

To avoid race conditions in NDIS and other protocol drivers that are bound to the same miniport adapter, after NDIS starts to set a network adapter to a low power state, it will fail any attempt to offload another protocol to that network adapter. For example, if an NDIS protocol driver tries to offload a protocol in the context of processing a **NetEventSetPower** event notification for that network adapter, NDIS will fail the request.

Before NDIS sends this OID request down to the underlying NDIS drivers or completes the request to the overlying driver, it sets the ULONG **ProtocolOffloadId** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_protocol_offload) structure to a unique value. Protocol drivers and NDIS use this protocol offload identifier with the [OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD](oid-pm-remove-protocol-offload.md) OID request to remove the protocol offload from the underlying network adapter.

**Note**  The protocol offload identifier is a unique value for each of the protocol offloads that are set on a network adapter. However, the protocol offload identifier is not globally unique across all network adapters.

 

If NDIS or an underlying network adapter rejects an offload, it generates an [**NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED**](./ndis-status-pm-offload-rejected.md) status indication. This can occur after returning NDIS\_STATUS\_SUCCESS for the OID. The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure contains the ULONG protocol offload identifier of the rejected protocol offload.

For information on how a Native 802.11 Wireless LAN miniport driver uses this OID, see [Adding and Deleting Low Power Protocol Offloads](./adding-and-deleting-low-power-protocol-offloads.md).

The miniport driver returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The requested protocol offload was added successfully. The **ProtocolOffloadId** member of the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_protocol_offload) structure contains a protocol offload identifier.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-pm-protocol-offload-list-full"></a>NDIS\_STATUS\_PM\_PROTOCOL\_OFFLOAD\_LIST\_FULL  
The request failed because the protocol offload list is full and the network adapter cannot add another protocol offload.

<a href="" id="ndis-status-resources"></a>NDIS\_STATUS\_RESOURCES  
NDIS or an underlying network adapter could not add the new protocol offload due to lack of resources.

<a href="" id="ndis-status-invalid-parameter"></a>NDIS\_STATUS\_INVALID\_PARAMETER  
One or more parameters in the [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_protocol_offload) structure were invalid.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.SET\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-not-supported"></a>NDIS\_STATUS\_NOT\_SUPPORTED  
The network adapter does not support the requested protocol offload.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for reasons other than the preceding reasons.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later. Mandatory for miniport drivers.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_protocol_offload)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[**NDIS\_STATUS\_PM\_OFFLOAD\_REJECTED**](./ndis-status-pm-offload-rejected.md)

[OID\_PM\_REMOVE\_PROTOCOL\_OFFLOAD](oid-pm-remove-protocol-offload.md)

[Adding and Deleting Low Power Protocol Offloads](./adding-and-deleting-low-power-protocol-offloads.md)

 

