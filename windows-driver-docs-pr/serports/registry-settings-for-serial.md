---
title: Registry Settings for Serial
description: Registry Settings for Serial
keywords:
- Serial driver WDK , registry settings
- registry WDK serial devices
- serial devices WDK , registry settings
- serial devices WDK , Serial driver
ms.date: 04/20/2017
---

# Registry Settings for Serial

> [!NOTE]
> This topic describes programming traditional COM ports. For information on USB attached serial ports, see [USB serial driver (Usbser.sys)](../usbcon/usb-driver-installation-based-on-compatible-ids.md).

This section describes the following registry settings that Serial uses to configure a serial device:

[Registry Settings for the Serial Service](registry-settings-for-the-serial-service.md)

[Registry Settings for a Plug and Play Serial Device](registry-settings-for-a-plug-and-play-serial-device.md)

[Registry Settings for a Legacy COM Port](registry-settings-for-a-legacy-com-port.md)

Serial uses the registry settings to configure a serial device in the following way:

- If a device-specific entry value is present, Serial uses it.

- If a device-specific entry value is not present, but there is a corresponding Serial service entry value, Serial uses the service entry value.

- If a device-specific entry value is not present and there is no corresponding Serial service entry value, Serial uses a default service value that is statically defined in *serial.sys*.

For general information on how to locate and work with Windows drivers registry keys, see [Registry Trees for Devices and Drivers](../install/overview-of-registry-trees-and-keys.md).
