---
title: Updating the DriverEntry Routine for an NDIS 6.0 Miniport Driver
description: Updating the DriverEntry Routine for an NDIS 6.0 Miniport Driver
ms.assetid: 72a0a702-06f1-499a-8fff-7dcfa04aab32
keywords:
- DriverEntry WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating the DriverEntry Routine for an NDIS 6.0 Miniport Driver





Like NDIS 5.*x*, NDIS 6.0 miniport drivers register with NDIS in the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. In NDIS 6.0, the [**NdisMInitializeWrapper**](https://msdn.microsoft.com/library/windows/hardware/ff553547) and [**NdisMRegisterUnloadHandler**](https://msdn.microsoft.com/library/windows/hardware/ff553606) functions are eliminated, along with the [**NdisMRegisterMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff553602) function. To register the miniport driver with NDIS 6.0, call the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function.

NDIS 6.0 miniport drivers do not call **NdisMRegisterUnloadHandler** to register an unload function. Instead, NDIS 6.0 miniport drivers specify a [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) entry point in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure. Unlike NDIS 5.*x* miniport drivers, NDIS 6.0 miniport drivers must register an unload handler.

Like **NdisMRegisterMiniport**, the input parameters to **NdisMRegisterMiniportDriver** include the driver object, registry path, and the driver characteristics structure. In addition, **NdisMRegisterMiniportDriver** requires a pointer to an NDIS\_HANDLE variable. NDIS provides the handle to identify the driver.

If an error occurs after a successful call to **NdisMRegisterMiniportDriver**, the driver must call the [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) function before **DriverEntry** returns. NDIS 6.0 miniport drivers do not call the [**NdisTerminateWrapper**](https://msdn.microsoft.com/library/windows/hardware/ff554814) function.

If the call to **NdisMRegisterMiniportDriver** succeeds, the miniport driver must later call the **NdisMDeregisterMiniportDriver** function. Call **NdisMDeregisterMiniportDriver** in the context of the miniport driver's [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function.

For more information about NDIS 6.0 driver initialization, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

 

 





