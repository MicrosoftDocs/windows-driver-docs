---
title: How to Open and Close Static Streams in a USB Bulk Endpoint
description: This article discusses static streams capability and explains how a USB client driver can open and close streams in a bulk endpoint of a USB 3.0 device.
ms.date: 01/16/2024
---

# How to open and close static streams in a USB bulk endpoint

This article discusses *static streams capability* and explains how a USB client driver can open and close streams in a bulk endpoint of a USB 3.0 device.

In USB 2.0 and earlier devices, a bulk endpoint can send or receive a single data stream through the endpoint. In USB 3.0 devices, bulk endpoints have the capability to send and receive multiple data streams through the endpoint.

The Microsoft-provided USB driver stack in Windows supports multiple streams. This enables a client driver to send independent I/O requests to each stream associated with a bulk endpoint in a USB 3.0 device. The requests to different streams aren't serialized.

For a client driver, streams represent multiple logical endpoints that have the same set of characteristics. To send a request to a particular stream, the client driver needs a handle to that stream (similar to a pipe handle for an endpoint). The URB for an I/O request to a stream is similar to an URB for an I/O request to a bulk endpoint. The only difference is the pipe handle. To send an I/O request to a stream, the driver specifies the pipe handle to the stream.

During device configuration, the client driver sends a select-configuration request and optionally a select-interface request. Those requests retrieve a set of pipe handles to the endpoints defined in the active setting of an interface. For an endpoint that supports streams, the endpoint pipe handle can be used to send I/O requests to the *default stream* (the first stream) until the driver has opened streams (discussed next).

If the client driver wants to send requests to streams other than the default stream, the driver must open and obtain handles to all streams. To do so, the client driver sends an *open-streams request* by specifying the number of streams to open. After the client driver is finished using streams, the driver can optionally close them by sending a *close-streams request*.

Kernel Mode Driver Framework (KMDF) doesn't support static streams intrinsically. The client driver must send Windows Driver Model (WDM) style URBs that open and close streams. This article describes how to format and send those URBs. A User Mode Driver Framework (UMDF)-client driver can't use the static streams capability.

The article contains some notes labeled as **WDM drivers**. Those notes describe routines for a WDM-based USB client driver that wants to send stream requests.

## Prerequisites

Before a client driver can open or close streams, the driver must have:

- Called the **[WdfUsbTargetDeviceCreateWithParameters](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)** method.

  The method requires the client contract version to be USBD_CLIENT_CONTRACT_VERSION_602. By specifying that version the client driver must adhere to a set of rules. For more information, see [Best Practices: Using URBs](usb-client-driver-contract-in-windows-8.md).

  The call retrieves a WDFUSBDEVICE handle to the framework's USB target device object. That handle is required in order to make subsequent calls to open streams. Typically, the client driver registers itself in the driver's **[EVT_WDF_DEVICE_PREPARE_HARDWARE](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)** event callback routine.

  **WDM drivers:** Call the **[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)** routine and obtain a USBD handle for the driver's registration with the USB driver stack.

- Configured the device and obtained a WDFUSBPIPE pipe handle to the bulk endpoint that supports streams. To obtain the pipe handle, call the **[WdfUsbInterfaceGetConfiguredPipe](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbinterfacegetconfiguredpipe)** method on the current alternate setting of an interface in the selected configuration.

  **WDM drivers:** Obtain a USBD pipe handle by sending a select-configuration or select-interface request. For more information, see [How to Select a Configuration for a USB Device](how-to-select-a-configuration-for-a-usb-device.md).

## How to open static streams

