---
title: Working with USB Interfaces
description: Working with USB Interfaces
ms.assetid: 6a1801e4-bd46-4a78-8c30-7dc62e41a37a
keywords: ["USB I/O targets WDK KMDF , USB interfaces", "USB interfaces WDK KMDF", "framework objects WDK KMDF , USB interface objects", "interface objects WDK KMDF", "alternate USB interface settings WDK KMDF"]
---

# Working with USB Interfaces


The framework represents each USB interface as a *framework USB interface object*. When a driver [creates a framework USB device object](working-with-usb-devices.md#creating-a-framework-usb-device-object), the framework creates a framework USB interface object for each USB interface that the device's first USB configuration contains.

Most USB devices have only one interface, and the interface has only one alternate setting. Drivers for such devices typically do not need to use the object methods that the framework's USB interface object defines.

If your driver supports USB devices that provide multiple interfaces or alternate settings, interface object methods enable the driver to perform the following operations:

-   [Obtain interface information.](#obtaining-interface-information)

-   [Select an alternate setting for a USB interface.](#selecting-an-alternate-setting-for-a-usb-interface)

### <a href="" id="obtaining-interface-information"></a> Obtaining Interface Information

After your driver has called [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428), it can call [**WdfUsbTargetDeviceGetInterface**](https://msdn.microsoft.com/library/windows/hardware/ff550092) to obtain a handle to a framework USB interface object that represents one of the device's USB interfaces. Then your driver can call several methods that the USB interface object defines for obtaining information about the USB interface.

Your driver can call the following methods anytime after it has called [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428):

<a href="" id="---------wdfusbinterfacegetinterfacenumber--------"></a>[**WdfUsbInterfaceGetInterfaceNumber**](https://msdn.microsoft.com/library/windows/hardware/ff550065)  
Returns the USB interface number that is associated with a USB interface object.

<a href="" id="---------wdfusbinterfacegetdescriptor--------"></a>[**WdfUsbInterfaceGetDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550060)  
Retrieves that USB interface descriptor that is associated with one of the alternate settings of a USB interface.

<a href="" id="---------wdfusbinterfacegetnumendpoints--------"></a>[**WdfUsbInterfaceGetNumEndpoints**](https://msdn.microsoft.com/library/windows/hardware/ff550068)  
Returns the number of endpoints that are associated with one of the alternate settings of a USB interface.

<a href="" id="---------wdfusbinterfacegetendpointinformation--------"></a>[**WdfUsbInterfaceGetEndpointInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550063)  
Retrieves information about an endpoint and its associated pipe.

Your driver can call the following methods after it has called [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101):

<a href="" id="---------wdfusbinterfacegetconfiguredsettingindex--------"></a>[**WdfUsbInterfaceGetConfiguredSettingIndex**](https://msdn.microsoft.com/library/windows/hardware/ff550059)  
Returns an index value that identifies the alternate setting that is currently selected for a USB interface.

<a href="" id="---------wdfusbinterfacegetnumconfiguredpipes--------"></a>[**WdfUsbInterfaceGetNumConfiguredPipes**](https://msdn.microsoft.com/library/windows/hardware/ff550066)  
Returns the number of pipes that are configured for a specified USB device interface.

<a href="" id="---------wdfusbinterfacegetconfiguredpipe--------"></a>[**WdfUsbInterfaceGetConfiguredPipe**](https://msdn.microsoft.com/library/windows/hardware/ff550057)  
Returns a handle to the framework pipe object that is associated with a specified USB device interface and pipe index.

### <a href="" id="selecting-an-alternate-setting-for-a-usb-interface"></a> Selecting an Alternate Setting for a USB Interface

After a driver has called [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428), the driver can call [**WdfUsbInterfaceGetNumSettings**](https://msdn.microsoft.com/library/windows/hardware/ff550070) to obtain the number of alternate settings that a USB interface supports.

After a driver has called [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101) to select a configuration for a USB device, the driver can call [**WdfUsbInterfaceSelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff550073) to select an alternate setting for one of the configuration's USB interfaces.

The device's alternate settings must be numbered contiguously, starting with zero.

For related information, see [How to select an alternate setting in a USB interface](https://msdn.microsoft.com/library/windows/hardware/hh968309).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Working%20with%20USB%20Interfaces%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




