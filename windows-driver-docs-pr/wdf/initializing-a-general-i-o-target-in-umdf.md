---
title: Initializing a General I/O Target in UMDF
description: Initializing a General I/O Target in UMDF
keywords:
- general I/O targets WDK UMDF , initializing
- initializing general I/O targets WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a General I/O Target in UMDF


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The steps that your driver uses to initialize a general I/O target depend on whether the I/O target is [local](general-i-o-targets-in-umdf.md) or remote.

### Initializing a local I/O target

Local I/O targets include a device's [default I/O target](general-i-o-targets-in-umdf.md) and file-handle-based I/O targets.

The framework initializes a driver's default I/O target for a device when the driver calls the [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice) method. To retrieve the [IWDFIoTarget](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiotarget) interface that enables the driver to access the device's default I/O target, the driver calls the [**IWDFDevice::GetDefaultIoTarget**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-getdefaultiotarget) method.

Most drivers send requests only to their default I/O target.

If a UMDF driver must send I/O requests to a handle-based interface, such as a network socket interface, the driver must create a file-handle-based I/O target object. To create a file-handle-based I/O target object, the driver must do the following:

1.  Call the **QueryInterface** method of the device's [IWDFDevice](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdevice) interface to retrieve a pointer to the [IWDFFileHandleTargetFactory](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffilehandletargetfactory) interface.

2.  Obtain a Win32 handle to a file, named pipe, or socket by calling the Win32 [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea), **CreateNamedPipe**, or **socket** function.

3.  Call the [**IWDFFileHandleTargetFactory::CreateFileHandleTarget**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdffilehandletargetfactory-createfilehandletarget) method to create a file-handle-based I/O target object for the file, pipe, or socket.

For a code example that shows how to retrieve the [IWDFFileHandleTargetFactory](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffilehandletargetfactory) interface, obtain a Win32 handle, and create a file-handle-based I/O target object, see the code example at [**IWDFFileHandleTargetFactory::CreateFileHandleTarget**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdffilehandletargetfactory-createfilehandletarget).

After the driver creates the file-handle-based I/O target, the driver can send I/O requests to the I/O target.

### Initializing a Remote I/O Target

Before your driver can use a remote I/O target, it must create a remote target object and open the target, as follows:

1.  Call [**IWDFDevice2::CreateRemoteTarget**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-createremotetarget) to create a remote target object.

2.  Call either [**IWDFRemoteTarget::OpenFileByName**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfremotetarget-openfilebyname) (for files) or [**IWDFRemoteTarget::OpenRemoteInterface**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfremotetarget-openremoteinterface) (for [device interfaces](using-device-interfaces-in-umdf-drivers.md)) to open the target for I/O operations.

 

