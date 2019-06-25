---
title: Working with USB Devices
description: This topic describes the operations that a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) driver starting in version 2 can perform using the USB device object methods provided by Windows Driver Frameworks (WDF).
ms.assetid: 8e06f3c4-1a58-4b9f-ae89-ff4e37eb8f0a
keywords:
- USB I/O targets WDK KMDF , framework USB device objects
- framework objects WDK KMDF , USB device objects
- USB request blocks WDK KMDF
- URBs WDK KMDF
- USB I/O targets WDK KMDF , USB devices
- control transfers WDK KMDF
- power-cycling ports WDK KMDF
- resetting ports WDK KMDF
- sending URBs WDK KMDF
- Unicode strings WDK KMDF
- status information WDK KMDF , USB I/O targets
- device objects WDK KMDF
ms.date: 06/24/2019
ms.localizationpriority: medium
---

# Working with USB Devices


This topic describes the operations that a Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) driver starting in version 2 can perform using the USB device object methods provided by Windows Driver Frameworks (WDF).

It contains the following sections:

-   [Creating a USB device object](#creating-a-framework-usb-device-object)
-   [Configuring a USB Device](#selecting-a-device-configuration)
-   [Obtaining Device Information](#obtaining-device-information)
-   [Getting USB Descriptors](#obtaining-a-device-s-unicode-strings)
-   [Sending a Control Transfer](#sending-a-control-transfer)
-   [Resetting and Power-Cycling a Device's Port](#resetting-and-power-cycling-a-device-s-port)
-   [Sending an URB to a Device](#sending-a-urb-to-a-device)

For step-by-step directions on writing a simple KMDF-based USB client driver, see [How to write your first USB client driver (KMDF)](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index).

## <a href="" id="creating-a-framework-usb-device-object"></a> Creating a USB device object


To use the framework's USB I/O target objects (WDFUSBDEVICE, WDFUSBINTERFACE, and WDFUSBPIPE), your client driver must first call [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters) to create a USB device object. Typically, a driver calls **WdfUsbTargetDeviceCreateWithParameters** from its [*EvtDevicePrepareHardware*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function.

When the driver calls [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters), the framework creates a WDFUSBDEVICE object and associates it with the FDO that represents the USB device. The method returns a handle to the new framework USB device object that the USB client driver can then use to communicate with the physical device.

After calling [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters), the driver can call [**WdfUsbTargetDeviceGetDeviceDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor) and [**WdfUsbTargetDeviceRetrieveConfigDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor) to obtain USB descriptors from the device. Those descriptors contain information about the device's first configuration, its interface settings, and their defined endpoints. (The USB descriptors are defined in the official USB specification.)

## <a href="" id="selecting-a-device-configuration"></a>Configuring a USB Device


The [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters) method also creates a framework USB interface object for each USB interface that the device's first configuration contains.

After calling [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters), the client driver must call [**WdfUsbTargetDeviceSelectConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceselectconfig) to select a configuration. This method creates framework interface objects for each alternate setting of the interface in the selected configuration.

The method also creates pipe objects that represent endpoints defined in each alternate setting of each interface of the selected configuration.

After you have selected a configuration, you can [change alternate settings](working-with-usb-interfaces.md#selecting-an-alternate-setting-for-a-usb-interface) for the configuration's interfaces, if necessary.

You can also call [**WdfUsbTargetDeviceSelectConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceselectconfig) to deconfigure a device.

For related information, see:

-   [How to select a configuration for a USB device](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)
-   [How to select an alternate setting in a USB interface](https://docs.microsoft.com/windows-hardware/drivers/usbcon/)

## <a href="" id="obtaining-device-information"></a> Obtaining Device Information


After configuring a device, your client driver can call the following methods to obtain information about a USB device:

<a href="" id="wdfusbtargetdevicequeryusbcapability"></a>[**WdfUsbTargetDeviceQueryUsbCapability**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)  
Determines whether the host controller and USB driver stack support a specific capability. Before calling [**WdfUsbTargetDeviceQueryUsbCapability**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability), a driver must call [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters).

<a href="" id="wdfusbtargetdevicegetiotarget"></a>[**WdfUsbTargetDeviceGetIoTarget**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicegetiotarget)  
Returns a handle to the I/O target object that is associated with a USB device. The driver can pass this handle to [**WdfRequestSend**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsend) or [**WdfIoTargetStop**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfiotarget/nf-wdfiotarget-wdfiotargetstop).

<a href="" id="wdfusbtargetdeviceretrieveinformation"></a>[**WdfUsbTargetDeviceRetrieveInformation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveinformation)  
Retrieves version and capability information that is associated with a USB device.

<a href="" id="wdfusbtargetdeviceisconnectedsynchronous--kmdf-only-"></a>[**WdfUsbTargetDeviceIsConnectedSynchronous (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceisconnectedsynchronous)  
Determines if the device is connected.

<a href="" id="wdfusbtargetdeviceretrievecurrentframenumber--kmdf-only-"></a>[**WdfUsbTargetDeviceRetrieveCurrentFrameNumber (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrievecurrentframenumber)  
Retrieves the current USB frame number.

## <a href="" id="obtaining-a-device-s-unicode-strings"></a>Getting USB Descriptors


To obtain the Unicode strings that are contained in a USB device's descriptors, the driver can call any of the following methods:

<a href="" id="wdfusbtargetdevicegetdevicedescriptor"></a>[**WdfUsbTargetDeviceGetDeviceDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor)  
Obtains a device's [USB device descriptor](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index).

<a href="" id="wdfusbtargetdeviceretrieveconfigdescriptor"></a>[**WdfUsbTargetDeviceRetrieveConfigDescriptor**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)  
Obtains a device's [USB configuration descriptor](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index), interface descriptors, and endpoint descriptors.

<a href="" id="---------wdfusbtargetdevicequerystring--------"></a>[**WdfUsbTargetDeviceQueryString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicequerystring)  
Copies a Unicode string to a driver-supplied buffer.

<a href="" id="---------wdfusbtargetdeviceallocandquerystring--------"></a>[**WdfUsbTargetDeviceAllocAndQueryString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceallocandquerystring)  
Copies a Unicode string to a framework-supplied buffer.

<a href="" id="---------wdfusbtargetdeviceformatrequestforstring--------"></a>[**WdfUsbTargetDeviceFormatRequestForString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforstring)  
Formats a request for a Unicode string. The driver can call [**WdfRequestSend**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsend) to send the request synchronously or asynchronously.

## <a href="" id="sending-a-control-transfer"></a> Sending a Control Transfer


Your driver can call the following methods to send an I/O request that describes a standard, device class-specific, or vendor-specific USB control transfer.

<a href="" id="---------wdfusbtargetdevicesendcontroltransfersynchronously--------"></a>[**WdfUsbTargetDeviceSendControlTransferSynchronously**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously)  
Synchronously sends a USB control transfer request.

<a href="" id="---------wdfusbtargetdeviceformatrequestforcontroltransfer--------"></a>[**WdfUsbTargetDeviceFormatRequestForControlTransfer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer)  
Formats a request for a USB control transfer. The driver can call [**WdfRequestSend**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsend) to send the request synchronously or asynchronously.

For related information, see [How to send a USB control transfer](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index).

## <a href="" id="resetting-and-power-cycling-a-device-s-port"></a> Resetting and Power-Cycling a Device's Port


Your driver can call the following methods to reset or power-cycle the USB port that a device is connected to:

<a href="" id="---------wdfusbtargetdeviceresetportsynchronously"></a>[**WdfUsbTargetDeviceResetPortSynchronously**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceresetportsynchronously)  
Synchronously sends a request to reset a device's USB port.

<a href="" id="---------wdfusbtargetdevicecycleportsynchronously--kmdf-only-"></a>[**WdfUsbTargetDeviceCyclePortSynchronously (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecycleportsynchronously)  
Synchronously sends a request to power-cycle a device's USB port.

<a href="" id="---------wdfusbtargetdeviceformatrequestforcycleport--kmdf-only-"></a>[**WdfUsbTargetDeviceFormatRequestForCyclePort (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcycleport)  
Formats a request to power-cycle a device's USB port. The driver must call [**WdfRequestSend**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsend) to send the request synchronously or asynchronously.

For related information, see [How to recover from USB pipe errors](https://docs.microsoft.com/windows-hardware/drivers/usbcon/).

## <a href="" id="sending-a-urb-to-a-device"></a> Sending an URB to a Device


If your KMDF driver communicates with its USB device by sending I/O requests that contain URBs, the driver can call the following methods:

<a href="" id="wdfusbtargetdevicecreateurb--kmdf-only-"></a>[**WdfUsbTargetDeviceCreateUrb (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)  
Allocates a USB request block (URB). Before calling [**WdfUsbTargetDeviceCreateUrb**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb), a driver must call [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters).

<a href="" id="wdfusbtargetdevicecreateisochurb--kmdf-only-"></a>[**WdfUsbTargetDeviceCreateIsochUrb (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateisochurb)  
Allocates an isochronous USB request block (URB). Before calling [**WdfUsbTargetDeviceCreateIsochUrb**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateisochurb), a driver must call [**WdfUsbTargetDeviceCreateWithParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters).

<a href="" id="---------wdfusbtargetdevicesendurbsynchronously--kmdf-only-"></a>[**WdfUsbTargetDeviceSendUrbSynchronously (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)  
Synchronously sends an I/O request that contains an URB.

<a href="" id="---------wdfusbtargetdeviceformatrequestforurb--kmdf-only-"></a>[**WdfUsbTargetDeviceFormatRequestForUrb (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforurb)  
Formats an I/O request that contains a URB. The driver must call [**WdfRequestSend**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsend) to send the request synchronously or asynchronously.

<a href="" id="---------wdfusbtargetdevicewdmgetconfigurationhandle--kmdf-only-"></a>[**WdfUsbTargetDeviceWdmGetConfigurationHandle (KMDF only)**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfusb/nf-wdfusb-wdfusbtargetdevicewdmgetconfigurationhandle)  
Returns a device's USBD configuration handle. Some URBs require this handle.

For general conceptual background on URBs, see [Allocating and Building URBs](https://docs.microsoft.com/windows-hardware/drivers/usbcon/how-to-add-xrb-support-for-client-drivers).

 

 





