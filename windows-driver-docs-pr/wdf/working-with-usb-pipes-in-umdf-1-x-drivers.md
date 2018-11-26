---
title: Working with USB Pipes in UMDF 1.x Drivers
description: Working with USB Pipes in UMDF 1.x Drivers
ms.assetid: face26da-fa79-4d32-8ad1-9e8022bb23b3
keywords:
- UMDF WDK , USB pipes
- User-Mode Driver Framework WDK , USB pipes
- user-mode drivers WDK UMDF , USB pipes
- USB pipes WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Working with USB Pipes in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework represents each pipe in a USB interface as a framework USB pipe object. When a driver configures a USB device, the framework creates a framework USB pipe object for each pipe in each selected interface. Pipe object methods enable a driver to:

-   [Obtain pipe information](#obtaining-umdf-usb-pipe-information).

-   [Read from a pipe](#reading-from-a-umdf-usb-pipe).

-   [Write to a pipe](#writing-to-a-umdf-usb-pipe).

-   [Stop, flush, or reset a pipe](#stopping-flushing).

-   [Set pipe policy](#setting-pipe-policy).

-   [Handle pipe errors](#handling-pipe-errors).

### Obtaining UMDF-USB Pipe Information

After a UMDF driver calls the [**IWDFUsbInterface::RetrieveUsbPipeObject**](https://msdn.microsoft.com/library/windows/hardware/ff560339) method to obtain a pointer to the [IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391) interface for a USB pipe object, the driver can call the following methods that the USB pipe object defines for obtaining information about the USB pipe:

<a href="" id="iwdfusbtargetpipe--getinformation"></a>[**IWDFUsbTargetPipe::GetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff560403)  
Retrieves information about a USB pipe and its endpoint.

<a href="" id="iwdfusbtargetpipe--gettype"></a>[**IWDFUsbTargetPipe::GetType**](https://msdn.microsoft.com/library/windows/hardware/ff560406)  
Returns the type of a USB pipe.

<a href="" id="iwdfusbtargetpipe--isinendpoint"></a>[**IWDFUsbTargetPipe::IsInEndPoint**](https://msdn.microsoft.com/library/windows/hardware/ff560410)  
Determines whether a USB pipe is connected to an input endpoint.

<a href="" id="iwdfusbtargetpipe--isoutendpoint"></a>[**IWDFUsbTargetPipe::IsOutEndPoint**](https://msdn.microsoft.com/library/windows/hardware/ff560414)  
Determines whether a USB pipe is connected to an output endpoint.

<a href="" id="iwdfusbtargetpipe--retrievepipepolicy"></a>[**IWDFUsbTargetPipe::RetrievePipePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff560418)  
Retrieves a WinUsb pipe policy.

### Reading from a UMDF-USB Pipe

To read data from a USB input pipe, your driver can use either (or both) of the following techniques:

-   Read data synchronously.

    To read data synchronously from a USB input pipe, a UMDF driver first calls the [**IWDFIoTarget::FormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559233) method to build a read request. Then the driver calls the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method, specifying the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag, to send the request synchronously.

-   Read data asynchronously.

    To read data asynchronously from a USB input pipe, a UMDF driver first calls the [**IWDFIoTarget::FormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559233) method to build a read request. Then the driver calls the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method without specifying the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag.

-   Read data synchronously and continuously.

    A *continuous reader* is a framework-supplied mechanism that ensures a read request is always available to a USB pipe. This mechanism guarantees that the driver is always ready to receive data from a device that provides an asynchronous, unsolicited input stream. For example, a driver for a network interface card (NIC) might use a continuous reader to receive input data.

    To configure a continuous reader for an input pipe, the driver's [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766) callback function must call the [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff560395) method. This method queues a set of read requests to the device's I/O target.

    Also, the driver's [**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799) callback function must call [**IWDFIoTargetStateManagement::Start**](https://msdn.microsoft.com/library/windows/hardware/ff559213) to start the continuous reader and the driver's [**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803) callback function must call [**IWDFIoTargetStateManagement::Stop**](https://msdn.microsoft.com/library/windows/hardware/ff559217) to stop the continuous reader.

    Each time that data is available from the device, the I/O target will complete a read request and the framework will call one of two callback functions: [**IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556910) if the I/O target successfully read the data, or [**IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure**](https://msdn.microsoft.com/library/windows/hardware/ff556915) if the I/O target reports an error.

    After a driver has called [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff560395), the driver cannot use [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) to send I/O requests to the pipe unless the driver's [**IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure**](https://msdn.microsoft.com/library/windows/hardware/ff556915) callback function is called and returns **FALSE**.

    Continuous readers are supported in UMDF versions 1.9 and later.

### Writing to a UMDF-USB Pipe

To write data to a USB output pipe, a UMDF driver can first call the [**IWDFIoTarget::FormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559236) method to build a write request. Then the driver can call the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method to send the request asynchronously.

### <a href="" id="stopping-flushing"></a>Stopping, Flushing, and Resetting a UMDF-USB Pipe

A UMDF driver can call the following methods to stop, flush, or reset a USB pipe:

<a href="" id="iwdfusbtargetpipe--abort"></a>[**IWDFUsbTargetPipe::Abort**](https://msdn.microsoft.com/library/windows/hardware/ff560397)  
Synchronously sends a request to stop all pending transfers on a USB pipe.

<a href="" id="iwdfusbtargetpipe--flush"></a>[**IWDFUsbTargetPipe::Flush**](https://msdn.microsoft.com/library/windows/hardware/ff560400)  
Synchronously sends a request to discard any data that WinUsb saved when the device returned more data than the client requested.

<a href="" id="iwdfusbtargetpipe--reset"></a>[**IWDFUsbTargetPipe::Reset**](https://msdn.microsoft.com/library/windows/hardware/ff560416)  
Synchronously sends a request to reset a USB pipe.

### <a href="" id="setting-pipe-policy"></a>Setting Policy for a UMDF-USB Pipe

A UMDF driver can call the [**IWDFUsbTargetPipe::SetPipePolicy**](https://msdn.microsoft.com/library/windows/hardware/ff560421) method to control the behavior that is used by WinUsb for a USB pipe (for example, time-outs, handling short packets, and other behaviors).

### Handling Pipe Errors

If your driver's USB target [completes](completing-i-o-requests.md) an I/O request with an error status value, your driver should do the following:

1.  Call [**IWDFIoTargetStateManagement::Stop**](https://msdn.microsoft.com/library/windows/hardware/ff559217) with the **WdfIoTargetCancelSentIo** flag set. This call stops the pipe and cancels any additional I/O requests that the driver has sent to the USB target, if the target has not completed the requests.

2.  Call [**IWDFUsbTargetPipe::Abort**](https://msdn.microsoft.com/library/windows/hardware/ff560397) to send an abort request to the pipe.

3.  Call [**IWDFUsbTargetPipe::Reset**](https://msdn.microsoft.com/library/windows/hardware/ff560416) to send a reset request to the pipe.

4.  Call [**IWDFIoTargetStateManagement::Start**](https://msdn.microsoft.com/library/windows/hardware/ff559213) to restart the pipe.

5.  Resend the I/O request that failed, and all I/O requests that followed the failed request.

 

 





