---
title: Getting started with Windows Store device apps
description: Start here to begin building Windows Store device apps.
ms.assetid: 6280E9CC-422B-4100-8B38-07BADD6A578A
---

# Getting started with Windows Store device apps


Start here to begin building Windows Store device apps.

![get started with windows store device apps](images/devices-diagram-350x350.png)

Device manufacturers can create a Windows Store device app that serves as a companion to their device. Windows Store device apps have more capabilities than regular Windows Store apps and can perform privileged operations, such as firmware updates. Also, Windows Store device apps can start from AutoPlay (on more devices than other apps can), automatically install the first time a device is connected, and extend the printer and camera experiences built into Windows.

**Note**  Windows Runtime device APIs don't require device metadata. That means your app doesn't need to be a Windows Store device app to use them. Windows Store apps can use these APIs to access USB, Human Interface Devices (HID), Bluetooth devices, and more. For more info, see [Integrating devices](http://go.microsoft.com/fwlink/p/?LinkId=533279).

 

If you're looking for info about Windows Store mobile broadband apps, see [Mobile Broadband](http://go.microsoft.com/fwlink/p/?LinkID=301754).

## <span id="1._get_set_up"></span><span id="1._GET_SET_UP"></span>1. Get set up


To develop a Windows Store device app: you need Microsoft Visual Studio, for developing Windows Store apps, and the Device Metadata Authoring Wizard, for developing device metadata.

**Note**  To develop Windows Store device apps in Windows 10, download Microsoft Visual Studio 2015 and Windows Driver Kit (WDK) 10. [Become a Windows Insider to get kits and tools](http://go.microsoft.com/fwlink/p/?LinkId=526775)

 

### <span id="If_you_re_also_developing_drivers"></span><span id="if_you_re_also_developing_drivers"></span><span id="IF_YOU_RE_ALSO_DEVELOPING_DRIVERS"></span>If you're also developing drivers

If you're developing Windows drivers in addition to Windows Store device apps, use Microsoft Visual Studio Professional 2013 or Microsoft Visual Studio Ultimate 2013 to create Windows Store device apps. These editions include the new Device Metadata Authoring Wizard and are also required by the Windows Driver Kit (WDK) 8.1.

1.  [Download Visual Studio Professional 2013 or Visual Studio Ultimate 2013](http://go.microsoft.com/fwlink/p/?LinkId=302196)
2.  [Download the WDK 8.1](http://go.microsoft.com/fwlink/p/?LinkId=302196)

### <span id="If_you_re_not_going_to_be_developing_drivers"></span><span id="if_you_re_not_going_to_be_developing_drivers"></span><span id="IF_YOU_RE_NOT_GOING_TO_BE_DEVELOPING_DRIVERS"></span>If you're not going to be developing drivers

If you don't need to develop drivers, you can use Microsoft Visual Studio Express 2013 for Windows to create Windows Store device apps. But this version of Visual Studio installs a version of the SDK that doesn’t include the Device Metadata Authoring Wizard. To get the new Device Metadata Authoring Wizard, you must also download the standalone Windows 8.1 SDK.

1.  [Download Visual Studio Express 2013 for Windows](http://go.microsoft.com/fwlink/p/?LinkId=302196)
2.  [Download the standalone Windows 8.1 SDK](http://go.microsoft.com/fwlink/p/?LinkId=302196)

## <span id="2._build_some_regular_windows_store_apps"></span><span id="2._BUILD_SOME_REGULAR_WINDOWS_STORE_APPS"></span>2. Build some regular Windows Store apps


A Windows Store device app is a special kind of Windows Store app. So, before you develop your first Windows Store device app, get set up to build some regular Windows Store apps.

-   [Sign up - register for a Windows Store developer account](http://go.microsoft.com/fwlink/p/?LinkId=302197)
-   [Get started with Microsoft Visual Studio 2013](http://go.microsoft.com/fwlink/p/?LinkID=267230)
-   See the [Windows Store design principles](http://go.microsoft.com/fwlink/p/?LinkID=299845)

## <span id="3._learn_what_makes_windows_store_device_apps_special"></span><span id="3._LEARN_WHAT_MAKES_WINDOWS_STORE_DEVICE_APPS_SPECIAL"></span>3. Learn what makes Windows Store device apps special


Learn about the special things that you can do with a Windows Store device app and what it takes to build one.

-   [Meet Windows Store device apps](meet-windows-store-device-apps.md)
-   [Building a Windows Store device app](the-workflow.md)

## <span id="4._download_samples"></span><span id="4._DOWNLOAD_SAMPLES"></span>4. Download samples


You can find device-related samples with the [Devices and sensors](http://go.microsoft.com/fwlink/p/?LinkID=302213) keyword in the sample gallery. Learn how APIs are used in the context of a full sample. You can tell a Windows Store device app because it includes a StoreManifest.xml file that associates it with device metadata. Those samples are tagged with the [Windows Store device app](http://go.microsoft.com/fwlink/p/?LinkID=299847) keyword.

## <span id="4._build_your_own_windows_store_device_app"></span><span id="4._BUILD_YOUR_OWN_WINDOWS_STORE_DEVICE_APP"></span>4. Build your own Windows Store device app


To begin, see [Build a Windows Store device app step-by-step](build-a-windows-store-device-app-step-by-step.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devapps\devapps]:%20Getting%20started%20with%20Windows%20Store%20device%20apps%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




