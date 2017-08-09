---
title: NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE
author: windows-driver-content
description: The NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE status indicates to NDIS and overlying drivers that the allocation state of virtual machine (VM) queues on the network adapter has changed.
ms.assetid: E8E62EE1-78F5-4DDB-9623-D31B807D753C
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_RECEIVE_FILTER_QUEUE_ALLOCATION_STATE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE


The **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE** status indicates to NDIS and overlying drivers that the allocation state of virtual machine (VM) queues on the network adapter has changed.

Remarks
-------

The miniport driver must issue an **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE** status indication when the VM queue capabilities of the network adapter change. The VM queue capabilities could change when one of the following conditions is true:

-   The VM queue allocation state is changed through a management application developed by the independent hardware vendor (IHV).

-   The VM queue allocation state changes for one or more network adapters that belong to a load balancing failover (LBFO) team managed by a MUX intermediate driver. For more information, see [NDIS MUX Intermediate Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566498).

When the miniport driver issues the **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE** status indication, it must follow these steps:

1.  The miniport driver initializes an [**NDIS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh451653) structure with the current VM queue allocation state on the network adapter. If VM queue allocation is allowed, the driver must set the **AllocationAllowed** member to TRUE. Otherwise, the driver must set the **AllocationAllowed** member to FALSE.
2.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure in the following way:

    -   The **StatusCode** member must be set to **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE**.

    -   The **StatusBuffer** member must be set to the pointer to a [**NDIS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh451653) structure. This structure contains the currently enabled hardware capabilities of the NIC switch.

    -   The **StatusBufferSize** member must be set to sizeof([**NDIS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh451653)).

3.  The miniport driver issues the status notification by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). The driver must pass a pointer to the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to the *StatusIndication* parameter.

Starting with NDIS 6.30, if VM queue allocation is no longer enabled or allowed, the overlying drivers that receive this status indication must issue an object identifier (OID) set request of [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](oid-receive-filter-free-queue.md). This OID requests the underlying miniport driver to free any VM queues that have been allocated on the network adapter.

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
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh451653)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_RECEIVE_FILTER_QUEUE_ALLOCATION_STATE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


