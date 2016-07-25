---
title: Standard USB Identifiers
description: Standard USB Identifiers
ms.assetid: 39acb62b-83f2-4d14-a678-c37817193f01
keywords: ["USB identifiers WDK device installations", "single-interface devices WDK USB", "multiple-interface devices WDK USB"]
---

# Standard USB Identifiers


## <a href="" id="ddk-standard-usb-identifiers-dg"></a>


<a href="" id="the-set-of-identifiers-generated-for-usb-devices-depends-on-whether-the-device-is-a-single-interface-device-or-a-multiple-interface-device-"></a>The set of identifiers generated for USB devices depends on whether the device is a single-interface device or a multiple-interface device.  

### Single-Interface USB Devices

When a new USB device is plugged in, the system-supplied USB hub driver composes the following device ID by using information extracted from the device's device descriptor:

USB\\VID\_v(4)&PID\_d(4)&REV\_r(4)

Where:

-   *v(4)* is the 4-digit vendor code that the USB committee assigns to the vendor.

-   *d(4)* is the 4-digit product code that the vendor assigns to the device.

-   *r(4)* is the revision code.

The hub driver extracts the vendor and product codes from the *idVendor* and *idProduct* fields of the device descriptor, respectively.

An INF model section can also specify the following hardware ID:

USB\\VID\_v(4)&PID\_d(4)

and the following compatible IDs:

USB\\CLASS\_c(2)&SUBCLASS\_s(2)&PROT\_p(2)

USB\\CLASS\_c(2)&SUBCLASS\_s(2)

USB\\CLASS\_c(2)

Where:

-   *c(2)* is the device class code taken from the device descriptor.

-   *s(2)* is the device subclass code.

-   *p(2)* is the protocol code.

The device class code, subclass code, and protocol code are determined by the *bDeviceClass, bDeviceSubClass,* and *bDeviceProtocol* fields of the device descriptor, respectively. These are 2-digit numbers.

### Multiple-Interface USB Devices

Devices with multiple interfaces are called *composite* devices. Starting with Windows 2000, when a new [USB composite device](https://msdn.microsoft.com/library/windows/hardware/ff537109) is plugged into a computer, the USB hub driver creates a physical device object (PDO) and notifies the operating system that its set of child devices has changed. After querying the hub driver for the hardware identifiers associated with the new PDO, the operating system searches the appropriate INF files to find a match for the identifiers. If it finds a match other than *USB\\COMPOSITE*, it loads the driver indicated in the INF file. However, if no other match is found, the operating system uses the compatible ID *USB\\COMPOSITE*, for which it loads the USB Generic Parent driver. The Generic Parent driver then creates a separate PDO and generates a separate set of hardware identifiers for each interface of the composite device.

Each interface has a device ID of the following form:

USB\\ VID\_v(4)&PID\_d(4)&MI\_z(2)

Where:

-   *v(4)* is the 4-digit vendor code that the USB committee assigns to the vendor.

-   *d(4)* is the 4-digit product code that the vendor assigns to the device.

-   *z(2)* is the interface number that is extracted from the *bInterfaceNumber* field of the interface descriptor.

An INF model section can also specify the following compatible IDs:

USB\\CLASS\_d(2)&SUBCLASS\_s(2)&PROT\_p(2)

USB\\CLASS\_d(2)&SUBCLASS\_s(2)

USB\\CLASS\_d(2)

USB\\COMPOSITE

Where:

-   *d(2)* is the device class code taken from the device descriptor.

-   *s(2)* is the subclass code.

-   *p(2)* is the protocol code.

The device class code, subclass code, and protocol code are determined by the *bInterfaceClass, bInterfaceSubClass, and bInterfaceProtocol* fields of the interface descriptor, respectively. These are 2-digit numbers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Standard%20USB%20Identifiers%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




