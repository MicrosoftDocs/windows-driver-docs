---
title: Camera Settings Page
description: Learn about the features and operation of the camera settings page in Windows 11, including how default values interact with camera apps.
ms.date: 10/23/2025
ms.topic: concept-article
#customer intent: As a user of camera apps with Windows 11, including Camera Companion Apps, I want to understand settings and default values so I can configure my camera settings.
---

# Camera settings page

This article describes the features and operation of the camera settings page in Windows 11. It describes the default values framework that allows users to configure the camera configuration. Any application that starts the camera uses this configuration.

Before Windows 11, users could adjust image controls only by using a utility provided by the camera manufacturer or a camera application UI. Image controls include brightness, contrast, and sharpness.

The persistence of the adjusted values typically followed a last-in model. The values depended on the behavior of the applications that use the camera. For example, if you adjust the camera's brightness level using the manufacturer's utility, that value would only hold until another application writes to the brightness control. This approach means that the behavior of one application has the potential to affect the camera experience with another application.

Windows 11 introduces a new default value framework, which allows customers to configure how their camera behaves whenever an application starts it. Windows 11 also introduces a new extensible camera settings page to manage cameras, which includes the default values.

### Terminology and prerequisites

| Term | Definition |
|--|--|
| Companion app | A custom application developed by the camera manufacturer that allows configuration and management of a camera in addition to the camera settings page. |
| Current value | The value of a camera control that is currently active in the camera's ISP and held in the camera's temporary memory. |
| Default value | An initial value of a camera control that is stored to disk and saved for a specific camera, for a specific user account, on a specific computer. |
| ISP | Image Signal Processor, the microchip in the camera responsible for controlling and reading from the sensor, processing the image data, and transferring the image data to the host computer. |
| NPU | Neural Processing Unit, dedicated hardware designed to process artificial intelligence workloads with high throughput and efficiency. |
| Sensor | The microchip in a camera that's responsible for capturing images and translating them to digital signals. |
| Windows Studio Effects | A collection of video effects available on select Windows computers with NPUs. |
| UVC | USB Video Class, the standardized interface for controlling and streaming from USB connected cameras. |

<a name="viewing-and-managing-cameras"></a>
## View and manage cameras

To open the camera settings page, in Windows search, enter and select **Settings**. From the navigation menu, select **Bluetooth & devices** > **Cameras**. Windows 11 introduced this page. It isn't available on earlier versions of Windows.

### Network cameras

The camera settings page allows you to search the local network for ONVIF-conformant network/IP cameras and connect them to the system. After you connect it, a network camera appears and operates like a traditional camera, such as a USB camera.

To remove network cameras that are connected to a system, in the camera settings page, select the camera from the **Connected cameras** list. Then select **Remove**.

For more information, see [Network cameras](network-cameras.md).

### Connected cameras

The camera settings page displays the cameras currently connected to the system. It allows you to access a page with more settings related to each camera. These settings include default image settings, the ability to disable the camera, and, for network cameras, the ability to remove or disconnect the camera.

Enabled color cameras are shown in the list. Specialty cameras, such as IR cameras, aren't shown.

### Disabled cameras

When a camera is disabled through the camera settings page, a section appears with a list of disabled cameras. Select **Enable** to enable camera again.

> [!NOTE]
> Some cameras don't appear in the camera settings page if they're missing a driver, in a nonfunctional state, or disabled through alternate utilities, such as Device Manager.

<a name="configuring-individual-cameras"></a>
## Configure individual cameras

Select an individual camera from **Connected cameras** in the camera settings page to view a page that displays a camera preview, allows management of the camera, and allows configuration of default imaging settings.

The default settings displayed on this page are saved per camera and per user account. Default imaging settings aren't backed up and restored during operating system reinstallation or during setup of a new Windows device.

### Disable a camera

To disable a camera, select it from **Connected cameras** on the camera settings page to open a page with its settings. Then, select **Disable**. Before it disables the camera, the page prompts you to confirm.

