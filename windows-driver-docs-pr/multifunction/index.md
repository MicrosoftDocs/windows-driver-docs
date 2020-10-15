---
title: Multifunction device driver design guide
description: Multifunction device driver design guide
ms.assetid: 110c0b9b-4870-4853-8fbf-a9faf0c5f2ca
keywords:
- multifunction devices WDK
- multifunction devices WDK , about multifunction devices
- combined function devices WDK
- multiple function devices WDK
- printer multiple functions WDK
- DVD/CD-ROM multiple functions WDK
- multifunction devices WDK , installing
- parent buses WDK multifunction devices
- INF files WDK multifunction devices
ms.date: 08/25/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multifunction device driver design guide

A *multifunction device* occupies one location on its parent bus but contains more than one function. Combination printer/scanner/fax devices and modem/network cards are common multifunction devices.

In a multifunction device, the individual functions are independent. This means the functions must have the following characteristics:

- The functions cannot have start-order dependencies.

- The resource requirements for one function cannot be expressed in terms of the resources of another function (for example, *function1* uses I/O port *x* and *function2* uses port *x* + 200).

- Each function must be able to operate as a separate device, even if it is serviced by the same drivers as another function.

- Each function on the device must be enumerated.

- Resource requirements for each function must be communicated to the PnP manager.

- There must be INF files and drivers for each function.

The component responsible for each of these tasks depends on the multifunction standard for the device's parent bus, the extent to which the device conforms to the standard, and the capabilities of the parent bus driver.

If the device complies with the multifunction standards for its bus, your driver requirements are significantly reduced. Industry-wide multifunction standards have been defined for the PC Card and PCI buses.

If you are working with a multifunction DVD/CD-ROM device used for data storage (not for audio/video playback), you should use the system-supplied WDM DVD class driver, which treats the device as a single logical unit.

For a multifunction device that combines other functionality, you can use a system-supplied driver and INF file if the device complies with the multifunction standards for its bus. The system supplied multifunction driver (mf.sys) can handle the bus-level enumeration and resource allocation requirements for the device, and the system-supplied INF (mf.sys) can install the multifunction device. You need to supply only a function driver and INF file for each of the individual device functions.

If the device does not comply with the standard for its bus, you might need to supply a driver equivalent to mf.sys in functionality, in addition to function drivers and INF files for the device functions.

To install a multifunction device, you typically provide a base INF file for the device and an additional INF file for each of the device's functions. The base INF file typically copies the INF files for the device's individual functions. For information about how to accomplish this, see [Copying INFs](../install/copying-inf-files.md).

The following sections describe driver and installation requirements for various types of multifunction devices:

[Supporting Multifunction PC Card Devices](supporting-multifunction-pc-card-devices.md)

[Supporting Multifunction PCI Devices](supporting-multifunction-pci-devices.md)

[Supporting Multifunction Devices On Other Buses](supporting-multifunction-devices-on-other-buses.md)

[Using the System-Supplied Multifunction Bus Driver](using-the-system-supplied-multifunction-bus-driver.md)

[Creating Resource Maps for a Multifunction Device](creating-resource-maps-for-a-multifunction-device.md)

See [INF File Sections](../install/inf-classinstall32-section.md) and [INF File Directives](../install/inf-addcomponent-directive.md) for information about INF file syntax.

The Windows Driver Kit (WDK) includes a separate section that describes how to support [multifunction audio devices](../audio/multifunction-audio-devices.md).