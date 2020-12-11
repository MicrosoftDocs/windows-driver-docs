---
title: Working with USB Devices in UMDF 1.x Drivers
description: Working with USB Devices in UMDF 1.x Drivers
keywords:
- UMDF WDK , USB devices
- User-Mode Driver Framework WDK , USB devices
- user-mode drivers WDK UMDF , USB devices
- USB devices WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Working with USB Devices in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework represents each USB device as a framework USB device object. A UMDF driver must create a framework USB device object before the driver can access the framework's support for USB I/O targets. UMDF provides USB device object methods that enable a UMDF driver to:

-   [Create a UMDF-USB device object](#creating-a-umdf-usb-device-object)

-   [Obtain device information](#obtaining-umdf-usb-device-information)

-   [Send a control transfer](#send-a-control-transfer-to-a-umdf-usb-device-object)

-   [Set power policy](#set-power-policy-for-a-umdf-usb-device-object)

### Creating a UMDF-USB Device Object

To use the framework's USB I/O target capabilities, a UMDF driver must first obtain a pointer to the [IWDFUsbTargetFactory](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetfactory) interface. To obtain the pointer, the driver must call the **QueryInterface** method of the device's [IWDFDevice](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdevice) interface. The following code example shows how to call **QueryInterface** to obtain the pointer:

```cpp
hr = pdevice->QueryInterface(IID_IWDFUsbTargetFactory, (LPVOID*)&ppUsbTargetFactory);
```

The driver must next call the [**IWDFUsbTargetFactory::CreateUsbTargetDevice**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetfactory-createusbtargetdevice) method to create a USB I/O target object for the device. After the driver creates the USB I/O target, the driver can send requests to the I/O target. Typically, drivers call **IWDFUsbTargetFactory::CreateUsbTargetDevice** from within an [**IPnpCallbackHardware::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware-onpreparehardware) callback function.

After the driver calls **IWDFUsbTargetFactory::CreateUsbTargetDevice**, the driver can [obtain USB device information](#obtaining-umdf-usb-device-information) (for example, USB descriptors for the device, USB interfaces, and interface endpoints). The USB descriptors are described in the USB specification.

### Obtaining UMDF-USB Device Information

After a UMDF driver calls the [**IWDFUsbTargetFactory::CreateUsbTargetDevice**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetfactory-createusbtargetdevice) method to create a UMDF-USB target device object, the driver can call the following methods that the USB target device object defines for obtaining information about a USB device:

<a href="" id="iwdfusbtargetdevice--retrievedescriptor"></a>[**IWDFUsbTargetDevice::RetrieveDescriptor**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrievedescriptor)  
Obtains a device's USB device descriptor.

<a href="" id="iwdfusbtargetdevice--getnuminterfaces"></a>[**IWDFUsbTargetDevice::GetNumInterfaces**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-getnuminterfaces)  
Obtains the number of USB interfaces that the device supports.

<a href="" id="iwdfusbtargetdevice--retrieveusbinterface"></a>[**IWDFUsbTargetDevice::RetrieveUsbInterface**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrieveusbinterface)  
Obtains a pointer to a [IWDFUsbInterface](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbinterface) interface that exposes one of the USB interfaces that the device supports.

<a href="" id="iwdfusbtargetdevice--retrievedeviceinformation"></a>[**IWDFUsbTargetDevice::RetrieveDeviceInformation**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrievedeviceinformation)  
Retrieves capability information that is associated with a USB device.

<a href="" id="iwdfusbtargetdevice--retrievepowerpolicy"></a>[**IWDFUsbTargetDevice::RetrievePowerPolicy**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrievepowerpolicy)  
Retrieves a WinUsb power policy.

<a href="" id="iwdfusbtargetdevice--getwinusbhandle"></a>[**IWDFUsbTargetDevice::GetWinUsbHandle**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-getwinusbhandle)  
Obtains the WinUsb interface handle that is associated with the I/O target device object.

### <a href="" id="send-a-control-transfer-to-a-umdf-usb-device-object"></a>Sending a Control Transfer to a UMDF-USB Device Object

A UMDF driver can call the [**IWDFUsbTargetDevice::FormatRequestForControlTransfer**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer) method to format an I/O request that describes a standard, device-class-specific, or vendor-specific USB control transfer. The driver can then call the [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) method to send the request synchronously or asynchronously.

### <a href="" id="set-power-policy-for-a-umdf-usb-device-object"></a>Setting Power Policy for a UMDF-USB Device

A UMDF driver can call the [**IWDFUsbTargetDevice::SetPowerPolicy**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-setpowerpolicy) method to set the power policy that is used by WinUsb for a USB device. The power policy for a USB device effects changes to power management states for the device.

 

