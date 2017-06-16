---
title: Using PnP Custom Notification
author: windows-driver-content
description: Using PnP Custom Notification
ms.assetid: de5562f8-07a8-4f4e-ac49-58c789bd9fde
keywords: ["notifications WDK PnP , custom", "custom notifications WDK PnP", "notifications WDK PnP , target device changes", "target device change notifications WDK PnP", "EventCategoryTargetDeviceChange notification"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using PnP Custom Notification


## <a href="" id="ddk-using-pnp-custom-notification-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20PnP%20Custom%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


