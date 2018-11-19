---
title: Initializing a NetDMA Provider Driver
description: Initializing a NetDMA Provider Driver
ms.assetid: d267b450-0e96-44d5-b034-455bdc4c9f8c
keywords:
- NetDMA provider drivers WDK networking , initializing
- initializing NetDMA provider drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a NetDMA Provider Driver


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




When a NetDMA device becomes available, the Plug and Play (PnP) manager loads the NetDMA provider driver to manage the dynamic memory access (DMA) engine (if the driver is not already loaded). The PnP manager then calls the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine (which every driver must provide) after it loads the driver.

In **DriverEntry**, the NetDMA provider driver sets standard driver entry points. The driver must provide the entry points for the [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) and [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routines in the [**DRIVER\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff544174) structure. The driver must also set entry points for the IRP\_MJ\_*Xxx* requests that the driver handles. For more information about supporting I/O request packets (IRPs), see [Writing Dispatch Routines](https://msdn.microsoft.com/library/windows/hardware/ff566407).

**Note**  A NetDMA provider driver also sets entry points that are specific to NetDMA providers. For more information about registering NetDMA provider entry points, see [Registering a NetDMA Provider](registering-a-netdma-provider.md).

 

The PnP manager passes two arguments to **DriverEntry**:

-   A pointer to a driver object that the I/O system created.

-   A pointer to a registry path that specifies where driver-specific parameters are stored.

The system calls the NetDMA provider driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine to add a functional device object (FDO) for a DMA engine. For more information about adding a DMA engine, see [Registering a NetDMA Provider](registering-a-netdma-provider.md).

The following IRPs are important for NetDMA provider drivers:

<a href="" id="irp-mn-start-device"></a>[**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)  
While handling this IRP, the NetDMA provider driver initializes the DMA hardware. For more information about handling this start IRP, see [Starting a NetDMA Provider](starting-a-netdma-provider.md).

<a href="" id="irp-mn-stop-device"></a>[**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755)  
While handling this IRP, the NetDMA provider driver stops the DMA hardware to allow a hardware reconfiguration. For more information about handling this stop IRP, see [Stopping a NetDMA Provider](stopping-a-netdma-provider.md).

<a href="" id="irp-mn-remove-device"></a>[**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738)  
While handling this IRP, the NetDMA provider driver deregisters a provider. For more information about deregistering a NetDMA provider, see [Deregistering a NetDMA Provider](deregistering-a-netdma-provider.md).

<a href="" id="--------irp-mn-filter-resource-requirements"></a>[**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874)  
If the DMA engine supports MSI-X, the NetDMA provider driver must set the DMA engine's CPU affinities for interrupts. For more information about setting the interrupt CPU affinities for MSI-X, see [Managing NetDMA Interrupts](managing-netdma-interrupts.md).

The PnP manager calls the NetDMA provider driver's [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine after all of the devices that the driver manages have been removed. For more information about unloading a NetDMA provider driver, see [Unloading a NetDMA Provider Driver](unloading-a-netdma-provider-driver.md).

 

 





