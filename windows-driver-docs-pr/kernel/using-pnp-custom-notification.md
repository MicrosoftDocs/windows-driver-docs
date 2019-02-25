---
title: Using PnP Custom Notification
description: Using PnP Custom Notification
ms.assetid: de5562f8-07a8-4f4e-ac49-58c789bd9fde
keywords: ["notifications WDK PnP , custom", "custom notifications WDK PnP", "notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using PnP Custom Notification





A driver can use the target device change notification mechanism to be notified of custom events on a device.

The programmer that defines the custom event must do the following:

1.  Define a new GUID for the custom event.

    Generate the GUID with **Uuidgen** or **Guidgen** (which are included in the Microsoft Windows SDK). Publish the GUID in an appropriate header file and documentation.

2.  Write code to trigger the custom event.

    In kernel mode, a driver calls [**IoReportTargetDeviceChange**](https://msdn.microsoft.com/library/windows/hardware/ff549625) with the custom GUID and a pointer to the PDO for the device. Custom events can only be triggered from kernel mode.

A driver writer uses custom notification with a procedure like the following:

1.  The driver (or application) registers for notification of the custom event.

    In kernel mode, a driver calls [**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526) and registers for an **EventCategoryTargetDeviceChange** on the device.

    In user mode, an application registers using **RegisterDeviceNotification**. See the Windows SDK for further information.

2.  A kernel-mode component triggers the custom event.

3.  The PnP manager calls notification routines registered on the device.

    The PnP manager calls the registered user-mode callback routines and then calls the kernel-mode callback routines.

4.  When user-mode notification is complete, the kernel-mode driver notification callback routine(s) respond to the custom event.

    See [Guidelines for Writing PnP Notification Callback Routines](guidelines-for-writing-pnp-notification-callback-routines.md) for general guidelines for notification callback routines. In addition to those guidelines, a custom notification callback routine must not open a handle to a device from within the callback routine thread.

 

 




