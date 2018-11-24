---
title: Connecting a UMDF Peripheral Driver to a Serial Port
description: The UMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port.
ms.assetid: 75FC5E79-59E9-4C07-9119-A4FE81CC318E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connecting a UMDF Peripheral Driver to a Serial Port


The UMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port. Additional resources might include an interrupt, and one or more GPIO input or output pins.

This driver implements an [**IPnpCallbackHardware2**](https://msdn.microsoft.com/library/windows/hardware/hh439727) interface, and registers this interface with the Windows driver framework during the call to the driver's [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method. The framework calls the methods in the **IPnpCallbackHardware2** interface to notify the driver of changes in the device's power state.

After the serially connected peripheral device enters an uninitialized D0 device power state, the driver framework calls the driver's [**IPnpCallbackHardware2::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) method to tell the driver to prepare this device for use. During this call, the driver receives two lists of hardware resources as input parameters. The *pWdfResourcesRaw* parameter points to the list of raw resources, and the *pWdfResourcesTranslated* parameter points to the list of translated resources. Both parameters are pointers to [**IWDFCmResourceList**](https://msdn.microsoft.com/library/windows/hardware/hh439762) objects. The translated resources include the connection ID that the peripheral driver needs to establish the logical connection to the serially connected peripheral device.

To enable a UMDF peripheral driver to receive connection IDs in its resource list, the INF file that installs the driver must include the following directive in its WDF-specific **DDInstall** section:

**UmdfDirectHardwareAccess = AllowDirectHardwareAccess**
For more information about this directive, see [Specifying WDF Directives in INF Files](https://msdn.microsoft.com/library/windows/hardware/ff560526). For an example of a INX file (used to build the corresponding INF file) that uses this directive, see the [SpbAccelerometer driver sample](http://go.microsoft.com/fwlink/p/?LinkId=618052).

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
                    if (Type == CM_RESOURCE_CONNECTION_TYPE_SERIAL_UART)
                    {
                        if (fConnIdFound == FALSE)
                        {
                            // Save the serial controller&#39;s connection ID.
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

The preceding code example copies the connection ID for the serially connected peripheral device into a variable named `connectionId`. The following code example shows how to incorporate the connection ID into a device path name that can be used to identify the serial controller that the peripheral device is connected to.

```cpp
WCHAR szTargetPath[100];
HRESULT hres;

// Create the device path using the well-known resource hub
// path name and the connection ID.
//
hres = StringCbPrintfW(&szTargetPath[0],
                       sizeof(DevicePath),
                       L"\\\\.\\RESOURCE_HUB\\%0*I64x",
                       (size_t)(sizeof(LARGE_INTEGER) * 2),
                       connectionId.QuadPart);
if (FAILED(hres))
{
     // Error handling
     ...
}
```

The preceding code example writes the device path name for the serial controller into the `szTargetPath` array. The following code example uses this path name to open a file handle to the serial controller.

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

In the preceding code example, the `pRemoteTarget` parameter is a pointer to an [**IWDFRemoteTarget**](https://msdn.microsoft.com/library/windows/hardware/ff560247) object. If the call to the [**IWDFRemoteTarget::OpenFileByName**](https://msdn.microsoft.com/library/windows/hardware/ff560273) method succeeds, the driver for the serially connected peripheral device can use the **IWDFRemoteTarget** object to send I/O requests to the serial controller.

To send a read or write request to the peripheral device, the driver first calls this object's [**IWDFRemoteTarget::FormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559233) or [**IWDFRemoteTarget::FormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559236) method to format the request. (The **IWDFRemoteTarget** interface inherits these two methods from the [**IWDFIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff559170) interface.)

To send an I/O control request to the serial controller, the driver first calls the [**IWDFRemoteTarget::FormatRequestForIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff559230) method to format the request. (The **IWDFRemoteTarget** interface inherits this method from the **IWDFIoTarget** interface.) Next, the driver calls the **IWDFIoRequest::Send** method to send the I/O control request to the serially connected peripheral device.

In the following code example, the peripheral driver sends an I/O control request to the serial controller.

```cpp
HRESULT hres;
IWDFMemory *pInputMemory = NULL;

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
}

// Format the request to be an I/O control request.
if (SUCCEEDED(hres))
{
    hres = pRemoteTarget->FormatRequestForIoctl(pWdfIoRequest,
                                                ioctlCode,
                                                NULL,
                                                pInputMemory, 
                                                NULL, 
                                                NULL,
                                                NULL);
    if (FAILED(hres))
    {
        // Error handling
        ...
    }
}

// Send the request to the serial controller.
if (SUCCEEDED(hres))
{
    ULONG Flags = fSynchronous ? WDF_REQUEST_SEND_OPTION_SYNCHRONOUS : 0;

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

1.  The `pWdfDevice` variable is a pointer to the [**IWDFDevice**](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface of the framework device object that represents the serially connected peripheral device. The [**IWDFDevice::CreateRequest**](https://msdn.microsoft.com/library/windows/hardware/ff557021) method creates an I/O request and encapsulates this request in the [**IWDFIoRequest**](https://msdn.microsoft.com/library/windows/hardware/ff558985) interface instance that is pointed to by the `pWdfIoRequest` parameter. The I/O request is later deleted (see step 6). This implementation is somewhat inefficient because it creates and then deletes a request object for each I/O request that is sent. A more efficient approach is to reuse the same request object for a series of I/O requests. For more information, see [Reusing Framework Request Objects](https://msdn.microsoft.com/library/windows/hardware/ff544600).
2.  The `pWdfDriver` variable is a pointer to the [**IWDFDriver**](https://msdn.microsoft.com/library/windows/hardware/ff558893) interface of the framework driver object that represents the peripheral driver. The `pInBuffer` and `inBufferSize` variables specify the address and size of the input buffer for the I/O control request. The [**IWDFDriver::CreatePreallocatedWdfMemory**](https://msdn.microsoft.com/library/windows/hardware/ff558902) method creates a framework memory object for the input buffer, and designates the **IWDFIoRequest** object pointed to by `pWdfIoRequest` as the memory object's parent object.
3.  The `pWdfRemoteTarget` variable is the remote target pointer that was obtained from the **OpenFileByName** call in an earlier code example. The [**IWDFRemoteTarget::FormatRequestForIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff559230) method formats the request for an I/O control operation. The `ioctlCode` variable is set to one of the I/O control codes listed in the table in [Serial I/O Request Interface](serial-i-o-request-interface.md).
4.  The `fSynchronous` variable is **TRUE** if the I/O control request is to be sent synchronously, and is **FALSE** if it is to be sent asynchronously. The `pCallback` variable is a pointer to a previously created [**IRequestCallbackRequestCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556904) interface. If the request is to be sent asynchronously, the call to the [**IWDFIoRequest::SetCompletionCallback**](https://msdn.microsoft.com/library/windows/hardware/ff559153) method registers this interface. Later, the [**IRequestCallbackRequestCompletion::OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905) method is called to notify the driver when the request asynchronously completes.
5.  The **Send** method sends the formatted write request to the serially connected peripheral device. The `Flags` variable indicates whether the write request is to be sent synchronously or asynchronously.
6.  If the request is sent synchronously, the [**IWDFIoRequest::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) method deletes both the I/O request object pointed to by `pWdfIoRequest` and the child object pointed to by `pInputMemory`. The **IWDFIoRequest** interface inherits this method from the [**IWDFObject**](https://msdn.microsoft.com/library/windows/hardware/ff560200) interface. If the request is sent asynchronously, the call to the **DeleteWdfObject** method should occur later, in the driver's **OnCompletion** method.

 

 




