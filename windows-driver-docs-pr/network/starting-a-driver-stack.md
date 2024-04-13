---
title: Starting a Driver Stack
description: Starting a Driver Stack
keywords:
- driver stacks WDK networking , starting
- starting driver stacks WDK networking
ms.date: 04/20/2017
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

    To initialize the miniport adapter, NDIS calls the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. If *MiniportInitializeEx* is successful, the miniport adapter enters the Paused state.

4.  NDIS attaches the filter modules, beginning with the module that is closest to the miniport driver and progressing to the top of the driver stack.

    To request the driver to attach a filter module to the driver stack, NDIS calls a filter driver's [*FilterAttach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_attach) function. If each attach operation is successful, the filter module enters the Paused state.

5.  After all the underlying drivers are in the Paused state, NDIS calls the protocol driver's [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function.

    Then the protocol driver binding enters the Opening state. The protocol driver calls the [**NdisOpenAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenadapterex) function to open the binding with the miniport adapter.

6.  NDIS allocates the necessary resources for the binding and calls the protocol driver's [*ProtocolOpenAdapterCompleteEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_open_adapter_complete_ex) function.

    The binding enters the Paused state.

7.  To complete the bind operation, the protocol driver calls the [**NdisCompleteBindAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscompletebindadapterex) function.

8.  NDIS restarts the driver stack. For more information about restarting the driver stack, see [Restarting a Driver Stack](restarting-a-driver-stack.md).

 

