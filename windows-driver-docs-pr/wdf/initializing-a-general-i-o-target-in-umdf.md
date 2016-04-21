---
title: Initializing a General I/O Target in UMDF
author: windows-driver-content
description: Initializing a General I/O Target in UMDF
ms.assetid: cf1b39c3-4c82-411b-8eef-117ac0fe793e
keywords: ["general I/O targets WDK UMDF , initializing", "initializing general I/O targets WDK UMDF"]
---

# Initializing a General I/O Target in UMDF


\[This topic applies to UMDF 1.*x*.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Initializing%20a%20General%20I/O%20Target%20in%20UMDF%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




