---
title: NDIS I/O Work Items
description: NDIS I/O Work Items
keywords:
- I/O work items WDK NDIS
- I/O WDK kernel , NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS I/O Work Items





Drivers can queue I/O work item callback functions for later execution. NDIS calls the driver-specified callback function at IRQL = PASSIVE\_LEVEL. This improves system performance by allowing the current function to return immediately and the driver to do work later at a lower IRQL.

NDIS 6.0 and later provide wrapper functions for the kernel I/O work item routines [**IoAllocateWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateworkitem), [**IoFreeWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeworkitem), and [**IoQueueWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioqueueworkitem). Instead of the private [**IO\_WORKITEM**](../kernel/eprocess.md) structure, NDIS uses the private **NDIS\_IO\_WORKITEM** structure.

NDIS 6.0 drivers call the [**NdisAllocateIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateioworkitem) function to allocate a work item. NDIS miniport drivers pass **NdisAllocateIoWorkItem** the adapter handle that NDIS passed to the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. **NdisAllocateIoWorkItem** gets the device object associated with the handle and passes the device object to the [**IoAllocateWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateworkitem) routine. Filter drivers pass in a filter handle.

**Note**  Protocol drivers cannot use [**NdisAllocateIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateioworkitem) because NDIS does not associate protocol drivers with device objects.

 

NDIS drivers call the [**NdisQueueIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisqueueioworkitem) function to queue work items. NDIS work items use the **CriticalWorkQueue** queue type.

NDIS drivers must call the [**NdisFreeIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreeioworkitem) function to free the resources associated with a work item that [**NdisAllocateIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateioworkitem) allocated.

## Related topics


[System Worker Threads](../kernel/system-worker-threads.md)

 

