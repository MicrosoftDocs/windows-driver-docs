---
title: Handling WDM IRPs Outside of the Framework
description: Handling WDM IRPs Outside of the Framework
ms.assetid: 43e1df0c-c0d1-4d41-87de-9f8f5831fb19
keywords: ["WDM IRPs WDK KMDF", "WDM IRPs WDK KMDF , outside framework", "IRPs WDK KMDF", "IRPs WDK KMDF , outside framework", "I/O request packets WDK KMDF"]
---

# Handling WDM IRPs Outside of the Framework


\[Applies to KMDF only\]

When the I/O manager delivers an I/O request packet (IRP) to a framework-based driver, the framework intercepts the IRP and then does one of the following:

-   Processes the IRP. For example, the framework processes IRPs that contain [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) and [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) major I/O function codes. While processing these IRPs, the framework might communicate with the driver by calling the driver's event callback functions.

-   Creates a framework request object for the IRP and delivers the request object to one of the driver's I/O queues so that the driver can receive it, typically in a request handler, and process it. The framework handles read, write, and device I/O control requests in this way.

-   Passes the IRP to the next-lower driver (if your driver is a filter driver), or completes the IRP with a status value of STATUS\_INVALID\_DEVICE\_REQUEST (if your driver is not a filter driver) because the IRP contains an I/O function code that the framework does not support.

Sometimes a driver must handle an I/O function code that the framework does not support.

Rarely, a driver might need to preprocess an IRP before the framework handles it, or the driver might need to postprocess an IRP after the framework and lower-level drivers have finished processing it.

As part of preprocessing, a driver might need to forward an IRP to a specific I/O queue.

The following topics describe these situations:

-   [Handling an IRP that the Framework Does Not Support](handling-an-irp-that-the-framework-does-not-support.md)
-   [Preprocessing and Postprocessing IRPs](preprocessing-and-postprocessing-irps.md)
-   [Dispatching IRPs to I/O Queues](dispatching-irps-to-i-o-queues.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20WDM%20IRPs%20Outside%20of%20the%20Framework%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




