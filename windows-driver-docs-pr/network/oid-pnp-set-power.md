---
title: OID_PNP_SET_POWER
description: OID_PNP_SET_POWER
ms.date: 08/08/2017
keywords: 
 -OID_PNP_SET_POWER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_SET\_POWER





The OID\_PNP\_SET\_POWER OID notifies a miniport driver that its underlying network adapter will be transitioning to the device power state specified in the *InformationBuffer*. The device power state is specified as one of the following [**NDIS\_DEVICE\_POWER\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_device_power_state) values:

-   **NdisDeviceStateD0**
-   **NdisDeviceStateD1**
-   **NdisDeviceStateD2**
-   **NdisDeviceStateD3**

An OID\_PNP\_SET\_POWER request may be preceded by an [OID\_PNP\_QUERY\_POWER](oid-pnp-query-power.md) request.

Starting with NDIS 6.30, NDIS will not pause and restart the NDIS drivers in the driver stack during power-state transitions if the following conditions are true:

-   The underlying miniport driver sets the **NDIS\_MINIPORT\_ATTRIBUTES\_NO\_PAUSE\_ON\_SUSPEND** flag in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_registration_attributes) structure. The driver passes a pointer to this structure in its call to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

-   All overlying filter drivers that are attached to the miniport driver support NDIS 6.30 or later versions of NDIS.

-   All overlying protocol drivers that are bound to the miniport driver support NDIS 6.30 or later versions of NDIS.

### Transitioning to a Low-Power State (D1-D3)

When the miniport driver handles a set request of OID\_PNP\_SET\_POWER to transition to a low-power state, it must do the following:

-   Fully prepare the network adapter for the indicated network device power state. The task that is performed by the miniport driver to accomplish this is device-dependent.

-   Wait for calls to the [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function to return.

-   Wait for send requests processed by the network adapter to complete. Once completed, the miniport driver must call the [**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete) function. The driver should set the **Status** member in each [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure to the appropriate NDIS\_STATUS\_*Xxx* value.

-   Complete all pending send requests by calling the [**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete) function. The driver must set the **Status** member in each [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure to **NDIS\_STATUS\_LOW\_POWER\_STATE**.

-   Reject all new send requests made to its [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) function immediately by calling the [**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete) function. The driver must set the **Status** member in each [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure to **NDIS\_STATUS\_LOW\_POWER\_STATE**.

The miniport driver that supports NDIS 6.30 and later versions of NDIS must also do the following:

-   Not wait for the completion of pending receive indications through calls to its [*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) function. Also, the miniport driver must not alter the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure or data for any packets that are waiting to be completed.

-   Handle the OID\_PNP\_SET\_POWER request to a low-power state from either the Paused or Running adapter states. For more information about these states, see [Miniport Adapter States and Operations](./miniport-adapter-states-and-operations.md).

Before the network adapter transitions to the D3 state, the miniport driver must turn off everything under the miniport driver's control by performing the following tasks:

-   Disable interrupts and the DMA engine on the network adapter.

-   Stop the receive engine on the network adapter.

-   Do not deallocate or modify receive descriptors and packet buffers that are associated with pending receive indications.

-   Cancel all NDIS timers.

**Note**  A miniport driver cannot access the network adapter after the bus driver has transitioned the network adapter to the D3 state.

 

### Transitioning to the Full-Power State (D0)

When the miniport driver handles a set request of OID\_PNP\_SET\_POWER to transition to a full-power state, it must restore the receive engine of the network adapter to the same state that the receive engine was in before the adapter was transitioned to the low-power state.

**Note**  The miniport driver must not access or change any receive buffers that are associated with pending receive indications.

 

NDIS calls the miniport driver's [*MiniportRestart*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_restart) function after the transition to a full-power state only if NDIS called the driver's [*MiniportPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause) function before the transition to a low-power state.

**Note**  An intermediate driver must always return **NDIS\_STATUS\_SUCCESS** to a query of OID\_PNP\_SET\_POWER. An intermediate driver should never propagate an OID\_PNP\_SET\_POWER request to an underlying miniport driver.

 

## Return status codes


The miniport driver's [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function returns one of the following values for this request:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The miniport driver completed the request successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)"><strong>NdisMOidRequestComplete</strong></a> function, passing NDIS_STATUS_SUCCESS for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported for NDIS 5.1, and NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)

[*MiniportPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause)

[*MiniportRestart*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_restart)

[*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists)

[*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists)

[**NDIS\_DEVICE\_POWER\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_device_power_state)

[**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists)

[**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete)

[**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list)

