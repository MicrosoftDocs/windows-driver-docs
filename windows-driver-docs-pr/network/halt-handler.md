---
title: Miniport Driver Halt Handler
description: Miniport Driver Halt Handler
keywords:
- MiniportHaltEx
- halt handler WDK NDIS
- unloading miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Driver Halt Handler





An NDIS miniport driver must supply a [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function to [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver).

*MiniportHaltEx* should undo everything that [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) did. For example, the NDIS miniport driver might:

-   Free ports. (For more information, see [Freeing an NDIS Port](freeing-an-ndis-port.md).)

-   Release all of the hardware resources that [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) claimed.

-   Free interrupt resources by calling [**NdisMDeregisterInterruptEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex).

-   Free any memory that [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) allocated.

-   Stop the NIC, unless the [*MiniportShutdownEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_shutdown) function has already restored the NIC to its initial state.

The following diagram illustrates unloading a miniport driver.

![diagram illustrating unloading a miniport driver.](images/207-11.png)

*MiniportHaltEx* should complete the operations that are necessary to unload the driver before returning. If the miniport driver has any outstanding receive indications (that is, received network data that it has indicated up to NDIS but which NDIS has not yet returned), *MiniportHaltEx* must not return until such data is returned to the miniport driver's [*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) function.

The preceding figure shows a set of calls that could be made by a *MiniportHaltEx* function. These calls are only a subset of the calls that could be made. The actual set of calls depends on previous actions of the miniport driver. The miniport driver can make these same calls in *MiniportInitializeEx* if it cannot successfully initialize the network adapter because of hardware problems or because it cannot acquire a resource that it needs. In such a case, *MiniportInitializeEx* should unload the driver by undoing its previous actions. Otherwise, *MiniportHaltEx* will undo the actions of *MiniportInitializeEx*.

The following list describes the calls that are required to reverse certain actions that the miniport driver might take:

-   If the miniport driver registered an interrupt, it should call [**NdisMDeregisterInterruptEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex).

-   If the miniport driver set up a timer or timers, it should call [**NdisCancelTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscanceltimerobject) for each timer that it created. If a call to **NdisCancelTimerObject** fails, the timer might have already fired. In this case, the miniport driver should wait for the timer handler to complete before returning from *MiniportHaltEx*.

-   If the miniport driver allocated any memory with [**NdisAllocateMemoryWithTagPriority**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatememorywithtagpriority), it should call [**NdisFreeMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreememory) to free that memory.

-   If the miniport driver allocated any memory with [**NdisMAllocateSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocatesharedmemory), or [**NdisMAllocateSharedMemoryAsyncEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocatesharedmemoryasyncex), it should call [**NdisMFreeSharedMemory**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreesharedmemory) to free that memory.

-   If the miniport driver allocated and initialized storage for a pool of packet descriptors with [**NdisAllocateNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisallocatenetbufferlistpool), it should call [**NdisFreeNetBufferPool**](/windows-hardware/drivers/ddi/nblapi/nf-nblapi-ndisfreenetbufferpool) to free that storage.

-   If the miniport driver allocated or reserved any hardware resources, these should be returned. For example, if the miniport driver mapped an I/O port range on a NIC, it should release the ports by calling [**NdisMDeregisterIoPortRange**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterioportrange).

## Related topics


[Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)

[Freeing an NDIS Port](freeing-an-ndis-port.md)

[Halting a Miniport Adapter](halting-a-miniport-adapter.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Miniport Driver Reset and Halt Functions](/previous-versions/windows/hardware/network/ff564064(v=vs.85))

 

