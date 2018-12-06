---
title: Porting Miniport Adapter Shutdown Operations to NDIS 6.0
description: Porting Miniport Adapter Shutdown Operations to NDIS 6.0
ms.assetid: cdf4f829-347e-4d81-9ac0-6d886cef6035
keywords:
- shutdown WDK networking
- porting miniport drivers WDK networking , shutdown operations
- adapters WDK networking , shutdown operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Adapter Shutdown Operations to NDIS 6.0





The NDIS 6.0 or later miniport driver's shutdown function, [*MiniportShutdownEx*](https://msdn.microsoft.com/library/windows/hardware/ff559449), differs from the NDIS 5.x [**MiniportShutdown**](https://msdn.microsoft.com/library/windows/hardware/ff550533) function in that it receives a *ShutdownAction* parameter in addition to the *MiniportAdapterContext* parameter. The *ShutdownAction* parameter specifies the reason for shutting down the miniport driver.

For more information about shutdown operations, see [Miniport Adapter Shutdown](miniport-adapter-shutdown.md).

## Related topics


[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

 

 






