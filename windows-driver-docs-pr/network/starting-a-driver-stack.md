---
title: Starting a Driver Stack
description: Starting a Driver Stack
ms.assetid: 316de69e-38e8-4ac6-83c5-5d13090ee6d5
keywords:
- driver stacks WDK networking , starting
- starting driver stacks WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting a Driver Stack





After the system detects a networking device, the system starts an NDIS driver stack for the device. The device can be a virtual device or a physical device. In either case, a driver stack start operation proceeds as follows:

1.  The system loads and initializes the drivers if they are not already loaded.

    It does not load the drivers in any particular order.

2.  The system calls each driver's **DriverEntry** function.

    After **DriverEntry** returns:

    -   The miniport adapter for the device is in the Halted state.
    -   The filter modules are in the Detached state.
    -   The protocol binding is in the Unbound state.

3.  The system requests NDIS to start the miniport adapter.

    To initialize the miniport adapter, NDIS calls the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. If *MiniportInitializeEx* is successful, the miniport adapter enters the Paused state.

4.  NDIS attaches the filter modules, beginning with the module that is closest to the miniport driver and progressing to the top of the driver stack.

    To request the driver to attach a filter module to the driver stack, NDIS calls a filter driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function. If each attach operation is successful, the filter module enters the Paused state.

5.  After all the underlying drivers are in the Paused state, NDIS calls the protocol driver's [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.

    Then the protocol driver binding enters the Opening state. The protocol driver calls the [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) function to open the binding with the miniport adapter.

6.  NDIS allocates the necessary resources for the binding and calls the protocol driver's [*ProtocolOpenAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570265) function.

    The binding enters the Paused state.

7.  To complete the bind operation, the protocol driver calls the [**NdisCompleteBindAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561702) function.

8.  NDIS restarts the driver stack. For more information about restarting the driver stack, see [Restarting a Driver Stack](restarting-a-driver-stack.md).

 

 