On some systems, more than one camera shares a common ISP. If you disable one camera, the action can disable multiple cameras. This situation is common on tablet form factor devices that have both an integrated front-facing, or *videoconferencing*, camera and a world-facing camera. In this scenario, the confirmation prompt explains that disabling one camera causes other cameras on the system to be disabled as a group.

In some circumstances, cameras require a system restart to be disabled. In this scenario, the camera continues to display in the **Connected cameras** list of the camera settings page. It remains grayed out with a message indicating the need to restart the computer.

### Troubleshoot a camera

To troubleshoot a camera, select it from the **Connected cameras** list on the camera settings page to open its subpage, and then select **Troubleshoot**. The **Get Help** utility offers an interactive camera troubleshooting experience.

### Adjust basic image settings

When you select camera from **Connected cameras** on the camera settings page, under **Basic settings**, the page presents sliders and toggles for basic imaging settings, as supported by the camera.

The following table lists available basic settings that the camera must implement for each setting to be visible. It lists the corresponding KS Property, or UVC Control for USB cameras. If none of the settings are available on the camera, the **Basic settings** section isn't visible.

| Basic setting | KS property | UVC control |
|--|--|--|
| Brightness | See remarks following this table | See remarks following this table |
| Contrast | [**KSPROPERTY_VIDEOPROCAMP_CONTRAST**](ksproperty-videoprocamp-contrast.md) | PU_CONTRAST_CONTROL |
| Sharpness | [**KSPROPERTY_VIDEOPROCAMP_SHARPNESS**](ksproperty-videoprocamp-sharpness.md) | PU_SHARPNESS_CONTROL |
| Saturation | [**KSPROPERTY_VIDEOPROCAMP_SATURATION**](ksproperty-videoprocamp-saturation.md) | PU_SATURATION_CONTROL |
| Video HDR | [**KSPROPERTY_CAMERACONTROL_EXTENDED_VIDEOHDR**](ksproperty-cameracontrol-extended-videohdr.md) | [**MSXU_CONTROL_VIDEO_HDR**](uvc-extensions-1-5.md) |

The **Brightness** control is a unique control because, depending on what controls the camera supports, it maps to either [**KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION**](ksproperty-cameracontrol-extended-evcompensation.md) ([**MSXU_CONTROL_EVCOMPENSATION**](uvc-extensions-1-5.md) for UVC Cameras), or the legacy [**KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS**](ksproperty-videoprocamp-brightness.md) control, which is PU_BRIGHTNESS_CONTROL for UVC cameras.

The ideal behavior of a slider for default image brightness is to act as a relative offset/bias to the camera's Auto Exposure (AE) algorithm. This approach ensures that adjustments are scene-independent and the camera can be set to always be a bit brighter or a bit darker for any given lighting environment.

The EV Compensation control is explicitly designed to act as a bias to a camera's AE algorithm. If a camera supports the EV Compensation control, the **Brightness** slider in the camera settings maps to this control. If the camera doesn't support the EV Compensation control but supports the legacy Brightness control, the **Brightness** slider maps to the legacy Brightness control. If the camera supports neither control, the **Brightness** slider isn't visible in the camera settings page.

Similarly, apps that offer in-app brightness sliders are encouraged to use the same logic to map the in-app brightness control to the EV Compensation or legacy Brightness control. This logic is implemented in the Windows Camera app.

### Adjust Windows Studio Effects (or Camera Effects)

When you select camera from **Connected cameras** on the camera settings page, under **Camera Effects**, the page presents sliders and toggles for camera effect settings, as supported by the camera.

Windows devices that support Windows Studio Effects instead use the name **Windows Studio Effects** for this section.

The following table lists the available Camera Effects, and the corresponding KS Property that the camera must implement for each setting to be visible. If none of the settings are available on the camera, the **Camera Effects** or **Windows Studio Effects** section isn't visible.

