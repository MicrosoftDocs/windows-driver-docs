---
title: Introduction to WinUSB for developers
description: This section describes the generic WinUSB driver (Winusb.sys) and its user-mode component (Winusb.dll) provided by Microsoft for all USB devices.
ms.date: 12/06/2023
ms.custom: contperf-fy22q4
---

# Introduction to WinUSB for developers

> [!IMPORTANT]
> This topic is for programmers. If you are a customer experiencing USB problems, see [Troubleshoot common USB problems](https://support.microsoft.com/help/17614/windows-10-troubleshoot-common-usb-problems)

WinUSB is a generic driver for USB devices that is included with Windows.

WinUSB includes:

- A kernel-mode driver (Winusb.sys)
- A user-mode dynamic link library (Winusb.dll) that exposes WinUSB functions described in [winusb.h](/windows/win32/api/winusb#functions). You can use these functions to manage USB devices with user-mode software.

By default, Winusb.sys is installed in the device's kernel-mode stack as an upper filter driver. Apps communicate with the device's UMDF function driver to issue read, write, or device I/O control requests. In this configuration, Winusb.sys serves as the device stack's Plug and Play and power owner.

You can also install Winusb.sys as the function driver for a USB device.

This section includes info on:

- Selecting the correct driver for a device
- Using WinUSB to communicate with USB devices
- Installing Winusb.sys as the function driver for a USB device

Also find detailed code examples that show how apps and USB devices communicate.

> [!NOTE]
> Windows 7 supports WinUSB on x86-based, x64-based, and Itanium-based systems. More recent versions of Windows support WinUSB on x86-based and x64-based systems.
>
> WinUSB supports isochronous transfers starting in Windows 8.

## Related topics

- [Microsoft-provided USB drivers](system-supplied-usb-drivers.md)
