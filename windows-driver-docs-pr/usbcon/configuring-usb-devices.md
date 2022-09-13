---
description: The topics in this section describe how a client driver must configure their device.
title: Overview of selecting a USB configuration in USB drivers overview
ms.date: 09/13/2022
---

# Overview of selecting a USB configuration in USB drivers

The topics in this section describe how a client driver must configure their device.

A USB device exposes its capabilities in the form of a series of interfaces called a *USB configuration*. Each interface consists of one or more alternate settings, and each alternate setting is made up of a set of endpoints. The device must provide at least one configuration, but it can provide multiple configurations that are mutually exclusive definitions of what the device can do. For more information about configuration descriptors, see [USB Configuration Descriptors](./usb-configuration-descriptors.md).

Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. Before sending I/O requests to the device, a client driver must read the device's configuration, parse the information, and select an appropriate configuration. The client driver must select at least one of the supported configurations in order to make the device to work.

A WDM-based client driver can select any of the configurations in a USB device.

If your client driver is based on [Kernel-Mode Driver Framework](../wdf/index.md) or [User-Mode Driver Framework](../wdf/index.md), you should use the respective framework interfaces for configuring a USB device. If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code selects the first configuration and the default alternate setting in each interface.

## In this section

| Topic | Description |
|--|--|
| [How to select a configuration for a USB device](./how-to-select-a-configuration-for-a-usb-device.md) | In this topic, you will learn about how to select a configuration in a universal serial bus (USB) device. |
| [How to select an alternate setting in a USB interface](./select-a-usb-alternate-setting.md) | This topic describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface. The client driver must issue this request after selecting a USB configuration. Selecting a configuration, by default, also activates the first alternate setting in each interface in that configuration. |
| [Configuring Usbccgp.sys to Select a Non-Default USB Configuration](./selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md) | This topic provides information about registry settings that configure the way Usbccgp.sys selects a USB configuration. The topic also describes how Usbccgp.sys handles select-configuration requests sent by a client driver that controls one of functions of a composite device. |

For information about special considerations related to the configuration of devices that require firmware downloads, see [Configuring USB Devices that Require Firmware Downloads](./configuring-usb-devices-that-require-firmware-downloads.md).

## Limitations for selecting a configuration

Certain restrictions apply if a client driver is using WDF objects or whether the device has a single interface or multiple interfaces. Consider the following restrictions before changing the default configuration:

- A client driver for a composite device that manages interfaces or interface collections through the [USB Generic Parent Driver](./usb-common-class-generic-parent-driver.md) (Usbccgp.sys) cannot change the device's configuration value. However, the client driver can configure Usbccgp.sys to select a configuration other than the first (default) configuration. For more information, see [Configuring Usbccgp.sys to Select a Non-Default USB Configuration](./selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md).
- A KMDF-based client driver that is using the framework's [USB I/O Targets](../wdf/usb-i-o-targets.md) can select only the first configuration.
- [WinUSB](winusb.md) supports only the first configuration.
- A class driver frequently lacks support for multiple configurations. If your device implements a class that is defined by a USB class specification, see the [USB technology](https://www.usb.org/defined-class-codes) website for information about device classes and class specifications. Microsoft provides class drivers for the supported USB device classes. For more information, see [Drivers for the Supported USB Device Classes](./supported-usb-classes.md).

## Related topics

- [USB Driver Development Guide](./usb-driver-development-guide.md)
- [USB Configuration Descriptors](./usb-configuration-descriptors.md)
- [Working with USB Devices](../wdf/working-with-usb-devices.md)
- [Working with USB Interfaces in UMDF](../wdf/working-with-usb-interfaces-in-umdf-1-x-drivers.md)
