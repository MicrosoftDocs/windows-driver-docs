---
title: Stopping a Driver Stack
description: Stopping a Driver Stack
ms.assetid: 2ecc0ebb-89d8-4cd8-ac1c-f9f1da7d2ca8
keywords:
- driver stacks WDK networking , stopping
- stopping driver stacks WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stopping a Driver Stack





If a device is removed, NDIS stops a driver stack. A driver stack stop operation proceeds as follows:

1.  NDIS pauses the driver stack. For more information about pausing the driver stack, see [Pausing a Driver Stack](pausing-a-driver-stack.md).

2.  NDIS calls the protocol driver's [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function.

    The binding enters the Closing state. After outstanding OID and send requests are complete and all receive data is returned, the binding enters the Unbound state.

3.  NDIS detaches all the filter modules, beginning from the top of the stack and progressing down to the miniport driver.

    After NDIS calls a filter driver's [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function and the filter driver releases all the resources for a filter module, the filter module is in the Detached state.

4.  NDIS halts the miniport adapter.

    After NDIS calls the miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function, the miniport driver releases all the resources for the miniport adapter and the miniport adapter is in the Halted state.

5.  If all of a filter driver's modules are detached, the system can unload the filter driver.

6.  If all the miniport adapters that a miniport driver manages are halted, the system can unload the miniport driver.

 

 





