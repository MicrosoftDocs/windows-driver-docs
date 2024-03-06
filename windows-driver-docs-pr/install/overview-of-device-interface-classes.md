---
title: Overview of Device Interface Classes
description: Learn more about device interface classes
keywords:
- interface classes WDK device installations
- device interfaces WDK device installations
- interfaces WDK device
- device interface classes WDK device installations
ms.date: 04/11/2022
---

# Overview of device interface classes

Any driver of a physical, logical, or virtual device to which user-mode code can direct I/O requests must supply a name for its user-mode clients. Using the name, a user-mode application (or other system component) identifies the device from which it is requesting I/O.

In Windows NT 4.0 and earlier versions of the NT-based operating system, drivers named their device objects and then set up symbolic links in the registry between these names and a user-visible Win32 logical name.

Starting with Windows 2000, drivers do not name device objects. Instead, they make use of *device interfaces* which are grouped by *device interface classes*. A device interface class is a way of exporting device and driver functionality to other system components, including other drivers, as well as user-mode applications. A driver can register and enable a *device interface* instance of the *device interface class* for each device object to which user-mode I/O requests might be sent.  Each *device interface class* should represent a conceptual functionality that any *device interface* in that class should support or represent such as a particular I/O contract.

Each device interface class is associated with a GUID. The system defines GUIDs for common device interface classes in device-specific header files. Vendors can create additional device interface classes.

For example, three different types of mouse devices could register *device interfaces* that are members of the same device interface class, even if one connects through a USB port, a second through a serial port, and the third through an infrared port. Each driver registers its device as a member of the interface class GUID_DEVINTERFACE_MOUSE. This GUID is defined in the header file *Ntddmou.h*.

Drivers can register and enable *device interfaces* for a device they control for as many *device interface classes* that the device and driver support the functionality for. For example, a driver for a disk that can be mounted should register for both its disk interface class (GUID_DEVINTERFACE_DISK) and the mountable device class (MOUNTDEV_MOUNTED_DEVICE_GUID).

When a driver registers a *device interface* instance of a *device interface class*, the I/O manager associates the device and the device interface class GUID with a symbolic link name. The driver must *enable* the *device interface* in order for that symbolic link to be usable for a driver or application to send I/O to. The registration of the link name persists across system starts, but the *device interface* must be enabled by the driver on every enumeration of the device. An application that uses a particular *device interface class* can query for instances of the *device interfaces* in that class and receive a list of symbolic link names representing devices that support the interface. The application can then use the symbolic link name as a target for I/O requests.

Do not confuse device interfaces with the interfaces that drivers can export in response to an [**IRP_MN_QUERY_INTERFACE**](../kernel/irp-mn-query-interface.md) request. That IRP is used to pass routine entry points between kernel-mode drivers.
