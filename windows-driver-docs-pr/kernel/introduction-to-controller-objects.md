---
title: Introduction to Controller Objects
author: windows-driver-content
description: Introduction to Controller Objects
MS-HAID:
- 'ioprogleg\_132f468c-d5d8-4d7b-8f0c-69826a164bf9.xml'
- 'kernel.introduction\_to\_controller\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a46732a7-1e60-41d5-96e9-d5284c000af1
keywords: ["controller objects WDK kernel , about controller objects", "ControllerControl routines, about ControllerControl routines", "overlapped I/O WDK kernel", "I/O WDK kernel , overlaps"]
---

# Introduction to Controller Objects


## <a href="" id="ddk-introduction-to-controller-objects-kg"></a>


As its name suggests, a controller object usually represents a physical device controller with attached devices. A lowest-level non-WDM driver for a set of similar devices coordinated by a physical controller can create a controller object and use it to synchronize I/O operations between the attached devices. The driver implements a [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routine and calls the I/O manager's controller object support routines.

**Note**   Use of controller objects is not supported in WDM drivers.

 

Generally, drivers use controller objects to synchronize operations to attached devices if the following criteria hold:

-   The controller does not carry out long operations without interrupting, so the driver does not need to create a device-dedicated thread or use system worker threads.

-   The devices connected to the controller are similar. That is, they are not devices with entirely different physical properties or operational functionality, such as the keyboard and mouse devices that can be connected to the keyboard and auxiliary device controller.

-   The driver is designed to be monolithic: single-layered in relation to the device controller and attached physical devices, rather than being designed as a port driver (for the controller) with one or more class drivers (for attached devices) layered over the port driver.

Drivers of devices with I/O channels and a set of logical device objects also might use a controller object to synchronize their I/O operations between or among the channels of such a device.

A controller object has no name and thus is not the target of I/O requests. It is simply a synchronization mechanism to serialize I/O from a set of device objects. Because a controller object has no name, it is invisible to user-mode protected subsystems, which cannot make device I/O requests without getting a handle for the file object that represents the target device object. A controller object is also invisible to higher-level drivers, which cannot attach their own device objects to a controller object. In other words, neither the I/O manager nor a higher-level driver can set up an IRP requesting I/O on a device represented by a controller object. I/O requests are always issued to device objects. Only the driver can use the controller object.

### Synchronization and Overlapped I/O

Monolithic drivers of physical devices with features like those of the "AT" disk controller are not required to use a controller object to synchronize their device I/O operations. For example, a driver writer could try something like the following synchronization technique instead of using a controller object:

-   Set up named device objects to represent the devices that are targets for I/O requests.

-   Maintain state information (perhaps a set of Device Busy flags in each device extension or in a single device extension) indicating which device object is the target of the current I/O operation.

-   Carry out I/O operations for the currently busy device object and requeue incoming IRPs for other device objects until the current IRP is completed.

The preceding synchronization technique serializes IRP processing for all of the driver's target device objects. Note that it also forces the driver to complete the current IRP before its [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine can begin processing the next IRP, which unfortunately decreases driver performance.

If certain device operations can be overlapped, using a controller object can increase a driver's I/O throughput, because this synchronization technique allows the driver to determine whether it can overlap operations just before it sets up the physical device. For example, a disk controller might allow the driver to overlap seeks on one disk with read/write operations on another disk.

Moreover, using a controller object is a relatively easy way to synchronize I/O operations for more than one target device object through a single physical device, such as an "AT" disk controller. Using a controller object allows a monolithic driver to synchronize I/O operations across a set of named device objects without having to maintain state about every device and the device controller in one or more device extensions, and without having to requeue IRPs.

However, some devices that are designed to overlap I/O operations, such as full-duplex serial controllers or bus-master adapters, generally have drivers that set up internal queues for IRPs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Controller%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


