---
title: Initializing a General I/O Target in UMDF
description: Initializing a General I/O Target in UMDF
ms.assetid: cf1b39c3-4c82-411b-8eef-117ac0fe793e
keywords:
- general I/O targets WDK UMDF , initializing
- initializing general I/O targets WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a General I/O Target in UMDF


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The steps that your driver uses to initialize a general I/O target depend on whether the I/O target is [local](general-i-o-targets-in-umdf.md) or remote.

### Initializing a local I/O target

Local I/O targets include a device's [default I/O target](general-i-o-targets-in-umdf.md) and file-handle-based I/O targets.

The framework initializes a driver's default I/O target for a device when the driver calls the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method. To retrieve the [IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170) interface that enables the driver to access the device's default I/O target, the driver calls the [**IWDFDevice::GetDefaultIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff558831) method.

Most drivers send requests only to their default I/O target.

If a UMDF driver must send I/O requests to a handle-based interface, such as a network socket interface, the driver must create a file-handle-based I/O target object. To create a file-handle-based I/O target object, the driver must do the following:

1.  Call the **QueryInterface** method of the device's [IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface to retrieve a pointer to the [IWDFFileHandleTargetFactory](https://msdn.microsoft.com/library/windows/hardware/ff558926) interface.

2.  Obtain a Win32 handle to a file, named pipe, or socket by calling the Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), **CreateNamedPipe**, or **socket** function.

3.  Call the [**IWDFFileHandleTargetFactory::CreateFileHandleTarget**](https://msdn.microsoft.com/library/windows/hardware/ff558930) method to create a file-handle-based I/O target object for the file, pipe, or socket.

For a code example that shows how to retrieve the [IWDFFileHandleTargetFactory](https://msdn.microsoft.com/library/windows/hardware/ff558926) interface, obtain a Win32 handle, and create a file-handle-based I/O target object, see the code example at [**IWDFFileHandleTargetFactory::CreateFileHandleTarget**](https://msdn.microsoft.com/library/windows/hardware/ff558930).

After the driver creates the file-handle-based I/O target, the driver can send I/O requests to the I/O target.

### Initializing a Remote I/O Target

Before your driver can use a remote I/O target, it must create a remote target object and open the target, as follows:

1.  Call [**IWDFDevice2::CreateRemoteTarget**](https://msdn.microsoft.com/library/windows/hardware/ff556928) to create a remote target object.

2.  Call either [**IWDFRemoteTarget::OpenFileByName**](https://msdn.microsoft.com/library/windows/hardware/ff560273) (for files) or [**IWDFRemoteTarget::OpenRemoteInterface**](https://msdn.microsoft.com/library/windows/hardware/ff560276) (for [device interfaces](using-device-interfaces-in-umdf-drivers.md)) to open the target for I/O operations.

 

 





