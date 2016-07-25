---
title: Registering a Device Interface Class
description: Registering a Device Interface Class
ms.assetid: 1518570d-1cfb-498e-91f7-35f9cc11aff5
keywords: ["interface classes WDK device installations", "registering device interface classes", "device interface classes WDK device installations"]
---

# Registering a Device Interface Class


## <a href="" id="ddk-registering-a-device-interface-class-dg"></a>


There are three ways to register a device interface class:

-   Kernel-mode components, such as most drivers, can call I/O manager routines. This topic describes how to use these routines.

-   User-mode [*device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) call **SetupDi***Xxx* functions. For more information about these functions, see [SetupDi Device Interface Functions](using-device-installation-functions.md#ddk-setupdi-device-interface-functions-dg).

-   An INF file can contain [**INF DDInstall.Interfaces sections**](inf-ddinstall-interfaces-section.md).

A WDM driver does not name its device objects. Instead, when the driver calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create a device object, it should specify a null string for the device name. For more information, see [Creating a Device Object](https://msdn.microsoft.com/library/windows/hardware/ff542862).

After creating the device object and attaching it to the device stack, one driver calls [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) to register a device interface class and to create an instance of the interface. Typically, the function driver makes this call from its [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, but sometimes the filter driver registers the interface.

The routine returns a symbolic link name. A driver passes the link name when it enables or disables the device interface instance. Other system components cannot use a device interface instance until the driver has enabled it. See [Enabling and Disabling a Device Interface Instance](enabling-and-disabling-a-device-interface-instance.md) for details.

The driver also uses the symbolic link name to access the registry key, in which it can store information that is specific to the device interface. (See [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) for more information.) Applications use the link name to open the device.

A driver can call [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) as many times as necessary to register instances of additional device interface classes.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Registering%20a%20Device%20Interface%20Class%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




