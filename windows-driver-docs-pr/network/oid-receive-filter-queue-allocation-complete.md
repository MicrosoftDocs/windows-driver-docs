---
title: OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE
author: windows-driver-content
description: NDIS protocol drivers issue object identifier (OID) method requests of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE to notify the miniport driver that an allocation has completed for the current batch of receive queues.
ms.assetid: d09fcab5-4c3b-432a-ba9e-fd4269537de6
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE Network Drivers Starting with Windows Vista
---

# OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE


NDIS protocol drivers issue object identifier (OID) method requests of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE to notify the miniport driver that an allocation has completed for the current batch of receive queues.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567195) structure that is followed by an [**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567197) structure for each queue. After a successful return from the OID method request, the **InformationBuffer** member of the **NDIS\_OID\_REQUEST** structure contains a pointer to the same array of structures, and the **CompletionStatus** member of each **NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_PARAMETERS** structure contains the completion status for each queue.

Remarks
-------

The OID method request of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE is optional for NDIS 6.20 and later miniport drivers. It is mandatory for miniport drivers that support the virtual machine queue (VMQ) interface.

After allocating one or more receive queues and optionally setting the initial filters, the protocol driver must issue the OID method request of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE in order to notify the miniport driver that the allocation has completed for the current batch of receive queues. This allows the miniport driver to balance the hardware resources among multiple receive queues; if necessary, it can allocate resources such as shared memory for the receive queues.

After a miniport driver receives an OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE request and it has filters that are set on the queue, the queue is in the Running state. In this state, the miniport driver can start indications of packets in the queue by calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598).

### Return Status Codes

The miniport driver returns one of the following status codes for the OID method request of OID\_RECEIVE\_FILTER\_QUEUE\_ALLOCATION\_COMPLETE.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>NDIS_STATUS_SUCCESS</strong></p></td>
<td><p>The queue allocation has completed. The information buffer contains the updated [<strong>NDIS_RECEIVE_QUEUE_ALLOCATION_COMPLETE_ARRAY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567195) structure and parameter structures with the completion status for the queue allocation.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_PENDING</strong></p></td>
<td><p>The request is pending completion. The final status code and results will be passed to the OID request completion handler of the caller.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_INVALID_PARAMETER</strong></p></td>
<td><p>One or more of the parameters that the overlying driver provided were not valid.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_INVALID_LENGTH</strong></p></td>
<td><p>The information buffer was too short. NDIS set the <strong>DATA</strong>.<strong>METHOD_INFORMATION</strong>.<strong>BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p><strong>NDIS_STATUS_NOT_SUPPORTED</strong></p></td>
<td><p>The NDIS version of the miniport driver is earlier than version 6.20.</p></td>
</tr>
<tr class="even">
<td><p><strong>NDIS_STATUS_FAILURE</strong></p></td>
<td><p>The request failed for other reasons.</p></td>
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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff567195)

[**NDIS\_RECEIVE\_QUEUE\_ALLOCATION\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567197)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_RECEIVE_FILTER_QUEUE_ALLOCATION_COMPLETE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


