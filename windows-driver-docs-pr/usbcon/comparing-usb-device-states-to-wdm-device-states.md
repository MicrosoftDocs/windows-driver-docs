---
Description: This topic describes the WDM device states to use for USB device power states as specified in section 9.1 of the Universal Serial Bus 2.0 specification.
title: USB Device Power States
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Device Power States


This topic describes the WDM device states to use for USB device power states as specified in section 9.1 of the Universal Serial Bus 2.0 specification.

USB device power states (as specified in section 9.1 of the Universal Serial Bus 2.0 specification) can be grouped into three general categories:

-   Attached: The device is attached, but not fully powered.
-   Powered: The device is in one of the fully powered states: Default, Address, or Configured.
-   Suspended: The device is the Idle state and operating on low power.

There is no direct correlation between the device power states defined in the WDM power model and the device power states defined in the USB standard. For example, the terms *suspended* and *idle* have very specific meanings in the USB specification; however these terms are often used differently in the WDM power model. Windows client drivers can put a USB device in the Suspended state. For more information, see [USB Selective Suspend](usb-selective-suspend.md). When a client driver is ready to suspend its device, it instructs the bus driver to idle it. For a discussion of idle requests, see [USB Selective Suspend](usb-selective-suspend.md).

Device power states in the WDM model can be summarized as follows:

-   **D0** - The working state. The device is fully powered.
-   **D1/D2** - The intermediate sleep states. These states allow the device to be armed for remote wakeup.
-   **D3** - The deepest sleep state. Devices in state **D3** cannot be armed for remote wakeup.

For a complete discussion of device power states in the WDM power model, see [Device Power States](https://msdn.microsoft.com/library/windows/hardware/ff543162).

The WDM power model uses the term *arming* of devices for remote wakeup. Arming is a software operation that normally, but not always, leads to the hardware operation of *enabling* the remote wakeup feature on a USB device. The WDM software operation that arms a device for remote wakeup is the wait wake IRP ([**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766)). For more information about this IRP, see [Supporting Devices that Have Wake-Up Capabilities](https://msdn.microsoft.com/library/windows/hardware/ff563907).

For an explanation of the relationship between this software operation and the enabling of the USB remote wakeup feature, see [Remote Wakeup of USB Devices](remote-wakeup-of-usb-devices.md).

This section contains the following sub-sections:

-   [Changing the Power State of a non-Composite Device](#changing-the-power-state-of-a-non-composite-device)
-   [Changing the Power State of a Composite Device](#changing-the-power-state-of-a-composite-device)
-   [Related topics](#related-topics)

## Changing the Power State of a non-Composite Device


The power policy manager for a USB device is responsible for setting the power state of the device. The power policy manager sets the power state by issuing a WDM power ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)) IRP. For more information about the power policy manager, see [Power Policy Ownership](https://msdn.microsoft.com/library/windows/hardware/ff544518).

The actions taken by bus driver depend on the device power level that the power policy manager requests. The following lists the actions that the bus driver takes for each level of set power request:

-   **D0**

    The bus driver performs the following tasks:

    1.  Ensures that all upsteam USB hubs are powered and ready to receive requests.
    2.  Resumes the port by clearing the PORT\_SUSPEND feature, if the device's USB port is suspended.
    3.  Completes the device's idle IRP with STATUS\_SUCCESS, if one is pending.
    4.  Disarm the device for remote wake if it was armed.
-   **D1/D2**

    The bus driver performs the following tasks:

    1.  Arms the device for remote wakeup, if a wait wake IRP ([**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766)) is pending.
    2.  Suspends the device's USB port by setting the PORT\_SUSPEND feature.
-   **D3**

    The bus driver performs the following tasks:

    1.  Suspends the device's USB port by setting the PORT\_SUSPEND feature.
    2.  Completes the device's wait wake IRP with STATUS\_POWER\_STATE\_INVALID, if one is pending.
    3.  Completes the device's idle IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) with STATUS\_POWER\_STATE\_INVALID, if one is pending.

## Changing the Power State of a Composite Device


A client driver for an interface on a composite device must share the power state of the composite device with the client drivers for the other interfaces on the device. Therefore a client driver for an interface cannot put the composite device into a lower power state without affecting other interfaces on the device. The [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) takes the following actions when an interface's client driver sends an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request.

-   **D0**

    The bus driver performs the following tasks:

    1.  Ensures that all upsteam USB hubs are powered and ready to receive requests.
    2.  Resumes the port by clearing the PORT\_SUSPEND feature, if the device's USB port is suspended.
    3.  Completes the client driver's idle IRP with STATUS\_SUCCESS, if one is pending.
-   **D1/D2**

    The bus driver takes no action.

-   **D3**

    The bus driver performs the following tasks:

    1.  Completes the client driver's wait wake IRP (IRP\_MN\_WAIT\_WAKE) with STATUS\_POWER\_STATE\_INVALID, if one is pending.
    2.  Completes the client driver's idle IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) with STATUS\_POWER\_STATE\_INVALID, if one is pending.

The generic parent driver suspends the USB port for the device when one of the following conditions is true:

-   The system is transitioning to a lower power state.
-   The client drivers for all functions on the composite device have initiated selective suspend.

## Related topics
[USB Power Management](usb-power-management.md)  



