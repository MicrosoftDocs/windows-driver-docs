---
title: Meet UWP device apps
description: This topic provides an overview of the features and capabilities that make a UWP device app uniquely different from a regular UWP app.
ms.assetid: 395745E6-7A97-4B26-A82C-0729E7B999C6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Meet UWP device apps


Device manufacturers can create a UWP device app that serves as a companion to their device. Device apps are able to use the full range of functionality of a peripheral or internal device and can perform privileged operations, such as firmware updates. This topic provides an overview of the features and capabilities that make a UWP device app uniquely different from a regular UWP app.

**Note**  Each of these features is optional. A single device app doesn't need to use all of them. All of these features require device metadata.

 

For more info about what a UWP device app is and how to create one, see [Building UWP device apps](the-workflow.md).

## <span id="_Device_update"></span><span id="_device_update"></span><span id="_DEVICE_UPDATE"></span> Device update


When specified as a privileged app in device metadata, UWP device apps can perform multistep device operations in a device background task. This special type of background task can run to completion even if the app is moved to the background and suspended. This is necessary to allow reliable device servicing, like changes to persistent settings or firmware, without requiring the user to sit and watch a progress bar.

![windows store device apps can perform device updates, like firmware updates, in the background](images/deviceupdateuserconsent.png)

To create a background task for device servicing (device updates), use the [DeviceServicingTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308965) trigger. A similar trigger, [DeviceUseTrigger](http://go.microsoft.com/fwlink/p/?LinkID=308967), which allows for reliable content synchronization, is available for all UWP apps . For more info, see [Device sync and update for UWP device apps](device-sync-and-update-for-uwp-device-apps.md).

**Note**  Device background tasks constrain the amount of time the app can run in the background and are not intended to allow indefinite operation or infinite synchronization.

 

## <span id="AutoPlay"></span><span id="autoplay"></span><span id="AUTOPLAY"></span>AutoPlay


You can configure any UWP app, including your UWP device app, to automatically start when your AutoPlay-supported device is connected to the PC. However, that app must support the AutoPlay handler and specify the experience ID in the app manifest. You can also choose to let additional UWP apps act as AutoPlay handlers for your device.

![example autoplay dialog for a device](images/autoplayfordeviceapps.png)

For more info about AutoPlay and which device classes are supported in Windows 8.1, see [AutoPlay for UWP device apps](autoplay-for-uwp-device-apps.md).

## <span id="Device_apps_for_printers"></span><span id="device_apps_for_printers"></span><span id="DEVICE_APPS_FOR_PRINTERS"></span>Device apps for printers


UWP device apps can highlight the special features of printers through customized print settings flyouts and notifications support. UWP device apps can also display printer status, manage print jobs, and perform printer maintenance.

For info, see these topics:

-   [How to display printer status](how-to-display-printer-status.md)
-   [How to customize print settings](how-to-customize-print-settings.md)
-   [Working with print notifications](working-with-print-notifications.md)
-   [How to manage print jobs](how-to-manage-print-jobs.md)
-   [How to do printer maintenance](how-to-do-printer-maintenance.md)
-   [Printer extension library overview](printer-extension-library-overview.md)

## <span id="Device_apps_for_cameras"></span><span id="device_apps_for_cameras"></span><span id="DEVICE_APPS_FOR_CAMERAS"></span>Device apps for cameras


UWP device apps can also highlight the special features of cameras through customized camera settings and special camera effects.

For more info, see these topics:

-   [How to customize camera options](how-to-customize-camera-options.md)
-   [Creating a camera driver MFT](creating-a-camera-driver-mft.md)
-   [Considerations for driver MFTs on multi-pin cameras](driver-mfts-on-multi-pin-cameras.md)
-   [Identifying the location of internal cameras](identifying-the-location-of-internal-cameras.md)

## <span id="Device_apps_for_internal_devices"></span><span id="device_apps_for_internal_devices"></span><span id="DEVICE_APPS_FOR_INTERNAL_DEVICES"></span>Device apps for internal devices


OEMs and component suppliers can develop UWP device apps for devices that are internal to the PC. To access a device that is associated with the system container, an app must be specified as a privileged app in device metadata. Apps for internal devices are typically preinstalled on the PC and can be downloaded from the Microsoft Store. For more info, see [UWP device apps for internal devices](uwp-device-apps-for-specialized-devices.md).

## <span id="Automatic_installation"></span><span id="automatic_installation"></span><span id="AUTOMATIC_INSTALLATION"></span>Automatic installation


UWP device apps can automatically install when a user connects the device to their PC. If a connection to the Internet isn't available, Windows will try again later. Device apps are installed to **All Apps**.

![windows store device apps can automatically install](images/autoinstalluserexperience.png)

**Warning**  It's important to consider that the automatic installation feature does not provide a notification to the user when the app is installed. Some users may find this experience confusing and frustrating, and give your app a bad rating.

 

For more info about automatic installation, see [Automatic installation for printers and cameras](auto-install-for-uwp-device-apps.md).

## <span id="related_topics"></span>Related topics


[Building UWP device apps](the-workflow.md)

[Automatic installation for UWP device apps](auto-install-for-uwp-device-apps.md)

[AutoPlay for UWP device apps](autoplay-for-uwp-device-apps.md)

[Device sync and update for UWP device apps](device-sync-and-update-for-uwp-device-apps.md)

 

 






