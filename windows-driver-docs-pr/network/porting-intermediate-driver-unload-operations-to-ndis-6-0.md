---
title: Porting Intermediate Driver Unload Operations to NDIS 6.0
description: Porting Intermediate Driver Unload Operations to NDIS 6.0
ms.assetid: 97853aeb-3aab-4012-97ab-7e5f52f03e43
keywords:
- intermediate drivers WDK networking , unloading
- NDIS intermediate drivers WDK , unloading
- porting intermediate drivers WDK networking , unload operations
- unloading intermediate drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Intermediate Driver Unload Operations to NDIS 6.0





For NDIS 6.0, intermediate drivers must specify a [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function entry point in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure. NDIS 6.0 drivers do not call the [**NdisMRegisterUnloadHandler**](https://msdn.microsoft.com/library/windows/hardware/ff553606) function.

For NDIS 6.0, the [**ProtocolUnload**](https://msdn.microsoft.com/library/windows/hardware/ff563261) function, which NDIS calls when an intermediate driver is uninstalled, is replaced by the [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) function. NDIS calls *ProtocolUninstall* when a user requests to uninstall an intermediate driver.

Before calling *ProtocolUninstall*, NDIS calls [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) once for each bound adapter. NDIS then calls *ProtocolUninstall* before the system actually unloads the driver. This timing provides a chance to release any device objects or other resources that might otherwise prevent the system from calling the intermediate driver's *MiniportDriverUnload* function and unloading the driver.

The [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) and [*ProtocolUninstall*](https://msdn.microsoft.com/library/windows/hardware/ff570279) functions are defined in the driver's [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) and [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structures.

Call [**NdisDeregisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561743) and [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) from the *MiniportDriverUnload* function.

For more information about unloading the miniport upper edge of an intermediate driver, see [Porting Miniport Driver Unload Operations to NDIS 6.0](porting-miniport-driver-unload-operations-to-ndis-6-0.md).

For more information about unloading the protocol lower edge of an intermediate driver, see [Porting Protocol Driver Unload Operations to NDIS 6.0](porting-protocol-driver-unload-operations-to-ndis-6-0.md).

For more information about unloading an NDIS 6.0 intermediate driver, see [Unloading an Intermediate Driver](unloading-an-intermediate-driver.md).

 

 





