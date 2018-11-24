---
title: Porting Protocol Driver Unload Operations to NDIS 6.0
description: Porting Protocol Driver Unload Operations to NDIS 6.0
ms.assetid: 0726ee66-dabc-49d6-b17a-ec6651855b44
keywords:
- protocol drivers WDK networking , unloading
- NDIS protocol drivers WDK , unloading
- porting protocol drivers WDK networking , unload operations
- unloading protocol drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Driver Unload Operations to NDIS 6.0





In NDIS 6.0, a protocol driver must call the [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) function, in its [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine, to deregister the protocol driver. The driver passes **NdisDeregisterProtocolDriver** the handle that it obtained at *NdisProtocolHandle* when it called the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function.

For NDIS 6.0, the [**ProtocolUnload**](https://msdn.microsoft.com/library/windows/hardware/ff563261) function--which NDIS calls when a protocol driver is uninstalled--is replaced by the [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function. Protocol drivers specify a *ProtocolUninstall* function entry point in the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure.

*ProtocolUninstall* is an optional function. NDIS calls *ProtocolUninstall* in response to a user request to uninstall an intermediate driver. NDIS calls [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) once for each bound adapter, then NDIS calls *ProtocolUninstall*. NDIS calls *ProtocolUninstall* before the system actually unloads the driver. This timing provides a chance to release any device objects or other resources that might otherwise prevent the system from calling the intermediate driver's [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function and unloading the driver.

For more information about unloading an NDIS 6.0 protocol driver, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md).

 

 





