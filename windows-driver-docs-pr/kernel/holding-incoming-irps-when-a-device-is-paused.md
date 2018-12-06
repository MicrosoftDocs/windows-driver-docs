---
title: Holding Incoming IRPs When A Device Is Paused
description: Holding Incoming IRPs When A Device Is Paused
ms.assetid: 4964e06b-f1b9-4421-89d1-ad79ce7d7307
keywords: ["holding IRPs", "IRPs WDK PnP", "I/O request packets WDK PnP", "pausing PnP devices"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Holding Incoming IRPs When A Device Is Paused





The drivers for a device must pause the device when its resources are being rebalanced. During resource rebalancing, some drivers pause the device in response to an [**IRP\_MN\_QUERY\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551725) request and other drivers delay pausing the device until they receive the [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request. In either case, the device must be paused when the **IRP\_MN\_STOP\_DEVICE** succeeds.

The drivers must finish any IRPs in progress on the device and refrain from starting any new IRPs that require access to the device.

To hold IRPs while a device is paused, a driver implements a procedure such as the following:

1.  In its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, define a flag in the device extension with a name like HOLD\_NEW\_REQUESTS. Clear the flag.

2.  Create a FIFO queue for holding IRPs.

    If the driver already queues IRPs, it can reuse the same queue because the driver is required to finish any outstanding requests before pausing the device.

    If the driver does not already have an IRP queue, it must create one in its *AddDevice* routine. What kind of queue it creates depends on how the driver flushes the queue. A driver might use an interlocked, doubly linked list and the **ExInterlocked*Xxx*List** routines.

3.  In its *DispatchPnP* code for **IRP\_MN\_QUERY\_STOP\_DEVICE** (or **IRP\_MN\_STOP\_DEVICE**), finish any outstanding requests and set the HOLD\_NEW\_REQUESTS flag.

4.  In a dispatch routine that accesses the device, such as [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034) or [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376), check whether the HOLD\_NEW\_REQUESTS flag is set. If so, the driver must mark the IRP pending and queue it.

    The driver's *DispatchPnP* routine must continue to process PnP IRPs rather than hold them and the [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine must continue to process power IRPs.

5.  In *DispatchPnP*, in response to a start or cancel-stop IRP, clear the HOLD\_NEW\_REQUESTS flag and start the IRPs in the IRP-holding queue.

    These actions are probably the last steps for processing these PnP IRPs. For example, in response to a start IRP, the driver must first perform any operations to start the device and then it can start the IRPs in the IRP-holding queue.

    Errors in processing IRPs from the IRP-holding queue do not affect the status returned for the start or cancel-stop IRPs.

 

 




