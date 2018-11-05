---
title: Unloading a Miniport Driver
description: Unloading a Miniport Driver
ms.assetid: c5199a0f-31c3-42e4-8758-cbe480dff682
keywords:
- miniport drivers WDK networking , unloading
- NDIS miniport drivers WDK , unloading
- unloading miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unloading a Miniport Driver





The driver object that is associated with an NDIS miniport driver specifies an [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine. The system calls the *Unload* routine when all the devices that the driver services have been removed. NDIS provides the *Unload* routine for miniport drivers. NDIS calls a miniport driver's [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function from the *Unload* routine.

A miniport driver must call [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) from *MiniportDriverUnload*.

A miniport driver's *MiniportDriverUnload* function should also release any driver-specific resources. The system will complete a driver unload operation after *MiniportDriverUnload* returns.

The functionality of the *MiniportDriverUnload* function is driver-specific. As a general rule, *MiniportDriverUnload* should undo the operations that were performed during driver initialization. For more information about driver initialization, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

 

 





