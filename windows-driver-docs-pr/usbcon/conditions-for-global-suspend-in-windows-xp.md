---
Description: 'The USB 2.0 Specification defines Global Suspend as the suspension of the entire bus behind a USB host controller by ceasing all USB traffic on the bus, including start-of-frame packets.'
MS-HAID:
- 'usbpower\_8255f0fd-43ba-4291-9a6d-88bc5ba280fc.xml'
- 'buses.conditions\_for\_global\_suspend\_in\_windows\_xp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB Global Suspend
---

# USB Global Suspend


The USB 2.0 Specification defines Global Suspend as the suspension of the entire bus behind a USB host controller by ceasing all USB traffic on the bus, including start-of-frame packets. Downstream devices that are not already suspended detect the Idle state on their upstream port and enter the suspend state on their own. Windows does not implement Global Suspend in this manner. Windows always selectively suspends each USB device behind a USB host controller before it will cease all USB traffic on the bus.

-   [Conditions for Global Suspend in Windows 7](#conditions-for-global-suspend-in-windows-7)
-   [Conditions for Global Suspend in Windows Vista](#conditions-for-global-suspend-in-windows-vista)
-   [Conditions for Global Suspend in Windows XP](#conditions-for-global-suspend-in-windows-xp)
-   [Related topics](#related-topics)

## Conditions for Global Suspend in Windows 7


Windows 7 is more aggressive about selectively suspending USB hubs than Windows Vista. The Windows 7 USB hub driver will selectively suspend any hub where all of its attached devices are in **D1**, **D2**, or **D3** device power state. The entire bus will enter Global Suspend once all USB hubs are selective suspended. The Windows 7 USB driver stack treats a device as Idle whenever the device is in a WDM device state of **D1**, **D2**, or **D3**.

## Conditions for Global Suspend in Windows Vista


The requirements for doing a global suspend are more flexible in Windows Vista than in Windows XP.

In particular, the USB stack treats a device as Idle in Windows Vista whenever the device is in a WDM device state of **D1**, **D2**, or **D3**.

The following diagram illustrates a scenario that might occur in Windows Vista.

![diagram illustrating a global suspend in windows vista](images/global-suspendlh.png)

This diagram illustrates a situation very similar to the one depicted in the section "Conditions for Global Suspend in Windows XP". However, in this case Device 3 qualifies as an Idle device. Since all devices are idle, the bus driver is able to call the idle notification callback routines associated with the pending idle request IRPs. Each driver suspends its device and the bus driver suspends the USB host controller as soon as it is safe to do so.

On Windows Vista all non-hub USB devices must be in **D1**, **D2**, or **D3** before Global Suspend will be initiated, at which time all USB hubs, including the root hub, will be suspended. This means that any USB client driver that does not support selective suspend will prevent the bus from entering Global Suspend.

## Conditions for Global Suspend in Windows XP


In order to maximize power savings on Windows XP, it is important that every device driver use idle request IRPs to suspend its device. If one driver suspends its device with an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request instead of an idle request IRP, it could prevent other devices from suspending.

The following diagram illustrates a scenario that might occur in Windows XP.

![diagram illustrating a global suspend in windows xp](images/global-suspendxp.png)

In this figure, device 3 is in power state D3 and does not have an idle request IRP pending. Device 3 does not qualify as an idle device for purposes of a global suspend in Windows XP, because it does not have an idle request IRP pending with its parent. This prevents the bus driver from calling the idle request callback routines associated with the drivers of other devices in the tree.

## Related topics


[USB Selective Suspend](usb-selective-suspend.md)

[USB Power Management](usb-power-management.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Global%20Suspend%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




