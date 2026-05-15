---
title: Camera Companion Apps
description: Describes companion apps, an extensibility feature for manufacturers of cameras to build custom applications that can configure the camera and adjust default image settings.
ms.date: 12/19/2024
ms.topic: concept-article
---

# Camera companion apps

This article describes companion apps, an extensibility feature for manufacturers of cameras to build custom applications that can configure the camera and adjust default image settings.

## Introduction

Windows 11 provides a camera companion app framework that allows manufacturers to develop applications with the following capabilities:

- Ability to display and/or modify the same default value settings that the camera settings page supports (for example, Brightness, Contrast, Background effects, and so on).

- Ability to register, update, or delete default value settings for other camera controls that are known to Windows but aren't exposed through the camera settings page (for example, the Hue control).

- Ability to register, update, or delete default value settings for manufacturer-proprietary camera controls (for example, the on/off control for a camera manufacturer's custom lighting adjustment effect).

When a camera registers an associated companion app, an entry is added to the camera settings page. If the app is installed, it can be launched from the camera settings page, else a link to the Microsoft Store is displayed to download it.

Companion apps have special access to an API that allows them to register, update, or delete default values like the camera settings page.

### Terminology and prerequisites

| Term | Definition |
|--|--|
| Companion app | A custom application developed by the camera manufacturer that allows configuration and management of a camera in addition to the camera settings page. |
| Current value | The value of a camera control that is currently active in the camera's ISP and held in the camera's temporary memory. |
| Default value | An initial value of a camera control that is stored to disk and saved for a specific camera, for a specific user account, on a specific PC. |
| HSA | Hardware Support App, a framework supported by Microsoft to automatically download and install hardware-associated apps from the Microsoft Store when the device is connected. |
| NPU | Neural Processing Unit, dedicated hardware designed to process artificial intelligence workloads with high throughput and efficiency. |
| Windows Studio Effects | A collection of video effects available on select Windows PCs with NPUs. |
| UVC | USB Video Class, the standardized interface for controlling and streaming from USB connected cameras. |

## Companion app requirements

Companion apps must be [packaged applications](/windows/apps/package-and-deploy) with a package identity. The companion app must also be released on the Microsoft Store, which allows the camera settings page to guide customers to the store to install the app if it isn't already installed.

Traditional desktop applications without a package identity can't be used as a companion app.

### Companion apps as HSAs

Companion apps aren't required to also be configured as a [Hardware Support App](/windows-hardware/drivers/devapps/hardware-support-app--hsa--steps-for-app-developers), but is highly recommended. HSAs are special apps in the Microsoft Store that are associated with a specific hardware device. When that device is connected to a PC, the HSA is automatically downloaded and installed from the Microsoft Store when available.

## Associate a companion app with a camera

The manufacturer of a camera can associate a companion app by populating a specific Device Property key with the Package Family Name (PFN) of the Companion app:

| Name | Type | Data |
|--|--|--|
| SCSVCamPfn | REG_SZ | \<PFN\> |

To identify the PFN of the companion app, run [Get-AppxPackage](/powershell/module/appx/get-appxpackage?view=windowsserver2022-ps&preserve-view=true) from PowerShell, for example:

Get-AppxPackage -Name *CompanionAppName*

To associate the companion app to a camera, use an [MSOS descriptor](create-camera-device-property-keys-from-ms-os-descriptor.md) in a UVC camera or the AddReg directive in the INF of the camera driver. For example, using the INF file:

```inf
[SocCaptureSim.RearCamera.AddReg]

HKR,,SCSVCamPfn,,%AppPFN%

...

[Strings]

AppPFN="Contoso.CameraCompanion_xxxxxxxx00000"

```

When a companion app is associated with a camera, the camera settings page includes a link to the companion app under the "Related settings" heading of the camera's specific settings page.

If the companion app is already installed, a link displays to "Open *{companion app name}*". When clicked, the app is launched.

If the companion app isn't already installed, a link displays to launch the Microsoft Store to download and install the app.

A camera can only have one companion app associated with it.

## Launch a companion app from the camera settings page

When the camera settings page launches the companion app, the symbolic link of the camera is passed as context via the [Application.OnLaunched](/uwp/api/windows.ui.xaml.application.onlaunched?view=winrt-22000&preserve-view=true) arguments.

| Argument | Type | Data |
|--|--|--|
| cameraId | String | Symbolic Link |

This functionality allows the companion app to display the correct camera's settings under the following scenarios:

1. A single companion app supports multiple cameras on a single system (for example, an OEM provided application supports the Front and Rear cameras on a tablet).

1. A customer has two of the same (or same brand) cameras connected to their system that are managed by the same companion app.

### Launch the camera settings page from a companion app

A companion app can launch the Windows camera settings page using a deeplink URI. For more information, see [Launch the camera settings page](/windows/uwp/audio-video-camera/launch-camera-settings).

## Configure default values from companion apps

A companion app can use the [**IMFCameraConfigurationManager**](/windows/win32/api/mfidl/nn-mfidl-imfcameraconfigurationmanager) API to configure the current user's default value configuration. This API allows the companion app to read any configured default values (for example, the default values set by the user using the camera settings page), modify any default values, register any new default values, or remove saved default values.

Default values are registered in the system's database as a pair of a KS Property GUID and corresponding value. This allows the architecture to be agnostic to the definition of the KS Property. This flexibility allows a companion app to set, edit, or delete default values for any of the following settings:

- Settings that are also configurable using the camera settings page (for example, Brightness, Contrast, Background effects, and so on)

- Settings for other camera controls that are known to Windows but aren't exposed through the camera settings page (for example, the Hue control)

- Settings for manufacturer-proprietary camera controls (for example, the on/off control for a camera manufacturer's custom lighting adjustment effect)

### Configure brightness from a companion app

There are a few ways for a camera to control the effective brightness of the captured image. For example, brightness can be increased by applying a simple gain to the image, or it can be increased by increasing the exposure time of the camera.

Windows supports a legacy Brightness control ([**KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS**](ksproperty-videoprocamp-brightness.md)) that was designed with simple gain controls in mind. Windows also supports an exposure compensation control ([**KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION**](ksproperty-cameracontrol-extended-evcompensation.md)) that is designed to command a positive or negative exposure value bias to a camera's Auto Exposure algorithm.

Regardless of which Brightness control is used by a camera, it should be implemented in the camera such that when "centered", the brightness is neutral, and that the customer can apply an offset by raising or lowering the value. For the best image quality, it's highly recommended for cameras to support the exposure compensation control so that if a customer adjusts the Brightness control in the camera settings page or in a companion app, the camera is commanded to apply a fixed positive or negative bias to exposure regardless of the lighting conditions at any time.

For more information, see the [camera settings page](camera-settings-page.md) for the behavior of the Brightness control on the camera settings page based on which control the camera implements. If a companion app also offers a Brightness slider, it's critical to replicate the logic to ensure synchronization between the Brightness slider in the camera settings page and the companion app.

The companion app sample linked below includes a reference implementation of this logic.

## Monitoring for real-time current value changes

If a companion app is running at the same time as the camera settings page, it's possible that the customer may change a default value using the camera settings page while the companion app is concurrently running in shared mode to display a preview. In this case, it's desirable for the companion app to monitor for changes to the default value of the controls so that it can stay in sync.

To do so, the companion app can use the [**IMFCameraControlMonitor**](/windows/win32/api/mfidl/nn-mfidl-imfcameracontrolmonitor) to monitor changes to the Current Value of controls (KS Properties) of interest. These changes can occur due to:

- A camera application (for example, Microsoft Teams) is using the camera and makes a change to the Current Value of a control.

- The camera settings page is using the camera and makes a change to the default value of a control (which also updates the Current Value).

This API can be used as a trigger to re-read the default value for a control of interest using the [**IMFCameraConfigurationManager**](/windows/win32/api/mfidl/nn-mfidl-imfcameraconfigurationmanager) API, and update the UI if any default values have changed.

## Companion app samples

A sample companion app is available on GitHub: [CameraSettingsExternalSettingsApp sample](https://github.com/microsoft/Windows-Camera/tree/master/Samples/CameraSettingsExternalSettingsApp). This sample demonstrates how to use the [**IMFCameraConfigurationManager**](/windows/win32/api/mfidl/nn-mfidl-imfcameraconfigurationmanager) API to change the default value for Contrast, Brightness, and Background Segmentation.

Another sample application demonstrating how to use the [**IMFCameraControlMonitor**](/windows/win32/api/mfidl/nn-mfidl-imfcameracontrolmonitor) API to monitor for changes to controls of interest is available on GitHub: [ControlMonitorApp sample](https://github.com/microsoft/Windows-Camera/tree/master/Samples/ControlMonitorApp).

## See also

[Application.OnLaunched](/uwp/api/windows.ui.xaml.application.onlaunched?view=winrt-22000&preserve-view=true)

[Camera settings page](camera-settings-page.md)

[CameraSettingsExternalSettingsApp sample](https://github.com/microsoft/Windows-Camera/tree/master/Samples/CameraSettingsExternalSettingsApp)

[ControlMonitorApp sample](https://github.com/microsoft/Windows-Camera/tree/master/Samples/ControlMonitorApp)

[Get-AppxPackage](/powershell/module/appx/get-appxpackage?view=windowsserver2022-ps&preserve-view=true)

[Hardware Support App](/windows-hardware/drivers/devapps/hardware-support-app--hsa--steps-for-app-developers)

[**IMFCameraConfigurationManager**](/windows/win32/api/mfidl/nn-mfidl-imfcameraconfigurationmanager)

[**IMFCameraControlMonitor**](/windows/win32/api/mfidl/nn-mfidl-imfcameracontrolmonitor)

[**KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS**](ksproperty-videoprocamp-brightness.md)

[**KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION**](ksproperty-cameracontrol-extended-evcompensation.md)

[Launch the camera settings page](/windows/uwp/audio-video-camera/launch-camera-settings)

[MSOS descriptor](create-camera-device-property-keys-from-ms-os-descriptor.md)

[Packaged applications](/windows/apps/package-and-deploy)
