---
title: Unloading a NetDMA Provider Driver
description: Unloading a NetDMA Provider Driver
ms.assetid: 2c7a0cbd-0a88-4e10-8eba-0b7e6e42c4fc
keywords:
- NetDMA provider drivers WDK networking , unloading
- unloading NetDMA provider drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unloading a NetDMA Provider Driver


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The Plug and Play (PnP) manager calls a NetDMA provider driver's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine after all of the dynamic memory access (DMA) engines that the driver manages have been removed. For more information about removing DMA engines, see [Deregistering a NetDMA Provider](deregistering-a-netdma-provider.md).

In [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886), the NetDMA provider driver releases any resources that it allocated in its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. For more information about the NetDMA provider driver's **DriverEntry** routine, see [Initializing a NetDMA Provider Driver](initializing-a-netdma-provider-driver.md).

 

 





