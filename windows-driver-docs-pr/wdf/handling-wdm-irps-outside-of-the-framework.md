---
title: Handling WDM IRPs Outside of the Framework
description: Handling WDM IRPs Outside of the Framework
ms.assetid: 43e1df0c-c0d1-4d41-87de-9f8f5831fb19
keywords:
- WDM IRPs WDK KMDF
- WDM IRPs WDK KMDF , outside framework
- IRPs WDK KMDF
- IRPs WDK KMDF , outside framework
- I/O request packets WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





