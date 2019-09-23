---
title: NDIS I/O Work Items
description: NDIS I/O Work Items
ms.assetid: 4f966ff3-2092-495f-863f-50f079085fa6
keywords:
- I/O work items WDK NDIS
- I/O WDK kernel , NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS I/O Work Items





Drivers can queue I/O work item callback functions for later execution. NDIS calls the driver-specified callback function at IRQL = PASSIVE\_LEVEL. This improves system performance by allowing the current function to return immediately and the driver to do work later at a lower IRQL.

NDIS 6.0 and later provide wrapper functions for the kernel I/O work item routines [**IoAllocateWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioallocateworkitem), [**IoFreeWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iofreeworkitem), and [**IoQueueWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioqueueworkitem). Instead of the private [**IO\_WORKITEM**](https://docs.microsoft.com/windows-hardware/drivers/kernel/eprocess) structure, NDIS uses the private **NDIS\_IO\_WORKITEM** structure.

NDIS 6.0 drivers call the [**NdisAllocateIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocateioworkitem) function to allocate a work item. NDIS miniport drivers pass **NdisAllocateIoWorkItem** the adapter handle that NDIS passed to the [*MiniportInitializeEx*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_initialize) function. **NdisAllocateIoWorkItem** gets the device object associated with the handle and passes the device object to the [**IoAllocateWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioallocateworkitem) routine. Filter drivers pass in a filter handle.

**Note**  Protocol drivers cannot use [**NdisAllocateIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocateioworkitem) because NDIS does not associate protocol drivers with device objects.

 

NDIS drivers call the [**NdisQueueIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisqueueioworkitem) function to queue work items. NDIS work items use the **CriticalWorkQueue** queue type.

NDIS drivers must call the [**NdisFreeIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfreeioworkitem) function to free the resources associated with a work item that [**NdisAllocateIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocateioworkitem) allocated.

## Related topics


[System Worker Threads](https://docs.microsoft.com/windows-hardware/drivers/kernel/system-worker-threads)

 

 






