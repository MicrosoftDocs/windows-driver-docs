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
ms.date: 04/20/2017
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

For step-by-step directions on writing a simple KMDF-based USB client driver, see [How to write your first USB client driver (KMDF)](https://msdn.microsoft.com/library/windows/hardware/hh706187).

## <a href="" id="creating-a-framework-usb-device-object"></a> Creating a USB device object


To use the framework's USB I/O target objects (WDFUSBDEVICE, WDFUSBINTERFACE, and WDFUSBPIPE), your client driver must first call [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) to create a USB device object. Typically, a driver calls **WdfUsbTargetDeviceCreateWithParameters** from its [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function.

When the driver calls [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428), the framework creates a WDFUSBDEVICE object and associates it with the FDO that represents the USB device. The method returns a handle to the new framework USB device object that the USB client driver can then use to communicate with the physical device.

After calling [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428), the driver can call [**WdfUsbTargetDeviceGetDeviceDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550090) and [**WdfUsbTargetDeviceRetrieveConfigDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550098) to obtain USB descriptors from the device. Those descriptors contain information about the device's first configuration, its interface settings, and their defined endpoints. (The USB descriptors are defined in the official USB specification.)

## <a href="" id="selecting-a-device-configuration"></a>Configuring a USB Device


The [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) method also creates a framework USB interface object for each USB interface that the device's first configuration contains.

After calling [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428), the client driver must call [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101) to select a configuration. This method creates framework interface objects for each alternate setting of the interface in the selected configuration.

The method also creates pipe objects that represent endpoints defined in each alternate setting of each interface of the selected configuration.

After you have selected a configuration, you can [change alternate settings](working-with-usb-interfaces.md#selecting-an-alternate-setting-for-a-usb-interface) for the configuration's interfaces, if necessary.

You can also call [**WdfUsbTargetDeviceSelectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff550101) to deconfigure a device.

For related information, see:

-   [How to select a configuration for a USB device](https://msdn.microsoft.com/library/windows/hardware/gg615081)
-   [How to select an alternate setting in a USB interface](https://msdn.microsoft.com/library/windows/hardware/hh968309)

## <a href="" id="obtaining-device-information"></a> Obtaining Device Information


After configuring a device, your client driver can call the following methods to obtain information about a USB device:

<a href="" id="wdfusbtargetdevicequeryusbcapability"></a>[**WdfUsbTargetDeviceQueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh439434)  
Determines whether the host controller and USB driver stack support a specific capability. Before calling [**WdfUsbTargetDeviceQueryUsbCapability**](https://msdn.microsoft.com/library/windows/hardware/hh439434), a driver must call [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428).

<a href="" id="wdfusbtargetdevicegetiotarget"></a>[**WdfUsbTargetDeviceGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff550093)  
Returns a handle to the I/O target object that is associated with a USB device. The driver can pass this handle to [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) or [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680).

<a href="" id="wdfusbtargetdeviceretrieveinformation"></a>[**WdfUsbTargetDeviceRetrieveInformation**](https://msdn.microsoft.com/library/windows/hardware/ff550100)  
Retrieves version and capability information that is associated with a USB device.

<a href="" id="wdfusbtargetdeviceisconnectedsynchronous--kmdf-only-"></a>[**WdfUsbTargetDeviceIsConnectedSynchronous (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550095)  
Determines if the device is connected.

<a href="" id="wdfusbtargetdeviceretrievecurrentframenumber--kmdf-only-"></a>[**WdfUsbTargetDeviceRetrieveCurrentFrameNumber (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550099)  
Retrieves the current USB frame number.

## <a href="" id="obtaining-a-device-s-unicode-strings"></a>Getting USB Descriptors


To obtain the Unicode strings that are contained in a USB device's descriptors, the driver can call any of the following methods:

<a href="" id="wdfusbtargetdevicegetdevicedescriptor"></a>[**WdfUsbTargetDeviceGetDeviceDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550090)  
Obtains a device's [USB device descriptor](https://msdn.microsoft.com/library/windows/hardware/ff539283).

<a href="" id="wdfusbtargetdeviceretrieveconfigdescriptor"></a>[**WdfUsbTargetDeviceRetrieveConfigDescriptor**](https://msdn.microsoft.com/library/windows/hardware/ff550098)  
Obtains a device's [USB configuration descriptor](https://msdn.microsoft.com/library/windows/hardware/ff539242), interface descriptors, and endpoint descriptors.

<a href="" id="---------wdfusbtargetdevicequerystring--------"></a>[**WdfUsbTargetDeviceQueryString**](https://msdn.microsoft.com/library/windows/hardware/ff550096)  
Copies a Unicode string to a driver-supplied buffer.

<a href="" id="---------wdfusbtargetdeviceallocandquerystring--------"></a>[**WdfUsbTargetDeviceAllocAndQueryString**](https://msdn.microsoft.com/library/windows/hardware/ff550074)  
Copies a Unicode string to a framework-supplied buffer.

<a href="" id="---------wdfusbtargetdeviceformatrequestforstring--------"></a>[**WdfUsbTargetDeviceFormatRequestForString**](https://msdn.microsoft.com/library/windows/hardware/ff550086)  
Formats a request for a Unicode string. The driver can call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request synchronously or asynchronously.

## <a href="" id="sending-a-control-transfer"></a> Sending a Control Transfer


Your driver can call the following methods to send an I/O request that describes a standard, device class-specific, or vendor-specific USB control transfer.

<a href="" id="---------wdfusbtargetdevicesendcontroltransfersynchronously--------"></a>[**WdfUsbTargetDeviceSendControlTransferSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550104)  
Synchronously sends a USB control transfer request.

<a href="" id="---------wdfusbtargetdeviceformatrequestforcontroltransfer--------"></a>[**WdfUsbTargetDeviceFormatRequestForControlTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff550082)  
Formats a request for a USB control transfer. The driver can call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request synchronously or asynchronously.

For related information, see [How to send a USB control transfer](https://msdn.microsoft.com/library/windows/hardware/ff539261).

## <a href="" id="resetting-and-power-cycling-a-device-s-port"></a> Resetting and Power-Cycling a Device's Port


Your driver can call the following methods to reset or power-cycle the USB port that a device is connected to:

<a href="" id="---------wdfusbtargetdeviceresetportsynchronously"></a>[**WdfUsbTargetDeviceResetPortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550097)  
Synchronously sends a request to reset a device's USB port.

<a href="" id="---------wdfusbtargetdevicecycleportsynchronously--kmdf-only-"></a>[**WdfUsbTargetDeviceCyclePortSynchronously (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550080)  
Synchronously sends a request to power-cycle a device's USB port.

<a href="" id="---------wdfusbtargetdeviceformatrequestforcycleport--kmdf-only-"></a>[**WdfUsbTargetDeviceFormatRequestForCyclePort (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550084)  
Formats a request to power-cycle a device's USB port. The driver must call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request synchronously or asynchronously.

For related information, see [How to recover from USB pipe errors](https://msdn.microsoft.com/library/windows/hardware/hh968307).

## <a href="" id="sending-a-urb-to-a-device"></a> Sending an URB to a Device


If your KMDF driver communicates with its USB device by sending I/O requests that contain URBs, the driver can call the following methods:

<a href="" id="wdfusbtargetdevicecreateurb--kmdf-only-"></a>[**WdfUsbTargetDeviceCreateUrb (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/hh439423)  
Allocates a USB request block (URB). Before calling [**WdfUsbTargetDeviceCreateUrb**](https://msdn.microsoft.com/library/windows/hardware/hh439423), a driver must call [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428).

<a href="" id="wdfusbtargetdevicecreateisochurb--kmdf-only-"></a>[**WdfUsbTargetDeviceCreateIsochUrb (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/hh439420)  
Allocates an isochronous USB request block (URB). Before calling [**WdfUsbTargetDeviceCreateIsochUrb**](https://msdn.microsoft.com/library/windows/hardware/hh439420), a driver must call [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428).

<a href="" id="---------wdfusbtargetdevicesendurbsynchronously--kmdf-only-"></a>[**WdfUsbTargetDeviceSendUrbSynchronously (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550105)  
Synchronously sends an I/O request that contains an URB.

<a href="" id="---------wdfusbtargetdeviceformatrequestforurb--kmdf-only-"></a>[**WdfUsbTargetDeviceFormatRequestForUrb (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff550088)  
Formats an I/O request that contains a URB. The driver must call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request synchronously or asynchronously.

<a href="" id="---------wdfusbtargetdevicewdmgetconfigurationhandle--kmdf-only-"></a>[**WdfUsbTargetDeviceWdmGetConfigurationHandle (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff551127)  
Returns a device's USBD configuration handle. Some URBs require this handle.

For general conceptual background on URBs, see [Allocating and Building URBs](https://msdn.microsoft.com/library/windows/hardware/hh450844).

 

 





