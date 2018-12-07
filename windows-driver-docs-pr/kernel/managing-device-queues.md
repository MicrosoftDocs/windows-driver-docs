---
title: Managing Device Queues
description: Managing Device Queues
ms.assetid: 8b7d39f8-0449-4e9b-a54c-fe60ee60842c
keywords: ["device queues WDK IRPs , managing", "supplemental IRP queues WDK kernel", "StartIo routines, supplemental device queues"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Managing Device Queues





The I/O manager usually (except for FSDs) creates an associated device queue object when a driver calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397). It also provides [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370) and [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358), which drivers can call to have the I/O manager insert IRPs into the associated device queue or call their [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routines.

Consequently, it is rarely necessary (or particularly useful) for a driver to set up its own device queue objects for IRPs. Likely candidates are drivers, such as the SCSI port driver, that must coordinate incoming IRPs from some number of closely coupled class drivers for heterogeneous devices that are serviced through a single controller or bus adapter.

In other words, a driver for a disk array controller is more likely to use a driver-created controller object than to set up supplemental device queue object(s), while a driver for an add-on bus adapter and of a set of class drivers is slightly more likely to use supplemental device queues.

### Using Supplemental Device Queues with a StartIo Routine

By calling **IoStartPacket** and **IoStartNextPacket**, a driver's Dispatch and [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) (or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972)) routines synchronize calls to its *StartIo* routine using the device queue that the I/O manager created when the driver created the device object. For a port driver with a *StartIo* routine, **IoStartPacket** and **IoStartNextPacket** insert and remove IRPs in the device queue for the port driver's shared device controller/adapter. If the port driver also sets up supplemental device queues to hold requests coming in from closely coupled higher-level class drivers, it must "sort" incoming IRPs into its supplemental device queues, usually in its *StartIo* routine.

The port driver must determine which supplemental device queue each IRP belongs in before trying to insert that IRP into the appropriate queue. A pointer to the target device object is passed with the IRP to the driver's Dispatch routine. The driver should save the pointer for use in "sorting" the incoming IRPs. Note that the device object pointer passed to the *StartIo* routine is the driver's own device object, which represents the device controller/adapter, so it cannot be used for this purpose.

After queuing any IRPs, the driver programs its shared controller/adapter to carry out the request. Thus, the port driver can process incoming requests for all devices on a first-come, first-served basis until a call to [**KeInsertDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552180) puts an IRP into a particular class driver's device queue.

By using its own device queue for all IRPs to be processed through its *StartIo* routine, the underlying port driver serializes operations through the shared device (or bus) controller/adapter to all attached devices. By sometimes holding IRPs for each supported device in a separate device queue, this port driver inhibits the processing of IRPs for an already busy device while increasing I/O throughput for every other device that does I/O through its shared hardware.

In response to the call to **IoStartPacket** from the port driver's Dispatch routine, the I/O manager either calls that driver's *StartIo* routine immediately or puts the IRP into the device queue associated with the device object for the port driver's shared controller/adapter.

The port driver must maintain its own state information about each of the heterogeneous devices that it services through the shared device controller/adapter.

**Keep in mind the following when designing class/port drivers with supplemental device queues:**

-   A driver cannot easily get a pointer to a device object created by any driver layered above itself, except for the device object at the top of its device stack.

    By design, the I/O manager does not provide a support routine for getting such a pointer. Moreover, the order in which drivers are loaded makes it impossible for lower drivers to get pointers for higher-level drivers' device objects, which have not yet been created when any lower-level driver is adding its device.

    Although **IoGetAttachedDeviceReference** returns a pointer to the highest-level device object in a driver's stack, a driver should use this pointer only to designate a target for I/O requests to its stack. A driver should not attempt to read or write the device object.

-   A driver cannot use a pointer to a device object created by any driver layered above itself, except to send requests to the top of its own device stack.

    There is no way to synchronize access to a single device object (and its device extension) between two drivers in a multiprocessor-safe manner. Neither driver can make any assumptions about what I/O processing the other driver is currently doing.

Even for closely coupled class/port drivers, each class driver should use the pointer to the port driver's device object(s) only to pass on IRPs using **IoCallDriver**. The underlying port driver must maintain its own state, probably in the port driver's device extension, about requests that it processes for any closely coupled class driver(s)' device(s).

### Managing Supplemental Device Queues Across Driver Routines

Any port driver that queues IRPs in supplemental device queues for a closely coupled set of class drivers also must handle the following situation efficiently:

1.  Its Dispatch routines have inserted IRPs for a particular device in the driver-created device queue for that device.

2.  IRPs for other devices continue to come in, to be queued to the driver's *StartIo* routine with **IoStartPacket**, and to be processed through the shared device controller.

3.  The device controller does not become idle, but each IRP held in the driver-created device queue also must be queued to the driver's *StartIo* routine as soon as possible.

Consequently, the port driver's *DpcForIsr* routine must attempt to transfer an IRP from the driver's internal device queue for a particular device into the device queue for the shared adapter/controller whenever the port driver completes an IRP, as follows:

1.  The *DpcForIsr* routine calls **IoStartNextPacket** to have the *StartIo* routine begin processing the next IRP queued to the shared device controller.

2.  The *DpcForIsr* routine calls [**KeRemoveDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553156) to dequeue the next IRP (if any) that it is holding in its internal device queue for the device on whose behalf it is about to complete an IRP.

3.  If **KeRemoveDeviceQueue** returns a non-NULL pointer, the *DpcForIsr* routine calls **IoStartPacket** with the just dequeued IRP to have it queued to the shared device controller/adapter. Otherwise, the call to **KeRemoveDeviceQueue** simply resets the state of the device queue object to Not-Busy, and the *DpcForIsr* routine omits the call to **IoStartPacket**.

4.  Then, the *DpcForIsr* routine calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with the input IRP for which the port driver has just completed I/O processing, either by setting the I/O status block with an error or by satisfying the I/O request.

Note that the preceding sequence implies that the *DpcForIsr* routine also must determine the device for which it is completing the current (input) IRP in order to manage internal queuing of IRPs efficiently.

If the port driver attempts to wait until its shared controller/adapter is idle before dequeuing IRPs held in its supplemental device queues, the driver might starve a device for which there was heavy I/O demand while it promptly serviced every other device for which the current I/O demand was actually much lighter.

 

 




