---
title: Working with USB Pipes
description: Working with USB Pipes
ms.assetid: d5422ff2-de1e-4a77-8b3c-0b2917b1d9ca
keywords:
- framework objects WDK KMDF , USB pipe objects
- USB pipes WDK KMDF
- pipe objects WDK KMDF
- USB I/O targets WDK KMDF , USB pipes
- continuous readers WDK USB
- resetting pipes WDK KMDF
- sending URBs WDK KMDF
- USB request blocks WDK KMDF
- URBs WDK KMDF
- stopping pipes WDK KMDF
- writing to pipes WDK KMDF
- reading from pipes WDK KMDF
- input pipes WDK KMDF
- output pipes WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Working with USB Pipes


The framework represents each pipe in a USB interface as a framework USB pipe object. When a driver [configures a USB device](working-with-usb-devices.md#selecting-a-device-configuration), the framework creates a framework USB pipe object for each pipe in each selected interface. Pipe object methods enable a driver to perform the following operations:

-   [Obtain pipe information.](#obtaining-pipe-information)

-   [Read from a pipe.](#reading-from-a-pipe)

-   [Write to a pipe.](#writing-to-a-pipe)

-   [Stop or reset a pipe.](#stopping-and-resetting-a-pipe)

-   [Send a URB to a pipe.](#sending-a-urb-to-a-pipe)

### <a href="" id="obtaining-pipe-information"></a> Obtaining Pipe Information

After calling [**WdfUsbInterfaceGetConfiguredPipe**](https://msdn.microsoft.com/library/windows/hardware/ff550057) to obtain a handle to a framework USB pipe object, your driver can call the following methods that the USB pipe object defines for obtaining information about the USB pipe:

<a href="" id="---------wdfusbtargetpipegetiotarget--------"></a>[**WdfUsbTargetPipeGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff551146)  
Returns a handle to the I/O target object that is associated with a USB pipe. The driver can pass this handle to [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027).

<a href="" id="---------wdfusbtargetpipegetinformation--------"></a>[**WdfUsbTargetPipeGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff551142)  
Retrieves information about a USB pipe and its endpoint.

<a href="" id="---------wdfusbtargetpipegettype--------"></a>[**WdfUsbTargetPipeGetType**](https://msdn.microsoft.com/library/windows/hardware/ff551148)  
Returns the type of a USB pipe.

<a href="" id="---------wdfusbtargetpipeisinendpoint--------"></a>[**WdfUsbTargetPipeIsInEndpoint**](https://msdn.microsoft.com/library/windows/hardware/ff551151)  
Determines whether a USB pipe is connected to an input endpoint.

<a href="" id="---------wdfusbtargetpipeisoutendpoint--------"></a>[**WdfUsbTargetPipeIsOutEndpoint**](https://msdn.microsoft.com/library/windows/hardware/ff551153)  
Determines whether a USB pipe is connected to an output endpoint.

<a href="" id="---------wdf-usb-pipe-direction-in--------"></a>[**WDF\_USB\_PIPE\_DIRECTION\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff553027)  
Determines whether a USB endpoint is an input endpoint.

<a href="" id="---------wdf-usb-pipe-direction-out--------"></a>[**WDF\_USB\_PIPE\_DIRECTION\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553032)  
Determines whether a USB endpoint is an output endpoint.

For related information, see [How to enumerate USB pipes](https://msdn.microsoft.com/library/windows/hardware/hh968306).

### <a href="" id="reading-from-a-pipe"></a> Reading from a Pipe

To read data from a USB input pipe, your driver can use any (or all) of the following three techniques:

-   Read data synchronously

    To read data synchronously from a USB input pipe, your driver can call the [**WdfUsbTargetPipeReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551155) method. This method builds and sends a read request, and it returns after the I/O operation has completed.

-   Read data asynchronously

    To read data asynchronously from a USB input pipe, your driver can call the [**WdfUsbTargetPipeFormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff551136) method to build a read request. Then the driver can call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request asynchronously (or synchronously).

-   Read data asynchronously and continuously

    A *continuous reader* is a framework-supplied mechanism for ensuring that a read request is always available to a USB pipe. This mechanism guarantees that the driver will always be ready to receive data from a device that provides an asynchronous, unsolicited input stream. For example, a driver for a network interface card (NIC) might use a continuous reader to receive input data.

    To configure a continuous reader for an input pipe, the driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function must call the [**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130) method. This method queues a set of read requests to the device's I/O target.

    Also, the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function must call [**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677) to start the continuous reader and the driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function must call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) to stop the continuous reader.

    Each time that data is available from the device, the I/O target will complete a read request and the framework will call one of two callback functions: [*EvtUsbTargetPipeReadComplete*](https://msdn.microsoft.com/library/windows/hardware/ff541826), if the I/O target successfully read the data, or [*EvtUsbTargetPipeReadersFailed*](https://msdn.microsoft.com/library/windows/hardware/ff541832), if the I/O target reports an error.

    If you do not supply the optional [*EvtUsbTargetPipeReadersFailed*](https://msdn.microsoft.com/library/windows/hardware/ff541832) callback, the framework responds to a failed read attempt by sending another read request. Therefore if the bus is in a state where it is not accepting reads, the framework continually sends new requests to recover from a failed read.

    After a driver has called [**WdfUsbTargetPipeConfigContinuousReader**](https://msdn.microsoft.com/library/windows/hardware/ff551130), the driver cannot use [**WdfUsbTargetPipeReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551155) or [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send I/O requests to the pipe unless the driver's [*EvtUsbTargetPipeReadersFailed*](https://msdn.microsoft.com/library/windows/hardware/ff541832) callback function is called and returns **FALSE**.

By default, the framework reports an error if your driver specifies a read buffer that is not a multiple of the pipe's maximum packet size. Your driver can call [**WdfUsbTargetPipeSetNoMaximumPacketSizeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff551160) to disable this test of read buffer sizes.

For related information, see:

-   [How to send USB bulk transfer requests](https://msdn.microsoft.com/library/windows/hardware/ff539199)
-   [How to transfer data to USB isochronous endpoints](https://msdn.microsoft.com/library/windows/hardware/hh406225)
-   [How to use the continuous reader for reading data from a USB pipe](https://msdn.microsoft.com/library/windows/hardware/hh968308)

### <a href="" id="writing-to-a-pipe"></a> Writing to a Pipe

To write data to a USB output pipe, your driver can use one (or both) of the following techniques:

-   Write data synchronously

    To write data synchronously to a USB output pipe, your driver can call the [**WdfUsbTargetPipeWriteSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551163) method. This method builds and sends a write request, and it returns after the I/O operation has completed.

-   Write data asynchronously

    To write data asynchronously to a USB input pipe, your driver can call the [**WdfUsbTargetPipeFormatRequestForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff551141) method to build a write request. Then the driver can call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request asynchronously.

For related information, see [How to send USB bulk transfer requests](https://msdn.microsoft.com/library/windows/hardware/ff539199).

### <a href="" id="stopping-and-resetting-a-pipe"></a> Stopping and Resetting a Pipe

Your driver can call the following methods to stop or reset a USB pipe:

<a href="" id="---------wdfusbtargetpipeabortsynchronously--------"></a>[**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129)  
Synchronously sends a request to stop a USB pipe.

<a href="" id="---------wdfusbtargetpipeformatrequestforabort--------"></a>[**WdfUsbTargetPipeFormatRequestForAbort**](https://msdn.microsoft.com/library/windows/hardware/ff551132)  
Formats a request to stop a USB pipe. The driver can call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request synchronously or asynchronously.

<a href="" id="---------wdfusbtargetpiperesetsynchronously--------"></a>[**WdfUsbTargetPipeResetSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551156)  
Synchronously sends a request to reset a USB pipe.

<a href="" id="---------wdfusbtargetpipeformatrequestforreset--------"></a>[**WdfUsbTargetPipeFormatRequestForReset**](https://msdn.microsoft.com/library/windows/hardware/ff551138)  
Formats a request to reset a USB pipe. The driver must call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request synchronously or asynchronously.

If your driver's USB target [completes](completing-i-o-requests.md) an I/O request with an error status value, your driver should do the following:

1.  Stop the pipe, and cancel any additional I/O requests that the driver has sent to the USB target, if the target has not completed the requests.

    Call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) with the [**WdfIoTargetCancelSentIo**](https://msdn.microsoft.com/library/windows/hardware/ff552388) flag set.

2.  Synchronously send an abort request to the pipe.

    Call [**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129), or call [**WdfUsbTargetPipeFormatRequestForAbort**](https://msdn.microsoft.com/library/windows/hardware/ff551132) followed by [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) with the [**WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS**](https://msdn.microsoft.com/library/windows/hardware/ff552491) flag set.

3.  Synchronously send a reset request to the pipe.

    Call [**WdfUsbTargetPipeResetSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551156), or call [**WdfUsbTargetPipeFormatRequestForReset**](https://msdn.microsoft.com/library/windows/hardware/ff551138) followed by [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) with the [**WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS**](https://msdn.microsoft.com/library/windows/hardware/ff552491) flag set.

4.  Restart the pipe.

    Call [**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677).

5.  Resend the I/O request that failed, and all I/O requests that followed the failed request.

After a significant number of multiple failures, the driver should attempt to reset the USB port by doing the following:

1.  Stop all active pipes, and cancel any additional I/O requests that the driver has sent to each pipe's USB target, if the target has not completed them.

    For each active pipe, call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) with the [**WdfIoTargetCancelSentIo**](https://msdn.microsoft.com/library/windows/hardware/ff552388) flag set.

2.  Synchronously send a request to reset the USB port.

    Call [**WdfUsbTargetDeviceResetPortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550097).

3.  Restart the pipes.

    Call [**WdfIoTargetStart**](https://msdn.microsoft.com/library/windows/hardware/ff548677) for each pipe that the driver stopped.

4.  Resend the last I/O request that failed, and all I/O requests that followed the failed request.

For related information, see [How to recover from USB pipe errors](https://msdn.microsoft.com/library/windows/hardware/hh968307).

### <a href="" id="sending-a-urb-to-a-pipe"></a> Sending an URB to a Pipe

If your KMDF driver communicates with a USB pipe by sending I/O requests that contain URBs, the driver can call the following methods:

<a href="" id="---------wdfusbtargetpipesendurbsynchronously--kmdf-only-"></a>[**WdfUsbTargetPipeSendUrbSynchronously (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff551158)  
Synchronously sends an I/O request that contains a URB.

<a href="" id="---------wdfusbtargetpipeformatrequestforurb--kmdf-only-"></a>[**WdfUsbTargetPipeFormatRequestForUrb (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff551139)  
Formats an I/O request that contains a URB. The driver can call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send the request synchronously or asynchronously.

<a href="" id="---------wdfusbtargetpipewdmgetpipehandle--kmdf-only-"></a>[**WdfUsbTargetPipeWdmGetPipeHandle (KMDF only)**](https://msdn.microsoft.com/library/windows/hardware/ff551162)  
Returns a device's USBD pipe handle. Some URBs require this handle.

 

 





