---
title: Windows Classes vs. Interface Classes
description: Windows Classes vs.
ms.assetid: 3df99388-6fcf-44bb-a6c9-99281a8879d7
keywords: ["device interface classes WDK device installations", "device setup classes WDK device installations", "interface classes WDK device installations", "setup classes WDK device installations"]
---

# Windows Classes vs. Interface Classes


## <a href="" id="ddk-setup-classes-versus-interface-classes-dg"></a>


It is important to distinguish between the two types of device classes: [*device interface classes*](device-interface-classes.md) and [*device setup classes*](device-setup-classes.md). The two can be easily confused because in user-mode code the same set of [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) and the same set of data structures ([device information sets](device-information-sets.md)) are used with both classes. Moreover, a device often belongs to both a setup class and several interface classes at the same time. Nevertheless, the two types of classes serve different purposes, make use of different areas in the registry, and rely on a different set of header files for defining class GUIDs.

[Device setup classes](device-setup-classes.md) provide a mechanism for grouping devices that are installed and configured in the same way. A setup class identifies the class installer and class co-installers that are involved in installing the devices that belong to the class. For example, all CD-ROM drives belong to the CDROM setup class and will use the same co-installer when installed.

[Device interface classes](device-interface-classes.md) provide a mechanism for grouping devices according to shared characteristics. Instead of tracking the presence in the system of an individual device, drivers and user applications can register to be notified of the arrival or removal of any device that belongs to a particular interface class.

Windows classes are defined in the system file *Devguid.h*. This file defines a series of GUIDs for setup classes. However, the device setup classes represented in *Devguid.h* must not be confused with device *interface* classes. The *Devguid.h* file only contains GUIDs for setup classes.

Definitions of interface classes are not provided in a single file. A device interface class is always defined in a header file that belongs exclusively to a particular class of devices. For example, *Ntddmou.h* contains the definition of GUID\_CLASS\_MOUSE, the GUID representing the mouse interface class; *Ntddpar.h* defines the interface class GUID for parallel devices; *Ntddpcm.h* defines the standard interface class GUID for PCMCIA devices; *Ntddstor.h* defines the interface class GUID for storage devices, and so on.

The GUIDs in header files that are specific to the device interface class should be used to register for notification of arrival of an instance of a device interface. If a driver registers for notification using a setup class GUID instead of an interface class GUID, then it will not be notified when an interface arrives.

When defining a new setup class or interface class, *do not use a single GUID to identify both a setup class and an interface class.*

For more information about GUIDs, see [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Windows%20Classes%20vs.%20Interface%20Classes%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




