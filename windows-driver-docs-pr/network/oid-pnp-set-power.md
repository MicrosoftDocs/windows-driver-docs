---
title: OID\_PNP\_SET\_POWER
author: windows-driver-content
description: OID\_PNP\_SET\_POWER
ms.assetid: 21232db2-7484-4878-a2f9-5131c18ecf57
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_PNP_SET_POWER Network Drivers Starting with Windows Vista
---

# OID\_PNP\_SET\_POWER


## <a href="" id="ddk-oid-pnp-set-power-nr"></a>


The OID\_PNP\_SET\_POWER OID notifies a miniport driver that its underlying network adapter will be transitioning to the device power state specified in the *InformationBuffer*. The device power state is specified as one of the following [**NDIS\_DEVICE\_POWER\_STATE**](ndis-device-power-state.md) values:

-   **NdisDeviceStateD0**
-   **NdisDeviceStateD1**
-   **NdisDeviceStateD2**
-   **NdisDeviceStateD3**

An OID\_PNP\_SET\_POWER request may be preceded by an [OID\_PNP\_QUERY\_POWER](oid-pnp-query-power.md) request.

Starting with NDIS 6.30, NDIS will not pause and restart the NDIS drivers in the driver stack during power-state transitions if the following conditions are true:

-   The underlying miniport driver sets the **NDIS\_MINIPORT\_ATTRIBUTES\_NO\_PAUSE\_ON\_SUSPEND** flag in the [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](ndis-miniport-adapter-registration-attributes.md) structure. The driver passes a pointer to this structure in its call to the [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md) function.

-   All overlying filter drivers that are attached to the miniport driver support NDIS 6.30 or later versions of NDIS.

-   All overlying protocol drivers that are bound to the miniport driver support NDIS 6.30 or later versions of NDIS.

### Transitioning to a Low-Power State (D1-D3)

When the miniport driver handles a set request of OID\_PNP\_SET\_POWER to transition to a low-power state, it must do the following:

-   Fully prepare the network adapter for the indicated network device power state. The task that is performed by the miniport driver to accomplish this is device-dependent.

-   Wait for calls to the [**NdisMIndicateReceiveNetBufferLists**](ndismindicatereceivenetbufferlists.md) function to return.

-   Wait for send requests processed by the network adapter to complete. Once completed, the miniport driver must call the [**NdisMSendNetBufferListsComplete**](ndismsendnetbufferlistscomplete.md) function. The driver should set the **Status** member in each [**NET\_BUFFER\_LIST**](net-buffer-list.md) structure to the appropriate NDIS\_STATUS\_*Xxx* value.

-   Complete all pending send requests by calling the [**NdisMSendNetBufferListsComplete**](ndismsendnetbufferlistscomplete.md) function. The driver must set the **Status** member in each [**NET\_BUFFER\_LIST**](net-buffer-list.md) structure to **NDIS\_STATUS\_LOW\_POWER\_STATE**.

-   Reject all new send requests made to its [*MiniportSendNetBufferLists*](miniportsendnetbufferlists.md) function immediately by calling the [**NdisMSendNetBufferListsComplete**](ndismsendnetbufferlistscomplete.md) function. The driver must set the **Status** member in each [**NET\_BUFFER\_LIST**](net-buffer-list.md) structure to **NDIS\_STATUS\_LOW\_POWER\_STATE**.

The miniport driver that supports NDIS 6.30 and later versions of NDIS must also do the following:

-   Not wait for the completion of pending receive indications through calls to its [*MiniportReturnNetBufferLists*](miniportreturnnetbufferlists.md) function. Also, the miniport driver must not alter the [**NET\_BUFFER\_LIST**](net-buffer-list.md) structure or data for any packets that are waiting to be completed.

-   Handle the OID\_PNP\_SET\_POWER request to a low-power state from either the Paused or Running adapter states. For more information about these states, see [Miniport Adapter States and Operations](https://msdn.microsoft.com/library/windows/hardware/ff560490).

Before the network adapter transitions to the D3 state, the miniport driver must turn off everything under the miniport driver's control by performing the following tasks:

-   Disable interrupts and the DMA engine on the network adapter.

-   Stop the receive engine on the network adapter.

-   Do not deallocate or modify receive descriptors and packet buffers that are associated with pending receive indications.

-   Cancel all NDIS timers.

**Note**  A miniport driver cannot access the network adapter after the bus driver has transitioned the network adapter to the D3 state.

 

### Transitioning to the Full-Power State (D0)

When the miniport driver handles a set request of OID\_PNP\_SET\_POWER to transition to a full-power state, it must restore the receive engine of the network adapter to the same state that the receive engine was in before the adapter was transitioned to the low-power state.

**Note**  The miniport driver must not access or change any receive buffers that are associated with pending receive indications.

 

NDIS calls the miniport driver's [*MiniportRestart*](miniportrestart.md) function after the transition to a full-power state only if NDIS called the driver's [*MiniportPause*](miniportpause.md) function before the transition to a low-power state.

**Note**  An intermediate driver must always return **NDIS\_STATUS\_SUCCESS** to a query of OID\_PNP\_SET\_POWER. An intermediate driver should never propagate an OID\_PNP\_SET\_POWER request to an underlying miniport driver.

 

## Return status codes


The miniport driver's [*MiniportOidRequest*](miniportoidrequest.md) function returns one of the following values for this request:

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
<td><p>The miniport driver will complete the request asynchronously. After the miniport driver has completed all processing, it must succeed the request by calling the [<strong>NdisMOidRequestComplete</strong>](ndismoidrequestcomplete.md) function, passing NDIS_STATUS_SUCCESS for the <em>Status</em> parameter.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_ACCEPTED</strong></p></td>
<td><p>The miniport driver is resetting.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

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
[*MiniportInitializeEx*](miniportinitializeex.md)

[*MiniportPause*](miniportpause.md)

[*MiniportRestart*](miniportrestart.md)

[*MiniportReturnNetBufferLists*](miniportreturnnetbufferlists.md)

[*MiniportSendNetBufferLists*](miniportsendnetbufferlists.md)

[**NDIS\_DEVICE\_POWER\_STATE**](ndis-device-power-state.md)

[**NdisMIndicateReceiveNetBufferLists**](ndismindicatereceivenetbufferlists.md)

[**NdisMSendNetBufferListsComplete**](ndismsendnetbufferlistscomplete.md)

[**NET\_BUFFER\_LIST**](net-buffer-list.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PNP_SET_POWER%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


