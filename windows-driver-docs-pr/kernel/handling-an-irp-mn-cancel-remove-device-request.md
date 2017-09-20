---
title: Handling an IRP_MN_CANCEL_REMOVE_DEVICE Request
author: windows-driver-content
description: Handling an IRP_MN_CANCEL_REMOVE_DEVICE Request
ms.assetid: 3382c47d-6ac8-409e-b558-ad2f2ae83715
keywords: ["IRP_MN_CANCEL_REMOVE_DEVICE", "spurious cancel-remove requests WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling an IRP\_MN\_CANCEL\_REMOVE\_DEVICE Request


## <a href="" id="ddk-handling-an-irp-mn-cancel-remove-device-request-kg"></a>


In response to an [**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff550823) request, the drivers for a device must return the device to the state it was in prior to receiving the **IRP\_MN\_QUERY\_REMOVE\_DEVICE** request. Typically, drivers return the device to the started state.

In addition to sending an **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** to a device, the PnP manager sends the IRP to the device's removal relations, if any. The PnP manager also sends a cancel-remove IRP to the device's children.

The PnP manager calls any **EventCategoryTargetDeviceChange** notification callbacks after the **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** request completes. Such callbacks were registered on the device by calling [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526). The PnP manager also calls any user-mode components that registered for such notification by calling **RegisterDeviceNotification**.

An **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** request must be handled first by the parent bus driver for a device and then by each higher driver in the device stack. A driver handles remove IRPs in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine.

A driver handles an **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** request with a procedure such as the following in its *DispatchPnP* routine:

1.  In a function or filter driver, postpone restarting the device until lower drivers have completed their restart operations.

    A function or filter driver sets an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, passes the **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** down the device stack, and postpones its restart operations until all lower drivers have finished with the IRP. (See [Postponing PnP IRP Processing Until Lower Drivers Finish](postponing-pnp-irp-processing-until-lower-drivers-finish.md).)

2.  After lower drivers finish, return the device to its previous PnP state.

    The drivers return the device to the state it was in prior to receiving the **IRP\_MN\_QUERY\_REMOVE\_DEVICE** request. Typically, drivers return the device to the started state. Exact operations depend on the device and the driver.

    If the device was previously enabled for wake-up, the device power policy owner (typically the function driver) should send an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request to reenable wake-up. See [Power Management](implementing-power-management.md) for details.

3.  Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS and complete the IRP with [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

    As with any PnP IRP, a bus driver completes the IRP.

    A function or filter driver also completes the IRP, in this case because the driver's *IoCompletion* routine interrupted completion processing by returning STATUS\_MORE\_PROCESSING\_REQUIRED.

    Drivers must succeed this IRP. If any driver fails this IRP, the device is left in an inconsistent state.

A driver might receive a spurious cancel-remove request when the device is started and active. This can occur, for example, if the driver (or a driver higher in the device stack) failed an **IRP\_MN\_QUERY\_REMOVE\_DEVICE** request. When a device is started and active, a driver simply succeeds a spurious cancel-remove request for the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20an%20IRP_MN_CANCEL_REMOVE_DEVICE%20Request%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


