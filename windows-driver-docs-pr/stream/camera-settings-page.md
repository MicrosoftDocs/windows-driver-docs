---
title: Camera Settings Page
description: Describes the features and operation of the camera settings page in Windows 11
ms.date: 12/18/2024
---

# Camera settings page

This article describes the features and operation of the camera settings page in Windows 11, and the default values framework that allows configuration of the camera configuration applied when an application starts the camera.

## Introduction

Prior to Windows 11, the only way for customers to adjust image controls such as Brightness, Contrast, Sharpness, and so on, was to use a utility provided by the camera manufacturer (if available) or if the camera application had UI to adjust the desired image control.

The persistence of the adjusted values typically followed a last-in model, making it dependent on the behavior of the applications using the camera. For example, if a customer adjusted the camera's brightness level using the manufacturer's utility, that value would only hold until another application writes to the brightness control. This meant that the behavior of one application had the potential to impact the camera experience with another application.

In Windows 11, a new Default Value framework was introduced, allowing customers to configure how their camera behaves whenever it's started by an application. A new extensible camera settings page was also introduced to manage cameras, including the default values.

### Terminology and prerequisites

| Term | Definition |
|--|--|
| Companion app | A custom application developed by the camera manufacturer that allows configuration and management of a camera in addition to the camera settings page. |
| Current value | The value of a camera control that is currently active in the camera's ISP and held in the camera's temporary memory. |
| Default value | An initial value of a camera control that is stored to disk and saved for a specific camera, for a specific user account, on a specific PC. |
| ISP | Image Signal Processor, the microchip within the camera responsible for controlling and reading from the sensor, processing the image data, and transferring the image data to the host PC. |
| NPU | Neural Processing Unit, dedicated hardware designed to process artificial intelligence workloads with high throughput and efficiency. |
| Sensor | The microchip within a camera that is responsible for capturing images and translating them to digital signals. |
| Windows Studio Effects | A collection of video effects available on select Windows PCs with NPUs. |
| UVC | USB Video Class, the standardized interface for controlling and streaming from USB connected cameras. |

## Viewing and managing cameras

The camera settings page can be launched by navigating to **Settings > Bluetooth & devices > Cameras**. This page was introduced in Windows 11 and isn't available on older versions of Windows.

### Network cameras

The camera settings page allows customers to initiate a search of the local network for ONVIF-conformant network/IP cameras and connect them to the system. Once connected, the network camera appears and operates like a traditional (for example, USB) camera.

Network cameras that have been connected to a system can be removed by selecting the camera from the **Connected cameras** list in the camera settings page, and then selecting the **Remove** button.

For more information, see [Network cameras](network-cameras.md).

### Connected cameras

The camera settings page displays the cameras currently connected to the system, and allows customers to access a subpage with additional settings related to each camera. These settings include default image settings, the ability to disable the camera, and in the case of network cameras, the ability to remove/disconnect the camera.

Enabled color cameras are shown in the list, and specialty cameras (such as IR cameras) aren't shown.

### Disabled cameras

When a camera is disabled through the camera settings page, a separate section appears with a list of disabled cameras. Clicking on **Enable** will re-enable the selected camera.

> [!NOTE]
> Some cameras may not show in the camera settings page if they're missing a driver, in a nonfunctional state, or disabled through alternate utilities such as Device Manager.

## Configuring individual cameras

By selecting an individual camera from the **Connected cameras** list in the camera settings page, a subpage is launched that displays a camera preview, allows management of the camera, and allows configuration of default imaging settings.

The default settings displayed on this page are saved per camera and per user account. Additionally, default imaging settings aren't backed up and restored during an OS reinstallation or during setup of a new Windows device.

### Disabling a camera

To disable a camera, select it from the **Connected cameras** list on the camera settings page to open its subpage, and then select the **Disable** button. Selecting this button triggers a prompt to confirm before disabling the camera.

On some systems, more than one camera shares a common ISP, so disabling one camera can disable multiple cameras. This is common on tablet form factor devices that have both an integrated front-facing (videoconferencing) and world-facing camera. In this scenario, the confirmation prompt includes a message indicating that disabling one camera causes other cameras on the system to be disabled as a group.

