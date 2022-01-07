---
title: Unloading a Miniport Driver
description: Unloading a Miniport Driver
keywords:
- miniport drivers WDK networking , unloading
- NDIS miniport drivers WDK , unloading
- unloading miniport drivers
ms.date: 04/20/2017
---

# Unloading a Miniport Driver





The driver object that is associated with an NDIS miniport driver specifies an [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine. The system calls the *Unload* routine when all the devices that the driver services have been removed. NDIS provides the *Unload* routine for miniport drivers. NDIS calls a miniport driver's [*MiniportDriverUnload*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_unload) function from the *Unload* routine.

A miniport driver must call [**NdisMDeregisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterminiportdriver) from *MiniportDriverUnload*.

A miniport driver's *MiniportDriverUnload* function should also release any driver-specific resources. The system will complete a driver unload operation after *MiniportDriverUnload* returns.

The functionality of the *MiniportDriverUnload* function is driver-specific. As a general rule, *MiniportDriverUnload* should undo the operations that were performed during driver initialization. For more information about driver initialization, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

 

