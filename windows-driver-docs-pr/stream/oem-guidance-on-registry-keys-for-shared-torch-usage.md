---
title: Shared camera TorchControl registry setting
description: The OEM-set AllowTorchControlSharing value in the registry key enables OEMs to configure torch control to work from shared Media Capture session.
ms.date: 04/27/2021
ms.localizationpriority: medium
---

# Camera TorchControl shared usage registry setting

The OEM-set **AllowTorchControlSharing** registry value enables OEMs to configure the Camera pipeline to allow access for [TorchControl](/uwp/api/Windows.Media.Devices.TorchControl) from [Windows.Media.Capture.MediaCapture](/uwp/api/Windows.Media.Capture.MediaCapture) instance that has been initialized as [MediaCaptureSharingMode.SharedReadOnly](/uwp/api/windows.media.capture.mediacapturesharingmode) mode.

This can be done for example to allow utility app to control a flashlight feature while not preventing other apps to access the same underlying camera device.

| Value (DWORD) | Explanation |
|--|--|
| **0** or **AllowTorchControlSharing** value not existing | TorchControl will **not** be allowed from shared mode MediaCapture instance |
| **1** | TorchControl will be allowed from shared mode MediaCapture instance |

**AllowTorchControlSharing registry value location:**

- OEMs should create a new registry value **AllowTorchControlSharing** (DWORD) and set it to 1 to allow shared mode control.

    **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\OEM\\Device\\Capture**

    To set the **AllowTorchControlSharing** registry value on a machine, the following command can be used from an elevated command prompt:

    ```console
    reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\OEM\Device\Capture" /v "AllowTorchControlSharing" /t REG_DWORD /d 1 /f 
    ```

    On a 64-bit OS the value can also be added to *Wow6432Node* path in registry:
    **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\WOW6432Node\\Microsoft\OEM\\Device\\Capture**

## Remarks

This functionality is available starting in:

| Windows 10 version | KB article |
|--|--|
| 19041.906 and 19042.906 | [KB8000842](https://support.microsoft.com/topic/march-29-2021-kb5000842-os-builds-19041-906-and-19042-906-preview-1a58a276-6a0a-47a5-aa7d-97af2d10b16d) |
| 18363.1533 | [KB5001396](https://support.microsoft.com/topic/april-22-2021-kb5001396-os-build-18363-1533-preview-e67788f0-4e70-4f9b-9c5e-ff977310eeea) |
| 17763.1911 | [KB5001384](https://support.microsoft.com/topic/april-22-2021-kb5001384-os-build-17763-1911-preview-e471f445-59be-42cb-8c57-5db644cbc698) |

- By default this registry value does not exist.

- TorchControl does not have an event mechanism to notify state changes thus by controlling the torch from multiple applications may cause the torch being in different state than one application thinks if the state was changed by another application.
