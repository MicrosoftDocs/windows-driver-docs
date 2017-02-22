---
Description: 'The bus driver (either an instance of the hub driver or the generic parent driver) determines when it is safe to suspend its device's children. If it is, it calls the idle notification callback routine supplied by each child's client driver.'
MS-HAID:
- 'usbpower\_f8bc1ea8-b465-43ee-892c-4f382739b43d.xml'
- 'buses.usb\_idle\_notification\_callback\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB Idle Notification Callback Routine
---

# USB Idle Notification Callback Routine


The bus driver (either an instance of the hub driver or the generic parent driver) determines when it is safe to suspend its device's children. If it is, it calls the idle notification callback routine supplied by each child's client driver.

The function prototype for USB\_IDLE\_CALLBACK is as follows:

``` syntax
typedef VOID (*USB_IDLE_CALLBACK)(__in PVOID Context);
```

A device driver must take the following actions in its idle notification callback routine:

-   Request an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) IRP for the device if the device needs to be armed for remote wakeup.
-   Cancel all I/O and prepare the device to go to a lower power state.
-   Put the device in a WDM sleep state by calling [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) with the *PowerState* parameter set to the enumerator value PowerDeviceD2 (defined in wdm.h; ntddk.h). In Windows XP, a driver must not put its device in PowerDeviceD3, even if the device is not armed for remote wake.

In Windows XP, a driver must rely on an idle notification callback routine to selectively suspend a device. If a driver running in Windows XP puts a device in a lower power state directly without using an idle notification callback routine, this might prevent other devices in the USB device tree from suspending. For more details, see [USB Global Suspend](conditions-for-global-suspend-in-windows-xp.md).

Both the hub driver and the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) call the idle notification callback routine at IRQL = PASSIVE\_LEVEL. This allows the callback routine to block while it waits for the power state change request to complete.

The callback routine is invoked only while the system is in **S0** and the device is in **D0**.

The following restrictions apply to idle request notification callback routines:

-   Device drivers can initiate a device power state transition from **D0** to **D2** in the idle notification callback routine, but no other power state transition is allowed. In particular, a driver must not attempt to change its device to **D0** while executing its callback routine.
-   Device drivers must not request more than one power IRP from within the idle notification callback routine.

## Arming Devices for Wakeup in the Idle Notification Callback Routine


The idle notification callback routine should determine whether its device has an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request pending. If no IRP\_MN\_WAIT\_WAKE request is pending, the callback routine should submit an IRP\_MN\_WAIT\_WAKE request before suspending the device. For more information about the wait wake mechanism, see [Supporting Devices That Have WakeUp Capabilities](https://msdn.microsoft.com/library/windows/hardware/ff563907).

## Related topics


[USB Selective Suspend](usb-selective-suspend.md)

[USB Power Management](usb-power-management.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Idle%20Notification%20Callback%20Routine%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