| Camera effect | KS property |
|--|--|
| Standard Blur | [**KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION**](ksproperty-cameracontrol-extended-backgroundsegmentation.md) (with KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_BLUR flag) |
| Portrait Blur | [**KSPROPERTY_CAMERACONTROL_EXTENDED_BACKGROUNDSEGMENTATION**](ksproperty-cameracontrol-extended-backgroundsegmentation.md) (with KSCAMERA_EXTENDEDPROP_BACKGROUNDSEGMENTATION_SHALLOWFOCUS flag) |
| Standard Eye Contact | [**KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION**](ksproperty-cameracontrol-extended-eyegazecorrection.md) (with KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON flag) |
| Enhanced Eye Contact  | [**KSPROPERTY_CAMERACONTROL_EXTENDED_EYEGAZECORRECTION**](ksproperty-cameracontrol-extended-eyegazecorrection.md) (with KSCAMERA_EXTENDEDPROP_EYEGAZECORRECTION_ON flag) |
| Auto Framing | [**KSPROPERTY_CAMERACONTROL_EXTENDED_DIGITALWINDOW**](ksproperty-cameracontrol-extended-digitalwindow.md) (with KSCAMERA_EXTENDEDPROP_DIGITALWINDOW_AUTOFACEFRAMING flag) |

This section displays the following controls:

- If a camera only supports **Standard Blur**, the control displays as a toggle with the label **Background blur**.
- If a camera supports both **Standard Blur** and **Portrait Blur**, the control displays as a toggle with the label **Background effects**, plus a radio button to select **Standard blur** and **Portrait blur** that's available when **Background effects** is turned on.
- If a camera only supports **Standard Eye Contact**, the control displays as a toggle with the label **Eye contact**.
- If a camera supports both **Standard Eye Contact** and **Enhanced Eye Contact**, the control displays as a toggle with the label **Eye contact**, plus a radio button to select **Standard** and **Enhanced** that's available when **Eye contact** is turned on.

### Adjust video rotation

When you select an external camera from **Connected cameras** on the camera settings page, you can see a dropdown menu that allows you to select a **Video rotation**. Available options are **No rotation**, **Right 90°**, **Left 90°**, or **180°**.

The **Video rotation** setting is only available for external cameras. If the camera is in use by another application when the setting is changed, it doesn't apply until the next time the camera is used.

> [!NOTE]
> When **Video rotation** is set to any value other than **No rotation**, Windows removes all compressed data types, for example, MJPEG, and H.264, from the camera and strictly outputs uncompressed data types. Legacy applications and cameras that depend on compressed data types being available might not function correctly when the **Video rotation** setting is configured.

### Reset camera settings

When you select a camera from **Connected cameras** on the camera settings page, the **Reset settings** button resets all camera settings to factory defaults.

When you reset to factory defaults, changes to the **Basic Settings**, **Windows Studio Effects** or **Camera Effects**, and **Video rotation** controls are erased. The camera is restarted with its factory configuration.

Using **Reset settings** also resets any default settings that were configured by a Companion App.

## Default value behavior

Changes to the **Basic Settings**, **Windows Studio Effects** (or **Camera Effects**), or **Video rotation** controls are applied immediately to the live camera stream and are visible in the preview. They're also saved as the default value for the next time an application opens the camera.

When no applications are using the camera, the behavior of the camera settings page is simple. Changes that you make to the **Basic Settings**, **Windows Studio Effects** (or **Camera Effects**), or **Video rotation** controls are immediately applied to the live camera preview stream. They're saved as updated default values that apply when applications start the camera in the future.

### How default values apply to camera applications

When an application opens and starts the camera, Windows starts the camera and then applies any default values to the camera. The default values are configured through the camera settings page. A value isn't used if the application wrote a given control after it opens the camera but before it starts the stream.

For example, if you set the default Contrast to 55% using the camera settings page, and then start the camera in an application, such as Microsoft Teams:

- **If the application opens a handle to the camera and then requests the stream to start**: Windows sets the camera's current value for the Contrast control (KSPROPERTY_VIDEOPROCAMP_CONTRAST) to 55%. Control of the camera is then handed over to the application.

