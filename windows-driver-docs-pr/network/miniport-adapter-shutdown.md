---
title: Miniport Adapter Shutdown
description: Miniport Adapter Shutdown
ms.assetid: 57d964f1-03c7-4b54-9d04-1d187c96e052
keywords:
- miniport adapters WDK networking , shutdown
- adapters WDK networking , shutdown
- MiniportShutdownEx
- miniport drivers WDK networking , system shutdown
- NDIS miniport drivers WDK , system shutdown
- shutdown WDK networking
- system shutdown WDK network
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Adapter Shutdown





An NDIS miniport driver must register a [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) function during miniport driver initialization.

NDIS calls an NDIS miniport driver's [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) function when the system is shutting down. *MiniportShutdownEx* restores the hardware to a known state.

The *ShutdownAction* parameter that NDIS passed to [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) informs the miniport driver of the reason for the shutdown.

The shutdown handler can be called as a result of a user operation, in which case it runs at IRQL = PASSIVE\_LEVEL. It can also be called as a result of an unrecoverable system error, in which case it can be running at any IRQL.

[*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) should call no **Ndis*Xxx*** functions. The miniport driver can call functions for reading and writing I/O ports or disabling the DMA engine to return the hardware to a known state.

Unlike [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388), [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449) should not release any allocated resources. *MiniportShutdownEx* should just stop the NIC.

## Related topics


[Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)

[Halting a Miniport Adapter](halting-a-miniport-adapter.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Writing NDIS Miniport Drivers](writing-ndis-miniport-drivers.md)

 

 






