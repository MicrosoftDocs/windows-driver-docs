---
Description: The topics in this section describe how a client driver must configure their device.
title: Selecting a USB configuration in USB drivers
author: windows-driver-content
---

# Selecting a USB configuration in USB drivers


The topics in this section describe how a client driver must configure their device.

A USB device exposes its capabilities in the form of a series of interfaces called a *USB configuration*. Each interface consists of one or more alternate settings, and each alternate setting is made up of a set of endpoints. The device must provide at least one configuration, but it can provide multiple configurations that are mutually exclusive definitions of what the device can do. For more information about configuration descriptors, see [USB Configuration Descriptors](usb-configuration-descriptors.md).

Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. Before sending I/O requests to the device, a client driver must read the device's configuration, parse the information, and select an appropriate configuration. The client driver must select at least one of the supported configurations in order to make the device to work.

A WDM-based client driver can select any of the configurations in a USB device.

If your client driver is based on [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff557565) or [User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff557565), you should use the respective framework interfaces for configuring a USB device. If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code selects the first configuration and the default alternate setting in each interface.

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
<td><p>[How to select a configuration for a USB device](how-to-select-a-configuration-for-a-usb-device.md)</p></td>
<td><p>In this topic, you will learn about how to select a configuration in a universal serial bus (USB) device.</p></td>
</tr>
<tr class="even">
<td><p>[How to select an alternate setting in a USB interface](select-a-usb-alternate-setting.md)</p></td>
<td><p>This topic describes the steps for issuing a select-interface request to activate an alternate setting in a USB interface. The client driver must issue this request after selecting a USB configuration. Selecting a configuration, by default, also activates the first alternate setting in each interface in that configuration.</p></td>
</tr>
<tr class="odd">
<td><p>[Configuring Usbccgp.sys to Select a Non-Default USB Configuration](selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md)</p></td>
<td><p>This topic provides information about registry settings that configure the way Usbccgp.sys selects a USB configuration. The topic also describes how Usbccgp.sys handles select-configuration requests sent by a client driver that controls one of functions of a composite device.</p></td>
</tr>
</tbody>
</table>

 

For information about special considerations related to the configuration of devices that require firmware downloads, see [Configuring USB Devices that Require Firmware Downloads](configuring-usb-devices-that-require-firmware-downloads.md).

## <a href="" id="ddk-configuring-usb-devices-kg"></a>Limitations for Selecting a Configuration


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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Selecting%20a%20USB%20configuration%20in%20USB%20drivers%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


