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

 

 





