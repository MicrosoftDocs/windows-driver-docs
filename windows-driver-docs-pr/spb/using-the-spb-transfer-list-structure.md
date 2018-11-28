---
title: Using the SPB_TRANSFER_LIST Structure for Custom IOCTLs
description: If your simple peripheral bus (SPB) controller driver supports one or more custom I/O control (IOCTL) requests, use the SPB_TRANSFER_LIST structure to describe the read and write buffers in these requests.
ms.assetid: 577122CC-D1F8-41C5-BE77-A22FC8516B82
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the SPB\_TRANSFER\_LIST Structure for Custom IOCTLs


If your simple peripheral bus (SPB) controller driver supports one or more custom I/O control (IOCTL) requests, use the [**SPB\_TRANSFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/hh406221) structure to describe the read and write buffers in these requests. This structure provides a uniform way to describe the buffers in a request, and avoids the buffer-copying overhead associated with METHOD\_BUFFERED I/O operations.

If your custom IOCTL requests use the **SPB\_TRANSFER\_LIST** structure, your SPB controller driver must call the [**SpbRequestCaptureIoOtherTransferList**](https://msdn.microsoft.com/library/windows/hardware/hh974775) method to capture these buffers in the process context of the request originator. Your driver can call the [**SpbRequestGetTransferParameters**](https://msdn.microsoft.com/library/windows/hardware/hh450924) method to access these buffers.

The [**IOCTL\_SPB\_FULL\_DUPLEX**](https://msdn.microsoft.com/library/windows/hardware/hh974774) and [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) requests, which are defined as part of the [SPB I/O request interface](https://msdn.microsoft.com/library/windows/hardware/hh698224), use the **SPB\_TRANSFER\_LIST** structure to describe their read and write buffers. The **SPB\_TRANSFER\_LIST** structure for an **IOCTL\_SPB\_FULL\_DUPLEX** request describes both the write buffer and the read buffer (in that order) in the request. The **SPB\_TRANSFER\_LIST** structure for an **IOCTL\_SPB\_EXECUTE\_SEQUENCE** request can describe an arbitrary sequence of read and write buffers.

Similarly, you can define your custom IOCTLs to require their **SPB\_TRANSFER\_LIST** structures to use some combination of read and write buffers, and specify any ordering of the buffers in the list that might be required.

The Kernel-Mode Driver Foundation (KMDF) driver for an SPB peripheral device calls a method such as [**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660) to send an IOCTL request to an SPB controller. This method has *InputBuffer* and *OutputBuffer* parameters. Drivers for some types of devices might use these two parameters to point to the write buffer and read buffer, respectively, for an IOCTL request. However, to send an IOCTL request to an SPB controller, the SPB peripheral device driver sets the *InputBuffer* parameter to point to a memory descriptor that points to an **SPB\_TRANSFER\_LIST** structure. This structure describes any read or write buffers that are required for the I/O control operation. The driver sets the *OutputBuffer* parameter to NULL.

Similarly, the User-Mode Driver Foundation (UMDF) driver for an SPB peripheral device calls a method such as [**IWDFIoTarget::FormatRequestForIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff559230) to format an I/O request for an I/O control operation. This method has *pInputMemory* and *pOutputMemory* parameters. Drivers for some types of devices might use these two parameters to point to the write buffer and read buffer for an IOCTL request. However, to send an IOCTL request to an SPB controller, the SPB peripheral device driver sets the *pInputMemory* parameter to point to a memory object that contains an **SPB\_TRANSFER\_LIST** structure. This structure describes any read or write buffers that are required for the I/O control operation. The driver sets the *pOutputMemory* parameter to NULL.

## Parameter Checking and Buffer Capture


When the SPB framework extension (SpbCx) receives an **IOCTL\_SPB\_EXECUTE\_SEQUENCE** request, SpbCx passes this request to the SPB controller driver by calling the driver's [*EvtSpbControllerIoSequence*](https://msdn.microsoft.com/library/windows/hardware/hh450810) function. Before this call, SpbCx inspects the **SPB\_TRANSFER\_LIST** structure that describes the buffers in the request. SpbCx captures these buffers in the process context of the request originator. (Buffers in user-mode memory can be accessed only in the process in which the memory is allocated.) Additionally, SpbCx checks whether the parameter values in the request are valid.

When SpbCx receives an **IOCTL\_SPB\_FULL\_DUPLEX** request or a custom IOCTL request, SpbCx passes this request to the SPB controller driver by calling the driver's [*EvtSpbControllerIoOther*](https://msdn.microsoft.com/library/windows/hardware/hh450805) callback function. Before making this call, SpbCx does no validation checking of the parameter values in the request, and does not capture the request's buffers in the context of the originator. Parameter checking and buffer capture for these requests is the responsibility of the SPB controller driver.

If an SPB controller driver supports the **IOCTL\_SPB\_FULL\_DUPLEX** request, or supports any custom IOCTL request that uses the **SPB\_TRANSFER\_LIST** structure for its buffers, the driver must implement an [*EvtIoInCallerContext*](https://msdn.microsoft.com/library/windows/hardware/ff541764) callback function. The driver supplies a pointer to this function as an input parameter in the call to the [**SpbControllerSetIoOtherCallback**](https://msdn.microsoft.com/library/windows/hardware/hh450907) method that registers the driver's *EvtSpbControllerIoOther* callback function. When SpbCx receives an **IOCTL\_SPB\_FULL\_DUPLEX** request or a custom IOCTL request, SpbCx calls the driver's *EvtIoInCallerContext* function in the originator's context. If the IOCTL request uses the **SPB\_TRANSFER\_LIST** structure, the *EvtIoInCallerContext* function calls the [**SpbRequestCaptureIoOtherTransferList**](https://msdn.microsoft.com/library/windows/hardware/hh974775) method to capture the buffers in the request. The *EvtIoInCallerContext* function might also perform some preliminary processing of the request.

The following code example shows an *EvtIoInCallerContext* function that is implemented by an SPB controller driver.

```cpp
VOID
EvtIoInCallerContext(
    _In_  WDFDEVICE   SpbController,
    _In_  WDFREQUEST  FxRequest
    ) 
{
    NTSTATUS status = STATUS_SUCCESS;
    WDF_REQUEST_PARAMETERS fxParams;
  
    WDF_REQUEST_PARAMETERS_INIT(&fxParams);
    WdfRequestGetParameters(FxRequest, &fxParams);

    if ((fxParams.Type != WdfRequestTypeDeviceControl) &&
        (fxParams.Type != WdfRequestTypeDeviceControlInternal))
    {
        status = STATUS_NOT_SUPPORTED;
        goto exit;
    }

    //
    // The driver should check for custom IOCTLs that it handles.
    // If the IOCTL is not recognized, complete the request with a
    // status of STATUS_NOT_SUPPORTED.
    //

    switch (fxParams.Parameters.DeviceIoControl.IoControlCode)
    {
        ...

    default:
        status = STATUS_NOT_SUPPORTED;
        goto exit;
    }

    //
    // The IOCTL is recognized. Capture the buffers in the request.
    //

    status = SpbRequestCaptureIoOtherTransferList((SPBREQUEST)FxRequest);

    //
    // If the capture fails, the driver must complete the request instead
    // of placing it in the SPB controller&#39;s request queue.
    //

    if (!NT_SUCCESS(status))
    {
        goto exit;
    }

    status = WdfDeviceEnqueueRequest(SpbController, FxRequest);

    if (!NT_SUCCESS(status))
    {
        goto exit;
    }

exit:

    if (!NT_SUCCESS(status))
    {
        WdfRequestComplete(FxRequest, status);
    }
}
```

In the preceding code example, the **switch** statement verifies that the request contains an IOCTL that the SPB controller driver recognizes. (For brevity, the body of the **switch** statement is not shown.) Next, the call to the **SpbRequestCaptureIoOtherTransferList** method captures the buffers in the request. If this call succeeds, the request is added to the SPB controller's I/O queue. Otherwise, the request is completed with an error status code.

For a [code example](https://msdn.microsoft.com/library/windows/hardware/hh974773#code-example) that shows parameter checking by an *EvtSpbControllerIoOther* function, see [Handling **IOCTL\_SPB\_FULL\_DUPLEX** Requests](https://msdn.microsoft.com/library/windows/hardware/hh974773).

 

 




