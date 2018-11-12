---
title: Porting Miniport Driver Unload Operations to NDIS 6.0
description: Porting Miniport Driver Unload Operations to NDIS 6.0
ms.assetid: c51c9d4c-3713-483d-8b07-7ae739d931d4
keywords:
- miniport drivers WDK networking , unloading
- NDIS miniport drivers WDK , unloading
- porting miniport drivers WDK networking , unload operations
- unloading miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Unload Operations to NDIS 6.0





For NDIS 6.0, miniport drivers must specify a [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function entry point in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure. NDIS 6.0 drivers do not call the [**NdisMRegisterUnloadHandler**](https://msdn.microsoft.com/library/windows/hardware/ff553606) function.

In *MiniportDriverUnload*, a miniport driver must call the [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) function to deregister the miniport driver. The driver passes **NdisMDeregisterMiniportDriver** the handle that it obtained at *NdisMiniportDriverHandle* when it called the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function.

For more information about unloading an NDIS 6.0 miniport driver, see [Unloading a Miniport Driver](unloading-a-miniport-driver.md).

 

 





