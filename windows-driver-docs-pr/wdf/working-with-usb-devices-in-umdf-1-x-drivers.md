---
title: Working with USB Devices in UMDF 1.x Drivers
description: Working with USB Devices in UMDF 1.x Drivers
ms.assetid: 144898a2-c4e1-495f-a6ca-72d9f09bda90
keywords:
- UMDF WDK , USB devices
- User-Mode Driver Framework WDK , USB devices
- user-mode drivers WDK UMDF , USB devices
- USB devices WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Working with USB Devices in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework represents each USB device as a framework USB device object. A UMDF driver must create a framework USB device object before the driver can access the framework's support for USB I/O targets. UMDF provides USB device object methods that enable a UMDF driver to:

-   [Create a UMDF-USB device object](#creating-a-umdf-usb-device-object)

-   [Obtain device information](#obtaining-umdf-usb-device-information)

-   [Send a control transfer](#send-a-control-transfer-to-a-umdf-usb-device-object)

-   [Set power policy](#set-power-policy-for-a-umdf-usb-device-object)

### Creating a UMDF-USB Device Object

To use the framework's USB I/O target capabilities, a UMDF driver must first obtain a pointer to the [IWDFUsbTargetFactory](https://msdn.microsoft.com/library/windows/hardware/ff560387) interface. To obtain the pointer, the driver must call the **QueryInterface** method of the device's [IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface. The following code example shows how to call **QueryInterface** to obtain the pointer:

```cpp
hr = pdevice->QueryInterface(IID_IWDFUsbTargetFactory, (LPVOID*)&ppUsbTargetFactory);
```

The driver must next call the [**IWDFUsbTargetFactory::CreateUsbTargetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560390) method to create a USB I/O target object for the device. After the driver creates the USB I/O target, the driver can send requests to the I/O target. Typically, drivers call **IWDFUsbTargetFactory::CreateUsbTargetDevice** from within an [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766) callback function.

After the driver calls **IWDFUsbTargetFactory::CreateUsbTargetDevice**, the driver can [obtain USB device information](https://msdn.microsoft.com/library/windows/hardware/ff561472#obtaining-umdf-usb-device-information) (for example, USB descriptors for the device, USB interfaces, and interface endpoints). The USB descriptors are described in the USB specification.

### Obtaining UMDF-USB Device Information

After a UMDF driver calls the [**IWDFUsbTargetFactory::CreateUsbTargetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff560390) method to create a UMDF-USB target device object, the driver can call the following methods that the USB target device object defines for obtaining information about a USB device:

<a href="" id="iwdfusbtargetdevice--retrievedescriptor"></a>[**IWDFUsbTargetDevice::RetrieveDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff560374)  
Obtains a device's USB device descriptor.

<a href="" id="iwdfusbtargetdevice--getnuminterfaces"></a>[**IWDFUsbTargetDevice::GetNumInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff560366)  
Obtains the number of USB interfaces that the device supports.

<a href="" id="iwdfusbtargetdevice--retrieveusbinterface"></a>[**IWDFUsbTargetDevice::RetrieveUsbInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560381)  
Obtains a pointer to a [IWDFUsbInterface](https://msdn.microsoft.com/library/windows/hardware/ff560312) interface that exposes one of the USB interfaces that the device supports.

<a href="" id="iwdfusbtargetdevice--retrievedeviceinformation"></a>[**IWDFUsbTargetDevice::RetrieveDeviceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff560377)  
Retrieves capability information that is associated with a USB device.

<a href="" id="iwdfusbtargetdevice--retrievepowerpolicy"></a>[**IWDFUsbTargetDevice::RetrievePowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff560379)  
Retrieves a WinUsb power policy.

<a href="" id="iwdfusbtargetdevice--getwinusbhandle"></a>[**IWDFUsbTargetDevice::GetWinUsbHandle**](https://msdn.microsoft.com/library/windows/hardware/ff560369)  
Obtains the WinUsb interface handle that is associated with the I/O target device object.

### <a href="" id="send-a-control-transfer-to-a-umdf-usb-device-object"></a>Sending a Control Transfer to a UMDF-USB Device Object

A UMDF driver can call the [**IWDFUsbTargetDevice::FormatRequestForControlTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff560363) method to format an I/O request that describes a standard, device-class-specific, or vendor-specific USB control transfer. The driver can then call the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method to send the request synchronously or asynchronously.

### <a href="" id="set-power-policy-for-a-umdf-usb-device-object"></a>Setting Power Policy for a UMDF-USB Device

A UMDF driver can call the [**IWDFUsbTargetDevice::SetPowerPolicy**](https://msdn.microsoft.com/library/windows/hardware/ff560385) method to set the power policy that is used by WinUsb for a USB device. The power policy for a USB device effects changes to power management states for the device.

 

 





