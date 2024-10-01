---
title: USB Device Power States
description: This article describes the Windows Driver Model (WDM) device states to use for USB device power states as specified in section 9.1 of the Universal Serial Bus 2.0 specification.
ms.date: 09/12/2024
---

# USB device power states

This article describes the Windows Driver Model (WDM) device states to use for USB device power states as specified in section 9.1 of the Universal Serial Bus 2.0 specification.

USB device power states (as specified in section 9.1 of the Universal Serial Bus 2.0 specification) can be grouped into three general categories:

- Attached: The device is attached, but not fully powered.
- Powered: The device is in one of the fully powered states: Default, Address, or Configured.
- Suspended: The device is the Idle state and operating on low power.

There's no direct correlation between the device power states defined in the WDM power model, and the device power states defined in the USB standard. For example, the terms *suspended* and *idle* have specific meanings in the USB specification; however these terms are often used differently in the WDM power model. Windows client drivers can put a USB device in the Suspended state. For more information, see [USB selective suspend](usb-selective-suspend.md). When a client driver is ready to suspend its device, it instructs the bus driver to idle it. For a discussion of idle requests, see [USB selective suspend](usb-selective-suspend.md).

Device power states in the WDM model can be summarized as follows:

- **D0** - The working state. The device is fully powered.
- **D1/D2** - The intermediate sleep states. These states allow the device to be armed for remote wakeup.
- **D3** - The deepest sleep state. Devices in state **D3** can't be armed for remote wakeup.

For a complete discussion of device power states in the WDM power model, see [Device power states](../kernel/device-power-states.md).

The WDM power model uses the term *arming* of devices for remote wakeup. Arming is a software operation that normally, but not always, leads to the hardware operation of *enabling* the remote wakeup feature on a USB device. The WDM software operation that arms a device for remote wakeup is the wait wake IRP ([**IRP_MN_WAIT_WAKE**](../kernel/irp-mn-wait-wake.md)). For more information about this IRP, see [Supporting devices that have wake-up capabilities](../kernel/supporting-devices-that-have-wake-up-capabilities.md).

For an explanation of the relationship between this software operation and the enabling of the USB remote wakeup feature, see [Remote Wakeup of USB Devices](remote-wakeup-of-usb-devices.md).

This section contains the following subsections:

- [Changing the power state of a noncomposite device](#changing-the-power-state-of-a-noncomposite-device)
- [Changing the power state of a composite device](#changing-the-power-state-of-a-composite-device)
- [Related topics](#related-topics)

## Changing the power state of a noncomposite device

The power policy manager for a USB device is responsible for setting the power state of the device. The power policy manager sets the power state by issuing a WDM power ([**IRP_MN_SET_POWER**](../kernel/irp-mn-set-power.md)) IRP. For more information about the power policy manager, see [Power Policy Ownership](../wdf/power-policy-ownership.md).

The actions taken by bus driver depend on the device power level that the power policy manager requests. The following lists the actions that the bus driver takes for each level of set power request:

- **D0**

    The bus driver performs the following tasks:

    1. Ensures that all upstream USB hubs are powered and ready to receive requests.
    1. Resumes the port by clearing the PORT_SUSPEND feature, if the device's USB port is suspended.
    1. Completes the device's idle IRP with STATUS_SUCCESS, if one is pending.
    1. Disarm the device for remote wake if it was armed.

- **D1/D2**

    The bus driver performs the following tasks:

    1. Arms the device for remote wakeup, if a wait wake IRP ([**IRP_MN_WAIT_WAKE**](../kernel/irp-mn-wait-wake.md)) is pending.
    1. Suspends the device's USB port by setting the PORT_SUSPEND feature.

- **D3**

    The bus driver performs the following tasks:

    1. Suspends the device's USB port by setting the PORT_SUSPEND feature.
    1. Completes the device's wait wake IRP with STATUS_POWER_STATE_INVALID, if one is pending.
    1. Completes the device's idle IRP ([**IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)) with STATUS_POWER_STATE_INVALID, if one is pending.

## Changing the power state of a composite device

A client driver for an interface on a composite device must share the power state of the composite device with the client drivers for the other interfaces on the device. Therefore a client driver for an interface can't put the composite device into a lower power state without affecting other interfaces on the device. The [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) takes the following actions when an interface's client driver sends an [**IRP_MN_SET_POWER**](../kernel/irp-mn-set-power.md) request.

- **D0**

    The bus driver performs the following tasks:

    1. Ensures that all upstream USB hubs are powered and ready to receive requests.
    1. Resumes the port by clearing the PORT_SUSPEND feature, if the device's USB port is suspended.
    1. Completes the client driver's idle IRP with STATUS_SUCCESS, if one is pending.

- **D1/D2**

    The bus driver takes no action.

- **D3**

    The bus driver performs the following tasks:

    1. Completes the client driver's wait wake IRP (IRP_MN_WAIT_WAKE) with STATUS_POWER_STATE_INVALID, if one is pending.
    1. Completes the client driver's idle IRP ([**IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION**](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)) with STATUS_POWER_STATE_INVALID, if one is pending.

The generic parent driver suspends the USB port for the device when one of the following conditions is true:

- The system is transitioning to a lower power state.
- The client drivers for all functions on the composite device initiated selective suspend.

## Related topics

- [USB Power Management](usb-power-management.md)
