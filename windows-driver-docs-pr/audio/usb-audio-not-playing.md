---
title: USB Audio Device Not Playing
description: Learn the cause of the Audio services not responding error and how to troubleshoot it in Windows 10 version 1703.
ms.date: 10/31/2025
ms.topic: troubleshooting
#customer intent: As a Windows user who encounters this error, I want to have troubleshooting options to resolve the issue.
---

# USB audio device not playing

This article discusses the *Audio services not responding* error and *USB audio device doesn't work* in Windows 10 version 1703.

## Symptoms

Consider the following scenario:

1. You connect a Universal Serial Bus (USB) audio device, such as an audio adapter or USB digital-to-analog converter (DAC), to a Windows computer for the first time.
1. The operating system detects the device and loads the standard USB audio 2.0 driver (usbaudio2.sys).
1. Windows then downloads the device-specific driver from Windows Update.
1. The downloaded device driver replaces the usbaudio2.sys driver.

In this scenario, the device can't be used. The computer doesn't have sound. The speaker icon on the task bar is marked with an X mark. When you select the icon, you receive the following message:

> *Audio services not responding. Both the Windows Audio and the Windows Audio End Point Builder services must be running for audio to work correctly.*

## Cause

This *audio not playing* problem occurs because the default USB audio 2.0 driver (usbaudio2.sys) uses the WaveRT port for operation but the device-specific driver doesn't. However, both drivers use the "wave" reference string when the device interface is registered.

When the device-specific driver replaces the default driver, the device interface that usbaudio2.sys creates is still used because the reference strings overlap. The operating system assumes that the new driver also supports the WaveRT port. Because the new driver doesn't support the WaveRT port, the system can't access the driver.

## Resolution

To fix this problem, use one of the following methods.

### Method 1

To uninstall the device:

1. Open Device Manager.
1. Double-click the name of the device.
1. Select the **Driver** tab.
1. Select **Uninstall Device**.

> [!NOTE]
> Don't select **Delete the driver software for this device**.

### Method 2

Connect the device to a different USB port. The problem might not occur if the device is connected to a different USB port.

### Method 3

If the device isn't yet connected, install the device-specific driver first by using the installer for the device. Then, connect the device. Windows now selects the device-specific driver instead of the default USB audio 2.0 driver. This method works because the problem only occurs if the device-specific driver replaces the default driver after the device is connected.

## Related content

- [Audio devices troubleshooting overview](audio-devices-troubleshooting.md)
