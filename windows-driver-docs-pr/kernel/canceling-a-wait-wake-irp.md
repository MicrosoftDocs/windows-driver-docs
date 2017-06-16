---
title: Canceling a Wait/Wake IRP
author: windows-driver-content
description: Canceling a Wait/Wake IRP
ms.assetid: 08e1d11a-91a3-496a-b3ad-f99456e4ce1d
keywords: ["power management WDK kernel , wake-up capabilities", "external wake signals WDK", "awakening devices", "wake-up capabilities WDK power management", "device wake ups WDK power management", "IRP_MN_WAIT_WAKE", "wait/wake IRPs WDK power management , canceling", "canceling wait/wake IRPs", "Cancel routines, wait/wake IRPs"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Canceling a Wait/Wake IRP


## <a href="" id="ddk-canceling-a-wait-wake-irp-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Canceling%20a%20Wait/Wake%20IRP%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


