---
title: Registering a NetDMA Provider
description: Registering a NetDMA Provider
ms.assetid: 63f60ed9-4a35-4c70-89f5-9bdfb7b9e732
keywords:
- NetDMA provider drivers WDK networking , registering
- registering NetDMA provider drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a NetDMA Provider


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




After a NetDMA provider driver successfully completes driver initialization and returns from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the Plug and Play (PnP) manager calls the NetDMA provider driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine to add dynamic memory access (DMA) engines. The PnP manager calls **AddDevice** once for each DMA engine that it detected. For more information about the NetDMA provider driver's **DriverEntry** routine, see [Initializing a NetDMA Provider Driver](initializing-a-netdma-provider-driver.md).

The [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine calls the [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) function to create a functional device object (FDO) and inserts the FDO at the top of the device stack. The NetDMA provider driver then calls the [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336) function to register the associated NetDMA provider.

The NetDMA provider driver supplies a [**NET\_DMA\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568738) structure in the *ProviderCharacteristics* parameter of **NetDmaRegisterProvider**. The characteristics structure contains:

-   The driver major and minor version numbers.

-   Entry points for NetDMA service functions, such as [**ProviderAllocateDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570393) and [**ProviderFreeDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570398).

-   The physical device object (PDO) that is associated with the NetDMA provider. The PnP manager supplies a pointer to the PDO in the *PhysicalDeviceObject* parameter of [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521).

-   The maximum number of the DMA channels that the DMA engine can support.

The NetDMA provider driver reports other capabilities of the DMA engine (such as the actual number of DMA channels that are available, maximum address space, and maximum transfer size) while handling the [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) IRP. For more information about handling this start IRP, see [Starting a NetDMA Provider](starting-a-netdma-provider.md).

The NetDMA provider driver provides a pointer to a block of driver-allocated context information in the *ProviderContext* parameter of [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336). This context area stores information about the NetDMA provider. The NetDMA interface passes the context information in subsequent calls to *ProviderXxx* functions that require a NetDMA provider context.

When **NetDmaRegisterProvider** returns, it provides a handle in the location that the *pNetDmaProviderHandle* parameter specifies. The NetDMA interface assigns this handle to identify the NetDMA provider. The NetDMA provider driver then uses this handle in all subsequent calls to *NetDmaXxx* functions that are associated with the NetDMA provider.

If a computer supports MSI-X, the NetDMA interface, while in the context of the [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336) function, can call the NetDMA provider driver's [**ProviderSetDmaChannelCpuAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff570402) function to specify the CPU affinity of the interrupt for each DMA channel. For more information about setting interrupt CPU affinities, see [Setting the NetDMA Interrupt CPU Affinities](setting-the-netdma-interrupt-cpu-affinities.md).

To deregister a NetDMA provider, a NetDMA provider driver calls the [**NetDmaDeregisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568328) function. For more information about deregistering a NetDMA provider, see [Deregistering a NetDMA Provider](deregistering-a-netdma-provider.md).

 

 