In some circumstances, cameras require a reboot of the system to be disabled. In this scenario, the camera continues to display in the **Connected cameras** list of the camera settings page, but will remain greyed out with a message indicating the need to reboot the PC.

### Troubleshooting a camera

To troubleshoot a camera, select it from the **Connected cameras** list on the camera settings page to open its subpage, and then select the **Troubleshoot** button. Selecting this button launches the **Get Help** utility that executes an interactive camera troubleshooting experience.

### Adjusting basic image settings

When a camera is selected from the **Connected cameras** list on the camera settings page, a selection of sliders and/or toggles for basic imaging settings may be available under the **Basic Settings** section, as supported by the camera.

The following table lists available basic settings, and the corresponding KS Property (or UVC Control, for USB cameras) that the camera must implement for each setting to be visible. If none of the settings are available on the camera, the **Basic Settings** section won't be visible.

| Basic setting | KS property | UVC control |
|--|--|--|
| Brightness | See remarks following this table | See remarks following this table |
| Contrast | [**KSPROPERTY_VIDEOPROCAMP_CONTRAST**](ksproperty-videoprocamp-contrast.md) | PU_CONTRAST_CONTROL |
| Sharpness | [**KSPROPERTY_VIDEOPROCAMP_SHARPNESS**](ksproperty-videoprocamp-sharpness.md) | PU_SHARPNESS_CONTROL |
| Saturation | [**KSPROPERTY_VIDEOPROCAMP_SATURATION**](ksproperty-videoprocamp-saturation.md) | PU_SATURATION_CONTROL |
| Video HDR | [**KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR**](ksproperty-cameracontrol-extended-videohdr.md) | [**MSXU_CONTROL_VIDEO_HDR**](uvc-extensions-1-5.md) |

The Brightness control is a unique control because, depending on what controls the camera supports, it maps to either [**KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION**](ksproperty-cameracontrol-extended-evcompensation.md) ([**MSXU_CONTROL_EVCOMPENSATION**](uvc-extensions-1-5.md) for UVC Cameras), or the legacy [**KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS**](ksproperty-videoprocamp-brightness.md) (PU_BRIGHTNESS_CONTROL for UVC cameras) control.

The ideal behavior of a slider for default image brightness is to act as a relative offset/bias to the camera's Auto Exposure (AE) algorithm. This ensures that adjustments are scene-independent and the camera can be set to always be a bit brighter or a bit darker for any given lighting environment.

The EV Compensation control is explicitly designed to act as a bias to a camera's AE algorithm. When a camera supports the EV Compensation control, the Brightness slider in the camera settings maps to this control. When the camera doesn't support the EV Compensation control but supports the legacy Brightness control, the Brightness slider maps to the legacy Brightness control. When neither control is supported by the camera, the Brightness slider isn't visible in the camera settings page.

Similarly, apps that offer in-app brightness sliders are encouraged to use the same logic to map the in-app brightness control to the EV Compensation or legacy Brightness control. This logic is implemented in the Windows Camera app.

### Adjusting Windows Studio Effects (or Camera Effects)

When a camera is selected from the **Connected cameras** list on the camera settings page, a selection of toggles and/or radio buttons for camera effect settings may be available under the **Camera Effects** section, as supported by the camera.

Windows devices that support Windows Studio Effects will instead name the section **Windows Studio Effects**.

The following is the list of available Camera Effects, and the corresponding KS Property that the camera must implement for each setting to be visible. If none of the settings are available on the camera, the **Camera Effects** (or **Windows Studio Effects**) section won't be visible.

| Camera effect | KS property |
|--|--|
| Standard Blur | [**KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION**](ksproperty-cameracontrol-extended-backgroundsegmentation.md) (with KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR flag) |
| Portrait Blur | [**KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION**](ksproperty-cameracontrol-extended-backgroundsegmentation.md) (with KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS flag) |
| Standard Eye Contact | [**KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION**](ksproperty-cameracontrol-extended-eyegazecorrection.md) (with KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON flag) |
| Enhanced Eye Contact  | [**KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION**](ksproperty-cameracontrol-extended-eyegazecorrection.md) (with KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON flag) |
| Auto Framing | [**KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW**](ksproperty-cameracontrol-extended-digitalwindow.md) (with KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING flag) |

