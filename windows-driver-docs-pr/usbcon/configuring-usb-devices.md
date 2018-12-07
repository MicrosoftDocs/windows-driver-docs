---
Description: The topics in this section describe how a client driver must configure their device.
title: Selecting a USB configuration in USB drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selecting a USB configuration in USB drivers


The topics in this section describe how a client driver must configure their device.

A USB device exposes its capabilities in the form of a series of interfaces called a *USB configuration*. Each interface consists of one or more alternate settings, and each alternate setting is made up of a set of endpoints. The device must provide at least one configuration, but it can provide multiple configurations that are mutually exclusive definitions of what the device can do. For more information about configuration descriptors, see [USB Configuration Descriptors](usb-configuration-descriptors.md).

Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. Before sending I/O requests to the device, a client driver must read the device's configuration, parse the information, and select an appropriate configuration. The client driver must select at least one of the supported configurations in order to make the device to work.

A WDM-based client driver can select any of the configurations in a USB device.

If your client driver is based on [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/) or [User-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/), you should use the respective framework interfaces for configuring a USB device. If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code selects the first configuration and the default alternate setting in each interface.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="how-to-select-a-configuration-for-a-usb-device.md" data-raw-source="[How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md)">How to select a configuration for a USB device</a></p></td>
<td><p>In this topic, you will learn about how to select a configuration in a universal serial bus (USB) device.</p></td>
</tr>
<tr class="even">
<td><p><a href="select-a-usb-alternate-setting.md" data-raw-source="[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md)">How to select an alternate setting in a USB interface</a></p></td>
<td><p>This topic describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface. The client driver must issue this request after selecting a USB configuration. Selecting a configuration, by default, also activates the first alternate setting in each interface in that configuration.</p></td>
</tr>
<tr class="odd">
<td><p><a href="selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md" data-raw-source="[Configuring Usbccgp.sys to Select a Non-Default USB Configuration](selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md)">Configuring Usbccgp.sys to Select a Non-Default USB Configuration</a></p></td>
<td><p>This topic provides information about registry settings that configure the way Usbccgp.sys selects a USB configuration. The topic also describes how Usbccgp.sys handles select-configuration requests sent by a client driver that controls one of functions of a composite device.</p></td>
</tr>
</tbody>
</table>

 

For information about special considerations related to the configuration of devices that require firmware downloads, see [Configuring USB Devices that Require Firmware Downloads](configuring-usb-devices-that-require-firmware-downloads.md).

## Limitations for Selecting a Configuration


Certain restrictions apply if a client driver is using WDF objects or whether the device has a single interface or multiple interfaces. Consider the following restrictions before changing the default configuration:

-   A client driver for a composite device that manages interfaces or interface collections through the [USB Generic Parent Driver](usb-common-class-generic-parent-driver.md) (Usbccgp.sys) cannot change the device's configuration value. However, the client driver can configure Usbccgp.sys to select a configuration other than the first (default) configuration. For more information, see [Configuring Usbccgp.sys to Select a Non-Default USB Configuration](selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md).
-   A KMDF-based client driver that is using the framework's [USB I/O Targets](https://msdn.microsoft.com/library/windows/hardware/ff544752) can select only the first configuration.
-   [WinUSB](winusb.md) supports only the first configuration.
-   A class driver frequently lacks support for multiple configurations. If your device implements a class that is defined by a USB class specification, see the [USB Technology](http://go.microsoft.com/fwlink/p/?linkid=8769) website for information about device classes and class specifications. Microsoft provides class drivers for the supported USB device classes. For more information, see [Drivers for the Supported USB Device Classes](supported-usb-classes.md).

## Related topics
[USB Driver Development Guide](usb-driver-development-guide.md)  
[USB Configuration Descriptors](usb-configuration-descriptors.md)  
[Working with USB Devices](https://msdn.microsoft.com/library/windows/hardware/ff553101)  
[Working with USB Interfaces in UMDF](https://msdn.microsoft.com/library/windows/hardware/ff561478)  



