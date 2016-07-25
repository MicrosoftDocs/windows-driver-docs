---
title: Identifiers for PCI Devices
description: Identifiers for PCI Devices
ms.assetid: 58d52af8-9afd-441f-9ed9-92f9e2775226
keywords: ["device identification strings WDK , PCI devices", "identification strings WDK device , PCI devices", "identifiers WDK device , PCI devices", "PCI device identifiers WDK device installations", "hardware IDs WDK device installations", "compatible IDs WDK device installations"]
---

# Identifiers for PCI Devices


## <a href="" id="ddk-identifiers-for-pci-devices-dg"></a>


The following is a list of the [device identification string](device-identification-strings.md) formats that the PCI bus driver uses to report hardware IDs. When the Plug and Play (PnP) manager queries the driver for the hardware IDs of a device, the PCI bus driver returns a list of hardware IDs in order of increasing generality.

PCI\\VEN\_v(4)&DEV\_d(4)&SUBSYS\_s(4)n(4)&REV\_r(2)

PCI\\VEN\_v(4)&DEV\_d(4)&SUBSYS\_s(4)n(4)

PCI\\VEN\_v(4)&DEV\_d(4)&REV\_r(2)

PCI\\VEN\_v(4)&DEV\_d(4)

PCI\\VEN\_v(4)&DEV\_d(4)&CC\_c(2)s(2)p(2)

PCI\\VEN\_v(4)&DEV\_d(4)&CC\_c(2)s(2)

Where:

-   v(4) is the four-character PCI SIG-assigned identifier for the vendor of the device, where the term *device*, following PCI SIG usage, refers to a specific PCI chip.

-   d(4) is the four-character vendor-defined identifier for the device.

-   s(4) is the four-character vendor-defined subsystem identifier.

-   n(4) is the four-character PCI SIG-assigned identifier for the vendor of the subsystem.

-   r(2) is the two-character revision number.

-   c(2) is the two-character base class code from the configuration space.

-   s(2) is the two-character subclass code.

-   p(2) is the Programming Interface code.

The following is an example of a hardware ID for a display adapter on a portable computer. The format of this hardware ID is PCI\\VEN\_v(4)&DEV\_d(4)&SUBSYS\_s(4)n(4)&REV\_r(2).

PCI\\VEN\_102C&DEV\_00E0&SUBSYS\_00000000&REV\_04

The following is the hardware ID for the display adapter in the previous example with the revision information removed. The format of this hardware ID is PCI\\VEN\_*v(4)*&DEV\_*d(4)*&SUBSYS\_*s(4)n(4).*

PCI\\VEN\_102C&DEV\_00E0&SUBSYS\_00000000

The following is a list of the device identification string formats that the PCI bus driver uses to report compatible IDs. The variety of these formats provides substantial flexibility to specify compatible IDs. The PCI bus driver constructs a list of compatible IDs based on the information that the driver can obtain from the device. When the PnP manager queries the driver for the compatible IDs of a device, the PCI bus driver returns a list of compatible IDs in order of decreasing compatibility.

PCI\\VEN\_v(4)&DEV\_d(4)&REV\_r(2)

PCI\\VEN\_v(4)&DEV\_d(4)

PCI\\VEN\_v(4)&CC\_c(2)s(2)p(2)

PCI\\VEN\_v(4)&CC\_c(2)s(2)

PCI\\VEN\_v(4)

PCI\\CC\_c(2)s(2)p(2)&DT\_d(4) (applies only to a PCI Express device)

PCI\\CC\_c(2)s(2)p(2)

PCI\\CC\_c(2)s(2)&DT\_d(4) (applies only to a PCI Express device)

PCI\\CC\_c(2)s(2)\`

Where:

-   The definitions of the following fields in a compatible ID are identical to the definitions of the corresponding fields that used in a hardware ID: *v(4)*, *r(2)*, *c(2)*, *s(2)*, and *p(2)*.

-   *d(4)* in the DEV\_*d(4)* field is the four-character vendor-defined identifier for the device.

-   *d(4)* in the DT\_*d(4)* field is the four-character device type, as specified in the PCI Express Base specification.

For the example of a display adapter on a portable computer, any of the following compatible IDs would match the information in an INF file for that adapter:

PCI\\VEN\_102C&DEV\_00E0&REV\_04

PCI\\VEN\_102C&DEV\_00E0

PCI\\VEN\_102C&DEV\_00E0&REV\_04&CC\_0300

PCI\\VEN\_102C&DEV\_00E0&CC\_030000

PCI\\VEN\_102C&DEV\_00E0&CC\_0300

PCI\\VEN\_102C&CC\_030000

PCI\\VEN\_102C&CC\_0300

PCI\\VEN\_102C

PCI\\CC\_030000

PCI\\CC\_0300

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Identifiers%20for%20PCI%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




