---
title: What's new for UWP device apps
description: This section provides a glimpse of what's new for UWP device apps.
ms.date: 08/12/2021
---

# What's new for UWP device apps

This section provides a glimpse of what's new for UWP device apps. For more info about device apps, see [Meet UWP device apps](meet-uwp-device-apps.md).

> [!TIP]
> Windows Runtime device APIs don't require device metadata. That means your app doesn't need to be a UWP device app to use them. UWP apps can use these APIs to access USB, Human Interface Devices (HID), Bluetooth GATT, Bluetooth RFCOMM, Wi-Fi Direct devices, and more. For more info, see [Integrating devices](/previous-versions/windows/apps/dn263141(v=win.10)).

## What's new for Windows 10

With Windows 10, there are no changes to the Microsoft Store device app functionality. The Windows 8.1 processes for building, testing, and submitting UWP device apps will continue to work with Windows 10. However, we recommend developing a Universal Windows Platform (UWP) app with custom capabilities. For more info, see [Hardware Support App (HSA): Steps for App Developers](hardware-support-app--hsa--steps-for-app-developers.md).

## Device metadata wizard

Windows 8.1 introduces a new device metadata wizard. Easily create device metadata packages for UWP device apps without needing to edit raw XML. The new wizard can also validate device metadata against your app locally, before you submit it to the Dashboard. For more info about how this wizard fits into the process, see [Build a UWP device app step-by-step](build-a-uwp-device-app-step-by-step.md).

> [!NOTE]
> To get the Device Metadata Authoring Wizard, you must install the [standalone SDK for Windows 8.1](https://developer.microsoft.com/windows/hardware/) before completing the steps in this topic. Installing Microsoft Visual Studio Express for Windows installs a version of the SDK that doesn't include the wizard.

## Background tasks for device sync and update

In Windows 8.1, UWP device apps can perform multi-step device operations in a background task so that they can run to completion even if the app is moved to the background and suspended. This is necessary to allow reliable device servicing (changes to persistent settings or firmware) and content synchronization, without requiring the user to sit and watch a progress bar. Use the [DeviceServicingTrigger](/uwp/api/Windows.ApplicationModel.Background.DeviceServicingTrigger) for device servicing and the [DeviceUseTrigger](/uwp/api/Windows.ApplicationModel.Background.DeviceUseTrigger) for content synchronization. Note that these background tasks constrain the amount of time the app can run in the background and are not intended to allow indefinite operation or infinite synchronization. For more info, see [Device sync and update for UWP device apps](device-sync-and-update-for-uwp-device-apps.md).

> [!NOTE]
> The [DeviceUseTrigger](/uwp/api/Windows.ApplicationModel.Background.DeviceUseTrigger), for device sync, doesn't require device metadata.

## AutoPlay for UWP device apps

You can configure your UWP device app to automatically launch when your peripheral device is plugged in to the PC (after the app is installed). In Windows 8.1, AutoPlay for device apps adds support for Human Interface Devices (HID), smart cards, and the general port. For more info, see [AutoPlay for UWP device apps](autoplay-for-uwp-device-apps.md).

## Printer capabilities

In Windows 8.1, UWP device apps can manage print jobs and perform printer maintenance tasks. For more info see [How to manage print jobs](how-to-manage-print-jobs.md) and [How to do printer maintenance](how-to-do-printer-maintenance.md).

You can see these features highlighted in the new sample, [Print job management and printer maintenance](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Print%20job%20management%20and%20printer%20maintenance). The printer extension library, that's included with the sample, wraps the COM implementation of the COM interface PrinterExtensionLib. This library was designed to make it easy to reuse in your own UWP device app.

## User experience changes

To provide an experience consistent with other UWP apps installed on Windows 8.1, UWP device apps are not pinned to **Start** when they're installed. From **Start**, users can swipe up (from the center of the screen) to view all apps, including recently installed UWP device apps.

The Windows 8.1 built-in Camera app no longer includes an **Options** button. This means that a customized camera-options flyout from a UWP device app won't appear in that app. However, any other UWP app that uses the **Windows.Media.Capture.CameraCaptureUI** class can still expose a customized flyout for **More options**, when installed.