1. Determine whether the underlying USB driver stack and the host controller supports the static streams capability by calling the **[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)** method. Typically, the client driver calls the routine in the driver's **[EVT_WDF_DEVICE_PREPARE_HARDWARE](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)** event callback routine.

   **WDM drivers:** Call the **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)** routine. Typically, the driver queries for the capabilities that it wants to use in the driver's start-device routine (**[IRP_MN_START_DEVICE](../kernel/irp-mn-start-device.md)**). For code example, see **USBD_QueryUsbCapability**.

   Provide the following information:

   - A handle to the USB device object that was retrieved, in a previous call to **[WdfUsbTargetDeviceCreateWithParameters](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)**, for client driver registration.

     **WDM drivers:** Pass the USBD handle that was retrieved in the previous call to **[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)**.

     If the client driver wants to use a particular capability, the driver must first query the underlying USB driver stack to determine whether the driver stack and the host controller support the capability. If the capability is supported, only then, the driver should send a request to use the capability. Some requests require URBs, such as the streams capability (discussed in step 5). For those requests, make sure that you use the same handle to query capabilities and allocate URBs. That is because the driver stack uses handles to track the supported capabilities that a driver can use.

     For instance, if you obtained a USBD_HANDLE (by calling **[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)**), query the driver stack by calling **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**, and allocate the URB by calling **[USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)**. Pass the same USBD_HANDLE in both those calls.

     If you call KMDF methods, **[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)** and **[WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)**, specify the same WDFUSBDEVICE handle to the framework target object in those method calls.

   - The GUID assigned to GUID_USB_CAPABILITY_STATIC_STREAMS.
   - An output buffer (pointer to USHORT). Upon completion, the buffer is filled with the maximum number of streams (per endpoint) supported by the host controller.
   - The length, in bytes, of the output buffer. For streams, the length is `sizeof (USHORT)`.

1. Evaluate the returned NTSTATUS value. If the routine completes successfully, returns STATUS_SUCCESS, the static streams capability is supported. Otherwise, the method returns an appropriate error code.

