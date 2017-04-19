---
Description: Enumeration of USB Composite Devices
title: Enumeration of USB Composite Devices
author: windows-driver-content
---

# Enumeration of USB Composite Devices


When a new USB device is connected to a host machine, the USB bus driver creates a physical device object (PDO) for the device and generates a PnP event to report the new PDO. The operating system then queries the bus driver for the hardware IDs associated with the PDO.

For all USB devices, the USB bus driver reports a [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) with the following format:

`USB\VID_xxxx&PID_yyyy`

**Note**  *xxxx* and *yyyy* are taken directly from **idVendor** and **idProduct** fields of the device descriptor, respectively.

 

The bus driver also reports a compatible identifier (ID) of `USB\COMPOSITE`, if the device meets the following requirements:

-   The device class field of the device descriptor (**bDeviceClass**) must contain a value of zero, or the class (**bDeviceClass**), subclass (**bDeviceSubClass**), and protocol (**bDeviceProtocol**) fields of the device descriptor must have the values 0xEF, 0x02 and 0x01 respectively, as explained in [USB Interface Association Descriptor](usb-interface-association-descriptor.md).

-   The device must have multiple interfaces.

-   The device must have a single configuration.

The bus driver also checks the device class (**bDeviceClass**), subclass (**bDeviceSubClass**), and protocol (**bDeviceProtocol**) fields of the device descriptor. If these fields are zero, the device is a composite device, and the bus driver reports an extra compatible identifier (ID) of USB\\COMPOSITE for the PDO.

After retrieving the hardware and compatible IDs for the new PDO, the operating system searches the INF files. If one of the INF files contains a match for the device ID, Windows loads the driver that is indicated by that INF file and the generic parent driver does not come into play. If no INF file contains the device ID, and the PDO has a compatible ID, Windows searches for the compatible ID. This produces a match in Usb.inf and causes the operating system to load the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md).

If you want the generic parent driver to manage your device, but your device does not have the characteristics necessary to ensure that the system will generate a compatible ID of USB\\COMPOSITE, you will have to provide an INF file that loads the generic parent driver. The INF file should contain a needs/includes section that references Usb.inf.

If your composite device has multiple configurations, the INF file you provide must specify which configuration the generic parent should use in the registry. The necessary registry keys are described in [Configuring Usbccgp.sys to Select a Non-Default USB Configuration](selecting-the-configuration-for-a-multiple-interface--composite--usb-d.md).

## Related topics
[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)  
[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Enumeration%20of%20USB%20Composite%20%20Devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


