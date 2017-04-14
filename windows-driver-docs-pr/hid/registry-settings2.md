---
title: Registry Settings
author: windows-driver-content
description: Registry Settings
ms.assetid: a2536911-0467-4bd0-a63b-55341f0d7567
keywords: ["joysticks WDK HID , registry settings", "virtual joystick drivers WDK HID , registry settings", "VJoyD WDK HID , registry settings", "registry WDK joysticks"]
---

# Registry Settings


## <a href="" id="ddk-registry-settings-di"></a>


The registry is used by the joystick interface to store configuration, calibration, and user preference information. It is also used to store customized text for the calibration program. The Windows 95/98/Me joystick calibration program can be customized through the registry to provide instructions to the user during calibration that are specific to the joystick.

The values fall into five groups:

Original data supplied by the OEM and installed from an INF file (described above).

[User Values](user-values.md) that specify how data is interpreted.

[Current Settings](current-settings.md) reflecting which devices are currently configured.

[Saved Settings](saved-settings.md) that allow different configurations to be recalled.

[Driver Settings](driver-settings.md) that are set up by the configuration manager as a device is set up.

The user values, current settings, and saved settings are all stored in the registry under the path belonging to the "current" joystick driver. Each of the joystick devices for which a driver is installed has a key under the path REGSTR\_PATH\_JOYCONFIG that has the form Msjstick.drv&lt;*xxxx*&gt;, where the *xxxx* is a four-digit number used to keep the key name unique. The number relates to the number of multimedia (sound, video and game controller) drivers that have been installed. At boot time, Msjstick.drv is initialized to the configuration for each of the game controller drivers. Since it can only deal with one configuration at a time, each one replaces the last and the "current" driver is the last one to be initialized. This means that the user is likely to lose all the current settings when a new driver is installed, and a minidriver cannot be structured on the assumption that the path to these registry values will always be the same.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Registry%20Settings%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


