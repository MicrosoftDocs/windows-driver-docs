---
title: Built-in Drivers for Windows Devices
description: Microsoft Windows contains built-in drivers for many device types. Learn how to check the built-in drivers for your device.
ms.date: 12/09/2024
ms.topic: end-user-help
---

# Built-in Drivers for Windows Devices

Microsoft Windows contains built-in drivers for many device types. If there is a built-in driver for your device type, you won't need to write your own driver. Your device can use the built-in driver.

## Built-in drivers for USB devices

If your device belongs to a device class that is defined by the USB Device Working Group (DWG), there may already be an existing Windows USB class driver for it. For more information, see [Drivers for the Supported USB Device Classes](../usbcon/supported-usb-classes.md).

## Check the built-in drivers for your device

You can display a list of installed drivers for your device and their properties by using `driverquery` command. To display the installed drivers on your local computer, open the Command Prompt window and type:

```cmd
driverquery
```

For more information, see [driverquery](/windows-server/administration/windows-commands/driverquery).









