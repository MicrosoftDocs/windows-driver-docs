---
title: Canceling a Wait/Wake IRP
description: Canceling a Wait/Wake IRP
ms.assetid: 08e1d11a-91a3-496a-b3ad-f99456e4ce1d
keywords: ["power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "wait/wake IRPs WDK power management , canceling", "canceling wait/wake IRPs", "Cancel routines, wait/wake IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Canceling a Wait/Wake IRP





Only the driver that sent a wait/wake IRP can cancel that IRP.

A driver might need to cancel a pending wait/wake IRP under the following circumstances:

-   The driver receives a PnP [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755), [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551705), [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738), or [**IRP\_MN\_SURPRISE\_REMOVAL**](https://msdn.microsoft.com/library/windows/hardware/ff551760) request for the device. The driver should reissue the wait/wake IRP ([**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)) after the device is restarted.

-   The system is going to sleep, but the device should not be enabled to wake the system.

    For example, the USB hub driver might send an **IRP\_MN\_WAIT\_WAKE** request at device start-up in case it later puts one of its input devices into a sleep state. While the system is in the working state, a wake signal from the device returns the device to the working state (but has no effect on the system power state). When the system prepares to shut down, the USB hub driver cancels this IRP if the device should not be allowed to awaken the system.

-   The system is entering a sleep state from which the device cannot awaken it. That is, it is entering a state less powered than the [**SystemWake**](systemwake.md) value specified in its [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure.

-   The device is entering a power state from which it cannot respond to a wake-up signal. That is, it is entering a state less-powered than the [**DeviceWake**](devicewake.md) value specified in its **DEVICE\_CAPABILITIES** structure.

To cancel a wait/wake IRP, the driver that sent the IRP calls [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338), passing the pointer to the IRP that was previously returned when the driver called **PoRequestPowerIrp**.

A driver must not cancel a wait/wake IRP that it did not send.

### <a href="" id="ddk-cancel-routines-for-wait-wake-irps-kg"></a>Cancel Routines for Wait/Wake IRPs

Many function and bus drivers should set [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routines for pending wait/wake IRPs; the following types of drivers must set such routines:

-   Drivers that change device settings to enable or disable wake-up.

-   Drivers that send [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) requests to drivers of parent devices.

A [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine allows a driver to disable wake-up for its device and to clean up any data related to the pending wait/wake IRP. Drivers that request wait/wake IRPs for parent devices can cancel those IRPs as well.

In its wait/wake *Cancel* routine, a driver should take the following steps:

1.  Call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) to reset the *Cancel* routine for the IRP to **NULL**.

2.  Call [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550), passing the **CancelIRQL** specified in the IRP to release the cancel spin lock for the IRP.

3.  Reset any relevant fields in the device extension. For example, when a wait/wake IRP is pending, most drivers set a flag and keep a pointer to the IRP in the device extension.

    Note that it is possible for a driver to receive a wait/wake IRP while it is canceling another such IRP. The driver must check to see whether it already has an IRP under spin lock protection (or its equivalent). If so, the driver must carefully synchronize its handling to ensure that it cancels the correct IRP. For more information about using spin locks in *Cancel* routines, see [Canceling IRPs](canceling-irps.md).

4.  Change any required device settings. For example, a modem driver would disable the device's wake setting.

5.  Set **Irp-&gt;IoStatus.Status** to STATUS\_CANCELLED.

6.  Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the wait/wake IRP, specifying IO\_NO\_INCREMENT.

7.  If the driver previously requested a related **IRP\_MN\_WAIT\_WAKE** for a parent device, the driver should cancel that IRP from within its *Cancel* routine. The driver must release the cancel spin lock before it cancels the parent's IRP.

    For example, a driver that acts as a bus driver for a device and owns power policy driver for its parent should cancel a related wait/wake IRP that it earlier sent to its parent. Calling [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338) would invoke the parent's *Cancel* routine, and so on down the device stack.

 

 




