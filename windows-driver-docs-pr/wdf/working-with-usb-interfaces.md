---
title: Working with USB Interfaces
description: Working with USB Interfaces
ms.assetid: 6a1801e4-bd46-4a78-8c30-7dc62e41a37a
keywords:
- USB I/O targets WDK KMDF , USB interfaces
- USB interfaces WDK KMDF
- framework objects WDK KMDF , USB interface objects
- interface objects WDK KMDF
- alternate USB interface settings WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





