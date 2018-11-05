---
title: AutoPlay for UWP device apps
description: This topic describes how to use the Device Metadata Authoring Wizard to enable AutoPlay. It also describes how to handle AutoPlay activations in your app.
ms.assetid: A95382E6-DFF4-4F36-9C9B-4B26161160DE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AutoPlay for UWP device apps


Device manufacturers can specify their UWP device app as an AutoPlay handler for their device. They can also let other UWP apps act as AutoPlay handlers for their device. This topic describes how to use the Device Metadata Authoring Wizard to enable AutoPlay. It also describes how to handle AutoPlay activations in your app. For more info about device apps, see [Meet UWP device apps](meet-uwp-device-apps.md).

**Note**  You don't need to use device metadata for all types of AutoPlay. Without device metadata, AutoPlay lets you provide your app as an option when a user connects a device to a PC. This includes non-volume devices like a camera or media player, or volume devices like a USB thumb drive, SD card, or DVD. AutoPlay also lets you register your app as an option when users share files between two machines by using Proximity (tapping). But your app can't install automatically without device metadata. For more info about using AutoPlay when device metadata isn't required, see [Auto-launching with AutoPlay](http://go.microsoft.com/fwlink/p/?LinkID=254861).

 

## <span id="AutoPlay_overview"></span><span id="autoplay_overview"></span><span id="AUTOPLAY_OVERVIEW"></span>AutoPlay overview


Depending on the version of your app, you can enable AutoPlay in these ways:

-   Only your UWP device app can handle AutoPlay activation for your device \[supported in Windows 8, Windows 8.1\].
-   Other UWP apps can handle AutoPlay activation for your device \[supported in Windows 8.1 only\].
-   Your UWP device app and other UWP apps can handle AutoPlay activation for your device \[supported in Windows 8.1 only\].

This example shows an AutoPlay dialog for an app named **Contoso Dashboard** that has registered as the AutoPlay handler for the **Contoso Pedometer** device:

![example autoplay dialog for a device](images/autoplayfordeviceapps.png)

When using device metadata with your app, AutoPlay supports these device types:

| Device class                 | AutoPlay supported in Windows 8                                                                    | AutoPlay supported in Windows 8.1                                                                    |
|------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Digital still camera         | ![autoplay is supported for this device class in windows 8](images/ap-tools.png)                   | ![autoplay is supported for this device class in windows 8.1](images/ap-tools.png)                   |
| Digital video camcorder      | ![autoplay is supported for this device class in windows 8](images/ap-tools.png)                   | ![autoplay is supported for this device class in windows 8.1](images/ap-tools.png)                   |
| Portable media player        | ![autoplay is supported for this device class in windows 8](images/ap-tools.png)                   | ![autoplay is supported for this device class in windows 8.1](images/ap-tools.png)                   |
| Cell phone                   | ![autoplay is supported for this device class in windows 8](images/ap-tools.png)                   | ![autoplay is supported for this device class in windows 8.1](images/ap-tools.png)                   |
| Mobile broadband             | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is not supported for this device class in windows 8.1](images/app-tools-doesnotapply.png) |
| Webcam                       | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is not supported for this device class in windows 8.1](images/app-tools-doesnotapply.png) |
| Human Interface Device (HID) | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is supported for this device class in windows 8.1](images/ap-tools.png)                   |
| Printers, scanners, fax      | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is not supported for this device class in windows 8.1](images/app-tools-doesnotapply.png) |
| PC                           | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is not supported for this device class in windows 8.1](images/app-tools-doesnotapply.png) |
| Smart card                   | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is supported for this device class in windows 8.1](images/ap-tools.png)                   |
| General port                 | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is supported for this device class in windows 8.1](images/ap-tools.png)                   |
| Bluetooth device             | ![autoplay is not supported for this device class in windows 8](images/app-tools-doesnotapply.png) | ![autoplay is not supported for this device class in windows 8.1](images/app-tools-doesnotapply.png) |

 

## <span id="Before_you_begin"></span><span id="before_you_begin"></span><span id="BEFORE_YOU_BEGIN"></span>Before you begin


-   **Make sure you have the Device Metadata Authoring Wizard**. You'll need it to enable AutoPlay. In this release, this wizard is included with Microsoft Visual Studio Professional and Microsoft Visual Studio Ultimate. But if you have Microsoft Visual Studio Express for Windows, you need to download the [standalone SDK for Windows 8.1](http://go.microsoft.com/fwlink/p/?linkid=309209) to get the wizard.

-   **Associate your app with the Microsoft Store**. You'll need your app's package information to enable AutoPlay. For more info, see the *Associate your app with the Microsoft Store* section in [Step 1: Create a UWP device app](step-1--create-a-uwp-device-app.md).

-   **Create the device metadata**. If you haven't started that yet, see [Step 2: Create device metadata](step-2--create-device-metadata.md) in the [Build a UWP device app step-by-step](build-a-uwp-device-app-step-by-step.md) guide.

## <span id="Enabling_AutoPlay"></span><span id="enabling_autoplay"></span><span id="ENABLING_AUTOPLAY"></span>Enabling AutoPlay


The **Device Metadata Authoring Wizard** lets you declare your UWP app to be the default AutoPlay handler for your device. You can also let other UWP apps act as AutoPlay handlers for your device. You can choose either of these options or both of these options.

**To enable AutoPlay with the Device Metadata Authoring Wizard**

