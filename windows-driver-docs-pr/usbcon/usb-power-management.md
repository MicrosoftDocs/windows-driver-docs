---
title: Overview of Implementing Power Management in USB Client Drivers
description: The articles in this section examine the ways in which the WDM power model interacts with the power management properties of USB devices.
ms.date: 01/17/2024
---

# Overview of implementing power management in USB client drivers

The articles in this section examine the ways in which the WDM power model interacts with the power management properties of USB devices.

Power management abilities of USB devices that comply with the Universal Serial Bus (USB) specification have a rich and complex set of power management features. It's important to understand how these features interact with the Windows Driver Model (WDM), and in particular how Microsoft Windows has adapted standard USB features to support the system wake-up architecture.

For information about WDM power management in kernel-mode drivers, see [Implementing power management](../kernel/introduction-to-power-management.md).

USB client drivers based on kernel-mode driver framework (KMDF) and user-mode driver framework (UMDF) should use the mechanisms supported by the base technology and respective frameworks for managing power for a USB device. For information about managing power in KMDF-based client drivers, see [Supporting PnP and power management in your driver](../wdf/supporting-pnp-and-power-management-in-your-driver.md); for UMDF-based client drivers, see [PnP and power management in UMDF-based drivers](../wdf/pnp-and-power-management-in-umdf-drivers.md).

## In this section

| Article | Description |
|---|---|
| [USB device power states](comparing-usb-device-states-to-wdm-device-states.md) | This article describes the WDM device states to use for USB device power states as specified in section 9.1 of the Universal Serial Bus 2.0 specification. |
| [Selective suspend in USB drivers (WDF)](selective-suspend-in-usb-drivers-wdf.md) | A USB function driver supports runtime idle detection by implementing USB selective suspend. Here's content for driver developers about how to implement selective suspend in USB drivers that are based on the Windows&reg; Driver Foundation (WDF). |
| [USB selective suspend](usb-selective-suspend.md) | This section provides information about choosing the correct mechanism for the selective suspend feature. |
| [How to register a composite driver](register-a-composite-driver.md) | This article describes how a driver of a USB multi-function device, called a composite driver, can register and unregister the composite device with the underlying USB driver stack. The Microsoft-provided driver, Usbccgp.sys, is the default composite driver that Windows loads. The procedure in this article applies to a custom Windows Driver Model (WDM)-based composite driver that replaces Usbccgp.sys. |
| [How to implement function suspend for a composite driver](how-to--implement-remote-and-function-wake-support.md) | This article provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices). In this article, you'll learn about implementing those features in a driver that controls a composite device. The article applies to composite drivers that replace Usbccgp.sys. |
| [Remote wake-up of USB devices](remote-wakeup-of-usb-devices.md) | This article describes best practices about implementing the remote wake-up capability in a client driver. |

## Related topics

- [USB driver development guide](usb-driver-development-guide.md)
