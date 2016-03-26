---
title: Writing a Simple WDF Driver
description: This topic describes the minimal functionality you need to write a Kernel-Mode Driver Framework (KMDF) driver. You need the same minimal functionality to write a User-Mode Driver Framework (UMDF) driver starting in UMDF version 2.
ms.assetid: 6225b81c-e0da-473a-ba38-24846436dae7
keywords: ["kernel-mode drivers WDK KMDF , writing a simple driver", "KMDF WDK , writing a simple driver", "Kernel-Mode Driver Framework WDK , writing a simple driver", "framework-based drivers WDK KMDF , writing a simple driver"]
---

# Writing a Simple WDF Driver


This topic describes the minimal functionality you need to write a Kernel-Mode Driver Framework (KMDF) driver. You need the same minimal functionality to write a User-Mode Driver Framework (UMDF) driver starting in UMDF version 2.

## <a href="" id="ddk-writing-a-simple-framework-based-driver-df"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Writing%20a%20Simple%20WDF%20Driver%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




