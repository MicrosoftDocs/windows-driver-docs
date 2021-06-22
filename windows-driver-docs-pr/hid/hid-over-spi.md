---
title: Introduction to HID over SPI
description: How to use Human Interface Device (HID) class devices over a Serial Peripheral Interface (SPI).
keywords:
- HID
- Human Interface Device
- HID miniport driver
- HID class extension
- SPI
- Serial Peripheral Interface
- Simple Peripheral Bus
ms.date: 06/22/2021
ms.localizationpriority: medium
---

# Introduction to HID over SPI

There’s [HID over I2C](hid-over-i2c-guide.md) and [HID over USB](hid-over-usb.md). Why use HID over SPI? SPI offers the following features:

- Faster than I2C – more bandwidth, higher clock rates
- Low latency
- Easy and inexpensive to implement in hardware
- Works well for devices that are integrated into the platform and not removable

This article describes how to use Human Interface Device (HID) class devices over a simple peripheral bus transport, with an immediate focus on SPI. The HID class consists primarily of devices that are used by humans to control the operation of computer systems. Typical examples of HID class devices include:

- Keyboards and pointing devices such as standard mouse devices, trackballs, and joysticks
- Front-panel controls like knobs, switches, buttons, and sliders
- Controls that might be found on devices like telephones, remote controls, games, or simulation devices, for example, data gloves, steering wheels, keypads and rudder pedals
- Devices that may not require human interaction but provide data in a similar format to HID class devices, for example, bar-code readers, thermometers, or other forms of sensors

The HID protocol was originally targeted at human interface devices. However, the HID protocol is very useful for any application that requires low-latency input-output operations to an external interface and the ability for that device to describe itself. Typical HID class devices include indicators, specialized displays, audio feedback, and force or tactile feedback.

The HID protocol is a asymmetric and identifies roles for the host and the device. The protocol will define a format (descriptors) for the device to describe its capabilities to the host. Once the host understands the format of communication with the device, it programs the device for sending data back to the host. The HID protocol also identifies ways of sending data to the device as well as status checks for identifying the current state of the device.

## See also

[HID over USB](hid-over-usb.md)

[HID over I2C](hid-over-i2c-guide.md)
