---
title: Initializing a Miniport Adapter
description: Initializing a Miniport Adapter
ms.assetid: 6d7a23dc-cc09-46d3-89d3-34e8e8f17a51
keywords:
- miniport adapters WDK networking , initializing
- adatpers WDK networking , initializing
- initializing miniport adapters
- Initializing state WDK networking
- MiniportInitializeEx
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a Miniport Adapter





When a networking device becomes available, the system loads the required NDIS miniport driver, if it is not already loaded. Subsequently, the Plug and Play (PnP) manager sends NDIS a Plug and Play IRP to start the device. NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function to initialize an adapter for network I/O operations. NDIS can call *MiniportInitializeEx* at any time after the driver is initialized. For more information about miniport driver initialization, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

Until [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) returns, NDIS submits no requests for the adapter being initialized. The adapter is in the Initializing state.

A miniport driver typically performs the following tasks in [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389):

1.  Obtains configuration information for the adapter.

2.  Obtains information about the hardware resources for the adapter.

3.  Calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) and provides the following attributes that are associated with the adapter:
    -   A pointer to a driver-allocated context area.
    -   Appropriate attributes flags.
    -   The time-out interval for calling its [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) function.
    -   The interface type.

4.  Initializes adapter-specific resources.

The miniport driver specifies the adapter attributes in the [**NDIS\_MINIPORT\_ADAPTER\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565920) structure that [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) passes to [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

Typically, [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) allocates adapter-specific resources in the following order:

1.  Nonpaged pool memory.

2.  [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) and [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) pools (see [Miniport Driver Send and Receive Operations](miniport-driver-send-and-receive-operations.md)).

3.  Spin locks.

4.  Timers.

5.  IO ports.

6.  DMA (see [Scatter/Gather DMA](scatter-gather-dma2.md)).

7.  Shared memory.

8.  Interrupts (see [Managing Interrupts](managing-interrupts.md)).

After [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) returns successfully, the adapter is in the Paused state. NDIS can call the [**MiniportRestart**](https://msdn.microsoft.com/library/windows/hardware/ff559435) function to transition the adapter to the Running state. For more information, see [Starting a Miniport Adapter](starting-an-adapter.md).

If [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) returns NDIS\_STATUS\_SUCCESS, the driver should release all the resources for the adapter in the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function. For more information, see [Halting a Miniport Adapter](halting-a-miniport-adapter.md).

If [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) failed, *MiniportInitializeEx* must release all resources that it allocated before it returns and the adapter returns to the Halted state.

## Related topics


[Halting a Miniport Adapter](halting-a-miniport-adapter.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Miniport Driver Send and Receive Operations](miniport-driver-send-and-receive-operations.md)

[Scatter/Gather DMA](scatter-gather-dma2.md)

[Starting a Miniport Adapter](starting-an-adapter.md)

 

 






