---
title: Registering a Device Interface Class
description: Registering a Device Interface Class
ms.assetid: 1518570d-1cfb-498e-91f7-35f9cc11aff5
keywords:
- interface classes WDK device installations
- registering device interface classes
- device interface classes WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a Device Interface Class





There are three ways to register a device interface class:

-   Kernel-mode components, such as most drivers, can call I/O manager routines. This topic describes how to use these routines.

-   User-mode [*device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) call **SetupDi***Xxx* functions. For more information about these functions, see [SetupDi Device Interface Functions](using-device-installation-functions.md#ddk-setupdi-device-interface-functions-dg).

-   An INF file can contain [**INF DDInstall.Interfaces sections**](inf-ddinstall-interfaces-section.md).

A WDM driver does not name its device objects. Instead, when the driver calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create a device object, it should specify a null string for the device name. For more information, see [Creating a Device Object](https://msdn.microsoft.com/library/windows/hardware/ff542862).

After creating the device object and attaching it to the device stack, one driver calls [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) to register a device interface class and to create an instance of the interface. Typically, the function driver makes this call from its [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, but sometimes the filter driver registers the interface.

The routine returns a symbolic link name. A driver passes the link name when it enables or disables the device interface instance. Other system components cannot use a device interface instance until the driver has enabled it. See [Enabling and Disabling a Device Interface Instance](enabling-and-disabling-a-device-interface-instance.md) for details.

The driver also uses the symbolic link name to access the registry key, in which it can store information that is specific to the device interface. (See [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) for more information.) Applications use the link name to open the device.

A driver can call [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) as many times as necessary to register instances of additional device interface classes.

 

 





