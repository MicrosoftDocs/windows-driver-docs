---
title: Halting a Miniport Adapter
description: Halting a Miniport Adapter
ms.assetid: fd57a2b1-593d-412b-96b5-eabd3ea392e0
keywords:
- miniport adapters WDK networking , halting
- adapters WDK networking , halting
- Halted state WDK networking
- MiniportHaltEx
- halting adapters
- stopping adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Halting a Miniport Adapter





NDIS calls an NDIS miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function to deallocate resources when an adapter is removed from the system, and to stop the hardware. NDIS can call *MiniportHaltEx* after the driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function returns successfully. For more information about *MiniportInitializeEx*, see [Initializing a Miniport Adapter](initializing-a-miniport-adapter.md).

[*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) must free any resources that the driver allocated for a device. The driver must call the reciprocals of the **Ndis*Xxx*** functions with which it originally allocated the resources. As a general rule, a *MiniportHaltEx* function should call the reciprocal **Ndis*Xxx*** functions in the reverse order used during initialization.

If an adapter generates interrupts, a miniport driver's [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function can be preempted by the driver's [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395) function until *MiniportHaltEx* disables interrupts.

NDIS does not call [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) if there are outstanding OID requests or send requests. NDIS submits no further requests for the affected device after NDIS calls *MiniportHaltEx*.

After [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) returns, the miniport driver is in the Halted state.

## Related topics


[Adapter States of a Miniport Driver](adapter-states-of-a-miniport-driver.md)

[Miniport Adapter States and Operations](miniport-adapter-states-and-operations.md)

[Miniport Driver Halt Handler](halt-handler.md)

[Writing NDIS Miniport Drivers](writing-ndis-miniport-drivers.md)

 

 






