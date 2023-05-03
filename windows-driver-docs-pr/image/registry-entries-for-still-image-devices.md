---
title: Registry entries for still image devices
description: Registry entries for still image devices
ms.date: 05/03/2023
---

# Registry entries for still image devices

Microsoft STI makes use of several registry entries, some of which can be modified by vendor-supplied components.

## Vendor-modifiable registry values

The following table lists the predefined registry value names and their meanings. Constants are defined in *stireg.h*. A value must be assigned to "TwainDS" if the device supports the still image [push model](creating-push-model-aware-applications.md). Values for the other names are optional.

| Constant | Value name string | Definition |
|--|--|--|
| STI_DEVICE_VALUE_ICM_PROFILE | "ICMProfile" | REG_MULTI_SZ type containing names of ICM profiles for the device. |
| STI_DEVICE_VALUE_ISIS_NAME | "ISISDriverName" | REG_SZ type containing the device's ISIS driver name, such as "epson.pxn". |
| STI_DEVICE_VALUE_TIMEOUT | "PollTimeout" | REG_DWORD type representing the time-out value, in milliseconds, that should be used when polling the device. The default value is 1000 (1 second). |
| STI_DEVICE_VALUE_TWAIN_NAME | "TwainDS" | REG_SZ type containing the displayable name of the device's TWAIN data source, such as "HP PictureScan 3.0". |

Clients of the **StillImage** COM interface should call [**IStillImage::SetDeviceValue**](/previous-versions/windows/hardware/drivers/ff543801(v=vs.85)) and [**IStillImage::GetDeviceValue**](/previous-versions/windows/hardware/drivers/ff543786(v=vs.85)) to reference the registry. Still image minidrivers can call the Win32 registry API, specifying the registry key received by the minidriver's [**IStiUSD::Initialize**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize) method. Values for predefined registry entries can also be set from within [the INF file](inf-files-for-still-image-devices.md).

## Customized registry values

Still image applications and minidrivers can also store customized, device-specific values in the registry. For example, user selections obtained from customized property sheet pages could be stored under a "UserSettings" subkey.

Additionally, values for customized registry entries can be set from within [the INF file](inf-files-for-still-image-devices.md) by including a **DeviceData** entry.

## Non-modifiable registry entries

The following table lists registry entries that should not be modified by vendor software.

| Registry Key | Definition |
|--|--|
| **HKLM\SYSTEM\CurrentControlSet\Control\StillImage\Logging\STICLI** | Specifies which vendor-generated messages are written to the still image log file. Can be any combination of the following bitmasks:<br><br>0x1 - informational messages<br><br>0x2 - warning messages<br><br>0x4 - error messages<br><br>See [**IStillImage::WriteToErrorLog**](/previous-versions/windows/hardware/drivers/ff543807(v=vs.85)). |
| **HKLM\SYSTEM\CurrentControlSet\Control\StillImage\Logging\STIMON** | Specifies which event monitor messages are written to the still image log file. Can be any combination of the following bitmasks:<br><br>0x1 - informational messages<br><br>0x2 - warning messages<br><br>0x4 - error messages |
| **HKLM\SYSTEM\CurrentControlSet\Control\Class{6BDD1FC6-810F-11D0-BEC7-08002BE2092F}** | Contains information about installed still image devices. |
| **HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\StillImage\Registered Applications** | Contains a list of registered imaging applications. |
| **HKLM\SYSTEM\CurrentControlSet\Control\DeviceClass{6bdd1fc6-810f-11d0-bec7-08002be2092f}** | Contains information about installed still image device interfaces. |
