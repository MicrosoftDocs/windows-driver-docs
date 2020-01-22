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

<a href="" id="wdffdoinitwdmgetphysicaldevice"></a>[**WdfFdoInitWdmGetPhysicalDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitwdmgetphysicaldevice)  
Retrieves the [**DEVICE_OBJECT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structure that represents a device's physical device object (PDO). A driver can call this method before the driver has created a framework device object for the device.

<a href="" id="wdfdevicewdmgetphysicaldevice"></a>[**WdfDeviceWdmGetPhysicalDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmgetphysicaldevice)  
Retrieves the WDM DEVICE\_OBJECT structure that represents a device's PDO. A driver can call this method after it has created a framework device object for the device.

<a href="" id="wdfdevicewdmgetdeviceobject"></a>[**WdfDeviceWdmGetDeviceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmgetdeviceobject)  
Returns the WDM device object that is associated with a specified framework device object.

<a href="" id="wdfdevicewdmgetattacheddevice"></a>[**WdfDeviceWdmGetAttachedDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmgetattacheddevice)  
Returns the next-lower WDM device object in the [device stack](wdm-concepts-for-kmdf-drivers.md#device-stacks).

<a href="" id="wdfwdmdevicegetwdfdevicehandle"></a>[**WdfWdmDeviceGetWdfDeviceHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfwdmdevicegetwdfdevicehandle)  
Returns a handle to the framework device object that is associated with a specified WDM device object.

<a href="" id="wdfwdmdrivergetwdfdriverhandle"></a>[**WdfWdmDriverGetWdfDriverHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfwdmdrivergetwdfdriverhandle)  
Returns a handle to the framework driver object that is associated with a specified WDM driver object.

### Obtaining WDM Information About I/O Requests

To obtain WDM information about I/O requests, a driver can call the following methods:

<a href="" id="wdfrequestwdmgetirp"></a>[**WdfRequestWdmGetIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestwdmgetirp)  
Returns the WDM [**IRP**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) structure that is associated with a specified framework request object. (On the other hand, a driver that receives a WDM IRP outside of the framework can create a framework request object for the IRP by calling [**WdfRequestCreateFromIrp**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreatefromirp).)

<a href="" id="wdfrequestgetparameters"></a>[**WdfRequestGetParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetparameters)  
Retrieves the parameters that are associated with a specified framework request object. Most of these parameters come from the request's WDM [I/O stack location](https://docs.microsoft.com/windows-hardware/drivers/kernel/i-o-stack-locations).)

<a href="" id="wdfrequestretrieveoutputwdmmdl"></a>[**WdfRequestRetrieveOutputWdmMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveoutputwdmmdl)  
Retrieves a memory descriptor list (MDL) that represents an I/O request's output buffer.

<a href="" id="wdfrequestretrieveinputwdmmdl"></a>[**WdfRequestRetrieveInputWdmMdl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestretrieveinputwdmmdl)  
Retrieves an MDL that represents an I/O request's input buffer.

<a href="" id="wdfrequestformatrequestusingcurrenttype"></a>[**WdfRequestFormatRequestUsingCurrentType**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestformatrequestusingcurrenttype)  
Copies the contents of the calling driver's I/O stack location to the I/O stack location of the driver's local I/O target.

<a href="" id="wdfrequestwdmformatusingstacklocation"></a>[**WdfRequestWdmFormatUsingStackLocation**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestwdmformatusingstacklocation)  
Sets the contents of the I/O stack location for the driver's local I/O target.

### Obtaining WDM Information About I/O Targets

To obtain WDM information about I/O targets, a driver can call the following methods:

<a href="" id="wdfiotargetwdmgettargetdeviceobject"></a>[**WdfIoTargetWdmGetTargetDeviceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetdeviceobject)  
Returns a pointer to the WDM device object that is associated with a local or remote I/O target.

<a href="" id="wdfiotargetwdmgettargetfileobject"></a>[**WdfIoTargetWdmGetTargetFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetfileobject)  
Returns a pointer to the WDM [**FILE\_OBJECT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object) structure that is associated with a remote I/O target.

<a href="" id="wdfiotargetwdmgettargetfilehandle"></a>[**WdfIoTargetWdmGetTargetFileHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle)  
Returns a handle to the file that is associated with a remote I/O target.

<a href="" id="wdfiotargetwdmgettargetphysicaldevice"></a>[**WdfIoTargetWdmGetTargetPhysicalDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetwdmgettargetphysicaldevice)  
Returns a pointer to the WDM physical device object (PDO) that represents a remote I/O target's device.

### Obtaining WDM Information About Interrupts and DPCs

To obtain WDM information about interrupts and deferred procedure calls (DPCs), a driver can call the following methods:

<a href="" id="wdfinterruptwdmgetinterrupt"></a>[**WdfInterruptWdmGetInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptwdmgetinterrupt)  
Returns a pointer to the WDM [**KINTERRUPT**](https://docs.microsoft.com/windows-hardware/drivers/kernel/eprocess) structure that is associated with a specified framework interrupt object.

<a href="" id="wdfdpcwdmgetdpc"></a>[**WdfDpcWdmGetDpc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdpc/nf-wdfdpc-wdfdpcwdmgetdpc)  
Returns a pointer to the WDM [**KDPC**](https://docs.microsoft.com/windows-hardware/drivers/kernel/eprocess) structure that is associated with a specified framework DPC object.

### <a href="" id="obtaining-wdm-information-about-usb-i-o-targets"></a> Obtaining WDM Information About USB I/O Targets

To obtain WDM information about USB I/O targets, a driver can call the following method:

<a href="" id="wdfusbtargetpipewdmgetpipehandle"></a>[**WdfUsbTargetPipeWdmGetPipeHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewdmgetpipehandle)  
Returns the USBD\_PIPE\_HANDLE-typed handle that is associated with a specified framework pipe object.

### Obtaining WDM Information About the Registry

To obtain WDM information about the registry, a driver can call the following method:

<a href="" id="wdfregistrywdmgethandle"></a>[**WdfRegistryWdmGetHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfregistry/nf-wdfregistry-wdfregistrywdmgethandle)  
Returns a WDM handle to the registry key that a framework registry-key object represents.

### Obtaining WDM Information About File Objects

To obtain WDM information about file objects, a driver can call the following method:

<a href="" id="wdffileobjectwdmgetfileobject"></a>[**WdfFileObjectWdmGetFileObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdffileobject/nf-wdffileobject-wdffileobjectwdmgetfileobject)  
Returns the WDM [**FILE\_OBJECT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object) structure that is associated with a specified framework file object.

 

 





