---
title: NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE
author: windows-driver-content
description: The NDIS\_STATUS\_RECEIVE\_QUEUE\_STATE status indicates to overlying drivers that the queue state of a virtual machine queue (VMQ) receive queue has changed.
ms.assetid: 59b42de9-6aa5-445e-a39a-de2421c945ea
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_RECEIVE_QUEUE_STATE Network Drivers Starting with Windows Vista
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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RECEIVE\_QUEUE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567214)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_RECEIVE\_FILTER\_FREE\_QUEUE](https://msdn.microsoft.com/library/windows/hardware/ff569789)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_RECEIVE_QUEUE_STATE%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


