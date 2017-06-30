---
title: Holding Incoming IRPs When A Device Is Paused
author: windows-driver-content
description: Holding Incoming IRPs When A Device Is Paused
ms.assetid: 4964e06b-f1b9-4421-89d1-ad79ce7d7307
keywords: ["holding IRPs", "IRPs WDK PnP", "I/O request packets WDK PnP", "pausing PnP devices"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Holding Incoming IRPs When A Device Is Paused


## <a href="" id="ddk-holding-incoming-irps-when-a-device-is-paused-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Holding%20Incoming%20IRPs%20When%20A%20Device%20Is%20Paused%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


