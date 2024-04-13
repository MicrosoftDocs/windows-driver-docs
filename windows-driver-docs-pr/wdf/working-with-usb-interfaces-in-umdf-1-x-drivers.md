---
title: Working with USB Interfaces in UMDF 1.x Drivers
description: Working with USB Interfaces in UMDF 1.x Drivers
keywords:
- UMDF WDK , USB interfaces
- User-Mode Driver Framework WDK , USB interfaces
- user-mode drivers WDK UMDF , USB interfaces
- USB interfaces WDK UMDF
ms.date: 04/20/2017
---

# Working with USB Interfaces in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework represents each USB interface as a framework USB interface object. When a UMDF driver creates a framework USB device object, the framework creates a framework USB interface object for each USB interface that the device supports.

Most USB devices have only one interface, and the interface has only one alternative setting. Drivers for such devices typically do not need to use the object methods that the framework's USB interface object defines.

If a UMDF driver supports USB devices that provide multiple interfaces or alternate settings, interface object methods enable the driver to:

-   [Obtain interface information](#obtaining-umdf-usb-interface-information).

-   [Select an alternate setting for a USB interface](#selecting-an-alternate-setting-for-a-umdf-usb-interface).

### Obtaining UMDF-USB Interface Information

After a UMDF driver has called the [**IWDFUsbTargetFactory::CreateUsbTargetDevice**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetfactory-createusbtargetdevice) method to create a UMDF-USB target device object, the driver can call the [**IWDFUsbTargetDevice::GetNumInterfaces**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-getnuminterfaces) method to obtain the number of USB interfaces that the device supports. Next, the driver can make calls to the [**IWDFUsbTargetDevice::RetrieveUsbInterface**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetdevice-retrieveusbinterface) method to obtain pointers to the [IWDFUsbInterface](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbinterface) interfaces that expose the USB interfaces that the device supports. Then the driver can call the following methods that each USB interface object defines for obtaining information about the USB interface:

<a href="" id="iwdfusbinterface--getinterfacenumber"></a>[**IWDFUsbInterface::GetInterfaceNumber**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getinterfacenumber)  
Obtains the USB interface number that is associated with a USB interface object.

<a href="" id="iwdfusbinterface--getinterfacedescriptor"></a>[**IWDFUsbInterface::GetInterfaceDescriptor**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getinterfacedescriptor)  
Obtains that USB interface descriptor that is associated with one of the alternate settings of a USB interface.

<a href="" id="iwdfusbinterface--getnumendpoints"></a>[**IWDFUsbInterface::GetNumEndPoints**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getnumendpoints)  
Obtains the number of endpoints (also known as pipes) that are associated with one of the alternate settings of a USB interface.

<a href="" id="iwdfusbinterface--getconfiguredsettingindex"></a>[**IWDFUsbInterface::GetConfiguredSettingIndex**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getconfiguredsettingindex)  
Obtains an index value that identifies the alternate setting that is currently selected for a USB interface.

<a href="" id="iwdfusbinterface--retrieveusbpipeobject"></a>[**IWDFUsbInterface::RetrieveUsbPipeObject**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-retrieveusbpipeobject)  
Retrieves a pointer to the [IWDFUsbTargetPipe](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe) interface that exposes the framework pipe object that is associated with a specified USB device interface and pipe index.

<a href="" id="iwdfusbinterface--getwinusbhandle"></a>[**IWDFUsbInterface::GetWinUsbHandle**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-getwinusbhandle)  
Obtains the WinUsb interface handle that is associated with a USB interface.

### Selecting an Alternate Setting for a UMDF-USB Interface

The UMDF driver can call the [**IWDFUsbInterface::SelectSetting**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-selectsetting) method to select an alternate setting for one of the USB interfaces that the device supports.

The device's alternate settings must be numbered contiguously, starting with zero.

**Important**   Selecting a setting invalidates any information about the interface and endpoints. Therefore, the driver should obtain this information again. The driver must also discard any USB pipe objects that it previously retrieved and recreate them.

 

 

