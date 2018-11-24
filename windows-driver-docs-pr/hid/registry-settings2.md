---
title: Registry Settings
description: Registry Settings
ms.assetid: a2536911-0467-4bd0-a63b-55341f0d7567
keywords:
- joysticks WDK HID , registry settings
- virtual joystick drivers WDK HID , registry settings
- VJoyD WDK HID , registry settings
- registry WDK joysticks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Settings





The registry is used by the joystick interface to store configuration, calibration, and user preference information. It is also used to store customized text for the calibration program. The Windows 95/98/Me joystick calibration program can be customized through the registry to provide instructions to the user during calibration that are specific to the joystick.

The values fall into five groups:

Original data supplied by the OEM and installed from an INF file (described above).

[User Values](user-values.md) that specify how data is interpreted.

[Current Settings](current-settings.md) reflecting which devices are currently configured.

[Saved Settings](saved-settings.md) that allow different configurations to be recalled.

[Driver Settings](driver-settings.md) that are set up by the configuration manager as a device is set up.

The user values, current settings, and saved settings are all stored in the registry under the path belonging to the "current" joystick driver. Each of the joystick devices for which a driver is installed has a key under the path REGSTR\_PATH\_JOYCONFIG that has the form Msjstick.drv&lt;*xxxx*&gt;, where the *xxxx* is a four-digit number used to keep the key name unique. The number relates to the number of multimedia (sound, video and game controller) drivers that have been installed. At boot time, Msjstick.drv is initialized to the configuration for each of the game controller drivers. Since it can only deal with one configuration at a time, each one replaces the last and the "current" driver is the last one to be initialized. This means that the user is likely to lose all the current settings when a new driver is installed, and a minidriver cannot be structured on the assumption that the path to these registry values will always be the same.

 

 




