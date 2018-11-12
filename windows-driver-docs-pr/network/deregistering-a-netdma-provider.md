---
title: Deregistering a NetDMA Provider
description: Deregistering a NetDMA Provider
ms.assetid: 4fe5f378-2683-44e7-8056-581783045ad4
keywords:
- NetDMA provider drivers WDK networking , deregistering
- deregistering NetDMA provider drivers
- unegistering NetDMA provider drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deregistering a NetDMA Provider


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




A NetDMA provider driver calls the [**NetDmaDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568328) function to deregister a NetDMA provider that it previously registered by calling the [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336) function. For more information about registering a NetDMA provider, see [Registering a NetDMA Provider](registering-a-netdma-provider.md).

The NetDMA provider driver calls the [**NetDmaProviderStop**](https://msdn.microsoft.com/library/windows/hardware/ff568335) function to notify the NetDMA interface that a previously started NetDMA provider is no longer available. The NetDMA provider driver must call **NetDmaProviderStop** before it deregisters a provider. For more information about stopping a NetDMA provider, see [Stopping a NetDMA Provider](stopping-a-netdma-provider.md).

A NetDMA provider driver typically calls the [**NetDmaDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568328) function in the context of processing the [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) IRP for the NetDMA provider.

 

 





