---
title: Writing a Simple WDF Driver
description: This topic describes the minimal functionality you need to write a Kernel-Mode Driver Framework (KMDF) driver. You need the same minimal functionality to write a User-Mode Driver Framework (UMDF) driver starting in UMDF version 2.
ms.assetid: 6225b81c-e0da-473a-ba38-24846436dae7
keywords:
- kernel-mode drivers WDK KMDF , writing a simple driver
- KMDF WDK , writing a simple driver
- Kernel-Mode Driver Framework WDK , writing a simple driver
- framework-based drivers WDK KMDF , writing a simple driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a Simple WDF Driver


This topic describes the minimal functionality you need to write a Kernel-Mode Driver Framework (KMDF) driver. You need the same minimal functionality to write a User-Mode Driver Framework (UMDF) driver starting in UMDF version 2.




When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h. If your driver name exceeds the maximum length, your driver will fail to load.

Each framework-based driver consists of a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine and a set of event callback functions that the framework calls when object-specific events occur. For example, a simple framework-based driver might consist of:

-   A [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine, which is called when the driver is loaded and which calls [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175).

-   An [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function, which the framework calls when the Plug and Play (PnP) manager reports the detection of a device with a hardware identifier (ID) that matches a hardware ID that the driver supports.

    You specify the hardware IDs that your driver supports by providing an INF file, which the operating system uses to install drivers the first time that one of your devices is connected to the computer. For more information about how the system uses INF files and hardware IDs, see [How Setup Selects Drivers](https://msdn.microsoft.com/library/windows/hardware/ff546228).

    The driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function calls [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a framework device object for the device that was detected.

-   A request handler, such as the [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) callback function, that the framework calls when the I/O manager sends an I/O request to the driver.

    When the I/O manager sends I/O requests to your driver, the framework places the requests in an I/O queue and then notifies your driver by calling a request handler.

    The driver must create at least one I/O queue for each device, so that the driver can receive I/O requests for the device. To create an I/O queue, the driver calls [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401), which creates a framework queue object and registers the device's request handlers.

For more information about writing a framework-based driver, see [Using the Framework to Develop a Driver](using-the-framework-to-develop-a-driver.md).

 

 





