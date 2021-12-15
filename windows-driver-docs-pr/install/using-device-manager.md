---
title: Device Manager for makers of devices and drivers
description: Device Manager offers ways to troubleshoot installation problems with your drivers and devices.
keywords:
- Device Manager WDK
- Device Manager WDK , about Device Manager
ms.date: 10/01/2018
---

# Using Device Manager

To start Device Manager, in File explorer, select and hold (or right-click) **This PC**, select **Manage**, and then select **Device Manager** from the System Tools that are listed in the resulting dialog.

Device Manager displays information about each device. This includes the device type, device status, manufacturer, device-specific properties, and information about the driver for the device.

If your device is required to start the computer, a problem with your device installation can prevent the computer from starting. In these cases, you have to use the kernel debugger to troubleshoot your device installation. For more info, see [Getting Started with WinDbg (Kernel-Mode)](../debugger/getting-started-with-windbg--kernel-mode-.md).

If your device is not required to start the computer, Device Manager places a yellow exclamation point next that device's name in the Device Manager dialog. Device Manager also provides an error message describing the problem. For more information about the error messages, see [Device Manager Error Messages](device-manager-error-messages.md).

Device manager can show hidden devices. This is helpful when you are testing the installation of a new PnP device. For more information, see [Viewing Hidden Devices](viewing-hidden-devices.md).

Device Manager provides detailed information in the Properties dialog for each device. Select and hold (or right-click) the name of the device, and then select **Properties**. The **General**, **Driver**, **Details**, and **Events** tabs contain information that can be useful when you debug errors. For more information, see [Device Manager Details Tab](device-manager-details-tab.md).