1.  Start the **Device Metadata Authoring Wizard** from *%ProgramFiles(x86)%*\\Windows Kits\\8.1\\bin\\x86, by double-clicking **DeviceMetadataWizard.exe**.
2.  Click **Edit Device Metadata**. This will let you edit your existing device metadata package.
3.  In the **Open** dialog box, locate the device metadata package associated with your UWP device app. (It has a **devicemetadata-ms** file extension.)
4.  (Optional.) If you don't have your device app's Package name, Publisher name, and App ID handy, click **App Info** to view the packaging information for your UWP device app.
5.  Click **Windows Info** to specify AutoPlay details.
6.  If you want to specify an app to be the default AutoPlay handler for your device, select **Use a UWP device app**. You can select any UWP app or UWP device app, but that app must handle the AutoPlay activation for your device and specify the corresponding experience ID in the app package manifest (as specified in the next procedure).
    -   **Package name**: In the app package manifest, this is the Name attribute of the Identity element.
    -   **Publisher name**: In the app package manifest, this is the Publisher attribute of the Identity element.
    -   **App ID**: In the app package manifest, this is the ID attribute of the Application element.
    -   **Verb**: This is the identifier for the AutoPlay activation. Your app will use it to determine if the activation came from your device. You can use any value for the Verb setting, except for **open**, which is reserved.
    -   **AutoPlay event type**: Leave this as **Device**. In the device metadata, the wizard will automatically specify the experience ID associated with your UWP device app.

7.  If you want to let other apps act as AutoPlay handlers for your device, select **Enable AutoPlay for registered apps**.
8.  When you're done, click **Next**.
9.  When you see the **Finish** page, write down the **Experience ID**. You'll need it in the next procedure, when you handle the AutoPlay activation in your app.
10. Verify your **Save information** and click **Save** to update your device metadata package.

## <span id="Handling_AutoPlay_activation"></span><span id="handling_autoplay_activation"></span><span id="HANDLING_AUTOPLAY_ACTIVATION"></span>Handling AutoPlay activation


To handle an AutoPlay activation in your app, you need to register for a `windows.autoPlayDevice` extension in the app package manifest and then handle that event in the `OnActivated` event of the Application object. Note that your app can register as an AutoPlay handler for multiple devices.

### <span id="To_register_your_app_as_an_AutoPlay_handler"></span><span id="to_register_your_app_as_an_autoplay_handler"></span><span id="TO_REGISTER_YOUR_APP_AS_AN_AUTOPLAY_HANDLER"></span>To register your app as an AutoPlay handler

To register your app as an AutoPlay handler for your device, you need to specify the experience ID associated with your UWP device app and the AutoPlay **Verb** and **ActionDisplayName** that will be used to activate your app.

1.  Open your app's project in Microsoft Visual Studio.
2.  In **Solution Explorer**, right-click the **Package.appxmanifest** file and select **View Code**. This will display the app package manifest in the XML (Text) Editor.
3.  In the `Application` element, below the `VisualElements` element, paste the following `Extensions` element into your package manifest file.
    ```XML
          <Extensions>
            <Extension Category="windows.autoPlayDevice">
              <AutoPlayDevice>
                <LaunchAction
                    Verb="showDevice1"
                    ActionDisplayName="Launch App for Device 1"
                    DeviceEvent="ExperienceID:{00000000-ABCD-EF00-0000-000000000000}"/>
              </AutoPlayDevice>
            </Extension>
          </Extensions>
    ```

4.  Replace the AutoPlay values from this example with the actual values for your app:
    -   `Verb`: This is the identifier for the AutoPlay activation. Your app will use it to determine if the activation came from your device. If your app was specified as the default AutoPlay handler for your device, this value should match the **Verb** that you specified in the device metadata. If your app was not specified as the default AutoPlay handler for your device, you can use any value for the Verb setting, except for **open**, which is reserved.
    -   `ActionDisplayName`: The string that AutoPlay displays for your app.
    -   `Experience ID`: The experience ID GUID that associates your app with your device. This is the value that you wrote down in the previous procedure.

### <span id="To_handle_AutoPlay_activation"></span><span id="to_handle_autoplay_activation"></span><span id="TO_HANDLE_AUTOPLAY_ACTIVATION"></span>To handle AutoPlay activation

When your device triggers an AutoPlay activation, the activation kind will be `Windows.ApplicationModel.Activation.ActivationKind.device`. Use the `eventObj` object passed by `OnActivated` to check how your app was activated. If it was from AutoPlay, you can use `eventObj` to determine which device ID and AutoPlay verb caused the activation.

In this example, the activation event parameter (eventObj) carries the device's ID as well as the verb for activation.

```JavaScript
<!DOCTYPE html>
<html>
<head>
  <script type="text/javascript">
    function OnActivated(eventObj) {
        if (eventObj.kind == Windows.ApplicationModel.Activation.ActivationKind.launch) {
            // Activated by the user.
        }
        else if (eventObj.kind == Windows.ApplicationModel.Activation.ActivationKind.device) {
            // Activated by a device, for AutoPlay.
            // Device path = eventObj.deviceInformationId;
            // verb (“showDevice1”) = eventObj.verb;
        }
    }

    Windows.UI.WebUI.WebUIApplication.addEventListener("activated", OnActivated, false);
  </script>
</head>

<body>
...
...
...
</body>
</html>
```

## <span id="related_topics"></span>Related topics


[Meet UWP device apps](meet-uwp-device-apps.md)

[Build a UWP device app step-by-step](build-a-uwp-device-app-step-by-step.md)

[Auto-launching with AutoPlay](http://go.microsoft.com/fwlink/p/?LinkID=254861)

[Launching, resuming, and multitasking](http://go.microsoft.com/fwlink/p/?LinkID=309316)

 

 