- **If the application opens a handle to the camera, writes the current value of the Contrast control to 45%, and then requests the stream to start**: Windows skips writing the current value for the Contrast control because the app already preinitialized it.

While the camera is running, the application might do the following actions with the current value of the Contrast control:

- **Do nothing**: the Contrast remains at the value set during initialization during the session.

- **Write it to a different value**: the Contrast changes to whatever the application set it to, during the session or until the same application writes it again, whichever comes first.

When camera applications, like Microsoft Teams, write to camera controls, like Contrast and Brightness, they do so by writing the camera's KS properties. This changes the current value of the control on the camera. It doesn't modify the default value like the camera settings page does.

### Use the camera settings page while the camera is in use

Behavior can be more complex when the camera settings page is used while another application is using the camera. The camera settings page always displays the default values. The preview stream and the video stream shown in the application represent the current values set on the camera.

Consider a basic scenario where an application opens the camera. The application has no UI to adjust the current value of the Contrast control. If you open the camera settings page to adjust the Contrast while the application runs, there are no issues. The app didn't change the current value of the Contrast control from the default value.

In a more complex scenario, the default value of the Contrast control is 55%. The application that uses the camera sets the current value of the Contrast control to 45%. In this case, the camera stream runs with the Contrast set to 45%. If you open the camera settings page while the application is running, the preview reflects a Contrast of 45%. The Contrast slider shows the default value of 55%, which is a mismatch.

You could change the Contrast using the application. The current value of the Contrast would change, which affects the video stream in both the app and in the camera settings page preview. The Contrast slider in the camera settings page continues to display 55%.

Alternatively, you could change the Contrast using the camera settings page. For example, adjust the slider to 40%. The camera settings page saves 40% as the new default value, and sets the camera's current value to 40%. This change causes the video stream in both the camera settings page and in the application to change and reflect a Contrast of 40%.

> [!NOTE]
> Some applications use the [**IMFCameraControlMonitor**](/windows/win32/api/mfidl/nn-mfidl-imfcameracontrolmonitor) API to monitor for external changes to controls. Suppose an application wants to keep the Contrast at 45% while it uses the camera. That application can monitor the Contrast KS Property. If the KS Property is changed externally in the camera settings page, the application can immediately rewrite the KS Property back to 45%.

Synchronization issues are uncommon. They only happen when you make real-time changes to image settings in an application and launches the camera settings page at the same time to adjust the same image setting.

To manage concurrent use situations, the camera settings page displays an information banner when the camera is in use by another application. This banner explains that the changes made in the camera settings page or in the application affect both the application and the preview in the camera settings page.

## Camera Companion Apps

Camera manufacturers might want to provide their own custom applications that allow customers to change default camera settings.

Windows 11 provides a Camera Companion App framework that allows manufacturers to develop applications with the following capabilities:

- Ability to display and modify the same default value settings that the camera settings page supports. For example, Brightness, Contrast, and Background effects.
- Ability to register, update, or delete default value settings for other camera controls that are known to Windows but aren't exposed through the camera settings page. For example, the Hue control.
- Ability to register, update, or delete default value settings for manufacturer-proprietary camera controls. For example, the on/off control for a camera manufacturer's custom lighting adjustment effect.

When a camera associates a specific Companion App with it, an entry for that app is added to the camera settings page. If the app is installed, it can be launched from the camera settings page or a link to the Microsoft Store is displayed to download it.

For more information, see [Camera companion apps](camera-companion-apps.md).

<a name="programmatically-launching-the-camera-settings-page"></a>
## Launch the camera settings page programmatically

An application can launch the camera settings page by using a deep link URI, which is helpful for applications that want to allow quick access to common camera controls. For more information, see [Launch the camera settings page](/windows/uwp/audio-video-camera/launch-camera-settings).

## Related content

- [Camera Companion Apps](camera-companion-apps.md)
- [Network cameras](network-cameras.md)
