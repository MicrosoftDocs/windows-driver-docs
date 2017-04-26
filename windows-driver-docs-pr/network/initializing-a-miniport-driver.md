---
title: Initializing a Miniport Driver
description: Initializing a Miniport Driver
ms.assetid: cda2437c-b292-4d21-b200-89c7b55cd46c
keywords:
- miniport drivers WDK networking , initializing
- initializing miniport drivers
- NDIS miniport drivers WDK , initializing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Initializing a Miniport Driver


## <a href="" id="ddk-initializing-a-miniport-driver-ng"></a>


When a networking device becomes available, the system loads the NDIS miniport driver to manage the device (if the driver is not already loaded). Every miniport driver must provide a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818) function. The system calls **DriverEntry** after it loads the driver. **DriverEntry** registers the miniport driver's characteristics with NDIS (including the supported NDIS version and the driver entry points).

The system passes two arguments to [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818):

-   A pointer to the driver object, which was created by the I/O system.

-   A pointer to the registry path, which specifies where driver-specific parameters are stored.

In [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818), miniport drivers pass both of these pointers in a call to the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function. Miniport drivers export a set of standard *MiniportXxx* functions by storing their entry points in an [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure and passing that structure to **NdisMRegisterMiniportDriver**.

A miniport driver also performs any other driver-specific initialization that it requires in [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818). The driver performs adapter-specific initialization in the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function. For more information about adapter initialization, see [Initializing an Adapter](initializing-a-miniport-adapter.md).

To allow a miniport driver to configure optional services, NDIS calls the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function within the context of the miniport driver's call to [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654). For more information about optional services, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

The miniport driver must eventually call [**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578) to release resources that it allocated by calling [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654). If the driver initialization fails after the call to **NdisMRegisterMiniportDriver** succeeded, the driver can call **NdisMDeregisterMiniportDriver** from within [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548818). Otherwise, the miniport driver must release the driver-specific resources that it allocates in it's [*MiniportDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff559378) function. For more information, see [Unloading a Miniport Driver](unloading-a-miniport-driver.md).

 

 





