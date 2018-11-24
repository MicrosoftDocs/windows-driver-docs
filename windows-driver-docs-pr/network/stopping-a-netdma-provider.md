---
title: Stopping a NetDMA Provider
description: Stopping a NetDMA Provider
ms.assetid: efa83c49-bdec-438d-a2de-e7f13f2466b9
keywords:
- NetDMA provider drivers WDK networking , stopping
- stopping NetDMA provider drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stopping a NetDMA Provider


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




A NetDMA provider driver calls the [**NetDmaProviderStop**](https://msdn.microsoft.com/library/windows/hardware/ff568335) function to notify the NetDMA interface that a dynamic memory access (DMA)- engine, which was started by calling the [**NetDmaProviderStart**](https://msdn.microsoft.com/library/windows/hardware/ff568334) function, is no longer available. For more information about starting a NetDMA provider, see [Starting a NetDMA Provider](starting-a-netdma-provider.md).

DMA provider drivers typically call **NetDmaProviderStop** while handling the [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) or [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) IRP.

The NetDMA provider driver must call **NetDmaProviderStop** before it deregisters a NetDMA provider. For more information about deregistering a NetDMA provider, see [Deregistering a NetDMA Provider](deregistering-a-netdma-provider.md).

A NetDMA provider driver can call [**NetDmaProviderStop**](https://msdn.microsoft.com/library/windows/hardware/ff568335) and [**NetDmaProviderStart**](https://msdn.microsoft.com/library/windows/hardware/ff568334) as many times as the application requires after the driver registers the NetDMA provider and before it deregisters the NetDMA provider. If the DMA engine is being restarted after it calls **NetDmaProviderStop**, the NetDMA provider driver can specify new attributes in the [**NET\_DMA\_PROVIDER\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff568737) structure in the *ProviderAttributes* parameter of **NetDmaProviderStart**.

The NetDMA interface waits for outstanding DMA operations to complete and frees all of the allocated DMA channels before it returns from the **NetDmaProviderStop** function. For more information about freeing DMA channels, see [Freeing a NetDMA Channel](freeing-a-netdma-channel.md).

 

 





