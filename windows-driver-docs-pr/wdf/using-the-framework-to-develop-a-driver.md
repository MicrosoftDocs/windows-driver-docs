---
title: Using WDF to Develop a Driver
description: This topic provides a high-level overview of the framework objects you'll use to develop a Kernel-Mode Driver Framework (KMDF) driver.
ms.assetid: 421b7eb8-11d3-4a37-8ae8-e2d3d216c9c7
keywords:
- kernel-mode drivers WDK KMDF , development steps
- KMDF WDK , development steps
- Kernel-Mode Driver Framework WDK , development steps
- framework-based drivers WDK KMDF , development steps
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using WDF to Develop a Driver


This topic provides a high-level overview of the framework objects you'll use to develop a Kernel-Mode Driver Framework (KMDF) driver. Except where indicated, you'll use the same objects to develop a User-Mode Driver Framework (UMDF) driver starting in UMDF version 2.

Windows Driver Frameworks (WDF) drivers consist of a [**DriverEntry routine**](https://msdn.microsoft.com/library/windows/hardware/ff540807) and a set of event callback functions that are defined by the [Windows Driver Framework objects](wdf-objects.md) that framework-based drivers use. The callback functions call object methods that the framework exports. The Windows Driver Kit (WDK) contains sample WDF drivers that demonstrate how to implement a driver's event callback functions. You can download these samples from the [Windows Dev Center - Hardware](http://go.microsoft.com/fwlink/p/?linkid=256387). For information about what samples are available, see [Sample KMDF Drivers](sample-kmdf-drivers.md) and [Sample UMDF Drivers](sample-umdf-drivers.md).

When you create a WDF driver, you will typically do the following:

-   Use a *framework driver object* to represent your driver.

    The driver's [**DriverEntry routine**](https://msdn.microsoft.com/library/windows/hardware/ff540807) must call [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) to create a framework driver object that represents the driver. The **WdfDriverCreate** method also registers the driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, which the framework calls each time that the Plug and Play (PnP) manager reports the existence of a device that the driver supports.

-   Use *framework device objects* to support PnP and power management in your driver.

    All drivers must call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a framework device object for each device that a driver supports. A device can be a piece of hardware that is plugged into the computer, or it can be a software-only device. Framework device objects support PnP and power management operations, and drivers can register event callback functions that notify the driver when a device enters or leaves its working state.

    For more information about framework device objects, see [Supporting PnP and Power Management in Your Driver](supporting-pnp-and-power-management-in-your-driver.md).

-   Use *framework queue objects* and *framework request objects* to support I/O operations in your driver.

    All drivers that receive read, write, or device I/O control requests from applications or other drivers must call [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create framework queue objects that represent I/O queues. Typically, drivers register one or more [request handlers](request-handlers.md) for each I/O queue. When the I/O manager sends an I/O request to the driver, the framework creates a framework request object for the request, places the request object in an I/O queue, and calls one of the driver's request handlers to inform the driver that a request is available. The driver obtains the I/O request and can requeue, complete, cancel, or forward the request.

    For more information about using the framework's queue objects and request objects, see [Framework Queue Objects](framework-queue-objects.md) and [Framework Request Objects](framework-request-objects.md).

-   Use *framework interrupt objects* to handle device interrupts.

    Drivers that handle device interrupts must call [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) to create a framework interrupt object for each interrupt and to register callback functions. These callback functions enable and disable the interrupt and serve as the interrupt service routine (ISR) and deferred procedure call (DPC) for the interrupt.

    For more information about framework interrupt objects, see [Handling Hardware Interrupts](handling-hardware-interrupts.md).

-   KMDF drivers can use the framework's *DMA enabler objects* and *DMA transaction objects* to handle a device's direct memory access (DMA) operations.

    If your KMDF driver's device supports DMA operations, the driver should call [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983) to create a DMA enabler object and [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) to create one or more DMA transaction objects. The DMA transaction object defines an [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) callback function that programs device hardware to perform a DMA operation.

    For more information about supporting DMA operations, see [Handling DMA Operations in Framework-based Drivers](handling-dma-operations-in-kmdf-drivers.md).

-   Use the framework's *I/O target objects* to send I/O requests to other drivers.

    To pass I/O requests to other drivers (typically the next lower driver in the driver stack), your driver sends the request to a I/O target object.

    For more information about I/O target objects, see [Using I/O Targets](using-i-o-targets.md).

-   A KMDF driver can use the framework's *WMI provider objects* and *WMI instance objects* to support Windows Management Instrumentation (WMI) capabilities.

    Most KMDF drivers should support WMI and should call [**WdfWmiInstanceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551178) to register callback functions that send or receive WMI data.

    For more information about WMI, see [Supporting WMI in Framework-based Drivers](supporting-wmi-in-kmdf-drivers.md).

-   Use the framework's synchronization capabilities.

    All drivers must be aware of multiprocessor synchronization issues and should use [synchronization techniques](synchronization-techniques-for-wdf-drivers.md) that the framework provides.

-   Use additional objects and features that the framework provides.

    The framework provides additional objects that your driver can use. For more information about these objects, see [WDF Support Objects](wdf-support-objects.md).

 

 





