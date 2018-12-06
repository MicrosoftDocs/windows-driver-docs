---
title: Getting started with UWP device apps
description: Start here to begin building UWP device apps.
ms.assetid: 6280E9CC-422B-4100-8B38-07BADD6A578A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Getting started with UWP device apps


Start here to begin building UWP device apps.

![get started with windows store device apps](images/devices-diagram-350x350.png)

Device manufacturers can create a UWP device app that serves as a companion to their device. UWP device apps have more capabilities than regular UWP apps and can perform privileged operations, such as firmware updates. Also, UWP device apps can start from AutoPlay (on more devices than other apps can), automatically install the first time a device is connected, and extend the printer and camera experiences built into Windows.

**Note**  Windows Runtime device APIs don't require device metadata. That means your app doesn't need to be a UWP device app to use them. UWP apps can use these APIs to access USB, Human Interface Devices (HID), Bluetooth devices, and more. For more info, see [Integrating devices](http://go.microsoft.com/fwlink/p/?LinkId=533279).

 

If you're looking for info about UWP mobile broadband apps, see [Mobile Broadband](http://go.microsoft.com/fwlink/p/?LinkID=301754).

## <span id="1._get_set_up"></span><span id="1._GET_SET_UP"></span>1. Get set up


To develop a UWP device app: you need Microsoft Visual Studio, for developing UWP apps, and the Device Metadata Authoring Wizard, for developing device metadata.

**Note**  To develop UWP device apps in Windows 10, download Microsoft Visual Studio 2017 and Windows Driver Kit (WDK) 10. [Become a Windows Insider to get kits and tools](http://go.microsoft.com/fwlink/p/?LinkId=526775)

 

### <span id="If_you_re_also_developing_drivers"></span><span id="if_you_re_also_developing_drivers"></span><span id="IF_YOU_RE_ALSO_DEVELOPING_DRIVERS"></span>If you're also developing drivers

If you're developing Windows drivers in addition to UWP device apps, use Microsoft Visual Studio Professional or Microsoft Visual Studio Ultimate to create UWP device apps. These editions include the new Device Metadata Authoring Wizard and are also required by the Windows Driver Kit (WDK) 8.1.

1.  [Download Visual Studio Professional or Visual Studio Ultimate](http://go.microsoft.com/fwlink/p/?LinkId=302196)
2.  [Download the WDK 8.1](http://go.microsoft.com/fwlink/p/?LinkId=302196)

### <span id="If_you_re_not_going_to_be_developing_drivers"></span><span id="if_you_re_not_going_to_be_developing_drivers"></span><span id="IF_YOU_RE_NOT_GOING_TO_BE_DEVELOPING_DRIVERS"></span>If you're not going to be developing drivers

If you don't need to develop drivers, you can use Microsoft Visual Studio Express for Windows to create UWP device apps. But this version of Visual Studio installs a version of the SDK that doesn’t include the Device Metadata Authoring Wizard. To get the new Device Metadata Authoring Wizard, you must also download the standalone Windows 8.1 SDK.

1.  [Download Visual Studio Express for Windows](http://go.microsoft.com/fwlink/p/?LinkId=302196)
2.  [Download the standalone Windows 8.1 SDK](http://go.microsoft.com/fwlink/p/?LinkId=302196)

## <span id="2._build_some_regular_windows_store_apps"></span><span id="2._BUILD_SOME_REGULAR_WINDOWS_STORE_APPS"></span>2. Build some regular UWP apps


A UWP device app is a special kind of UWP app. So, before you develop your first UWP device app, get set up to build some regular UWP apps.

-   [Sign up - register for a Microsoft Store developer account](http://go.microsoft.com/fwlink/p/?LinkId=302197)
-   [Get started with Microsoft Visual Studio](http://go.microsoft.com/fwlink/p/?LinkID=267230)
-   See the [Microsoft Store design principles](http://go.microsoft.com/fwlink/p/?LinkID=299845)

## <span id="3._learn_what_makes_windows_store_device_apps_special"></span><span id="3._LEARN_WHAT_MAKES_WINDOWS_STORE_DEVICE_APPS_SPECIAL"></span>3. Learn what makes UWP device apps special


Learn about the special things that you can do with a UWP device app and what it takes to build one.

-   [Meet UWP device apps](meet-uwp-device-apps.md)
-   [Building a UWP device app](the-workflow.md)

## <span id="4._download_samples"></span><span id="4._DOWNLOAD_SAMPLES"></span>4. Download samples


You can find device-related samples with the [Devices and sensors](http://go.microsoft.com/fwlink/p/?LinkID=302213) keyword in the sample gallery. Learn how APIs are used in the context of a full sample. You can tell a UWP device app because it includes a StoreManifest.xml file that associates it with device metadata. Those samples are tagged with the [UWP device app](http://go.microsoft.com/fwlink/p/?LinkID=299847) keyword.

## <span id="4._build_your_own_windows_store_device_app"></span><span id="4._BUILD_YOUR_OWN_WINDOWS_STORE_DEVICE_APP"></span>4. Build your own UWP device app


To begin, see [Build a UWP device app step-by-step](build-a-uwp-device-app-step-by-step.md).

 

 





