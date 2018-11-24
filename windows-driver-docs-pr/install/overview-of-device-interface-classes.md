---
title: Overview of Device Interface Classes
description: Overview of Device Interface Classes
ms.assetid: e463e3f0-cbc8-490e-a7c4-4837d43c20e3
keywords:
- interface classes WDK device installations
- device interfaces WDK device installations
- interfaces WDK device
- device interface classes WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Device Interface Classes





Any driver of a physical, logical, or virtual device to which user-mode code can direct I/O requests must supply some sort of name for its user-mode clients. Using the name, a user-mode application (or other system component) identifies the device from which it is requesting I/O.

In Windows NT 4.0 and earlier versions of the NT-based operating system, drivers named their device objects and then set up symbolic links in the registry between these names and a user-visible Win32 logical name.

Starting with Windows 2000, drivers do not name device objects. Instead, they make use of *device interface classes*. A device interface class is a way of exporting device and driver functionality to other system components, including other drivers, as well as user-mode applications. A driver can register a device interface class, then enable an instance of the class for each device object to which user-mode I/O requests might be sent.

Each device interface class is associated with a GUID. The system defines GUIDs for common device interface classes in device-specific header files. Vendors can create additional device interface classes.

For example, three different types of mouse devices could be members of the same device interface class, even if one connects through a USB port, a second through a serial port, and the third through an infrared port. Each driver registers its device as a member of the interface class GUID_DEVINTERFACE_MOUSE. This GUID is defined in the header file *Ntddmou.h*.

Typically, drivers register for only one interface class. However, drivers for devices that have specialized functionality beyond that defined for their standard interface class might also register for an additional class. For example, a driver for a disk that can be mounted should register for both its disk interface class (GUID_DEVINTERFACE_DISK) and the mountable device class (MOUNTDEV_MOUNTED_DEVICE_GUID).

When a driver registers an instance of a device interface class, the I/O manager associates the device and the device interface class GUID with a symbolic link name. The link name is stored in the registry and persists across system starts. An application that uses the interface can query for instances of the interface and receive a symbolic link name representing a device that supports the interface. The application can then use the symbolic link name as a target for I/O requests.

Do not confuse device interfaces with the interfaces that drivers can export in response to an [**IRP_MN_QUERY_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request. That IRP is used to pass routine entry points between kernel-mode drivers.

 

 