1. Determine the number of streams to open. The maximum number of streams that can be opened is limited by:
   - The maximum number of streams supported by the host controller. That number is received by **[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)** (for WDM drivers, **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**), in the caller-supplied output buffer. The Microsoft-provided USB driver stack supports up to 255 streams. **WdfUsbTargetDeviceQueryUsbCapability** takes that limitation into consideration while calculating the number of streams. The method never returns a value that is greater than 255.
   - The maximum number of streams supported by the endpoint in the device. To get that number, inspect the endpoint companion descriptor (see **[USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR](/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_superspeed_endpoint_companion_descriptor)** in Usbspec.h). To obtain the endpoint companion descriptor, you must parse the configuration descriptor. To obtain the configuration descriptor, the client driver must call the **[WdfUsbTargetDeviceRetrieveConfigDescriptor](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor)** method. You must use the helper routines, **[USBD_ParseConfigurationDescriptorEx](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_parseconfigurationdescriptorex)** and **[USBD_ParseDescriptor](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_parsedescriptors)**. For code example, see the example function named RetrieveStreamInfoFromEndpointDesc in [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

   To determine the maximum number of streams, choose the lesser of two values supported by the host controller and the endpoint.

1. Allocate an array of **[USBD_STREAM_INFORMATION](/windows-hardware/drivers/ddi/usb/ns-usb-_usbd_stream_information)** structures with *n* elements, where *n* is the number of streams to open. The client driver is responsible for releasing this array after the driver is finished using streams.

1. Allocate an URB for the open-streams request by calling the **[WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)** method. If the call completes successfully, the method retrieves a WDF memory object and the address of the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure that is allocated by the USB driver stack.

   **WDM drivers:** Call the **[USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)** routine.

1. Format the URB for the open-stream request. The URB uses the **[_URB_OPEN_STATIC_STREAMS](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_open_static_streams)** structure to define the request. To format the URB, you need:
   - The USBD pipe handle to the endpoint. If you have a WDF pipe object, you can obtain the USBD pipe handle by calling the **[WdfUsbTargetPipeWdmGetPipeHandle](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewdmgetpipehandle)** method.
   - The stream array (created in step 4)
   - A pointer to the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure (created in step 5).

   To format the URB, call **[UsbBuildOpenStaticStreamsRequest](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbbuildopenstaticstreamsrequest)** and pass the required information as parameter values. Make sure that the number of streams specified to **UsbBuildOpenStaticStreamsRequest** doesn't exceed the maximum number of supported streams.

1. Send the URB as a WDF request object by calling the **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** method. To send the request synchronously, call the **[WdfUsbTargetDeviceSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)** method instead.

   **WDM drivers:** Associate the URB with an IRP, and submit the IRP to the USB driver stack. For more information, see [How to Submit an URB](send-requests-to-the-usb-driver-stack.md).

1. After the request is complete, check the status of the request.

   If USB driver stack fails the request, the URB status contains the relevant error code. Some common failure conditions are described in the Remarks section.

If the status of the request (IRP or the WDF request object) indicates USBD_STATUS_SUCCESS, the request was completed successfully. Inspect the array of **[USBD_STREAM_INFORMATION](/windows-hardware/drivers/ddi/usb/ns-usb-_usbd_stream_information)** structures received on completion. The array is filled with information about the requested streams. The USB driver stack populates each structure in the array with stream information, such as handles (received as USBD_PIPE_HANDLE), stream identifiers, and the maximum number transfer size. Streams are now open to transfer data.

For an open-streams request, you'll need to allocate an URB and an array. The client driver must release the URB by calling the **[WdfObjectDelete](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete)** method on the associated WDF memory object, after the open streams request completes. If the driver sent the request synchronously by calling **[WdfUsbTargetDeviceSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)**, then it must release the WDF memory object, after the method returns. If the client driver sent the request asynchronously by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)**, the driver must release the WDF memory object in the driver-implemented completion routine associated with the request.

The stream array can be released after the client driver is finished using streams or has stored them for I/O requests. In the code example included in this article, the driver stores the streams array in the device context. The driver releases the device context just before releasing the device object is removed.

## How to transfer data to a particular stream

To send a data transfer request to a particular stream, you'll need a WDF request object. Typically, the client driver isn't required to allocate a WDF request object. When the I/O Manager receives a request from an application, the I/O Manager creates an IRP for the request. That IRP is intercepted by the framework. The framework then allocates a WDF request object to represent the IRP. After that, the framework passes the WDF request object to the client driver. The client driver can then associate the request object with the data transfer URB and send it down to the USB driver stack.

If the client driver doesn't receive a WDF request object from the framework and wants to send the request asynchronously, the driver must allocate a WDF request object by calling the **[WdfRequestCreate](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreate)** method. Format the new object by calling **[WdfUsbTargetPipeFormatRequestForUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforurb)**, and the send the request by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)**.

In the synchronous cases, passing a WDF request object is optional.

To transfer data to streams, you must use URBs. The URB must be formatted by calling **[WdfUsbTargetPipeFormatRequestForUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforurb)**.

The following WDF methods *aren't* supported for streams:

- **[WdfUsbTargetPipeFormatRequestForRead](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforread)**
- **[WdfUsbTargetPipeFormatRequestForWrite](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforwrite)**
- **[WdfUsbTargetPipeReadSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipereadsynchronously)**
- **[WdfUsbTargetPipeWriteSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipewritesynchronously)**

The following procedure assumes that the client driver receives the request object from framework.

1. Allocate an URB by calling **[WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)**. This method allocates a WDF memory object that contains the newly allocated URB. The client driver can choose to allocate an URB for every I/O request or allocate an URB and reuse it for the same type of request.

1. Format the URB for a bulk transfer by calling **[UsbBuildInterruptOrBulkTransferRequest](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbbuildinterruptorbulktransferrequest)**. In the *PipeHandle* parameter, specify the handle to the stream. The stream handles were obtained in a previous request, described in the [How to open static streams](#how-to-open-static-streams) section.

1. Format the WDF request object by calling the **[WdfUsbTargetPipeFormatRequestForUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforurb)** method. In the call, specify the WDF memory object that contains the data transfer URB. The memory object was allocated in step 1.

1. Send the URB as a WDF request either by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** or **[WdfUsbTargetPipeSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipesendurbsynchronously)**. If you call **WdfRequestSend**, you must specify a completion routine by calling **[WdfRequestSetCompletionRoutine](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetcompletionroutine)** so that the client driver can get notified when the asynchronous operation is complete. You must free the data transfer URB in the completion routine.

**WDM drivers:** Allocate an URB by calling **[USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)** and format it for bulk transfer (see **[_URB_BULK_OR_INTERRUPT_TRANSFER](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_bulk_or_interrupt_transfer)**). To format the URB, you can call **[UsbBuildInterruptOrBulkTransferRequest](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbbuildinterruptorbulktransferrequest)** or format the URB structure manually. Specify the handle to the stream in the URB's **UrbBulkOrInterruptTransfer.PipeHandle** member.

## How to close static streams

The client driver can close streams after the driver is finished using them. However, the close-stream request is optional. The USB driver stack closes all streams when the endpoint associated with the streams is de-configured. An endpoint is de-configured when an alternate configuration or interface is selected, the device is removed, and so on. A client driver must close streams if the driver wants to open a different number of streams. To send a close-stream request:

1. Allocate an **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure by calling **[WdfUsbTargetDeviceCreateUrb](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreateurb)**.

1. Format the URB for the close-streams request. The **UrbPipeRequest** member of the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure is an **[_URB_PIPE_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_pipe_request)** structure. Fill in its members as follows:
    - The **Hdr** member of **[_URB_PIPE_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_pipe_request)** must be URB_FUNCTION_CLOSE_STATIC_STREAMS
    - The **PipeHandle** member must be the handle to the endpoint that contains the open streams in use.

1. Send the URB as a WDF request either by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** or **[WdfUsbTargetDeviceSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)**.

The close-handle request closes all streams that were previously opened by the client driver. The client driver can't use the request to close specific streams in the endpoint.

## Best practices for sending a static streams request

The USB driver stack performs validations on the received URB. To avoid validation errors:

- Don't send an open-stream or close-stream request to an endpoint that doesn't support streams. Call **[WdfUsbTargetDeviceQueryUsbCapability](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicequeryusbcapability)** (for WDM drivers, **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**) to determine static streams support and only send streams requests if the endpoint supports them.
- Don't request a number (of streams to open) that exceeds the maximum number of streams supported or send a request without specifying the number of streams. Determine the number of streams based on the number of streams supported by the USB driver stack and the device's endpoint.
- Don't send an open-stream request to an endpoint that already has open streams.
- Don't send a close-stream request to an endpoint that doesn't have open streams.
- After static streams are open for an endpoint, don't send I/O requests by using the endpoint pipe handle that was obtained through a select-configuration or select-interface requests. This is true even if the static streams have been closed.

## Reset and abort pipe operations

At times, transfers to or from an endpoint can fail. Such failures can result from an error condition on the endpoint or host controller, such as a stall or halt condition. To clear the error condition, the client driver first cancels pending transfers and then resets the pipe with which the endpoint is associated. To cancel pending transfers, the client driver can send an abort-pipe request. To reset a pipe, the client driver must send a reset-pipe request.

For stream transfers, both abort-pipe and reset-pipe requests aren't supported for individual streams associated with the bulk endpoint. If a transfer fails on a particular stream pipe, the host controller stops transfers on all other pipes (for other streams). To recover from the error condition, the client driver should manually cancel transfers to each stream. Then, the client driver must send a reset-pipe request by using the pipe handle to bulk endpoint. For that request, the client driver must specify the pipe handle to the endpoint in a **[_URB_PIPE_REQUEST](/windows-hardware/drivers/ddi/usb/ns-usb-_urb_pipe_request)** structure and set the URB function (**Hdr.Function**) to URB_FUNCTION_SYNC_RESET_PIPE_AND_CLEAR_STALL.

## Complete example

The following code example shows how to open streams.

```cpp
NTSTATUS
    OpenStreams (
    _In_ WDFDEVICE Device,
    _In_ WDFUSBPIPE Pipe)
{
    NTSTATUS status;
    PDEVICE_CONTEXT deviceContext;
    PPIPE_CONTEXT pipeContext;
    USHORT cStreams = 0;
    USBD_PIPE_HANDLE usbdPipeHandle;
    WDFMEMORY urbMemory = NULL;
    PURB      urb = NULL;

    PAGED_CODE();

    deviceContext =GetDeviceContext(Device);
    pipeContext = GetPipeContext (Pipe);

    if (deviceContext->MaxStreamsController == 0)
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE,
            "%!FUNC! Static streams are not supported.");

        status = STATUS_NOT_SUPPORTED;
        goto Exit;
    }

    // If static streams are not supported, number of streams supported is zero.

    if (pipeContext->MaxStreamsSupported == 0)
    {
        status = STATUS_DEVICE_CONFIGURATION_ERROR;

        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE,
            "%!FUNC! Static streams are not supported by the endpoint.");

        goto Exit;
    }

    // Determine the number of streams to open.
    // Compare the number of streams supported by the endpoint with the
    // number of streams supported by the host controller, and choose the
    // lesser of the two values. The deviceContext->MaxStreams value was
    // obtained in a previous call to WdfUsbTargetDeviceQueryUsbCapability
    // that determined whether or not static streams is supported and
    // retrieved the maximum number of streams supported by the
    // host controller. The device context stores the values for IN and OUT
    // endpoints.

    // Allocate an array of USBD_STREAM_INFORMATION structures to store handles to streams.
    // The number of elements in the array is the number of streams to open.
    // The code snippet stores the array in its device context.

    cStreams = min(deviceContext->MaxStreamsController, pipeContext->MaxStreamsSupported);

    // Allocate an array of streams associated with the IN bulk endpoint
    // This array is released in CloseStreams.

    pipeContext->StreamInfo = (PUSBD_STREAM_INFORMATION) ExAllocatePoolWithTag (
        NonPagedPool,
        sizeof (USBD_STREAM_INFORMATION) * cStreams,
        USBCLIENT_TAG);

    if (pipeContext->StreamInfo == NULL)
    {
        status = STATUS_INSUFFICIENT_RESOURCES;

        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE,
            "%!FUNC! Could not allocate stream information array.");

        goto Exit;
    }

    RtlZeroMemory (pipeContext->StreamInfo,
        sizeof (USBD_STREAM_INFORMATION) * cStreams);

    // Get USBD pipe handle from the WDF target pipe object. The client driver received the
    // endpoint pipe handles during device configuration.

    usbdPipeHandle = WdfUsbTargetPipeWdmGetPipeHandle (Pipe);

    // Allocate an URB for the open streams request.
    // WdfUsbTargetDeviceCreateUrb returns the address of the
    // newly allocated URB and the WDFMemory object that
    // contains the URB.

    status = WdfUsbTargetDeviceCreateUrb (
        deviceContext->UsbDevice,
        NULL,
        &urbMemory,
        &urb);

    if (status != STATUS_SUCCESS)
    {
        TraceEvents(TRACE_LEVEL_ERROR, TRACE_DEVICE,
            "%!FUNC! Could not allocate URB for an open-streams request.");

        goto Exit;
    }

    // Format the URB for the open-streams request.
    // The UsbBuildOpenStaticStreamsRequest inline function formats the URB by specifying the
    // pipe handle to the entire bulk endpoint, number of streams to open, and the array of stream structures.

    UsbBuildOpenStaticStreamsRequest (
        urb,
        usbdPipeHandle,
        (USHORT)cStreams,
        pipeContext->StreamInfo);

    // Send the request synchronously.
    // Upon completion, the USB driver stack populates the array of with handles to streams.

    status = WdfUsbTargetPipeSendUrbSynchronously (
        Pipe,
        NULL,
        NULL,
        urb);

    if (status != STATUS_SUCCESS)
    {
        goto Exit;
    }

Exit:
    if (urbMemory)
    {
        WdfObjectDelete (urbMemory);
    }

    return status;
}
```

## Related topics

- [USB I/O Operations](usb-device-i-o.md)
