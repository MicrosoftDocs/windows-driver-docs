---
title: Comparison of Setup Classes and Interface Classes
description: A comparison of setup classes and interface classes.
keywords:
- device interface classes WDK device installations
- device setup classes WDK device installations
- interface classes WDK device installations
- setup classes WDK device installations
ms.date: 08/05/2025
ms.topic: concept-article
ai-usage: ai-assisted
---

# Comparison of setup classes and interface classes

Understanding the distinction between setup classes and interface classes is crucial for successful Windows driver development and device management. While these classes might appear similar, they serve fundamentally different purposes in the Windows device ecosystem. Setup classes govern how devices are installed and configured by the operating system. Interface classes enable runtime communication and functionality between drivers, applications, and devices. Mastering this distinction will help you choose the correct class type for device installation, implement proper device notifications, and avoid common development pitfalls.

A device often belongs to both a setup class and several interface classes at the same time. Nevertheless, the two types of classes serve different purposes, make use of different areas in the registry, and rely on a different set of header files for defining class GUIDs.

## Comparison

The following table summarizes the key differences and relationships between setup classes and interface classes:

| Aspect | Setup classes | Interface classes |
|--------|---------------|-------------------|
| **Primary Purpose** | Device installation and configuration | Device functionality and communication |
| **Usage** | Used by Windows during device installation | Used by drivers and applications for device interaction |
| **Registry Location** | Stored in setup class registry keys | Stored in interface class registry keys |
| **GUID Definitions** | Defined in *Devguid.h* | Defined in device-specific header files (for example, *Ntddmou.h*, *Ntddpar.h*) |
| **Grouping Criteria** | Devices installed and configured similarly | Devices with shared characteristics or functionality |
| **Notification** | Not used for device arrival or removal notifications | Used for registering device arrival and removal notifications |
| **Examples** | Human Interface Device, Audio Device, Video Device | HID mouse, HID keyboard, USB device |
| **Relationship** | A device belongs to one setup class | A device can belong to multiple interface classes |
| **Lifetime** | Relevant during installation process | Relevant during device operation |

It's important to distinguish between the two types of device classes: *[device interface classes](./overview-of-device-interface-classes.md)* and *[device setup classes](./overview-of-device-setup-classes.md)*. The two can be easily confused. In user-mode code, both classes use the same set of [device installation functions](/previous-versions/ff541299(v=vs.85)). They also use the same set of data structures ([device information sets](device-information-sets.md)).

Both a USB mouse and a USB keyboard could fall under the same setup class (Human Interface Device), but they utilize different interface classes to communicate with the system.

Same setup class, different interface classes:

- **Devices**: A USB mouse and a USB keyboard.
- **Setup Class**: Both devices can belong to the *Human Interface Devices* setup class.
- **Interface Classes**: The mouse might use the *HID mouse* interface class, while the keyboard uses the *HID keyboard* interface class.

Consider a USB audio device and a USB video device. Both might use the same interface class (USB device), but they belong to different setup classes, such as *Audio* and *Display*, respectively.

Same interface class, different setup classes:

- **Devices**: A USB audio device and a USB video device.
- **Interface Class**: Both devices might use the *USB device* interface class.
- **Setup Classes**: The audio device could belong to the *Audio* setup class, while the video device belongs to the *Display* setup class.

## Device setup classes

[Device setup classes](./overview-of-device-setup-classes.md) are predefined categories used solely for the installation and configuration of devices in Windows. They help the operating system understand how to manage the device during the installation process. Setup classes provide a mechanism for grouping devices that are installed and configured in the same way. For more information about setup classes, see [System-defined device setup classes available to vendors](./system-defined-device-setup-classes-available-to-vendors.md).

Windows device setup classes are defined in the system file *Devguid.h*. This file defines a series of GUIDs for setup classes. However, the device setup classes represented in *Devguid.h* must not be confused with device *interface* classes. The *Devguid.h* file only contains GUIDs for setup classes.

## Device interface classes

[Device interface classes](./overview-of-device-interface-classes.md) provide a mechanism for grouping devices according to shared characteristics or functionality. Drivers and user applications can register for notifications about devices in a particular interface class. This means they get notified when any device belonging to that class arrives or is removed from the system. They don't need to track individual devices.

Definitions of interface classes aren't provided in a single file. A device interface class is always defined in a header file that belongs exclusively to a particular class of devices. For example, *Ntddmou.h* contains the definition of GUID_DEVINTERFACE_MOUSE, the GUID representing the mouse interface class. *Ntddpar.h* defines the interface class GUID for parallel devices. *Ntddpcm.h* defines the standard interface class GUID for PCMCIA devices. *Ntddstor.h* defines the interface class GUID for storage devices.

To register for device notifications, use the GUIDs found in the header files that are specific to the device interface class. These GUIDs allow you to be notified when a device interface instance arrives. If a driver registers for notification using a setup class GUID instead of an interface class GUID, it isn't notified when an interface arrives.

When defining a new setup class or interface class, *don't use a single GUID to identify both a setup class and an interface class.*

## Related articles

- [Overview of device setup classes](./overview-of-device-setup-classes.md)
- [System-defined device setup classes available to vendors](./system-defined-device-setup-classes-available-to-vendors.md)
- [Creating a new device setup class](./creating-a-new-device-setup-class.md)
- [Overview of device interface classes](./overview-of-device-interface-classes.md)
- [Using GUIDs in drivers](../kernel/using-guids-in-drivers.md).
