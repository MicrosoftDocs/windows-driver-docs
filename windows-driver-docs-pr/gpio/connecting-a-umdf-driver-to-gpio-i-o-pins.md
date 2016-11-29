---
title: Connecting a UMDF Driver to GPIO I/O Pins
author: windows-driver-content
description: A GPIO I/O resource is a set of one or more GPIO pins that are configured as data inputs or data outputs.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6869D298-5EB4-4991-A67F-F4398CE2D191
---

# Connecting a UMDF Driver to GPIO I/O Pins


A GPIO I/O resource is a set of one or more GPIO pins that are configured as data inputs or data outputs. The driver for a peripheral device that physically connects to these pins acquires the corresponding GPIO I/O resource from the Plug and Play (PnP) manager. The following discussion assumes that this driver is designed to use the [user-mode driver framework](https://msdn.microsoft.com/library/windows/hardware/ff560442) (UMDF). The UMDF driver opens a logical connection to the GPIO pins in this resource and obtains a target object that encapsulates the connection. To write to or read from the GPIO pins in the connection, the driver sends I/O requests to the target object.

The UMDF driver implements an [**IPnpCallbackHardware2**](https://msdn.microsoft.com/library/windows/hardware/hh439727) interface, and registers this interface with the framework during the call to the driver's [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method. The framework calls the methods in the **IPnpCallbackHardware2** interface to notify the driver of changes in the device's power state.

When power is restored to a peripheral device, the framework calls the [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) method to notify the driver that this device must be prepared for use. During this call, the driver receives two lists of hardware resources as input parameters. The *pWdfResourcesRaw* parameter points to the list of raw resources, and the *pWdfResourcesTranslated* parameter points to the list of translated resources. Both parameters are pointers to [**IWDFCmResourceList**](https://msdn.microsoft.com/library/windows/hardware/hh439762) objects.

The translated resources include a *connection ID*, which is a 64-bit identifier that the peripheral driver needs to establish a logical connection to the GPIO resource. When the driver for the peripheral device calls the [**IWDFDevice2::CreateRemoteTarget**](https://msdn.microsoft.com/library/windows/hardware/ff556928) method to open the resource, the driver supplies a string that contains the connection ID.

To enable a UMDF peripheral driver to receive connection IDs in its resource list, the INF file that installs the driver must include the following directive in its WDF-specific **DDInstall** section:

**UmdfDirectHardwareAccess = AllowDirectHardwareAccess**
For more information about this directive, see [Specifying WDF Directives in INF Files](https://msdn.microsoft.com/library/windows/hardware/ff560526). For an example of a INX file (used to build the corresponding INF file) that uses this directive, see the SimDeviceUmdf sample driver in the [GPIO sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=616032) collection on GitHub.

The following code example shows how the driver's **OnPrepareHardware** method can obtain the connection ID for a GPIO I/O resource from the lists of resources that the Plug and Play (PnP) manager has assigned to the driver.

```ManagedCPlusPlus
HRESULT
  XyzDevice::OnPrepareHardware(
    _In_ IWDFDevice3 *pWdfDevice,
    _In_ IWDFCmResourceList *pWdfResourcesRaw,
    _In_ IWDFCmResourceList *pWdfResourcesTranslated
    )
{
    HRESULT hr;
    int ResourceCount, Index;
    PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor;
    XYZ_DEVICE_CONTEXT *DeviceExtension;

    ...

    hr = pWdfDevice->RetrieveContext((void**)&DeviceExtension);
    ResourceCount = pWdfResourcesTranslated->GetCount();
    for (Index = 0; Index < ResourceCount; Index += 1) {
        Descriptor = pWdfResourcesTranslated->GetDescriptor(Index);
        switch (Descriptor->Type) {

        //
        // GPIO I/O descriptors
        //

        case CmResourceTypeConnection:

            //
            // Check against expected connection type.
            //

            if ((Descriptor->u.Connection.Class == CM_RESOURCE_CONNECTION_CLASS_GPIO) &&
                (Descriptor->u.Connection.Type == CM_RESOURCE_CONNECTION_TYPE_GPIO_IO)) {

                DeviceExtension->ConnectionId.LowPart = Descriptor->u.Connection.IdLowPart;
                DeviceExtension->ConnectionId.HighPart = Descriptor->u.Connection.IdHighPart;

        ...

}
```

In the preceding code example, the `DeviceExtension` variable is a pointer to the device context for the peripheral device. The driver stores the connection ID for the GPIO device in the device context.

The following code example shows how the peripheral device driver can use the GPIO resource description that it obtained in the previous code example to open a [**IWDFRemoteTarget**](https://msdn.microsoft.com/library/windows/hardware/ff560247) object that encapsulates the driver's connection to the GPIO I/O resource.

```ManagedCPlusPlus
HRESULT IoRoutine(IWDFDevice3 *pWdfDevice, BOOLEAN ReadOperation) 
{
    XYZ_DEVICE_CONTEXT *DeviceExtension;
    WCHAR ReadStringBuffer[100];
    IWDFRemoteTarget *pWdfTarget;
    BOOL DesiredAccess;
    HRESULT hr;

    hr = pWdfDevice->RetrieveContext((void**)&DeviceExtension);

    // Create the device path using the well-known resource hub
    // path name and the connection ID.
    //
    // TODO: Replace this hardcoded string with the appropriate
    //       helper method from Reshub.h when available.
    hr = StringCbPrintfW(&ReadStringBuffer[0],
                         sizeof(ReadStringBuffer),
                         L"\\\\.\\RESOURCE_HUB\\%0*I64x",
                         (size_t)(sizeof(LARGE_INTEGER) * 2),
                         connectionId.QuadPart);
    if (FAILED(hr)) {
        goto IoErrorEnd;
    }
     
    hr = pWdfDevice->CreateRemoteTarget(NULL,
                                       pWdfDevice,
                                       &pWdfTarget);
    if (FAILED(hr)) {
        goto IoErrorEnd;
    }   

    if (ReadOperation) {
        DesiredAccess = GENERIC_READ;
    } else {
        DesiredAccess = GENERIC_WRITE;
    }    
     
    UMDF_IO_TARGET_OPEN_PARAMS openParams;

    openParams.dwShareMode = 0;
    openParams.dwCreationDisposition = OPEN_EXISTING;
    openParams.dwFlagsAndAttributes = FILE_FLAG_OVERLAPPED;
    hr = pWdfTarget->OpenFileByName(&ReadStringBuffer[0],
                                    DesiredAccess,
                                    &openParams);
    if (FAILED(hr)) {
        goto IoErrorEnd;
    }

    ...

}
```

At the start of the preceding code example, the value of the `ReadOperation` variable indicates whether the connection is to be opened for read (**TRUE**) or write (**FALSE**) operations. The `pWdfDevice` variable is a pointer to the framework device object for the peripheral device. The [**StringCbPrintfW**](https://msdn.microsoft.com/library/windows/desktop/ms647510) routine creates a string that contains the name of the GPIO I/O resource. This string contains the connection ID that the driver obtained in the earlier code example. The [**IWDFRemoteTarget::OpenFileByName**](https://msdn.microsoft.com/library/windows/hardware/ff560273) method uses this string to open a logical connection to the GPIO I/O resource. The **OPEN\_EXISTING** option and **FILE\_FLAG\_OVERLAPPED** flag are described in [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858).

After the peripheral device driver has opened a connection to a GPIO I/O resource, this driver can send I/O control requests that either read data from or write data to the GPIO pins. A driver that opens a GPIO I/O resource for reads sends [**IOCTL\_GPIO\_READ\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406483) I/O control requests to read data from the pins in the resource. A driver that opens a GPIO I/O resource for writes sends [**IOCTL\_GPIO\_WRITE\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406487) I/O control requests to write data to the pins in the resource. The following code example shows how the driver performs a GPIO read or write operation.

```ManagedCPlusPlus
HRESULT hr;
IWDFIoRequest *pWdfIoRequest = NULL;
IWDFMemory *pWdfMemory = NULL;
IWDFRequestCompletionParams *pWdfParams = NULL;

//
// Create unformatted I/O request object.
//

hr = pWdfDevice->CreateRequest(NULL, 
                               NULL, 
                               &pWdfIoRequest);
if (FAILED(hr)) {
    goto RwErrorExit;
}

//
// Allocate memory for the input or output buffer.
//

hr = pWdfDriver->CreatePreallocatedWdfMemory(Data, 
                                             Size, 
                                             NULL,
                                             pWdfIoRequest,
                                             &pWdfMemory);
if (FAILED(hr)) {
    goto RwErrorExit;
}

//
// Format the I/O request.
//

if (ReadOperation) {
    hr = pWdfTarget->FormatRequestForIoctl(pWdfIoRequest,
                                           IOCTL_GPIO_READ_PINS,
                                           NULL,
                                           pWdfMemory, 
                                           NULL, 
                                           NULL,
                                           NULL);
} else {
    hr = pWdfTarget->FormatRequestForIoctl(pWdfIoRequest,
                                           IOCTL_GPIO_WRITE_PINS,
                                           NULL,
                                           NULL, 
                                           NULL, 
                                           pWdfMemory,
                                           NULL);
}                                                            

if (FAILED(hr)) {
    goto RwErrorExit;
}

//
// Send the request to the GPIO controller.
//

ULONG Flags = WDF_REQUEST_SEND_OPTION_SYNCHRONOUS | WDF_REQUEST_SEND_OPTION_TIMEOUT;

hr = pWdfIoRequest->Send(pWdfTarget, Flags, -20000000);

if (FAILED(hr)) {
    goto RwErrorExit;
}

pWdfIoRequest->GetCompletionParams(&pWdfParams);
hr = pWdfParams->GetCompletionStatus();

SAFE_RELEASE(pWdfParams);
SAFE_RELEASE(pWdfMemory);
pWdfIoRequest->DeleteWdfObject();
SAFE_RELEASE(pWdfIoRequest);

...
```

The preceding code example does the following:

-   The `pWdfDevice` variable is a pointer to the [**IWDFDevice**](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface of the framework device object that represents the peripheral device. The [**IWDFDevice::CreateRequest**](https://msdn.microsoft.com/library/windows/hardware/ff557021) method creates an I/O request and encapsulates this request in the [**IWDFIoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff558985) object that is pointed to by the `pWdfIoRequest` variable.
-   The `pWdfDriver` variable is a pointer to the [**IWDFDriver**](https://msdn.microsoft.com/library/windows/hardware/ff558893) interface of the framework driver object that represents the peripheral device driver. The `Data` and `Size` variables specify the address and size of the input or output buffer for the **IOCTL\_GPIO\_*XXX*\_PINS** request. The [**IWDFDriver::CreatePreallocatedWdfMemory**](https://msdn.microsoft.com/library/windows/hardware/ff558902) method creates a framework memory object for this buffer, and designates the **IWDFIoRequest** object pointed to by `pWdfIoRequest` as the memory object's parent object (so that the memory object is automatically deleted when its parent is deleted).
-   The `pWdfTarget` variable is the remote target pointer that was obtained from the **OpenFileByName** call in an earlier code example. The `ReadOperation` variable indicates whether the connection was previously opened for read or write. The [**IWDFRemoteTarget::FormatRequestForIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff548604) method formats the I/O request for an IOCTL.
-   The [**Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method sends the formatted I/O request to the GPIO pins. The `Flags` variable indicates that the I/O request is to be sent synchronously and that a time-out is specified. The *Timeout* parameter value, -20000000, indicates that the synchronous **Send** call times out after two seconds.
-   The [**IWDFIoRequest::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) method deletes both the I/O request object pointed to by `pWdfIoRequest` and the child object pointed to by `pWdfMemory`. The **IWDFIoRequest** interface inherits this method from the [**IWDFObject**](https://msdn.microsoft.com/library/windows/hardware/ff560200) interface.

An alternative implementation of the preceding code example might create **IWDFIoRequest** and **IWDFMemory** objects during initialization, and repeatedly use these same objects instead of creating and deleting new objects each time an I/O request is sent. For more information, see [**IWDFIoRequest2::Reuse**](https://msdn.microsoft.com/library/windows/hardware/ff559048) and [**IWDFMemory::SetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff560162).

## For more information


For more information about **IOCTL\_GPIO\_READ\_PINS** requests, including the mapping of data input pins to the bits in the request output buffer, see [**IOCTL\_GPIO\_READ\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406483). For more information about **IOCTL\_GPIO\_WRITE\_PINS** requests, including the mapping of the bits in the request input buffer to data output pins, see [**IOCTL\_GPIO\_WRITE\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406487).

The following sample drivers show how to write a GPIO peripheral driver that runs in user mode:

-   The SimDeviceUmdf sample driver in the [GPIO sample drivers](http://go.microsoft.com/fwlink/p/?LinkId=617729) collection on GitHub
-   The [SpbAccelerometer](http://go.microsoft.com/fwlink/p/?LinkId=618052) sample driver

 

 


--------------------