When a camera only supports **Standard Blur**, the control displays as an on/off toggle with the label **Background blur**.

When a camera supports both **Standard Blur** and **Portrait Blur**, the control displays as an on/off toggle with the label **Background effects**, plus a radio button to select **Standard blur** and **Portrait blur** that is available when **Background effects** is turned on.

When a camera only supports **Standard Eye Contact**, the control displays as an on/off toggle with the label **Eye contact**.

When a camera supports both **Standard Eye Contact** and **Enhanced Eye Contact**, the control displays as an on/off toggle with the label **Eye contact**, plus a radio button to select **Standard** and **Enhanced** that is available when **Eye contact** is turned on.

### Adjusting Video Rotation

When an external camera is selected from the **Connected cameras** list on the camera settings page, a dropdown is available allowing the customer to select a **Video rotation**. Available options are **No rotation**, **Right 90°**, **Left 90°**, or **180°**.

The **Video rotation** setting is only available for external cameras. If the camera is in use by another application when the setting is changed, it will not apply until the next time the camera is used.

> [!NOTE]
> When **Video rotation** is set to any value other than "No rotation", Windows removes all compressed data types (for example, MJPEG, H.264, and so on) from the camera and strictly outputs uncompressed data types. Legacy applications and/or cameras that depend on compressed data types being available may not function correctly when the **Video rotation** setting is configured.

### Resetting camera settings

When a camera is selected from the **Connected cameras** list on the camera settings page, the **Reset settings** button allows all camera settings to be reset to factory defaults.

When this button is used, changes to the **Basic Settings**, **Windows Studio Effects** (or **Camera Effects**), or **Video rotation** controls are erased, and the camera is restarted with its factory configuration.

Using the **Reset settings** button also resets any default settings that were configured by a Companion App.

## Default value behavior

Changes to the **Basic Settings**, **Windows Studio Effects** (or **Camera Effects**), or **Video rotation** controls are applied immediately to the live camera stream (and visible in the preview) and are also saved as the default value for the next time an application opens the camera.

When no applications are using the camera, the behavior of the camera settings page is simple. Changes that customers make to the **Basic Settings**, **Windows Studio Effects** (or **Camera Effects**), or **Video rotation** controls are immediately applied to the live camera preview stream, and saved as updated default values that will apply when applications start the camera in the future.

### How default values apply to camera applications

When an application opens and starts the camera, Windows starts the camera and then applies any default values to the camera that were configured through the camera settings page, unless the application wrote a given control after opening the camera but before starting the stream.

For example, consider a scenario where the customer set the default Contrast to 55% using the camera settings page, and then starts the camera in an application (like Microsoft Teams):

1. **If the application opens a handle to the camera and then requests the stream to start**: Windows sets the camera's current value for the Contrast control (KSPROPERTY_VIDEOPROCAMP_CONTRAST) to 55%. Control of the camera is then handed over to the application.

1. **If the application opens a handle to the camera, writes the current value of the Contrast control to 45%, and then requests the stream to start**: Windows skips writing the Current Value for the Contrast control because the app already preinitialized it.

Once the camera is running, the application may do the following with the current value of the Contrast control:

1. **Do nothing**, in which case the Contrast remains at the value set during initialization for the duration of the session.

1. **Write it to a different value**, in which case the Contrast changes to whatever the application set it to, for the duration of the session or until the same application writes it again, whichever comes first.

When camera applications (like Microsoft Teams) write to camera controls (Contrast, Brightness, and so on), they do so by writing the camera's KS properties. This changes the current value of the control on the camera, and doesn't modify the default value like the camera settings page does.

### Using the camera settings page while the camera is in use

Behavior can be more complex when the camera settings page is used while another application is using the camera. The camera settings page always displays the default values, but the preview stream (and the video stream shown in the application) represents the Current Values set on the camera.

Consider a basic scenario where an application opens the camera, and the application has no UI to adjust the Current Value of the Contrast control. If the customer opens the camera settings page to adjust the Contrast while the application is running, there are no issues because the app hasn't changed the Current Value of the Contrast control away from the Default Value.

