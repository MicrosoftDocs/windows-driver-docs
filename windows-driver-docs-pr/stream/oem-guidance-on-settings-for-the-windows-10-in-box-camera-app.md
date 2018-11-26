---
title: OEM guidance on settings for the Windows 10 in-box camera app
description: The new in-box camera app for Windows 10 is designed to work well with the wide variety of hardware supported by the Windows platform without any configuration required by the OEM.
ms.assetid: 567D2083-9837-44A6-97FB-AD0C9B9EB067
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# OEM guidance on settings for the Windows 10 in-box camera app


The new in-box camera app for Windows 10 is designed to work well with the wide variety of hardware supported by the Windows platform without any configuration required by the OEM. The camera app is designed to determine settings that are advertised by device hardware and choose appropriate defaults and options for the user.

The following sections discuss the logic the in-box camera app uses so that OEMs can understand how the app configures itself, and if necessary, adjust their driver accordingly.

We recommend that OEMs first configure the drivers to properly advertise device capabilities, test their application, and then consider modifications if needed.

## Background and legacy behavior


In Windows Phone 7.5 (Mango), the camera manifest file (CameraSettings.xml) was introduced to provide a way for OEMs to specify supported camera configurations and customize the camera application. In Windows 10, this mechanism is no longer supported and has been replaced using built-in logic in the camera app to choose and display the appropriate settings to the user.

## Logic for choosing resolutions to display


-   **Still image logic**

    For still image resolutions, the in-box camera app displays to the user a list of aspect ratios, which will be derived from the resolutions supported by the driver. The app will always capture in the highest resolution supported for each aspect ratio. Aspect ratios within 1% are considered to be the same.

    **Recommendation to OEMs:** OEMs should ensure their driver supports a resolution setting that matches their device's screen aspect ratio. That resolution should provide a high quality capture experience as it will be chosen as default (see the *Logic for choosing default resolution* section below).

-   **Video logic**

    For video capture, the camera app will make available to the user the three highest resolutions specified by the driver that support a frame rate greater than 15 frames per second (fps). The camera app will display to the user all available frame rates higher that 15 fps for these three resolutions (thus supporting high frame rate capture).

    **Recommendation to OEMs:** OEMs should ensure that their driver supports their desired video capture resolutions at greater than 15 fps (25+ fps is recommended for best customer experience), and ensure that the three highest resolutions advertised are the resolutions the OEM wants presented to the user. Ensure the driver also specifies capabilities for high frame rates.

## Logic for choosing default resolution


-   **Still image logic**

    The camera app will choose a default resolution for still capture by choosing the resolution advertised by the driver that most closely matches the aspect ratio of the device's screen unless that resolution is less than 60% of the highest resolution option. This is done to filter out very low resolutions that result in a poor user experience.

-   **Video logic**

    The camera app will choose a default resolution for video capture by choosing the highest resolution that supports 30 fps capture.

    If resolutions higher than 1080p@30 fps are available, the app will not default to it. Instead the app will choose 1080p@30 fps to limit concerns over battery, storage, and thermal issues. 4K resolutions will still be able to be selected by the user.

## Logic for choosing default camera


If a default sensor is specified, the camera app will use that sensor by default. If no default sensor is specified, the camera app will use the back sensor. If there is no back sensor, the app will use the front sensor.

## Legacy OEM settings and settings not supported in Windows 10 camera


Legacy OEM settings specified for Windows Phone 8 and Windows Phone 8.1 devices via the camera manifest file are no longer supported.

This includes the following settings:

| Setting                  | Description                                                                                                                                                                                                    |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QuickBar actions         | The QuickBar no longer exists in Windows 10. Instead a dashboard is available at the top of the screen. Settings on the dashboard are determined by hardware capabilities and are not customizable by the OEM. |
| Scene modes              | The new camera app no longer provides scene modes or the ability for an OEM to customize scene modes.                                                                                                          |
| Custom property settings | The Windows 10 camera app no longer supports the setting of custom properties by property GUID and value.                                                                                                      |
| Custom menu Items        | The Windows 10 camera app no longer supports the addition of custom menu items.                                                                                                                                |

 

 

 




