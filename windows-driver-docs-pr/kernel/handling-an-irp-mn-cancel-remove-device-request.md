---
title: Handling an IRP_MN_CANCEL_REMOVE_DEVICE Request
description: Handling an IRP_MN_CANCEL_REMOVE_DEVICE Request
ms.assetid: 3382c47d-6ac8-409e-b558-ad2f2ae83715
keywords: ["IRP_MN_CANCEL_REMOVE_DEVICE", "spurious cancel-remove requests WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling an IRP\_MN\_CANCEL\_REMOVE\_DEVICE Request





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

 

 