Now, consider a more complex scenario, where the Default Value of the Contrast control is 55%, but the application that is using the camera has set the Current Value of the Contrast control to 45%. In this case, the camera stream is running with the Contrast set to 45%. If the customer opens the camera settings page while the application is running, they'll see a preview that reflects a Contrast of 45%, but the Contrast slider below will show the Default Value of 55%, which is a mismatch.

At this point, the customer could change the Contrast using their application. The Current Value of the Contrast would change, impacting the video stream in both the app and in the camera settings page preview, however the Contrast slider in the camera settings page will continue to display 55%.

Alternatively, the customer could change the Contrast using the camera settings page. For example, assume they adjusted the slider to 40%. The camera settings page saves 40% as the new Default Value, and set the camera's Current Value to 40%. This causes the video stream in both the camera settings page and in the application to change and reflect a Contrast of 40%.

> [!NOTE]
> Some applications may use the [**IMFCameraControlMonitor**](/windows/win32/api/mfidl/nn-mfidl-imfcameracontrolmonitor) API to monitor for external changes to controls. Consider an application that wishes to keep the Contrast at 45% while using the camera - that application may monitor the Contrast KS Property, and immediately re-write the KS Property back to 45% if it is changed externally using the camera settings page.

Synchronization issues are uncommon, and they only happen in the specific scenario where a customer makes real-time changes to image settings within an application, and concurrently launches the camera settings page to adjust the same image setting.

To manage concurrent use situations, an info banner is displayed in the camera settings page when the camera is in use by another application, indicating the changes made in the camera settings page or in the application will affect both the application and the preview in the camera settings page.

## Camera Companion Apps

Camera manufacturers may wish to provide their own custom applications that allow customers to change default camera settings.

Windows 11 provides a Camera Companion App framework that allows manufacturers to develop applications with the following capabilities:

- Ability to display and/or modify the same Default Value settings that the camera settings page supports (for example, Brightness, Contrast, Background effects, and so on).

- Ability to register, update, or delete Default Value settings for other camera controls that are known to Windows but aren't exposed through the camera settings page (for example, the Hue control).

- Ability to register, update, or delete Default Value settings for manufacturer-proprietary camera controls (for example, the on/off control for a camera manufacturer's custom lighting adjustment effect).

When a camera associates a specific Companion App with it, an entry for that app is added to the camera settings page. If the app is installed, it can be launched from the camera settings page, else a link to the Microsoft Store is displayed to download it.

For more information about building a Companion App, see [Camera companion apps](camera-companion-apps.md).

## Programmatically launching the camera settings page

The camera settings page can be launched by an application using a deep link URI, which is helpful for applications that wish to allow quick access to common camera controls. For more information, see [Launch the camera settings page](/windows/uwp/audio-video-camera/launch-camera-settings).

## See also

[Camera Companion Apps](camera-companion-apps.md)

[**IMFCameraControlMonitor**](/windows/win32/api/mfidl/nn-mfidl-imfcameracontrolmonitor)

[**KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION**](ksproperty-cameracontrol-extended-backgroundsegmentation.md)

[**KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW**](ksproperty-cameracontrol-extended-digitalwindow.md)

[**KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION**](ksproperty-cameracontrol-extended-evcompensation.md)

[**KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION**](ksproperty-cameracontrol-extended-eyegazecorrection.md)

[**KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR**](ksproperty-cameracontrol-extended-videohdr.md)

[**KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS**](ksproperty-videoprocamp-brightness.md)

[**KSPROPERTY_VIDEOPROCAMP_CONTRAST**](ksproperty-videoprocamp-contrast.md)

[**KSPROPERTY_VIDEOPROCAMP_SATURATION**](ksproperty-videoprocamp-saturation.md)

[**KSPROPERTY_VIDEOPROCAMP_SHARPNESS**](ksproperty-videoprocamp-sharpness.md)

[**MSXU_CONTROL_EVCOMPENSATION**](uvc-extensions-1-5.md)

[**MSXU_CONTROL_VIDEO_HDR**](uvc-extensions-1-5.md)

[Network cameras](network-cameras.md)
