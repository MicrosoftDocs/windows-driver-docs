---
title: Automatic installation for UWP device apps
description: This topic describes how automatic installation works and how the app, metadata, and drivers can be updated and uninstalled.
ms.assetid: ED9C7A63-5D2A-45D3-AD62-32C6876142FC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Automatic installation for UWP device apps


In Windows 8.1, device manufacturers can configure their UWP device apps to automatically install when the user connects their device to the PC. This topic describes how automatic installation works and how the app, metadata, and drivers can be updated and uninstalled. For more info about device apps, see [Meet UWP device apps](meet-uwp-device-apps.md).

**Note**  It's important to consider that the automatic installation feature does not provide a notification to the user when the app is installed. Some users may find this experience confusing and frustrating, and give your app a bad rating.

 

Automatic installation is enabled when you specify your device app's package details in the **UWP device app** portion of the **App Info** page of the **Device Metadata Authoring Wizard**. For more info, see [Step 2: Create device metadata](step-2--create-device-metadata.md).

## <span id="Acquisition_overview"></span><span id="acquisition_overview"></span><span id="ACQUISITION_OVERVIEW"></span>Acquisition overview


A UWP device app can be acquired by the user in one of three ways:

-   **Automatic installation**: The app is automatically acquired and installed the first time a peripheral device is connected to the PC. This is the most common way a UWP device app is installed.
-   **Manual install**: The user finds an app in the Microsoft Store and installs it from there. This is typically how app updates and other UWP apps are installed.
-   **OEM preinstall**: An app for a PC internal device or system component can be preinstalled by an OEM as part of a new PC. For more info, see [Preinstall Apps Using DISM](http://go.microsoft.com/fwlink/p/?LinkId=325524).

**Note**  UWP device apps for PC internal devices are not eligible for automatic installation. They can only be acquired through manual install and OEM preinstall.

 

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


In order for automatic installation to work, the user needs to:

-   Opt in to the **Recommended Settings** during Windows installation.

-   Be signed in to the Microsoft Store.

-   Be online.

This allows Windows to automatically acquire the metadata, app, and drivers (if needed). If no Internet connection is available, the automatic installation will happen at a later time, when it can access the Internet.

## <span id="How_automatic_installation_works"></span><span id="how_automatic_installation_works"></span><span id="HOW_AUTOMATIC_INSTALLATION_WORKS"></span>How automatic installation works


![four steps for automatic installation: device connect, device metadata download, device driver download (as applicable), app download](images/autoinstallbehindscenes.png)

There are four stages to automatic installation:

1.  **Device is connected**: When the device is plugged in or paired with the PC, Windows requests the device metadata from Windows Metadata and Internet Services (WMIS) and, if needed, the device drivers from Windows Update.

2.  **Device metadata is downloaded**: Windows downloads the device metadata from WMIS and parses it to identify the app that's associated with the device. This triggers the download of the app.

3.  **Device drivers are downloaded**: If drivers are needed, Windows downloads them from Windows Update and automatically installs them.

4.  **Device app is installed**: Windows downloads the app and installs it to the **All Apps** screen of the currently logged-in user.

If there's an error during any of these steps, the user will see an error message on the **Devices** page of the **Settings** app.

### <span id="If_there_is_no_Internet_connection"></span><span id="if_there_is_no_internet_connection"></span><span id="IF_THERE_IS_NO_INTERNET_CONNECTION"></span>If there is no Internet connection

If the PC isn't connected to the Internet or is on a metered connection, Windows will wait to perform the automatic installation. The next time the PC has an unrestricted Internet connection, Windows will automatically try again. The installation is performed silently in the background, without interruption to the user.

### <span id="If_the_user_is_not_logged_into_the_Windows_Store"></span><span id="if_the_user_is_not_logged_into_the_windows_store"></span><span id="IF_THE_USER_IS_NOT_LOGGED_INTO_THE_WINDOWS_STORE"></span>If the user is not logged into the Microsoft Store

If the user isn't logged in to the Microsoft Store with a Microsoft account, Windows will wait to perform the automatic installation. The next time the user logs in to the Microsoft Store with a Microsoft account, Windows will automatically try again. The installation is performed silently in the background, without interruption to the user.

## <span id="Updating_device_drivers"></span><span id="updating_device_drivers"></span><span id="UPDATING_DEVICE_DRIVERS"></span>Updating device drivers


Driver updates are distributed through Windows Update as optional updates, as long as the user has opted in to receiving updates from Windows Update. Driver updates aren't automatically distributed to devices if the user has completed device setup and already has metadata and drivers installed.

Driver updates aren't coupled to app updates, so driver updates should be designed to ensure compatibility with existing apps. If a driver update is distributed through Windows Update, or if the user manually reinstalls or updates the driver, the app should handle this appropriately. If your app uses a custom driver, be sure to maintain compatibility and functional contracts. For more info, see [UWP device apps for internal devices](uwp-device-apps-for-specialized-devices.md).

## <span id="Updating_device_metadata"></span><span id="updating_device_metadata"></span><span id="UPDATING_DEVICE_METADATA"></span>Updating device metadata


The metadata that’s distributed by WMIS can be updated to point to a new or different UWP device app. About 8 to 15 days after the submission of updated metadata that indicates a new app, new devices that are connected and set up for the first time will get the new app. But a new app indicated in updated metadata isn't automatically distributed to PCs for which the device setup is already complete, because the users have previously received device metadata for the device.

The UWP device app is automatically downloaded only once, when the device is initially set up. If the device metadata is updated to point to a different app, the old app should advertise the new one to the user, so that users can acquire it from the Microsoft Store manually. Eventually, the old app should be removed from the Microsoft Store. Users can also get to the new app by going to the **Devices** page on the **Settings** app and clicking the **Get app** link for that device.

**Special note for adding privileged access**: If newer metadata grants a UWP device app privileged access to a device (when access did not exist before), submit your metadata at least 20 days before you submit your app. The new metadata will be available to new users 8-15 days after it is submitted. Then, publish the app update to the Microsoft Store. When the user gets the app update, assuming that the user updated any required driver, the app will have privileged access to the device.

## <span id="Updating_device_apps"></span><span id="updating_device_apps"></span><span id="UPDATING_DEVICE_APPS"></span>Updating device apps


UWP device app updates are manually triggered by users, just like any other UWP app updates. The Microsoft Store shows all available app updates to the user. The user manually chooses to update the app. You should design apps to be compatible with older metadata and drivers. The device metadata or driver might not be up-to-date with the app, since manual installation of a UWP device app from the Microsoft Store doesn’t automatically trigger distribution of metadata or drivers.

## <span id="Uninstalling_device_software"></span><span id="uninstalling_device_software"></span><span id="UNINSTALLING_DEVICE_SOFTWARE"></span>Uninstalling device software


The device driver and device metadata are uninstalled independently of the Microsoft Store device app. When a user uninstalls a device, only the driver and metadata are automatically uninstalled as part of the device uninstall.

The UWP device app must be manually uninstalled by the user. When that's done, the device driver and device metadata are not automatically uninstalled.

 

 





