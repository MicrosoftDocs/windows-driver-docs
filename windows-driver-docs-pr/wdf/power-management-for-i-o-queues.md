---
title: Power Management for I/O Queues
description: Power Management for I/O Queues
ms.assetid: 2e1bf9d2-615b-49b0-b677-f41b23c42eda
keywords:
- power management WDK KMDF , I/O queues
- I/O queues WDK KMDF , power management
- I/O requests WDK KMDF , power management
- power-managed I/O queues WDK KMDF
- working states WDK KMDF
- PowerManaged settings WDK KMDF
- low-power states WDK KMDF
- sleep power management WDK KMDF
- power states WDK KMDF
- device power states WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Management for I/O Queues


When the framework receives an I/O request that is directed to one of your driver's devices, the framework puts the request in an I/O queue. The driver can obtain I/O requests from the I/O queue by providing request handlers or by polling the queue. For more information about I/O queues, see [Framework Queue Objects](framework-queue-objects.md).

As you are designing your driver, you should group the I/O requests that your driver will receive into two categories:

1.  Requests that require a device to be in its working (D0) state, including:
    -   Read or write requests that require the device's function driver to read data from, or write data to, the device.
    -   Device control requests that a function or bus driver cannot service without accessing the device.

2.  Requests that do not require a device to be in its working (D0) state, including:
    -   Device control requests that a function or bus driver can service without accessing the device.
    -   Possibly all the requests that a filter driver receives.
    -   All the requests that all drivers in a driver stack receive, if the stack supports a software-only device that does not communicate with any hardware.

Unless you are writing a filter driver, or a driver for a stack that does not communicate with hardware, it is likely that your driver will receive some requests that require the device to be in its working state, together with some that do not.

To support these two types of requests, the framework provides two types of I/O queues: those that are *power-managed* and those that are not. When your driver creates each of its I/O queues, it sets the **PowerManaged** member in the queue's [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure to either **WdfTrue** or **WdfFalse** to indicate one of the following:

-   If your driver sets **PowerManaged** to **WdfTrue**, the queue is power-managed.

    When I/O requests are available in a power-managed queue, the framework delivers the requests to the driver only if the device is in its working (D0) state. Therefore, whenever your driver receives a request from a power-managed queue, the framework guarantees that the device is available. If the device is not in its working state, the framework stores requests in the queue until the device becomes available.

    If the device is in a low-power state because it is idle, and if the framework puts an I/O request in one of your driver's power-managed queues, the framework asks the driver stack to restore the device to its working state before it delivers the request to your driver.

    If the device is in a low-power state because the system is not in its working (S0) state, and if the framework puts an I/O request in one of your driver's power-managed queues, the framework waits until the device returns to its working (D0) state and then delivers the request to your driver.

    Because the framework does not deliver I/O requests from a power-managed queue to the driver if the device is not in its working state, *drivers that are located above the* [power policy owner](power-policy-ownership.md) *in the driver stack must not use power-managed I/O queues*. If a driver that is located above the power policy owner uses a power-managed queue, and if the device is in a low-power state, the driver does not receive the request and cannot pass it to the power policy owner. Therefore the power policy owner, which controls the device's power state, does not wake the device.

-   If your driver sets **PowerManaged** to **WdfFalse**, the queue is not power-managed.

    When I/O requests are available in a queue that is not power-managed, the framework delivers the requests to the driver regardless of whether the device is in its working (D0) state. If you have set up your queue so that it only receives requests that do not require accessing the device, your driver can service each request, even if the device is not available.

For more information about power-managed I/O queues, see [Using Power-Managed I/O Queues](using-power-managed-i-o-queues.md).

A few drivers require some direct control over Plug and Play (PnP) and power management operations. These drivers can use *self-managed I/O*. For more information, see [Using Self-Managed I/O](using-self-managed-i-o.md).

 

 





