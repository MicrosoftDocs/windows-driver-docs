---
title: Connecting a KMDF Peripheral Driver to a Serial Port
description: The KMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port.
ms.assetid: EDE62C5E-3563-42EE-884E-DF473CD724A5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connecting a KMDF Peripheral Driver to a Serial Port


The KMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port. Additional resources might include an interrupt, and one or more GPIO input or output pins.

This driver implements a set of Plug and Play and power management event callback functions. To register these functions with KMDF, the driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) event callback function calls the [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135) method. The framework calls the power management event callback functions to notify the driver of changes in the power state of the peripheral device. Included in these functions is the [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) function, which performs any operations that are needed to make the device accessible to the driver.

After the serially connected peripheral device enters an uninitialized D0 device power state, the driver framework calls the *EvtDevicePrepareHardware* function to tell the peripheral driver to prepare the device for use. During this call, the driver receives two lists of hardware resources as input parameters. The *ResourcesRaw* parameter is a WDFCMRESLIST object handle to the list of [*raw resources*](https://msdn.microsoft.com/library/windows/hardware/ff544561), and the *ResourcesTranslated* parameter is a WDFCMRESLIST object handle to the list of [*translated resources*](https://msdn.microsoft.com/library/windows/hardware/ff544561). The translated resources include the *connection ID* that the driver requires to establish a logical connection to the peripheral device.

The following code example shows how the *EvtDevicePrepareHardware* function obtains the connection ID from the *ResourcesTranslated* parameter.

```cpp
BOOLEAN fConnectionIdFound = FALSE;
LARGE_INTEGER connectionId = 0;
ULONG resourceCount;
NTSTATUS status = STATUS_SUCCESS;

resourceCount = WdfCmResourceListGetCount(ResourcesTranslated);

// Loop through the resources and save the relevant ones.

for (ULONG ix = 0; ix < resourceCount; ix++)
{
    PCM_PARTIAL_RESOURCE_DESCRIPTOR pDescriptor;

    pDescriptor = WdfCmResourceListGetDescriptor(ResourcesTranslated, ix);

    if (pDescriptor == NULL)
    {
        status = E_POINTER;
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
                    if (fConnectionIdFound == FALSE)
                    {
                        // Save the connection ID.

                        connectionId.LowPart = pDescriptor->u.Connection.IdLowPart;
                        connectionId.HighPart = pDescriptor->u.Connection.IdHighPart;
                        fConnectionIdFound = TRUE;
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
            // Check for interrupt resource.
            ...
        }
        break;

    default:
        // Don&#39;t care about other resource descriptors.
        break;
    }
}
```

The preceding code example copies the connection ID for a serially connected peripheral device into a variable named `connectionId`.

The following code example shows how to incorporate this connection ID into a device path name that can be used to open a logical connection to the peripheral device. This device path name identifies the resource hub as the system component from which to obtain the parameters required to access the peripheral device.

```cpp
// Use the connection ID to create the full device path name.
 
DECLARE_UNICODE_STRING_SIZE(szDeviceName, RESOURCE_HUB_PATH_SIZE);

status = RESOURCE_HUB_CREATE_PATH_FROM_ID(&szDeviceName,
                                          connectionId.LowPart,
                                          connectionId.HighPart);

if (!NT_SUCCESS(status))
{
     // Error handling
     ...
}
```

In the preceding code example, the **DECLARE\_UNICODE\_STRING\_SIZE** macro creates the declaration of an initialized [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) variable named `szDeviceName` that has a buffer large enough to contain a device path name in the format used by the resource hub. This macro is defined in the Ntdef.h header file. The **RESOURCE\_HUB\_PATH\_SIZE** constant specifies the number of bytes in the device path name. The **RESOURCE\_HUB\_CREATE\_PATH\_FROM\_ID** macro generates the device path name from the connection ID. **RESOURCE\_HUB\_PATH\_SIZE** and **RESOURCE\_HUB\_CREATE\_PATH\_FROM\_ID** are defined in the Reshub.h header file.

The following code example uses the device path name to open a file handle (named `SerialIoTarget`) to the serially connected peripheral device.

```cpp
// Open the peripheral device on the serial port as a remote I/O target.
 
WDF_IO_TARGET_OPEN_PARAMS openParams;
WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME(&openParams,
                                            &szDeviceName,
                                            (GENERIC_READ | GENERIC_WRITE));

openParams.ShareAccess = 0;
openParams.CreateDisposition = FILE_OPEN;
openParams.FileAttributes = FILE_ATTRIBUTE_NORMAL;

status = WdfIoTargetOpen(SerialIoTarget, &openParams);

if (!NT_SUCCESS(status))
{
    // Error handling
    ...
}
```

In the preceding code example, the [**WDF\_IO\_TARGET\_OPEN\_PARAMS\_INIT\_OPEN\_BY\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff552381) function initializes the [**WDF\_IO\_TARGET\_OPEN\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552377) structure so the driver can open a logical connection to the serially connected peripheral device by specifying the name of the device. The `SerialIoTarget` variable is a WDFIOTARGET handle to a framework I/O target object. This handle was obtained from a previous call to the [**WdfIoTargetCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548591) method, which is not shown in the example. If the call to the [**WdfIoTargetOpen**](https://msdn.microsoft.com/library/windows/hardware/ff548634) method succeeds, the driver can use the `SerialIoTarget` handle to send I/O requests to the peripheral device.

In the *EvtDriverDeviceAdd* event callback function, the peripheral driver can call the [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951) method to allocate a framework request object for use by the driver. Later, when the object is no longer needed, the driver calls the [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) method to delete the object. The driver can reuse the framework request object obtained from the **WdfRequestCreate** call multiple times to send I/O requests to the peripheral device. To synchronously send a read, write, or IOCTL request, the driver calls the [**WdfIoTargetSendReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548669), [**WdfIoTargetSendWriteSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548672), or [**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660) method.

In the following code example, the driver calls **WdfIoTargetSendWriteSynchronously** to synchronously send an [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) request to the peripheral device. At the start of this example, the `pBuffer` variable points to a nonpaged buffer that contains the data that is to be written to the peripheral device, and the `dataSize` variable specifies the size, in bytes, of this data.

```cpp
ULONG_PTR bytesWritten;
NTSTATUS status;

// Describe the input buffer.

WDF_MEMORY_DESCRIPTOR memoryDescriptor;
WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(&memoryDescriptor, pBuffer, dataSize);

// Configure the write request to time out after 2 seconds.

WDF_REQUEST_SEND_OPTIONS requestOptions;
WDF_REQUEST_SEND_OPTIONS_INIT(&requestOptions, WDF_REQUEST_SEND_OPTION_TIMEOUT);
requestOptions.Timeout = WDF_REL_TIMEOUT_IN_SEC(2);

// Send the write request synchronously.

status = WdfIoTargetSendWriteSynchronously(SerialIoTarget,
                                           SerialRequest,
                                           &memoryDescriptor,
                                           NULL,
                                           &requestOptions,
                                           &bytesWritten);
if (!NT_SUCCESS(status))
{
    // Error handling
    ...
}
```

The preceding code example does the following:

1.  The [**WDF\_MEMORY\_DESCRIPTOR\_INIT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552393) function call initializes the `memoryDescriptor` variable, which is a [**WDF\_MEMORY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff552392) structure that describes the input buffer. Previously, the driver called a routine such as [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) to allocate the buffer from nonpaged pool, and copied the write data to this buffer.
2.  The [**WDF\_REQUEST\_SEND\_OPTIONS\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552497) function call initializes the `requestOptions` variable, which is a [**WDF\_REQUEST\_SEND\_OPTIONS**](https://msdn.microsoft.com/library/windows/hardware/ff552491) structure that contains the optional settings for the write request. In this example, the structure configures the request to time out if it doesn't complete after two seconds.
3.  The call to the **WdfIoTargetSendWriteSynchronously** method sends the write request to the peripheral device. The method returns synchronously, after the write operation completes or times out. If necessary, another driver thread can call [**WdfRequestCancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549941) to cancel the request.

In the **WdfIoTargetSendWriteSynchronously** call, the driver supplies a variable named `SerialRequest`, which is a handle to a framework request object that the driver previously created. After the **WdfIoTargetSendWriteSynchronously** call, the driver should typically call the [**WdfRequestReuse**](https://msdn.microsoft.com/library/windows/hardware/ff550026) method to prepare the framework request object to be used again.

 

 




