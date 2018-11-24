---
title: Hardware Resources for User-Mode SPB Peripheral Drivers
description: Code examples for a UMDF driver for a peripheral device on an SPB, and obtains the hardware resources.
ms.assetid: 4D240011-1F4E-4C1E-8258-A2CF44BD3F06
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Resources for User-Mode SPB Peripheral Drivers


The code examples in this topic show how the [User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff560442) (UMDF) driver for a peripheral device on a [simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903) (SPB) obtains the hardware resources that it requires to operate the device. Included in these resources is the information that the driver uses to establish a logical connection to the device. Additional resources might include an interrupt, and one or more GPIO input or output pins. (A GPIO pin is a pin on a general-purpose I/O controller device that is configured as an input or an output; for more information, see [GPIO Controller Drivers](https://msdn.microsoft.com/library/windows/hardware/hh439512).) Unlike a device that is memory-mapped, an SPB-connected peripheral device doesn't require a block of system memory addresses to map its registers into.

This driver implements an [**IPnpCallbackHardware2**](https://msdn.microsoft.com/library/windows/hardware/hh439727) interface, and registers this interface with the UMDF during the call to the driver's [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method. The framework calls the methods in the **IPnpCallbackHardware2** interface to notify the driver of changes in the device's power state.

When power is restored to the SPB-connected peripheral device, the driver framework calls the [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) method to notify the driver that this device must be prepared for use. During this call, the driver receives two lists of hardware resources as input parameters. The *pWdfResourcesRaw* parameter points to the list of raw resources, and the *pWdfResourcesTranslated* parameter points to the list of translated resources. Both parameters are pointers to [**IWDFCmResourceList**](https://msdn.microsoft.com/library/windows/hardware/hh439762) objects. The translated resources include the *connection ID* that the SPB peripheral driver needs to establish a logical connection to the SPB-connected peripheral device. For more information, see [Connection IDs for SPB Peripheral Devices](https://msdn.microsoft.com/library/windows/hardware/hh698216).

To enable a UMDF peripheral driver to receive connection IDs in its resource list, the INF file that installs the driver must include the following directive in its WDF-specific **DDInstall** section:

**UmdfDirectHardwareAccess = AllowDirectHardwareAccess**
For more information about this directive, see [Specifying WDF Directives in INF Files](https://msdn.microsoft.com/library/windows/hardware/ff560526).

The following code example shows how the driver's **OnPrepareHardware** method obtains the connection ID from the *pWdfResourcesTranslated* parameter.

```cpp
BOOLEAN fConnectIdFound = FALSE;
BOOLEAN fDuplicateFound = FALSE;
LARGE_INTEGER connectionId = 0;
ULONG resourceCount;

resourceCount = pWdfResourcesTranslated->GetCount();

// Loop through the resources and save the relevant ones.
for (ULONG ix = 0; ix < resourceCount; ix++)
{
    PCM_PARTIAL_RESOURCE_DESCRIPTOR pDescriptor;

    pDescriptor = pWdfResourcesTranslated->GetDescriptor(ix);

    if (pDescriptor == NULL)
    {
        hr = E_POINTER;
        break;
    }

    // Determine the resource type.
    switch (pDescriptor->Type)
    {
    case CmResourceTypeConnection:
        {
            // Check against the expected connection types.
            UCHAR Class = pDescriptor->u.Connection.Class;
            UCHAR Type = pDescriptor->u.Connection.Type;

            if (Class == CM_RESOURCE_CONNECTION_CLASS_SERIAL)
            {
                if (Type == CM_RESOURCE_CONNECTION_TYPE_SERIAL_I2C)
                {
                    if (fConnIdFound == FALSE)
                    {
                        // Save the SPB connection ID.
                        connectionId.LowPart = pDescriptor->u.Connection.IdLowPart;
                        connectionId.HighPart = pDescriptor->u.Connection.IdHighPart;
                        fConnectIdFound = TRUE;
                    }
                    else
                    {
                        fDuplicateFound = TRUE;
                    }
                }
            }

            if (Class == CM_RESOURCE_CONNECTION_CLASS_GPIO)
            {
                // Check for GPIO pin resource.
                ...
            }
        }
        break;

    case CmResourceTypeInterrupt:
        {
            // Check for interrupt resources.
            ...
        }
        break;

    default:
        // Ignore all other resource descriptors.
        break;
    }
}
```

The preceding code example copies the connection ID for an SPB-connected peripheral device into a variable named `connectionId`. The following code example shows how to incorporate the connection ID into a device path name that can be used to identify the peripheral device.

```cpp
WCHAR szTargetPath[100];
HRESULT hres;

// Create the device path using the well-known resource hub
// path name and the connection ID.
//
// TODO: Replace this hardcoded string with the appropriate
//       helper method from Reshub.h when available.
hres = StringCbPrintfW(&szTargetPath[0],
                       sizeof(szTargetPath),
                       L"\\\\.\\RESOURCE_HUB\\%0*I64x",
                       (size_t)(sizeof(LARGE_INTEGER) * 2),
                       connectionId.QuadPart);
if (FAILED(hres))
{
     // Error handling
     ...
}
```

The preceding code example writes the path name for the SPB-connected peripheral device into the `szTargetPath` array. The following code example uses this device path name to open a file handle to the SPB-connected peripheral device.

```cpp
UMDF_IO_TARGET_OPEN_PARAMS openParams;

openParams.dwShareMode = 0;
openParams.dwCreationDisposition = OPEN_EXISTING;
openParams.dwFlagsAndAttributes = FILE_FLAG_OVERLAPPED;
hres = pRemoteTarget->OpenFileByName(&szTargetPath[0],
                                     (GENERIC_READ | GENERIC_WRITE),
                                     &openParams);
if (FAILED(hres))
{
    // Error handling
    ...
}
```

In the preceding code example, the `pRemoteTarget` variable is a pointer to an [**IWDFRemoteTarget**](https://msdn.microsoft.com/library/windows/hardware/ff560247) object. If the call to the [**IWDFRemoteTarget::OpenFileByName**](https://msdn.microsoft.com/library/windows/hardware/ff560273) method succeeds, the driver for the SPB-connected peripheral device can use the **IWDFRemoteTarget** object to send I/O requests to the peripheral device. Before the driver sends a read, write, or IOCTL request to the peripheral device, the driver calls the [**IWDFRemoteTarget::FormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559233), [**IWDFRemoteTarget::FormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559236), or [**IWDFRemoteTarget::FormatRequestForIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff559230) method to format the I/O request. The **IWDFRemoteTarget** interface inherits these three methods from the [**IWDFIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff559170) interface. Next, the driver calls the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method to send the I/O request to the SPB-connected peripheral device.

In the following code example, the SPB peripheral driver calls the **Send** method to send an [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) request to the SPB-connected peripheral device.

```cpp
HRESULT hres;
IWDFMemory *pInputMemory = NULL;
IWDFRemoteTarget *pWdfIoRequest = NULL;

// Create a new I/O request.
if (SUCCEEDED(hres))
{
    hres = pWdfDevice->CreateRequest(NULL, 
                                     pWdfDevice, 
                                     &pWdfIoRequest);
    if (FAILED(hres))
    {
        // Error handling
        ...
    }
}

// Allocate memory for the input buffer.
if (SUCCEEDED(hres))
{
    hres = pWdfDriver->CreatePreallocatedWdfMemory(pInBuffer, 
                                                   inBufferSize, 
                                                   NULL,
                                                   pWdfIoRequest,
                                                   &pInputMemory);
    if (FAILED(hres))
    {
        // Error handling
        ...
    }

    // After this call, the parent holds the only reference.
    pWdfMemory->Release();
}

// Format the I/O request for a write operation.
if (SUCCEEDED(hres))
{
    hres = pRemoteTarget->FormatRequestForWrite(pWdfIoRequest,
                                                NULL,
                                                pInputMemory, 
                                                NULL, 
                                                0);
    if (FAILED(hres))
    {
        // Error handling
        ...
    }
}

// Send the request to the SPB controller.
if (SUCCEEDED(hres))
{
    ULONG Flags = fSynchronous ? WDF_REQUEST_SEND_OPTION_SYNCHRONOUS : 0;

    // Set the I/O completion callback.
    if (!fSynchronous)
    {
        pWdfIoRequest->SetCompletionCallback(pCallback, NULL);
    }

    hres = pWdfIoRequest->Send(pRemoteTarget, Flags, 0);
    if (FAILED(hres))
    {
        // Error handling
        ...
    }
}

if (fSynchronous || FAILED(hres))
{
    pWdfIoRequest->DeleteWdfObject();
    SAFE_RELEASE(pWdfIoRequest);
}
```

The preceding code example does the following:

1.  The `pWdfDevice` variable is a pointer to the [**IWDFDevice**](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface of the framework device object that represents the SPB-connected peripheral device. The [**IWDFDevice::CreateRequest**](https://msdn.microsoft.com/library/windows/hardware/ff557021) method creates an I/O request and encapsulates this request in the [**IWDFIoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff558985) interface instance that is pointed to by the `pWdfIoRequest` variable.
2.  The `pWdfDriver` variable is a pointer to the [**IWDFDriver**](https://msdn.microsoft.com/library/windows/hardware/ff558893) interface of the framework driver object that represents the SPB peripheral driver. The `pInBuffer` and `inBufferSize` variables specify the address and size of the input buffer that contains the data for the write request. The [**IWDFDriver::CreatePreallocatedWdfMemory**](https://msdn.microsoft.com/library/windows/hardware/ff558902) method creates a framework memory object for the input buffer, and designates the **IWDFIoRequest** object pointed to by `pWdfIoRequest` as the memory object's parent object (so that the memory object is automatically released when its parent is released). After the driver calls the **Release** method to release its local reference to the memory object, the parent holds the sole reference to this object.
3.  The `pWdfRemoteTarget` variable is the remote target pointer that was obtained from the **OpenFileByName** call in an earlier code example. The [**IWDFRemoteTarget::FormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559236) method formats the I/O request for a write operation.
4.  The `fSynchronous` variable is **TRUE** if the write request is to be sent synchronously, and is **FALSE** if it is to be sent asynchronously. The `pCallback` variable is a pointer to a previously created [**IRequestCallbackRequestCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556904) interface. If the request is to be sent asynchronously, the call to the [**IWDFIoRequest::SetCompletionCallback**](https://msdn.microsoft.com/library/windows/hardware/ff559153) method registers this interface. Later, the [**IRequestCallbackRequestCompletion::OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905) method is called to notify the driver when the request asynchronously completes.
5.  The **Send** method sends the formatted write request to the SPB-connected peripheral device. The `Flags` variable indicates whether the write request is to be sent synchronously or asynchronously.
6.  If the request is sent synchronously, the [**IWDFIoRequest::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) method deletes both the I/O request object pointed to by `pWdfIoRequest` and the child object pointed to by `pInputMemory`. The **IWDFIoRequest** interface inherits this method from the [**IWDFObject**](https://msdn.microsoft.com/library/windows/hardware/ff560200) interface. If the request is sent asynchronously, the call to the **DeleteWdfObject** method should occur later, in the driver's **OnCompletion** method.

An alternative implementation of the preceding code example might create **IWDFIoRequest** and **IWDFMemory** objects during driver initialization, and repeatedly use these same objects instead of creating and deleting new objects each time an I/O request is sent. For more information, see [**IWDFIoRequest2::Reuse**](https://msdn.microsoft.com/library/windows/hardware/ff559048) and [**IWDFMemory::SetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff560162).

In addition, an alternative implementation might inspect the I/O status code from the I/O request if the **Send** call succeeds. For more information, see [**IWDFIoRequest::GetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff559084).

 

 




