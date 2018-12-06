---
title: Video stabilization registry settings
description: The OEM-set MaxPixelsPerSecond value in the VideoStabilization registry key enables OEMs to configure video stabilization settings on a device and apply video stabilization to a video at capture-time.
ms.assetid: F0F7A705-0F39-4A62-A110-A2E47DFB7B42
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video stabilization registry settings


The OEM-set **MaxPixelsPerSecond** value in the **VideoStabilization** registry key enables OEMs to configure video stabilization settings on a device and apply video stabilization to a video at capture-time. The configuration takes into account the device’s recording resolution, along with its hardware and software capabilities.

## Overview


The **VideoStabilization** registry key **MaxPixelsPerSecond** value is used to specify the maximum capabilities of video stabilization on a device, under optimal circumstances. All apps can read the registry key and avoid attempting unreasonable usage of video stabilization.

The value entered in the **MaxPixelsPerSecond** value sets the limit beyond which the MFT will not try to turn on video stabilization, even if an app enables it. The registry key needs to indicate the greatest resolution and frame rate at which a device can run video stabilization. If the **MaxPixelsPerSecond** value is not set, the video stabilization MFT will use a fallback value. Finally, if that fails as well, video stabilization will use its internal logic to switch off in order to prevent a sub-optimal user experience.

## Video stabilization requirements


A device is considered capable of running video stabilization when all of the following can happen:

-   Video stabilization is turned on and is not in pass-through mode

-   Recording is turned on

-   Preview is active

-   No noise or dropped frames are seen in the preview

-   No noise or dropped frames are seen in the recorded video

## Set the video stabilization registry key


**VideoStabilization registry key format:**

-   OEMs should set a **MaxPixelsPerSecond** QWORD value that defines the cutoff value for number of pixels per second, beyond which video stabilization will be forced to run in pass-through mode, even if it is enabled by an app.

-   **MaxPixelsPerSecond** is defined as follows:

    `MaxPixelsPerSecond = width * height * frame-rate`

    For example, for 1080p resolution at 30 fps, **MaxPixelsPerSecond** would be defined as 1920 \* 1080 \* 30 = 62208000.

**VideoStabilization registry key location:**

-   OEMs should create and set the **VideoStabilization** registry key for video stabilization in the following location:

    **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows Media Foundation\\Platform\\VideoStabilization**

    To set the **VideoStabilization** registry key **MaxPixelsPerSecond** value on a 32-bit machine, use the following command at an elevated command prompt:

    ```console
    reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Media Foundation\Platform\VideoStabilization" /v "MaxPixelsPerSecond" /t REG_QWORD /d 62208000 /f 
    ```

-   On 64-bit machines, OEMs should also create and set the same key on the Wow6432Node path:

    **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows Media Foundation\\Platform\\VideoStabilization**

    To set the **VideoStabilization** registry key **MaxPixelsPerSecond** value on a 64-bit machine, use the following command at an elevated command prompt:

    ```console
    reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Windows Media Foundation\Platform\VideoStabilization" /v "MaxPixelsPerSecond" /t REG_QWORD /d 62208000 /f 
    ```

When set, the **VideoStabilization** registry key will be visible to the video stabilization MFT and first and third party apps.

If the **MaxPixelsPerSecond** value is set, the video stabilization MFT will never try to stabilize frame rates or resolutions above the limit. Instead, it will go into pass-through mode even if the app requests video stabilization. The video stabilization MFT has a mechanism to recommend frame rate and resolution to the app for a given device. Apps can choose the recommendation to avoid such a pass-through on those devices that have the registry key populated.

If the **MaxPixelsPerSecond** value is not set, the video stabilization MFT will attempt to stabilize up to the default value but no higher.

The default value is 62208000 pixels per second, which is 1920 pixels x 1080 pixels x 30 fps. When video stabilization attempts to stabilize but cannot maintain real time stabilization of the video frames, the internal logic will switch video stabilization to pass-through mode (turning off video stabilization) without dropping any frames.

If video stabilization switched off in the previous session, the MFT will attempt to start video stabilization in regular mode for every new session, before deciding to switch to pass-through mode. This is because it can not rely on the previous mode to make future decisions, since the device may have been under stress when it was last operated.

## Video stabilization test requirements


OEMs need to verify end-to-end capabilities of their devices with video stabilization working. They need to verify an acceptable experience at the given largest pixels per second resolution.

OEMs must verify the following:

-   The video stabilization internal logic is disabled at the registry key location provided by Microsoft. Disabling the internal logic guarantees that video stabilization will not go into pass-through mode during testing if it encounters a stressful situation.

-   Video stabilization can run alone, without background tasks or other features

-   Smooth preview rendering with video stabilization enabled and the internal logic disabled

-   Smooth video recording with video stabilization enabled and the internal logic disabled

-   Desired pixels per second count achieved in stabilized recording

-   No overheating

**Note** Retail systems should not have the registry key to disable the video stabilization internal logic described in this section. However, retail systems should have the **VideoStabilization** registry key with a **MaxPixelsPerSecond** value determined through this test process.


**Note** The **VideoStabilization** registry key **MaxPixelsPerSecond** value functions only when attribute [MF\_LOW\_LATENCY](https://msdn.microsoft.com/library/windows/desktop/hh162832) is set on the effect. When the provided video stabilization effect is added to the MediaCapture pipeline, the attribute is automatically set. However, if the video stabilization effect is inserted into a custom pipeline or a pipeline that does not set the **MF\_LOW\_LATENCY** attribute, the registry key has no effect.
