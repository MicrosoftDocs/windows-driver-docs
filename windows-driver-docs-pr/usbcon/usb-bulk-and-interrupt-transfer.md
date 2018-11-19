---
Description: This topic provides a brief overview about USB bulk transfers. 
title: How to send USB bulk transfer requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to send USB bulk transfer requests


This topic provides a brief overview about USB bulk transfers. It also provides step-by-step instructions about how a client driver can send and receive bulk data from the device.

-   [About bulk endpoints](#ddk-usb-bulk-and-interrupt-transfer-kg)
-   [Bulk transactions](#bulk-transactions)
-   [USB client driver tasks for a bulk transfer](#usb-client-driver-tasks-for-a-bulk-transfer)
-   [Bulk transfer request example](#bulk-transfer-request-example)
    -   [Prerequisites](#prerequisites)
    -   [Step 1: Get the transfer buffer.](#step-1--get-the-transfer-buffer--)
    -   [Step 2: Format and send a framework request object to the USB driver stack.](#step-2--format-and-send-a-framework-request-object-to-the-usb-driver-stack-)
    -   [Step 3: Implement a completion routine for the request.](#step-3--implement-a-completion-routine-for-the-request-)

## About bulk endpoints


A USB bulk endpoint can transfer large amounts of data. Bulk transfers are reliable that allow hardware error detection, and involves limited number of retries in the hardware. For transfers to bulk endpoints, bandwidth is not reserved on the bus. When there are multiple transfer requests that target different types of endpoints, the controller first schedules transfers for time critical data, such as isochronous and interrupt packets. Only if there is unused bandwidth available on the bus, the controller schedules bulk transfers. Where there is no other significant traffic on the bus, bulk transfer can be fast. However, when the bus is busy with other transfers, bulk data can wait indefinitely.

Here are the key features of a bulk endpoint:

-   Bulk endpoints are optional. They are supported by a USB device that wants to transfer large amounts of data. For example, transferring files to a flash drive, data to or from a printer or a scanner.
-   USB full speed, high speed, and SuperSpeed devices support bulk endpoints. Low speed devices do not support bulk endpoints.
-   The endpoint is a unidirectional and data can be transferred either in an IN or OUT direction. Bulk IN endpoint is used to read data from the device to the host and bulk OUT endpoint is used to send data from the host to the device.
-   The endpoint has CRC bits to check for errors and thus provides data integrity. For CRC errors, data is retransmitted automatically.
-   A SuperSpeed bulk endpoint can support streams. Streams allow the host to send transfers to individual stream pipes.
-   Maximum packet size of a bulk endpoint depends on the bus speed of the device. For full speed, high speed, and SuperSpeed; the maximum packet sizes are 64, 512, and 1024 bytes respectively.

## Bulk transactions


Like all other USB transfers, the host always initiates a bulk transfer. The communication takes place between the host and the target endpoint. The USB protocol does not enforce any format on the data sent in a bulk transaction.

How the host and device communicate on the bus depends on the speed at which the device is connected. This section describes some examples of high speed and SuperSpeed bulk transfers that show the communication between the host and device.

You can see the structure of transactions and packets by using any USB analyzer, such as Beagle, Ellisys, LeCroy USB protocol analyzers. An analyzer device shows how data is sent to or received from a USB device over the wire. In this example, let's examine some traces captured by a LeCroy USB analyzer. This example is for information only. This is not an endorsement by Microsoft.

**Bulk OUT transaction example**

This analyzer trace shows an example bulk OUT transaction at high speed.

![trace of an example data transaction.](images/bulk-out-hs.png)

In the preceding trace, the host initiates a bulk OUT transfer to a high-speed bulk endpoint, by sending a token packet with PID set to OUT (OUT token). The packet contains the address of the device and target endpoint. After the OUT packet, the host sends a data packet that contains the bulk payload. If the endpoint accepts the incoming data, it sends an ACK packet. In this example, we can see that the host sent 31 bytes to device address:1; endpoint address: 2.

If the endpoint is busy at the time the data packet arrives and is not able to receive data, the device can send a NAK packet. In that case, the host starts sending PING packets to the device. The device responds with NAK packets as long as the device is not ready to receive data. When the device is ready, it responds with an ACK packet. The host can then resume the OUT transfer.

This analyzer trace shows an example SuperSpeed bulk OUT transaction.

![trace of an example data transaction.](images/bulk-out.png)

In the preceding trace, the host initiates an OUT transaction to a SuperSpeed bulk endpoint by sending a data packet. The data packet contains the bulk payload, device, and endpoint addresses. In this example, we can see that the host sent 31 bytes to device address:4; endpoint address: 2.

The device receives and acknowledges data packet and sends an ACK packet back to the host. If the endpoint is busy at the time the data packet arrives and is not able to receive data, the device can send a NRDY packet. Unlike high speed, after receiving the NRDY packet, the host does not repeatedly poll the device. Instead, the host waits for an ERDY from the device. When the device is ready, it sends an ERDY packet and the host can then send data to the endpoint.

**Bulk IN transaction example**

This analyzer trace shows an example bulk IN transaction at high speed.

![trace of an example data transaction.](images/bulk-in-hs.png)

In the preceding trace, the host initiates the transaction by sending a token packet with PID set to IN (IN token). The device then sends a data packet with bulk payload. If the endpoint has no data to send or is not yet ready to send data, the device can send a NAK handshake packet. The host retries the IN transfer until it receives an ACK packet from the device. That ACK packet implies that the device has accepted the data.

This analyzer trace shows an example SuperSpeed bulk IN transaction.

![trace of an example data transaction.](images/bulk-in.png)

To initiate a bulk IN transfer from a SuperSpeed endpoint, the host starts a bulk transaction by sending an ACK packet. The USB Specification version 3.0 optimizes this initial portion of the transfer by merging ACK and IN packets into one ACK packet. Instead of an IN token, for SuperSpeed, the host sends an ACK token to initiate a bulk transfer. The device responds with a data packet. The host then acknowledges the data packet by sending an ACK packet. If the endpoint is busy and was not able to send data, the device can send status of NRDY. In that case, the host waits for until it gets an ERDY packet from the device.

## USB client driver tasks for a bulk transfer


An application or a driver on the host always initiates a bulk transfer to send or receive data. The client driver submits the request to the USB driver stack. The USB driver stack programs the request into the host controller and then sends the protocol packets (as described in the preceding section) over the wire to the device.

Let's see how the client driver submits the request for a bulk transfer as a result of an application's or another driver's request. Alternatively, the driver can initiate the transfer on its own. Irrespective of the approach, a driver must have the transfer buffer and the request in order to initiate the bulk transfer.

For a KMDF driver, the request is described in a framework request object (see [WDF Request Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265664)). The client driver calls methods of the request object by specifying the WDFREQUEST handle to send the request to the USB driver stack. If the client driver is sending a bulk transfer in response to a request from an application or another driver, the framework creates a request object and delivers the request to the client driver by using a framework queue object. In that case, the client driver may use that request for the purposes of sending the bulk transfer. If the client driver initiated the request, the driver may choose to allocate its own request object.

If the application or another driver sent or requested data, the transfer buffer is passed to the driver by the framework. Alternatively, the client driver can allocate the transfer buffer and create the request object if the driver initiates the transfer on its own.

Here are the main tasks for the client driver:

1.  Get the transfer buffer.
2.  Get, format, and send a framework request object to the USB driver stack.
3.  Implement a completion routine to get notified when the USB driver stack completes the request.

This topic describes those tasks by using an example in which the driver initiates a bulk transfer as a result of an application's request to send or receive data.

To read data from the device, the client driver can use the framework provided continuous reader object. For more information, see [How to use the continuous reader for reading data from a USB pipe](how-to-use-the-continous-reader-for-getting-data-from-a-usb-endpoint--umdf-.md).

## Bulk transfer request example


Consider an example scenario, where an application wants to read or write data to your device. The application calls Windows APIs to send such requests. In this example, the application opens a handle to the device by using the device interface GUID published by your driver in kernel mode. The application then calls [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467) or [**WriteFile**](https://msdn.microsoft.com/library/windows/desktop/aa365747) to initiate a read or write request. In that call, the application also specifies a buffer that contains the data to read or write and the length of that buffer.

The I/O Manager receives the request, creates an I/O Request Packet (IRP), and forwards it to the client driver.

The framework intercepts the request, creates a framework request object, and adds it to the framework queue object. The framework then notifies the client driver that a new request is waiting to be processed. That notification is done by invoking the driver’s queue callback routines for [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776) or [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813).

When the framework delivers the request to the client driver, it receives these parameters:

-   WDFQUEUE handle to the framework queue object that contains the request.
-   WDFREQUEST handle to the framework request object that contains details about this request.
-   The transfer length, that is, the number of bytes to read or write.

In the client driver's implementation of [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776) or [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813), the driver inspects the request parameters and can optionally perform validation checks.

If you are using streams of a SuperSpeed bulk endpoint, you will send the request in an URB because KMDF does not support streams intrinsically. For information about submitting a request for transfer to streams of a bulk endpoint, see [How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md).

If you are not using streams, you can use KMDF defined methods to send the request as described in the following procedure:

### Prerequisites

Before you begin, make sure that you have this information:

-   The client driver must have created the framework USB target device object and obtained the WDFUSBDEVICE handle by calling the [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) method.

    If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code performs those tasks. The template code obtains the handle to the target device object and stores in the device context. For more information, see "Device source code" in [Understanding the USB client driver code structure (KMDF)](understanding-the-kmdf-template-code-for-usb.md).

-   WDFREQUEST handle to the framework request object that contains details about this request.
-   The number of bytes to read or write.
-   The WDFUSBPIPE handle to the framework pipe object that is associated with the target endpoint. You must have obtained pipe handles during device configuration by enumerating pipes. For more information, see [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

    If the bulk endpoint supports streams, you must have the pipe handle to the stream. For more information, see [How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md).

### <a href="" id="step-1--get-the-transfer-buffer--"></a>Step 1: Get the transfer buffer.

The transfer buffer or the transfer buffer MDL contains the data to send or receive. This topic assumes that you are sending or receiving data in a transfer buffer. The transfer buffer is described in a WDF memory object (see [WDF Memory Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265645)). To get the memory object associated with the transfer buffer, call one of these methods:

-   For a bulk IN transfer request, call the [**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019) method.
-   For a bulk OUT transfer request, call the [**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015) method.

The client driver does not need to release this memory. The memory is associated with the parent request object and is released when the parent is released.

### <a href="" id="step-2--format-and-send-a-framework-request-object-to-the-usb-driver-stack-"></a>Step 2: Format and send a framework request object to the USB driver stack.

You can send the transfer request asynchronously or synchronously.

These are the asynchronous methods:

-   [**WdfUsbTargetPipeFormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff551136)
-   [**WdfUsbTargetPipeFormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff551141)

The methods in this list format the request. If you send the request asynchronously, set a pointer to the driver-implemented completion routine by calling the [**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030) method (described in the next step). To send the request, call the [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) method.

If you send the request synchronously, call these methods:

-   [**WdfUsbTargetPipeReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551155)
-   [**WdfUsbTargetPipeWriteSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551163)

For code examples, see the Examples section of the reference topics for those methods.
### <a href="" id="step-3--implement-a-completion-routine-for-the-request-"></a>Step 3: Implement a completion routine for the request.

If the request is sent asynchronously, you must implement a completion routine to get notified when the USB driver stack completes the request. Upon completion, the framework invokes the driver's completion routine. The framework passes these parameters:

-   WDFREQUEST handle to the request object.
-   WDFIOTARGET handle to the I/O target object for the request.
-   A pointer to a [**WDF\_REQUEST\_COMPLETION\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552454) structure that contains completion information. USB-specific information is contained in the **CompletionParams-&gt;Parameters.Usb** member.
-   WDFCONTEXT handle to the context that the driver specified in its call to [**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030).

In the completion routine, perform these tasks:

-   Check the status of the request by getting the **CompletionParams-&gt;IoStatus.Status** value.
-   Check the USBD status set by the USB driver stack.
-   In case of pipe errors, perform error recovery operations. For more information, see [How to recover from USB pipe errors](how-to-recover-from-usb-pipe-errors.md).
-   Check the number of bytes transferred.

    A bulk transfer is complete when the requested number of bytes have been transferred to or from the device. If you send the request buffer by calling KMDF method, then check the value received in **CompletionParams-&gt;Parameters.Usb.Completion-&gt;Parameters.PipeWrite.Length** or **CompletionParams-&gt;Parameters.Usb.Completion-&gt;Parameters.PipeRead.Length** members.

    In a simple transfer where the USB driver stack sends all the requested bytes in one data packet, you can check compare the **Length** value with the number of bytes requested. If the USB driver stack transfers the request in multiple data packets, you must keep track of the number of bytes transferred and the remaining number of bytes.

-   If total number of bytes were transferred, complete the request. If an error condition occurred, complete the request with the returned error code. Complete the request by calling the [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) method. If you want to set information, such as the number of bytes transferred, call [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549945withinformation).
-   Make sure that when you complete the request with information, the number of bytes must be equal to or less than the number of bytes requested. The framework validates those values. If length set in the completed request is greater than the original request length, a bugcheck can occur.

This example code shows how the client driver can submit a bulk transfer request. The driver sets a completion routine. That routine is shown in the next code block.

```cpp
/*++

Routine Description:

This routine sends a bulk write request to the 
USB driver stack. The request is sent asynchronously and 
the driver gets notified through a completion routine.

Arguments:

Queue - Handle to a framework queue object.
Request - Handle to the framework request object.
Length - Number of bytes to transfer.


Return Value:

VOID

--*/


VOID Fx3EvtIoWrite(
    IN WDFQUEUE  Queue,
    IN WDFREQUEST  Request,
    IN size_t  Length
    )
{
    NTSTATUS  status;
    WDFUSBPIPE  pipe;
    WDFMEMORY  reqMemory;
    PDEVICE_CONTEXT  pDeviceContext;

    pDeviceContext = GetDeviceContext(WdfIoQueueGetDevice(Queue));

    pipe = pDeviceContext->BulkWritePipe;

    status = WdfRequestRetrieveInputMemory(
                                           Request,
                                           &reqMemory
                                           );
    if (!NT_SUCCESS(status))
    {
        goto Exit;
    }

    status = WdfUsbTargetPipeFormatRequestForWrite(
                                                   pipe,
                                                   Request,
                                                   reqMemory,
                                                   NULL
                                                   );
    if (!NT_SUCCESS(status))
       {
        goto Exit;
    }

    WdfRequestSetCompletionRoutine(
                                   Request,
                                   BulkWriteComplete,
                                   pipe
                                   );

    if (WdfRequestSend( Request,
                        WdfUsbTargetPipeGetIoTarget(pipe),
                        WDF_NO_SEND_OPTIONS) == FALSE) 
       {
        status = WdfRequestGetStatus(Request);
        goto Exit;
    }

Exit:
    if (!NT_SUCCESS(status)) {
        WdfRequestCompleteWithInformation(
                                          Request,
                                          status,
                                          0
                                          );
    }
    return;
}
```

This example code shows the completion routine implementation for a bulk transfer. The client driver completes the request in the completion routine and sets this request information: status and the number of bytes transferred.

```cpp
/*++

Routine Description:

This completion routine is invoked by the framework when
the USB drive stack completes the previously sent 
bulk write request. The client driver completes the 
the request if the total number of bytes were transferred
to the device.
In case of failure it queues a work item to start the 
error recovery by resetting the target pipe.

Arguments:

Queue - Handle to a framework queue object.
Request - Handle to the framework request object.
Length - Number of bytes to transfer.
Pipe - Handle to the pipe that is the target for this request.

Return Value:

VOID

--*/

VOID BulkWriteComplete(  
    _In_ WDFREQUEST                  Request,  
    _In_ WDFIOTARGET                 Target,  
    PWDF_REQUEST_COMPLETION_PARAMS   CompletionParams,  
    _In_ WDFCONTEXT                  Context  
    )  
{

    PDEVICE_CONTEXT deviceContext;

    size_t          bytesTransferred=0; 

    NTSTATUS        status;


    UNREFERENCED_PARAMETER (Target);
    UNREFERENCED_PARAMETER (Context);


    KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, 
        "In completion routine for Bulk transfer.\n"));

    // Get the device context. This is the context structure that
    // the client driver provided when it sent the request.

    deviceContext = (PDEVICE_CONTEXT)Context;

    // Get the status of the request
    status = CompletionParams->IoStatus.Status;
    if (!NT_SUCCESS (status))
    {
        // Get the USBD status code for more information about the error condition.
        status = CompletionParams->Parameters.Usb.Completion->UsbdStatus;

        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL,
            "Bulk transfer failed. 0x%x\n",  
            status));       

        // Queue a work item to start the reset-operation on the pipe
        // Not shown.

        goto Exit;
    }

    // Get the actual number of bytes transferred.
    bytesTransferred = 
            CompletionParams->Parameters.Usb.Completion->Parameters.PipeWrite.Length;

    KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL,
            "Bulk transfer completed. Transferred %d bytes. \n",  
            bytesTransferred));

Exit:

    // Complete the request and update the request with 
    // information about the status code and number of bytes transferred.

    WdfRequestCompleteWithInformation(Request, status, bytesTransferred);

    return;
}
```

## Related topics
[USB I/O Transfers](usb-device-i-o.md)  
[How to open and close static streams in a USB bulk endpoint](how-to-open-streams-in-a-usb-endpoint.md)  



