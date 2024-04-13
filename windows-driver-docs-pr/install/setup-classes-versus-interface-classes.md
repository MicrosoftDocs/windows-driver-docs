---
title: Setup Classes Vs. Interface Classes
description: Learn more about setup classes vs. interface classes
keywords:
- device interface classes WDK device installations
- device setup classes WDK device installations
- interface classes WDK device installations
- setup classes WDK device installations
ms.date: 04/11/2022
---

# Setup classes vs. interface classes

It is important to distinguish between the two types of device classes: [*device interface classes*](./overview-of-device-interface-classes.md) and [*device setup classes*](./overview-of-device-setup-classes.md). The two can be easily confused because in user-mode code the same set of [device installation functions](/previous-versions/ff541299(v=vs.85)) and the same set of data structures ([device information sets](device-information-sets.md)) are used with both classes. Moreover, a device often belongs to both a setup class and several interface classes at the same time. Nevertheless, the two types of classes serve different purposes, make use of different areas in the registry, and rely on a different set of header files for defining class GUIDs.

[Device setup classes](./overview-of-device-setup-classes.md) provide a mechanism for grouping devices that are installed and configured in the same way. For example, all CD-ROM drives belong to the CDROM setup class.

[Device interface classes](./overview-of-device-interface-classes.md) provide a mechanism for grouping devices according to shared characteristics or functionality. Instead of tracking the presence in the system of an individual device, drivers and user applications can register to be notified of the arrival or removal of any device that belongs to a particular interface class.

Windows device setup classes are defined in the system file *Devguid.h*. This file defines a series of GUIDs for setup classes. However, the device setup classes represented in *Devguid.h* must not be confused with device *interface* classes. The *Devguid.h* file only contains GUIDs for setup classes.

Definitions of interface classes are not provided in a single file. A device interface class is always defined in a header file that belongs exclusively to a particular class of devices. For example, *Ntddmou.h* contains the definition of GUID_DEVINTERFACE_MOUSE, the GUID representing the mouse interface class; *Ntddpar.h* defines the interface class GUID for parallel devices; *Ntddpcm.h* defines the standard interface class GUID for PCMCIA devices; *Ntddstor.h* defines the interface class GUID for storage devices, and so on.

The GUIDs in header files that are specific to the device interface class should be used to register for notification of arrival of an instance of a device interface. If a driver registers for notification using a setup class GUID instead of an interface class GUID, then it will not be notified when an interface arrives.

When defining a new setup class or interface class, *do not use a single GUID to identify both a setup class and an interface class.*

For more information about GUIDs, see [Using GUIDs in drivers](../kernel/using-guids-in-drivers.md).
