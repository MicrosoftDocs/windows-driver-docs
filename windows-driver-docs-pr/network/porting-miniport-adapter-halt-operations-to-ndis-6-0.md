---
title: Porting Miniport Adapter Halt Operations to NDIS 6.0
description: Porting Miniport Adapter Halt Operations to NDIS 6.0
ms.assetid: 0d107941-5f70-41d3-a4ab-c3f496c31087
keywords:
- miniport adapters WDK networking , halt operations
- adapters WDK networking , halt operations
- porting miniport drivers WDK networking , adapters
- halting adapters
- stopping adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Adapter Halt Operations to NDIS 6.0





In NDIS 6.0 and later, the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function replaces the NDIS 5.x [*MiniportHalt*](https://msdn.microsoft.com/library/windows/hardware/ff549451) function. *MiniportHaltEx* has a *HaltAction* parameter in addition to the *MiniportAdapterContext* parameter. The *HaltAction* parameter specifies the reason for halting the miniport adapter.

For more information about halting an adapter, see [Halting a Miniport Adapter](halting-a-miniport-adapter.md).

## Related topics


[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

 

 






