---
title: Registering a Device Interface Class
description: Learn more about how to register a device interface class
keywords:
- interface classes WDK device installations
- registering device interface classes
- device interface classes WDK device installations
ms.date: 04/11/2022
---

# Registering a device interface class

There are two ways to register a device interface class:

- A driver controlling a PnP device can register a *device interface* in a particular *device interface class*.  As part of registering the *device interface*, the *device interface class* will be implicitly created. This topic describes how to use the routines to register a *device interface*.

- An INF file can contain [**INF DDInstall.Interfaces sections**](inf-ddinstall-interfaces-section.md).

A WDM driver does not name its device objects. Instead, when the driver calls [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) to create a device object, it should specify a null string for the device name. For more information, see [Creating a device object](../kernel/creating-a-device-object.md).

After creating the device object and attaching it to the device stack, one driver calls [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) to register a *device interface class* and to create a *device interface* instance of the class. Typically, the function driver makes this call from its [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, but sometimes a filter driver registers the interface.

The routine returns a symbolic link name. A driver passes the link name when it enables or disables the device interface instance. Other system components cannot use a device interface instance until the driver has enabled it. See [Enabling and disabling a device interface instance](enabling-and-disabling-a-device-interface-instance.md) for details.

The driver also uses the symbolic link name to access the registry key, in which it can store information that is specific to the device interface (See [**IoOpenDeviceInterfaceRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioopendeviceinterfaceregistrykey) for more information). Applications use the link name to open the device.

A driver can call [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) as many times as necessary to register instances of additional device interface classes.

To use *device interfaces* from a WDF driver, please see [Using device interfaces (WDF)](../wdf/using-device-interfaces.md).
