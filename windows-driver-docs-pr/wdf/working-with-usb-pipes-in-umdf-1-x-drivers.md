---
title: Working with USB Pipes in UMDF 1.x Drivers
description: Working with USB Pipes in UMDF 1.x Drivers
keywords:
- UMDF WDK , USB pipes
- User-Mode Driver Framework WDK , USB pipes
- user-mode drivers WDK UMDF , USB pipes
- USB pipes WDK UMDF
ms.date: 04/20/2017
---

# Working with USB Pipes in UMDF 1.x Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework represents each pipe in a USB interface as a framework USB pipe object. When a driver configures a USB device, the framework creates a framework USB pipe object for each pipe in each selected interface. Pipe object methods enable a driver to:

-   [Obtain pipe information](#obtaining-umdf-usb-pipe-information).

-   [Read from a pipe](#reading-from-a-umdf-usb-pipe).

-   [Write to a pipe](#writing-to-a-umdf-usb-pipe).

-   [Stop, flush, or reset a pipe](#stopping-flushing).

-   [Set pipe policy](#setting-pipe-policy).

-   [Handle pipe errors](#handling-pipe-errors).

### Obtaining UMDF-USB Pipe Information

After a UMDF driver calls the [**IWDFUsbInterface::RetrieveUsbPipeObject**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbinterface-retrieveusbpipeobject) method to obtain a pointer to the [IWDFUsbTargetPipe](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbtargetpipe) interface for a USB pipe object, the driver can call the following methods that the USB pipe object defines for obtaining information about the USB pipe:

<a href="" id="iwdfusbtargetpipe--getinformation"></a>[**IWDFUsbTargetPipe::GetInformation**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-getinformation)  
Retrieves information about a USB pipe and its endpoint.

<a href="" id="iwdfusbtargetpipe--gettype"></a>[**IWDFUsbTargetPipe::GetType**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-gettype)  
Returns the type of a USB pipe.

<a href="" id="iwdfusbtargetpipe--isinendpoint"></a>[**IWDFUsbTargetPipe::IsInEndPoint**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-isinendpoint)  
Determines whether a USB pipe is connected to an input endpoint.

<a href="" id="iwdfusbtargetpipe--isoutendpoint"></a>[**IWDFUsbTargetPipe::IsOutEndPoint**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-isoutendpoint)  
Determines whether a USB pipe is connected to an output endpoint.

<a href="" id="iwdfusbtargetpipe--retrievepipepolicy"></a>[**IWDFUsbTargetPipe::RetrievePipePolicy**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-retrievepipepolicy)  
Retrieves a WinUsb pipe policy.

### Reading from a UMDF-USB Pipe

To read data from a USB input pipe, your driver can use either (or both) of the following techniques:

-   Read data synchronously.

    To read data synchronously from a USB input pipe, a UMDF driver first calls the [**IWDFIoTarget::FormatRequestForRead**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforread) method to build a read request. Then the driver calls the [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) method, specifying the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag, to send the request synchronously.

-   Read data asynchronously.

    To read data asynchronously from a USB input pipe, a UMDF driver first calls the [**IWDFIoTarget::FormatRequestForRead**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforread) method to build a read request. Then the driver calls the [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) method without specifying the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag.

-   Read data synchronously and continuously.

    A *continuous reader* is a framework-supplied mechanism that ensures a read request is always available to a USB pipe. This mechanism guarantees that the driver is always ready to receive data from a device that provides an asynchronous, unsolicited input stream. For example, a driver for a network interface card (NIC) might use a continuous reader to receive input data.

    To configure a continuous reader for an input pipe, the driver's [**IPnpCallbackHardware::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware-onpreparehardware) callback function must call the [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe2-configurecontinuousreader) method. This method queues a set of read requests to the device's I/O target.

    Also, the driver's [**IPnpCallback::OnD0Entry**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0entry) callback function must call [**IWDFIoTargetStateManagement::Start**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotargetstatemanagement-start) to start the continuous reader and the driver's [**IPnpCallback::OnD0Exit**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0exit) callback function must call [**IWDFIoTargetStateManagement::Stop**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotargetstatemanagement-stop) to stop the continuous reader.

    Each time that data is available from the device, the I/O target will complete a read request and the framework will call one of two callback functions: [**IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete-onreadercompletion) if the I/O target successfully read the data, or [**IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed-onreaderfailure) if the I/O target reports an error.

    After a driver has called [**IWDFUsbTargetPipe2::ConfigureContinuousReader**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe2-configurecontinuousreader), the driver cannot use [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) to send I/O requests to the pipe unless the driver's [**IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed-onreaderfailure) callback function is called and returns **FALSE**.

    Continuous readers are supported in UMDF versions 1.9 and later.

### Writing to a UMDF-USB Pipe

To write data to a USB output pipe, a UMDF driver can first call the [**IWDFIoTarget::FormatRequestForWrite**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforwrite) method to build a write request. Then the driver can call the [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) method to send the request asynchronously.

### <a href="" id="stopping-flushing"></a>Stopping, Flushing, and Resetting a UMDF-USB Pipe

A UMDF driver can call the following methods to stop, flush, or reset a USB pipe:

<a href="" id="iwdfusbtargetpipe--abort"></a>[**IWDFUsbTargetPipe::Abort**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-abort)  
Synchronously sends a request to stop all pending transfers on a USB pipe.

<a href="" id="iwdfusbtargetpipe--flush"></a>[**IWDFUsbTargetPipe::Flush**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-flush)  
Synchronously sends a request to discard any data that WinUsb saved when the device returned more data than the client requested.

<a href="" id="iwdfusbtargetpipe--reset"></a>[**IWDFUsbTargetPipe::Reset**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-reset)  
Synchronously sends a request to reset a USB pipe.

### <a href="" id="setting-pipe-policy"></a>Setting Policy for a UMDF-USB Pipe

A UMDF driver can call the [**IWDFUsbTargetPipe::SetPipePolicy**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-setpipepolicy) method to control the behavior that is used by WinUsb for a USB pipe (for example, time-outs, handling short packets, and other behaviors).

### Handling Pipe Errors

If your driver's USB target [completes](completing-i-o-requests.md) an I/O request with an error status value, your driver should do the following:

1.  Call [**IWDFIoTargetStateManagement::Stop**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotargetstatemanagement-stop) with the **WdfIoTargetCancelSentIo** flag set. This call stops the pipe and cancels any additional I/O requests that the driver has sent to the USB target, if the target has not completed the requests.

2.  Call [**IWDFUsbTargetPipe::Abort**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-abort) to send an abort request to the pipe.

3.  Call [**IWDFUsbTargetPipe::Reset**](/windows-hardware/drivers/ddi/wudfusb/nf-wudfusb-iwdfusbtargetpipe-reset) to send a reset request to the pipe.

4.  Call [**IWDFIoTargetStateManagement::Start**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotargetstatemanagement-start) to restart the pipe.

5.  Resend the I/O request that failed, and all I/O requests that followed the failed request.

 

