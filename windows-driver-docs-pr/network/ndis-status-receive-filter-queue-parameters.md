---
title: NDIS_STATUS_RECEIVE_FILTER_QUEUE_PARAMETERS
description: The NDIS_STATUS_RECEIVE_FILTER_QUEUE_PARAMETERS status indicates to NDIS and overlying drivers that the current virtual machine (VM) queue parameters have changed on the network adapter.
ms.assetid: 30782C77-578F-4533-8B6B-9D2F64EE6189
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_RECEIVE_FILTER_QUEUE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS


The **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS** status indicates to NDIS and overlying drivers that the current virtual machine (VM) queue parameters have changed on the network adapter.

Remarks
-------

The miniport driver must issue an **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS** status indication when the current VM queue parameters have changed on the network adapter. The VM queue parameters could change when one of the following conditions is true:

-   The VM queue parameters are changed through a management application developed by the independent hardware vendor (IHV).

-   The VM queue parameters change for one or more network adapters that belong to a load balancing failover (LBFO) team managed by a MUX intermediate driver. For more information, see [NDIS MUX Intermediate Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566498).

When the miniport driver issues the **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS** status indication, it must follow these steps:

1.  The miniport driver initializes an [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure with the current VM queue parameters on the network adapter. The driver must also set the **Flags** member of this structure with the appropriate NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_*Xxx*\_CHANGED flags to report on **NDIS\_RECEIVE\_QUEUE\_PARAMETERS** member values that have changed.

    **Note**  Starting with NDIS 6.30, the miniport driver can only issue an **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS** status indication to report on changes to the **InterruptCoalescingDomainId** member.




When the miniport driver initializes the **Header** member of this structure, it sets the **Type** member of **Header** to NDIS\_OBJECT\_TYPE\_DEFAULT. The miniport driver sets the **Revision** member of **Header** to NDIS\_RECEIVE\_QUEUE\_PARAMETERS\_REVISION\_2 and the **Size** member to NDIS\_SIZEOF\_RECEIVE\_QUEUE\_PARAMETERS\_REVISION\_2.


2.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure in the following way:

    -   The **StatusCode** member must be set to **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS**.

    -   The **StatusBuffer** member must be set to the pointer to a [**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211) structure. This structure contains the currently enabled hardware capabilities of the NIC switch.

    -   The **StatusBufferSize** member must be set to sizeof([**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211)).

3.  The miniport driver issues the status notification by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). The driver must pass a pointer to the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to the *StatusIndication* parameter.

Overlying drivers can use the **NDIS\_STATUS\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS** status indication to determine the current VM queue parameters on the network adapter. Alternatively, these drivers can also issue object identifier (OID) query requests of [OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](oid-receive-filter-queue-parameters.md) to obtain these parameters at any time.

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_RECEIVE\_QUEUE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567211)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_RECEIVE\_FILTER\_QUEUE\_PARAMETERS](oid-receive-filter-queue-parameters.md)








