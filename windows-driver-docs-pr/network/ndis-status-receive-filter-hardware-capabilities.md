---
title: NDIS_STATUS_RECEIVE_FILTER_HARDWARE_CAPABILITIES
description: The miniport driver issues an NDIS_STATUS_RECEIVE_FILTER_HARDWARE_CAPABILITIES status indication when its hardware receive filtering capabilities change.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_RECEIVE_FILTER_HARDWARE_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES


The miniport driver issues an **NDIS\_STATUS\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES** status indication when its hardware receive filtering capabilities change. These capabilities include the hardware capabilities that are currently disabled by INF file settings or through the **Advanced** properties page.

**Note**  This status indication should only be made by miniport drivers that support NDIS receive filters.

 

When the miniport driver makes this status indication, it sets the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure to a pointer to an [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_capabilities) structure. The driver initializes this structure with its currently enabled receive filter capabilities.

## Remarks

NDIS receive filters are used in the following NDIS interfaces:

-   [NDIS Packet Coalescing](./ndis-packet-coalescing.md). For more information about how to use receive filters in this interface, see [Managing Packet Coalescing Receive Filters](./guidelines-for-managing-packet-coalescing-receive-filters.md).

-   [Single Root I/O Virtualization (SR-IOV)](./single-root-i-o-virtualization--sr-iov-.md). For more information about how to use receive filters in this interface, see [Setting a Receive Filter on a Virtual Port](./setting-a-receive-filter-on-a-virtual-port.md).

-   [Virtual Machine Queue (VMQ)](./virtual-machine-queue--vmq--in-ndis-6-20.md). For more information about how to use receive filters in this interface, see [Setting and Clearing VMQ Filters](./setting-and-clearing-vmq-filters.md).

The miniport driver issues the **NDIS\_STATUS\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES** status indication when one of the following conditions is true:

-   The hardware receive filter capabilities change on a single network adapter. For example, receive filters can be enabled or disabled through a management application developed by the independent hardware vendor (IHV).

-   The hardware receive filter capabilities change for the load balancing failover (LBFO) team of network adapters that are managed by a MUX intermediate driver. For example, the hardware receive filter capabilities could change when an adapter is added to or removed from the team.

    For more information, see [NDIS MUX Intermediate Drivers](./ndis-mux-intermediate-drivers.md).

The miniport driver follows these steps when it issues the **NDIS\_STATUS\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES** status indication:

1.  The miniport initializes the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_capabilities) structure with the receive filter capabilities that are currently enabled on the network adapter.

    When the miniport driver initializes the **Header** member, it sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT. The miniport driver sets the **Revision** member of **Header** to NDIS\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2 and the **Size** member to NDIS\_SIZEOF\_RECEIVE\_FILTER\_CAPABILITIES\_REVISION\_2.

2.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure for the status indication in the following way:

    -   The **StatusCode** member must be set to [**NDIS\_STATUS\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES**](ndis-status-receive-filter-current-capabilities.md).

    -   The **StatusBuffer** member must be set to the address of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_capabilities) structure.

    -   The **StatusBufferSize** member must be set to `sizeof(NDIS_RECEIVE_FILTER_CAPABILITIES)`.

3.  The miniport driver issues the status indication by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex). The driver must pass a pointer to the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure to the *StatusIndication* parameter.

**Note**  Overlying drivers can use the **NDIS\_STATUS\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES** status indication to determine the currently enabled receive filter capabilities of the network adapter. Alternatively, these drivers can also issue OID query requests of [OID\_RECEIVE\_FILTER\_HARDWARE\_CAPABILITIES](./oid-receive-filter-hardware-capabilities.md) to obtain the hardware receive filter capabilities at any time.

 

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_capabilities)

[OID\_RECEIVE\_FILTER\_CURRENT\_CAPABILITIES](./oid-receive-filter-current-capabilities.md)

