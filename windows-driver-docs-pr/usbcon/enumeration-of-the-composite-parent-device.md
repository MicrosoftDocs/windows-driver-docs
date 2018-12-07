---
Description: Enumeration of USB Composite Devices
title: Enumeration of USB Composite Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
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



