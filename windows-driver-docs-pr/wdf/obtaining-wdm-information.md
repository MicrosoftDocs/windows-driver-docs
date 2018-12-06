---
title: Obtaining WDM Information
description: Obtaining WDM Information
ms.assetid: a43ffa5b-6166-4624-8dee-a54aaa8c7283
keywords:
- WDM information WDK KMDF
- status information WDK KMDF , WDM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining WDM Information


\[Applies to KMDF only\]

The framework provides several object methods that enable your driver to obtain WDM-defined information.

### Obtaining WDM Information About the Driver and its Devices

To obtain WDM information about a driver and its devices, the driver can call the following methods:

<a href="" id="wdffdoinitwdmgetphysicaldevice"></a>[**WdfFdoInitWdmGetPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff547281)  
Retrieves the [**DEVICE_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure that represents a device's physical device object (PDO). A driver can call this method before the driver has created a framework device object for the device.

<a href="" id="wdfdevicewdmgetphysicaldevice"></a>[**WdfDeviceWdmGetPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff546946)  
Retrieves the WDM DEVICE\_OBJECT structure that represents a device's PDO. A driver can call this method after it has created a framework device object for the device.

<a href="" id="wdfdevicewdmgetdeviceobject"></a>[**WdfDeviceWdmGetDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff546942)  
Returns the WDM device object that is associated with a specified framework device object.

<a href="" id="wdfdevicewdmgetattacheddevice"></a>[**WdfDeviceWdmGetAttachedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff546934)  
Returns the next-lower WDM device object in the [device stack](wdm-concepts-for-kmdf-drivers.md#device-stacks).

<a href="" id="wdfwdmdevicegetwdfdevicehandle"></a>[**WdfWdmDeviceGetWdfDeviceHandle**](https://msdn.microsoft.com/library/windows/hardware/ff551175)  
Returns a handle to the framework device object that is associated with a specified WDM device object.

<a href="" id="wdfwdmdrivergetwdfdriverhandle"></a>[**WdfWdmDriverGetWdfDriverHandle**](https://msdn.microsoft.com/library/windows/hardware/ff551176)  
Returns a handle to the framework driver object that is associated with a specified WDM driver object.

### Obtaining WDM Information About I/O Requests

To obtain WDM information about I/O requests, a driver can call the following methods:

<a href="" id="wdfrequestwdmgetirp"></a>[**WdfRequestWdmGetIrp**](https://msdn.microsoft.com/library/windows/hardware/ff550037)  
Returns the WDM [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) structure that is associated with a specified framework request object. (On the other hand, a driver that receives a WDM IRP outside of the framework can create a framework request object for the IRP by calling [**WdfRequestCreateFromIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549953).)

<a href="" id="wdfrequestgetparameters"></a>[**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969)  
Retrieves the parameters that are associated with a specified framework request object. Most of these parameters come from the request's WDM [I/O stack location](https://msdn.microsoft.com/library/windows/hardware/ff551821).)

<a href="" id="wdfrequestretrieveoutputwdmmdl"></a>[**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021)  
Retrieves a memory descriptor list (MDL) that represents an I/O request's output buffer.

<a href="" id="wdfrequestretrieveinputwdmmdl"></a>[**WdfRequestRetrieveInputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550016)  
Retrieves an MDL that represents an I/O request's input buffer.

<a href="" id="wdfrequestformatrequestusingcurrenttype"></a>[**WdfRequestFormatRequestUsingCurrentType**](https://msdn.microsoft.com/library/windows/hardware/ff549955)  
Copies the contents of the calling driver's I/O stack location to the I/O stack location of the driver's local I/O target.

<a href="" id="wdfrequestwdmformatusingstacklocation"></a>[**WdfRequestWdmFormatUsingStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550036)  
Sets the contents of the I/O stack location for the driver's local I/O target.

### Obtaining WDM Information About I/O Targets

To obtain WDM information about I/O targets, a driver can call the following methods:

<a href="" id="wdfiotargetwdmgettargetdeviceobject"></a>[**WdfIoTargetWdmGetTargetDeviceObject**](https://msdn.microsoft.com/library/windows/hardware/ff548682)  
Returns a pointer to the WDM device object that is associated with a local or remote I/O target.

<a href="" id="wdfiotargetwdmgettargetfileobject"></a>[**WdfIoTargetWdmGetTargetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548686)  
Returns a pointer to the WDM [**FILE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff545834) structure that is associated with a remote I/O target.

<a href="" id="wdfiotargetwdmgettargetfilehandle"></a>[**WdfIoTargetWdmGetTargetFileHandle**](https://msdn.microsoft.com/library/windows/hardware/ff548683)  
Returns a handle to the file that is associated with a remote I/O target.

<a href="" id="wdfiotargetwdmgettargetphysicaldevice"></a>[**WdfIoTargetWdmGetTargetPhysicalDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548691)  
Returns a pointer to the WDM physical device object (PDO) that represents a remote I/O target's device.

### Obtaining WDM Information About Interrupts and DPCs

To obtain WDM information about interrupts and deferred procedure calls (DPCs), a driver can call the following methods:

<a href="" id="wdfinterruptwdmgetinterrupt"></a>[**WdfInterruptWdmGetInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff547393)  
Returns a pointer to the WDM [**KINTERRUPT**](https://msdn.microsoft.com/library/windows/hardware/ff554237) structure that is associated with a specified framework interrupt object.

<a href="" id="wdfdpcwdmgetdpc"></a>[**WdfDpcWdmGetDpc**](https://msdn.microsoft.com/library/windows/hardware/ff547167)  
Returns a pointer to the WDM [**KDPC**](https://msdn.microsoft.com/library/windows/hardware/ff551882) structure that is associated with a specified framework DPC object.

### <a href="" id="obtaining-wdm-information-about-usb-i-o-targets"></a> Obtaining WDM Information About USB I/O Targets

To obtain WDM information about USB I/O targets, a driver can call the following method:

<a href="" id="wdfusbtargetpipewdmgetpipehandle"></a>[**WdfUsbTargetPipeWdmGetPipeHandle**](https://msdn.microsoft.com/library/windows/hardware/ff551162)  
Returns the USBD\_PIPE\_HANDLE-typed handle that is associated with a specified framework pipe object.

### Obtaining WDM Information About the Registry

To obtain WDM information about the registry, a driver can call the following method:

<a href="" id="wdfregistrywdmgethandle"></a>[**WdfRegistryWdmGetHandle**](https://msdn.microsoft.com/library/windows/hardware/ff549935)  
Returns a WDM handle to the registry key that a framework registry-key object represents.

### Obtaining WDM Information About File Objects

To obtain WDM information about file objects, a driver can call the following method:

<a href="" id="wdffileobjectwdmgetfileobject"></a>[**WdfFileObjectWdmGetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff547324)  
Returns the WDM [**FILE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff545834) structure that is associated with a specified framework file object.

 

 





