---
title: Full-Duplex I/O Requests
description: Some buses, such as SPI, support full-duplex bus transfers.
ms.assetid: C80FE3F2-6659-4DE8-8F77-F77EDA60400F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Full-Duplex I/O Requests


Some buses, such as SPI, support full-duplex bus transfers. These transfers improve I/O performance by simultaneously writing data to a device and reading data from the same device. To support full-duplex bus transfers, the [simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903) (SPB) [I/O request interface](https://msdn.microsoft.com/library/windows/hardware/hh698224) defines the [**IOCTL\_SPB\_FULL\_DUPLEX**](https://msdn.microsoft.com/library/windows/hardware/hh974774) I/O control code (IOCTL).

Support for the **IOCTL\_SPB\_FULL\_DUPLEX** IOCTL is optional. Only [SPB controller drivers](https://msdn.microsoft.com/library/windows/hardware/hh698220) for bus controllers that implement full-duplex transfers in hardware support this IOCTL. If an SPB controller driver does not support full-duplex transfers, this driver fails all **IOCTL\_SPB\_FULL\_DUPLEX** requests that it receives and completes them with the error status code STATUS\_NOT\_SUPPORTED.

## Transfer List


The format for an **IOCTL\_SPB\_FULL\_DUPLEX** request is similar to that of an [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) request. Both requests use an [**SPB\_TRANSFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/hh406221) structure to describe the list of read and write transfers for the request. The transfer list in an **IOCTL\_SPB\_EXECUTE\_SEQUENCE** request can have an arbitrary combination of read buffers and write buffers. In contrast, the transfer list in an **IOCTL\_SPB\_FULL\_DUPLEX** request must always have exactly one read buffer and one write buffer. The write buffer is always the first buffer in the transfer list, and the read buffer is second.

An additional requirement for an **IOCTL\_SPB\_FULL\_DUPLEX** request is that the **DelayInUs** members must always be zero in the [**SPB\_TRANSFER\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh406223) structures that describe the read buffer and the write buffer.

The following code example shows how the driver for an SPB peripheral device builds a transfer list for an **IOCTL\_SPB\_FULL\_DUPLEX** request.

```cpp
const ULONG transfers = 2;

SPB_TRANSFER_LIST_AND_ENTRIES(transfers) seq;
SPB_TRANSFER_LIST_INIT(&(seq.List), transfers);

{
    ULONG index = 0;
    seq.List.Transfers[index] = SPB_TRANSFER_LIST_ENTRY_INIT_SIMPLE(
        SpbTransferDirectionToDevice,
        0,
        pWriteBuffer,
        writeBufferLength);

    seq.List.Transfers[index + 1] = SPB_TRANSFER_LIST_ENTRY_INIT_SIMPLE(
        SpbTransferDirectionFromDevice,
        0,
        pReadBuffer,
        readBufferLength);
}
```

The preceding code example uses the [**SPB\_TRANSFER\_LIST\_INIT**](https://msdn.microsoft.com/library/windows/hardware/hh406224) and [**SPB\_TRANSFER\_LIST\_ENTRY\_INIT\_SIMPLE**](https://msdn.microsoft.com/library/windows/hardware/hh406214) functions to initialize the transfer list header and entries. The **SPB\_TRANSFER\_LIST\_AND\_ENTRIES** macro, which is defined in the Spb.h header file, simplifies the declaration of the transfer list. This macro defines the `seq` variable to be a structure that contains an **SPB\_TRANSFER\_LIST** structure and an **SPB\_TRANSFER\_LIST\_ENTRY** array of two elements.

## Full-Duplex Bus Transfers


In response to an **IOCTL\_SPB\_FULL\_DUPLEX** request from an SPB peripheral device driver, the SPB controller driver initiates a full-duplex transfer on the bus. The first byte of the write buffer is written to the device on the same tick of the bus clock on which the first byte of the read buffer is read from the device.

The read buffer and write buffer for an **IOCTL\_SPB\_FULL\_DUPLEX** request are not required to be the same length. If the write buffer is smaller than the read buffer, the SPB controller driver stops writing the contents of the write buffer to the device after the buffer is emptied, but continues to fill the read buffer until it is full. Similarly, if the read buffer is smaller than the write buffer, the SPB controller driver stops filling the read buffer after it is full, but continues to write the contents of the write buffer to the device until the buffer is emptied.

## Example: KMDF Driver


The Kernel-Mode Driver Foundation (KMDF) driver for an SPB peripheral device calls a method such as [**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660) to send an IOCTL request to an SPB controller. This method has *InputBuffer* and *OutputBuffer* parameters. Drivers for some types of devices might use these two parameters to point to the write buffer and the read buffer, respectively, for an IOCTL request. However, to send an IOCTL request to an SPB controller, the SPB peripheral device driver sets the *InputBuffer* parameter to point to a memory descriptor that points to an **SPB\_TRANSFER\_LIST** structure. For example, this structure describes both the write buffer and the read buffer (in that order) for an **IOCTL\_SPB\_FULL\_DUPLEX** request. The driver sets the *OutputBuffer* parameter to NULL.

The following code example shows a **WdfIoTargetSendIoctlSynchronously** call that sends an **IOCTL\_SPB\_FULL\_DUPLEX** request to an SPB peripheral device. The `seq` variable in this example is a transfer list that was defined in the code example in [Transfer List](#transfer-list).

```cpp
ULONG_PTR BytesTransferred = 0;
NTSTATUS Status;
  
WDF_MEMORY_DESCRIPTOR MemoryDescriptor;
WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(
                            &MemoryDescriptor,  
                            &seq,  
                            sizeof(seq));

Status = WdfIoTargetSendIoctlSynchronously(
                            SpbIoTarget,
                            NULL,
                            IOCTL_SPB_FULL_DUPLEX,
                            &MemoryDescriptor,  // InputBuffer
                            NULL,               // OutputBuffer
                            NULL,
                            &BytesTransferred);
```

In the preceding code example, the `MemoryDescriptor` variable is a framework memory descriptor. The [**WDF\_MEMORY\_DESCRIPTOR\_INIT\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff552393) macro initializes this descriptor to serve as a container for the structure contained in the `seq` variable. In the call to the **WdfIoTargetSendIoctlSynchronously** method, the `SpbIoTarget` variable is a previously opened handle to the target peripheral device on the bus. The *InputBuffer* parameter to this method is a pointer to the memory descriptor. The *OutputBuffer* parameter is NULL.

The **WdfIoTargetSendIoctlSynchronously** call in this code example sets the `BytesTransferred` variable to the total number of bytes transferred (bytes written plus bytes read). For example, if the request has a 1-byte write buffer and a 4-byte read buffer, and the call is successful, the `BytesTransferred` value should be 5.

## Example: UMDF Driver


The User-Mode Driver Foundation (UMDF) driver for an SPB peripheral device calls a method such as [**IWDFIoTarget::FormatRequestForIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff559230) to format an I/O request for an I/O control operation. This method has *pInputMemory* and *pOutputMemory* parameters. Drivers for some types of devices might use these two parameters to point to the read buffer and the write buffer for an IOCTL request. However, to send an IOCTL request to an SPB controller, the SPB peripheral device driver sets the *pInputMemory* parameter to point to a memory object that contains an **SPB\_TRANSFER\_LIST** structure. For example, this structure describes both the write buffer and the read buffer for a **IOCTL\_SPB\_FULL\_DUPLEX** request. The driver sets the *pOutputMemory* parameter to NULL.

The following code example shows an **IWDFIoTarget::FormatRequestForIoctl** call that formats an **IOCTL\_SPB\_FULL\_DUPLEX** request to an SPB peripheral device. The `seq` variable in this example is a transfer list that was defined in the code example in [Transfer List](#transfer-list).

```cpp
ULONG_PTR BytesTransferred = 0;
HRESULT hr;

pWdfMemory->SetBuffer(seq, sizeof(seq));

hr = pWdfRemoteTarget->FormatRequestForIoctl( 
                         pWdfIoRequest,
                         IOCTL_SPB_FULL_DUPLEX,
                         NULL,
                         pWdfMemory,  // pInputMemory
                         NULL,        // pOutputMemory 
                         NULL,
                         NULL);

if (FAILED(hr))
{
    goto exit;
}

hr = pWdfIoRequest->Send(pRemoteTarget,
                         WDF_REQUEST_SEND_OPTION_SYNCHRONOUS,
                         0);

if (FAILED(hr))
{
    goto exit;
}

{
    IWDFRequestCompletionParams* pWdfParams = 0;

    pWdfIoRequest->GetCompletionParams(&pWdfParams);
    hr = pWdfParams->GetCompletionStatus();
    if (SUCCEEDED(hr))
    {
        BytesTransferred = pWdfParams->GetInformation();
    }
    SAFE_RELEASE(pWdfParams);
}
```

The preceding code example uses the following object pointers:

-   The `pWdfMemory` variable is a pointer to a previously allocated framework memory ([**IWDFMemory**](https://msdn.microsoft.com/library/windows/hardware/ff559249)) object. The peripheral device driver uses this object as a container for the transfer list in the `seq` variable.
-   The `pWdfRemoteTarget` parameter is a pointer to a previously opened remote I/O target ([**IWDFRemoteTarget**](https://msdn.microsoft.com/library/windows/hardware/ff560247)) object. This object represents the peripheral device driver's connection to the peripheral device.
-   The `pWdfIoRequest` variable is a pointer to a previously created framework request ([**IWDFIoRequest2**](https://msdn.microsoft.com/library/windows/hardware/ff558988)) object. The peripheral device driver uses this object as a container for the **IOCTL\_SPB\_FULL\_DUPLEX** request.

The preceding code example does the following:

1.  The call to the [**IWDFMemory::SetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff560162) method reuses the memory object pointed to by `pWdfMemory` to serve as a container for the transfer list.
2.  The **FormatRequestForIoctl** call reuses the request object pointed to by `pWdfIoRequest` to serve as a container for the **IOCTL\_SPB\_FULL\_DUPLEX** request. The *pInputMemory* parameter to this method is a pointer to the memory object that contains the transfer list. The *pOutputMemory* parameter is NULL.
3.  The call to the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method sends the I/O request to the device. This call is synchronous, and returns after the SPB controller driver completes the request.
4.  The call to the [**IWDFIoRequest::GetCompletionParams**](https://msdn.microsoft.com/library/windows/hardware/ff559084) method gets the completion parameters from the request.
5.  The call to the [**IWDFRequestCompletionParams::GetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff560305) method gets the *information* value from the completion parameters (the **Information** field in the I/O status block). This value is the total number of bytes transferred (bytes written plus bytes read) by the **IOCTL\_SPB\_FULL\_DUPLEX** request.

 

 




