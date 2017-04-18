---
title: What's new for Windows Store device apps
description: This section provides a glimpse of what's new for Windows Store device apps.
ms.assetid: AF18ACFD-EA38-4ABD-9369-3974C019E132
---

# What's new for Windows Store device apps


This section provides a glimpse of what's new for Windows Store device apps. For more info about device apps, see [Meet Windows Store device apps](meet-windows-store-device-apps.md).

**Tip**  Windows Runtime device APIs don't require device metadata. That means your app doesn't need to be a Windows Store device app to use them. Windows Store apps can use these APIs to access USB, Human Interface Devices (HID), Bluetooth GATT, Bluetooth RFCOMM, Wi-Fi Direct devices, and more. For more info, see [Integrating devices](http://go.microsoft.com/fwlink/p/?LinkId=533279).

 

## <span id="What_s_new_for_Windows_10"></span><span id="what_s_new_for_windows_10"></span><span id="WHAT_S_NEW_FOR_WINDOWS_10"></span>What's new for Windows 10


With Windows 10, there are no changes to the Windows Store device app functionality. The Windows 8.1 processes for building, testing, and submitting Windows Store device apps will continue to work with Windows 10. However, it is recomended to develop a Universal Windows Platform app with Custom Capabilities. For more info, see [Developing a Universal Windows Platform app with Custom Capabilities](developing-a-universal-windows-platform-app-with-custom-capabilities.md)

## <span id="Device_metadata_wizard"></span><span id="device_metadata_wizard"></span><span id="DEVICE_METADATA_WIZARD"></span>Device metadata wizard


Windows 8.1 introduces a new device metadata wizard. Easily create device metadata packages for Windows Store device apps without needing to edit raw XML. The new wizard can also validate device metadata against your app locally, before you submit it to the Dashboard. For more info about how this wizard fits into the process, see [Build a Windows Store device app step-by-step](build-a-windows-store-device-app-step-by-step.md).

**Note**  To get the Device Metadata Authoring Wizard, you must install the [standalone SDK for Windows 8.1](http://go.microsoft.com/fwlink/p/?linkid=309209) before completing the steps in this topic. Installing Microsoft Visual Studio Express 2013 for Windows installs a version of the SDK that doesn't include the wizard.

 

## <span id="_Background_tasks_for_device_sync_and_update"></span><span id="_background_tasks_for_device_sync_and_update"></span><span id="_BACKGROUND_TASKS_FOR_DEVICE_SYNC_AND_UPDATE"></span> Background tasks for device sync and update


In Windows 8.1, Windows Store device apps can perform multi-step device operations in a background task so that they can run to completion even if the app is moved to the background and suspended. This is necessary to allow reliable device servicing (changes to persistent settings or firmware) and content synchronization, without requiring the user to sit and watch a progress bar. Use the [DeviceServicingTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308965) for device servicing and the [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967) for content synchronization. Note that these background tasks constrain the amount of time the app can run in the background and are not intended to allow indefinite operation or infinite synchronization. For more info, see [Device sync and update for Windows Store device apps](device-sync-and-update-for-windows-store-device-apps.md).

**Note**  The [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967), for device sync, doesn't require device metadata.

 

## <span id="AutoPlay_for_Windows_Store_device_apps"></span><span id="autoplay_for_windows_store_device_apps"></span><span id="AUTOPLAY_FOR_WINDOWS_STORE_DEVICE_APPS"></span>AutoPlay for Windows Store device apps


You can configure your Windows Store device app to automatically launch when your peripheral device is plugged in to the PC (after the app is installed). In Windows 8.1, AutoPlay for device apps adds support for Human Interface Devices (HID), smart cards, and the general port. For more info, see [AutoPlay for Windows Store device apps](autoplay-for-windows-store-device-apps.md).

## <span id="Printer_capabilities"></span><span id="printer_capabilities"></span><span id="PRINTER_CAPABILITIES"></span>Printer capabilities


In Windows 8.1, Windows Store device apps can manage print jobs and perform printer maintenance tasks. For more info see [How to manage print jobs](how-to-manage-print-jobs.md) and [How to do printer maintenance](how-to-do-printer-maintenance.md).

You can see these features highlighted in the new sample, [Print job management and printer maintenance](http://go.microsoft.com/fwlink/p/?LinkID=299829). The printer extension library, that's included with the sample, wraps the COM implementation of the COM interface PrinterExtensionLib. This library was designed to make it easy to reuse in your own Windows Store device app.

## <span id="User_experience_changes"></span><span id="user_experience_changes"></span><span id="USER_EXPERIENCE_CHANGES"></span>User experience changes


To provide an experience consistent with other Windows Store apps installed on Windows 8.1, Windows Store device apps are not pinned to **Start** when they're installed. From **Start**, users can swipe up (from the center of the screen) to view all apps, including recently installed Windows Store device apps.

The Windows 8.1 built-in Camera app no longer includes an **Options** button. This means that a customized camera-options flyout from a Windows Store device app won't appear in that app. However, any other Windows Store app that uses the **Windows.Media.Capture.CameraCaptureUI** class can still expose a customized flyout for **More options**, when installed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devapps\devapps]:%20What's%20new%20for%20Windows%20Store%20device%20apps%20%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




