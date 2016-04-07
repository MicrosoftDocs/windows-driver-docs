---
title: Working with USB Interfaces in UMDF 1.x Drivers
description: Working with USB Interfaces in UMDF 1.x Drivers
ms.assetid: fc25e3b2-1631-445e-9340-a8cc92c68733
keywords: ["UMDF WDK , USB interfaces", "User-Mode Driver Framework WDK , USB interfaces", "user-mode drivers WDK UMDF , USB interfaces", "USB interfaces WDK UMDF"]
---

# Working with USB Interfaces in UMDF 1.x Drivers


\[This topic applies to UMDF 1.*x*.\]

The framework represents each USB interface as a framework USB interface object. When a UMDF driver creates a framework USB device object, the framework creates a framework USB interface object for each USB interface that the device supports.

Most USB devices have only one interface, and the interface has only one alternative setting. Drivers for such devices typically do not need to use the object methods that the framework's USB interface object defines.

If a UMDF driver supports USB devices that provide multiple interfaces or alternate settings, interface object methods enable the driver to:

-   [Obtain interface information](https://msdn.microsoft.com/library/windows/hardware/ff561478#obtaining-umdf-usb-interface-information).

-   [Select an alternate setting for a USB interface](https://msdn.microsoft.com/library/windows/hardware/ff561478#selecting-an-alternate-setting-for-a-umdf-usb-interface).

### Obtaining UMDF-USB Interface Information

After a UMDF driver has called the [**IWDFUsbTargetFactory::CreateUsbTargetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560390) method to create a UMDF-USB target device object, the driver can call the [**IWDFUsbTargetDevice::GetNumInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff560366) method to obtain the number of USB interfaces that the device supports. Next, the driver can make calls to the [**IWDFUsbTargetDevice::RetrieveUsbInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560381) method to obtain pointers to the [IWDFUsbInterface](https://msdn.microsoft.com/library/windows/hardware/ff560312) interfaces that expose the USB interfaces that the device supports. Then the driver can call the following methods that each USB interface object defines for obtaining information about the USB interface:

<a href="" id="iwdfusbinterface--getinterfacenumber"></a>[**IWDFUsbInterface::GetInterfaceNumber**](https://msdn.microsoft.com/library/windows/hardware/ff560327)  
Obtains the USB interface number that is associated with a USB interface object.

<a href="" id="iwdfusbinterface--getinterfacedescriptor"></a>[**IWDFUsbInterface::GetInterfaceDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff560320)  
Obtains that USB interface descriptor that is associated with one of the alternate settings of a USB interface.

<a href="" id="iwdfusbinterface--getnumendpoints"></a>[**IWDFUsbInterface::GetNumEndPoints**](https://msdn.microsoft.com/library/windows/hardware/ff560334)  
Obtains the number of endpoints (also known as pipes) that are associated with one of the alternate settings of a USB interface.

<a href="" id="iwdfusbinterface--getconfiguredsettingindex"></a>[**IWDFUsbInterface::GetConfiguredSettingIndex**](https://msdn.microsoft.com/library/windows/hardware/ff560317)  
Obtains an index value that identifies the alternate setting that is currently selected for a USB interface.

<a href="" id="iwdfusbinterface--retrieveusbpipeobject"></a>[**IWDFUsbInterface::RetrieveUsbPipeObject**](https://msdn.microsoft.com/library/windows/hardware/ff560339)  
Retrieves a pointer to the [IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391) interface that exposes the framework pipe object that is associated with a specified USB device interface and pipe index.

<a href="" id="iwdfusbinterface--getwinusbhandle"></a>[**IWDFUsbInterface::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560337)  
Obtains the WinUsb interface handle that is associated with a USB interface.

### Selecting an Alternate Setting for a UMDF-USB Interface

The UMDF driver can call the [**IWDFUsbInterface::SelectSetting**](https://msdn.microsoft.com/library/windows/hardware/ff560343) method to select an alternate setting for one of the USB interfaces that the device supports.

The device's alternate settings must be numbered contiguously, starting with zero.

**Important**   Selecting a setting invalidates any information about the interface and endpoints. Therefore, the driver should obtain this information again. The driver must also discard any USB pipe objects that it previously retrieved and recreate them.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Working%20with%20USB%20Interfaces%20in%20UMDF%201.x%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




