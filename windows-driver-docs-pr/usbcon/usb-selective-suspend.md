---
Description: 'This section provides information about choosing the correct mechanism for the selective suspend feature.'
MS-HAID:
- 'usbpower\_01a84111-d3de-4cc1-a9c1-1cdd2718b92a.xml'
- 'buses.usb\_selective\_suspend'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB Selective Suspend
author: windows-driver-content
---

# USB Selective Suspend


This section provides information about choosing the correct mechanism for the selective suspend feature.

In Microsoft Windows XP and later operating systems, the USB core stack supports a modified version of the "selective suspend" feature that is described in revision 2.0 of the Universal Serial Bus Specification.

The USB selective suspend feature allows the hub driver to suspend an individual port without affecting the operation of the other ports on the hub. Selective suspension of USB devices is especially useful in portable computers, since it helps conserve battery power. Many devices, such as fingerprint readers and other kinds of biometric scanners, only require power intermittently. Suspending such devices, when the device is not in use, reduces overall power consumption. More importantly, any device that is not selectively suspended may prevent the USB host controller from disabling its transfer schedule, which resides in system memory. DMA transfers by the host controller to the scheduler can prevent the system's processors from entering deeper sleep states, such as C3. The Windows selective suspend behavior is different for devices operating in Windows XP and Windows Vista and later versions of Windows.

There are two different mechanisms for selectively suspending a USB device: idle request IRPs ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) and set power IRPs ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)). The mechanism to use depends on the operating system and the type of device: composite or non-composite.

## <a href="" id="------selecting-a-selective-suspend-mechanism"></a> Selecting a Selective Suspend Mechanism


Client drivers, for an interface on a composite device, that enable the interface for remote wakeup with a wait wake IRP (IRP\_MN\_WAIT\_WAKE), must use the idle request IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) mechanism to selectively suspend a device.

The version of the Windows operating system determines the way drivers for non-composite devices enable selective suspend.

-   Windows XP: On Windows XP all client drivers must use idle request IRPs ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) to power down their devices. Client drivers must not use WDM power IRPs to selectively suspend their devices. Doing so will prevent other devices from selectively suspending. See [Conditions for Global Suspend in Windows XP](conditions-for-global-suspend-in-windows-xp.md) for more information.
-   Windows Vista and later versions of Windows: Driver writers have more choices for powering down devices in Windows Vista and in the later versions of Windows. Although Windows Vista supports the Windows idle request IRP mechanism, drivers are not required to use it.

The following table shows the scenarios that require the use of the idle request IRP and the ones that can use a WDM power IRP to suspend a USB device:

| Windows Version     | Function on Composite Device, Armed for Wake | Function on Composite Device, Not Armed for Wake | Single Interface USB Device |
|---------------------|----------------------------------------------|--------------------------------------------------|-----------------------------|
| Windows 7           | Must use idle request IRP                    | Can use WDM Power IRP                            | Can use WDM Power IRP       |
| Windows Server 2008 | Must use idle request IRP                    | Can use WDM Power IRP                            | Can use WDM Power IRP       |
| Windows Vista       | Must use idle request IRP                    | Can use WDM Power IRP                            | Can use WDM Power IRP       |
| Windows Server 2003 | Must use idle request IRP                    | Must use idle request IRP                        | Must use idle request IRP   |
| Windows XP          | Must use idle request IRP                    | Must use idle request IRP                        | Must use idle request IRP   |

 

This section explains the Windows selective suspend mechanism and includes the following topics:

[Sending a USB Idle Request IRP](sending-a-usb-idle-request-irp.md)

[Canceling a USB Idle Request](canceling-a-usb-idle-request.md)

[USB Idle Request IRP Completion Routine](usb-idle-request-irp-completion-routine.md)

[USB Idle Notification Callback Routine](usb-idle-notification-callback-routine.md)

[USB Global Suspend](conditions-for-global-suspend-in-windows-xp.md)

[Enabling Selective Suspend](enabling-selective-suspend.md)

## Related topics
[USB Power Management](usb-power-management.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Selective%20Suspend%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


