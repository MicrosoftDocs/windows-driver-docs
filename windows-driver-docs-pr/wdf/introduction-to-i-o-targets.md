---
title: Introduction to I/O Targets
description: Introduction to I/O Targets
ms.assetid: 06ab7b3e-6b3e-4cfe-a7a6-17292300c472
keywords:
- I/O targets WDK KMDF , about I/O targets
- I/O target objects WDK KMDF
- remote I/O targets WDK KMDF
- local I/O targets WDK KMDF
- function drivers WDK KMDF
- filter drivers WDK KMDF
- miniport drivers WDK KMDF
- specialized I/O targets WDK KMDF
- I/O targets WDK KMDF , types
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to I/O Targets





When a [function driver](wdm-concepts-for-kmdf-drivers.md), filter driver, or [miniport driver](creating-kmdf-miniport-drivers.md) receives an I/O request, the driver might be able to process the request by itself or it might need the assistance of other drivers. If the driver needs assistance, it can forward the request to another driver, or it can create one or more new requests and send them to another driver.

In Kernel-Mode Driver Framework, an *I/O target* represents a device object that is the target of an I/O request. A function, filter, or miniport driver can use an I/O target to send I/O requests to another driver. These drivers often send their I/O requests to the next-lower driver in the driver stack. Therefore, each framework-based function, filter, and miniport driver has a *local I/O target* for each device, which is the device's next-lower driver.

Occasionally, a driver must send an I/O request to a different target--the top of a different driver stack or, rarely, some other driver within the sending driver's stack. Therefore, the framework also provides *remote I/O targets*, which consist of all of the I/O targets except the local I/O target.

Each I/O target is represented by an *I/O target object*. Each I/O target object is primarily a queue that controls when a request is delivered to the target device object. When a driver sends a request to an I/O target, the framework stores the request in the queue until it can deliver the request to the target device object.

The framework supports both *general I/O targets* and *specialized I/O targets*:

-   [General I/O targets](general-i-o-targets.md) can be used by all function, filter, and miniport drivers, but they do not support any special, device-specific data formats.

-   Specialized I/O targets enable function, filter, and miniport drivers to easily send I/O requests that require special, target-specific data formatting. Currently, the framework provides support for the following specialized I/O targets:
    -   [USB I/O targets](usb-i-o-targets.md)

If the framework provides specialized I/O targets that support your device's data format, your driver should use the specialized I/O targets. Otherwise, the driver should use general I/O targets.

 

 





