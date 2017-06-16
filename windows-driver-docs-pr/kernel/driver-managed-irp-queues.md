---
title: Driver-Managed IRP Queues
author: windows-driver-content
description: Driver-Managed IRP Queues
ms.assetid: b701e4aa-96ba-44af-96a5-b6cecf075bac
keywords: ["device queues WDK IRPs , objects", "IRPs WDK kernel , queuing", "queuing IRPs", "dequeuing IRPs", "internal IRP queues WDK kernel", "cancel-safe IRP queues WDK kernel", "driver-managed IRP queues WDK kernel", "supplemental IRP queues WDK kernel", "interlocked IRP queues WDK kernel", "device queues WDK IRPs", "device queues WDK IRPs , about device queues"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver-Managed IRP Queues


## <a href="" id="ddk-driver-managed-irp-queues-kg"></a>


Except for file system drivers, the I/O manager associates a device queue object (for queuing IRPs) with each device object that a driver creates.

Most device drivers call the I/O manager's support routines to use the associated device queue, which holds IRPs whenever device I/O requests for a target device object come in faster than the driver can process them to completion. With this technique, IRPs are queued to a driver-supplied [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine.

For good performance, most intermediate drivers simply pass IRPs on to lower drivers as fast as they come in, so intermediate drivers almost never use the device queues associated with their respective device objects.

However, you can design a driver to manage internal queues of IRPs by explicitly setting up one or more device queues, interlocked queues, or cancel-safe queues. This approach can be particularly useful if the driver controls a device that overlaps I/O operations. For such a device, it can be difficult to manage concurrent processing of two or more IRPs for the same target device object using only a single queue.

The simplest way to build an internal queue is to use the cancel-safe IRP queue framework. You can implement the queuing mechanism of your choice in your driver. You can then use [**IoCsqInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff549054) to register a set of callback routines that handle IRP insertion and deletion, as well as locking and unlocking your queue. The cancel-safe IRP queue framework provides the [**IoCsqInsertIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549066), [**IoCsqRemoveIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549070), and [**IoCsqRemoveNextIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549072) routines that automatically use the callback routines to safely insert and remove IRPs from the driver's queue. The system also uses your callback routines to safely remove any IRPs that are canceled.

You also might opt to set up supplemental queues for IRPs in the driver of a device controller for a set of heterogeneous physical devices. For example, the SCSI port driver uses device queue objects for internal queues. This driver both has a *StartIo* routine and sets up device queue objects as supplemental queues, in addition to the device queue associated with the device object it creates to represent an HBA. The SCSI port driver uses its supplemental device queues to hold IRPs bound for particular logical units on the HBA-controlled SCSI bus(es).

The system floppy controller driver is an example of a driver that has no *StartIo* routine and uses an interlocked queue. This driver sets up a doubly linked interlocked queue into which and from which the driver and its device-dedicated thread insert and remove IRPs.

The Kernel defines the device queue object type. The executive support component provides routines for inserting and removing IRPs in interlocked queues. Drivers for Windows XP and later versions of Windows can use [cancel-safe IRP queues](cancel-safe-irp-queues.md) to handle IRP queuing.

The following sections explain how to use device queues, interlocked queues, and cancel-safe queues:

[Setting up and Using Device Queues](setting-up-and-using-device-queues.md)

[Managing Device Queues](managing-device-queues.md)

[Setting Up and Using Interlocked Queues](setting-up-and-using-interlocked-queues.md)

[Managing Interlocked Queues with a Driver-Created Thread](managing-interlocked-queues-with-a-driver-created-thread.md)

[Cancel-Safe IRP Queues](cancel-safe-irp-queues.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Driver-Managed%20IRP%20Queues%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


