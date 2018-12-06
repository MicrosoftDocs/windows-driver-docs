---
title: NDIS_STATUS_RECEIVE_QUEUE_STATE
description: The NDIS_STATUS_RECEIVE_QUEUE_STATE status indicates to overlying drivers that the queue state of a virtual machine queue (VMQ) receive queue has changed.
ms.assetid: 59b42de9-6aa5-445e-a39a-de2421c945ea
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_RECEIVE_QUEUE_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE


The NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE status indicates to overlying drivers that the queue state of a virtual machine queue (VMQ) receive queue has changed.

Remarks
-------

NDIS 6.20 and later miniport drivers that support the virtual machine queue interface generate this status indication.

The miniport driver supplies an [**NDIS\_RECEIVE\_QUEUE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567214) structure in the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure.

The change to the *DMA Stopped* state is the only queue state change indication that is required. A miniport driver must indicate this state after it receives an [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569789) set request and stops the DMA. In this case, the miniport driver sets the **QueueState** member of the [**NDIS\_RECEIVE\_QUEUE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567214) structure to **NdisReceiveQueueOperationalStateDmaStopped**.

After the miniport driver receives the [OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569789) set request, it must stop DMA to any shared memory that was allocated for the specified queue.

If the miniport driver stopped the DMA for some other reason (for example, it freed the last filter on a queue), the queue should not enter the *DMA Stopped* state. However, the DMA can be stopped in the *Paused* or *Running* states if there are no filters set on the queue.

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RECEIVE\_QUEUE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567214)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569789)

 

 




