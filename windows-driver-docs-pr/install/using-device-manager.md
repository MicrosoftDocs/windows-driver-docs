---
title: Using Device Manager
description: Device Manager offers ways to troubleshoot installation problems with your drivers and devices.
keywords:
- Device Manager WDK
- Device Manager WDK, about Device Manager
ms.date: 04/22/2025
ms.topic: concept-article
---

# Using Device Manager

To start Device Manager, launch the **Start** menu search functionality and search for "Device Manager". Alternatively, in File Explorer, right-click **This PC**, select **Manage**, and then select **Device Manager** from the system tools that are listed in the resulting dialog.

Device Manager displays information about each device. This information includes the device type, device status, manufacturer, device-specific properties, and information about the driver for the device.

If your device is required to boot the computer, a problem with your device installation can prevent the computer from starting. In these cases, you have to use the kernel debugger to troubleshoot your device installation. For more info, see [Getting Started with WinDbg (Kernel-Mode)](../debugger/getting-started-with-windbg--kernel-mode-.md).

If there's a problem with your device that isn't required to boot the computer, Device Manager places a yellow exclamation point next that device's name in the Device Manager dialog. Device Manager also shows an error message describing the problem. For more information about the error messages, see [Device Manager Error Messages](device-manager-error-messages.md).

By default, Device Manager can hide some devices from the view. To see all devices, see [Viewing Hidden Devices](viewing-hidden-devices.md).

Device Manager provides detailed information in the **Properties** dialog for each device. Right-click the name of the device, and then select **Properties**. The **General**, **Driver**, **Details**, and **Events** tabs contain information that can be useful when you debug errors. For more information, see [Device Manager Details Tab](device-manager-details-tab.md).
