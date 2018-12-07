---
Description: This topic provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this topic cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes.
title: How to recover from USB pipe errors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to recover from USB pipe errors


This topic provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this topic cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes.

A USB client driver communicates with its device by sending control transfers to the default endpoint; data transfers to bulk, interrupt, and isochronous endpoints of the device. At times, those transfers can fail due to various reasons, such as a stall condition in the endpoint. If the transfer fails, the associated pipe cannot process requests until the error condition is cleared.

For control transfers, the USB driver stack clears the error conditions automatically. For data transfers, the client must take appropriate steps to recover from the error condition. When a data transfer fails, the USB driver stack reports the error to the client driver through failed USBD status codes. Based on the status code, the driver can then provide an error recovery mechanism.

This topic provides guidelines about error recovery through these operations.

-   Reset the USB pipe
-   Reset the USB port to which the device is connected
-   Cycle the USB port to re-enumerate the device stack for the client driver

To clear an error condition, start with the reset-pipe operation and perform more complex operations, such as reset-port and cycle-port, only if it is necessary.

<em>***About coordinating various recovery mechanisms</em>*:  **

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>The client driver must coordinate the different operations for recovery and ensure that only one method is used at a given time. For example, consider a device with two endpoints: a bulk and an interrupt. After sending a few data transfer requests to the device, the driver notices that requests fail on the bulk pipe. To recover from those errors, the driver resets the bulk pipe. However, that operation does not resolve the transfer errors and bulk transfers continue to fail. Therefore, the driver issues a request to reset the USB port. Meanwhile, the transfers start to fail on the interrupt pipe, and subsequently a reset-device request. To recover from the interrupt transfer failures, the driver issues a reset-pipe request on the interrupt pipe. If those two operations are not coordinated, the driver can start two reset-device operations simultaneously, due to failures on both pipes. Those simultaneous operations can be problematic.</p>
<p>The client driver must make sure that at a given time, the driver performs only one reset-port or cycle-port operation. During those operations, a reset-pipe operation should not be in progress on any pipe and the driver must not issue a new reset-pipe request.</p>
<p><em>Pankaj Gupta, Microsoft Windows USB Core Team</em></p></td>
</tr>
</tbody>
</table>

 

## What you need to know


### Technologies

-   [Kernel-Mode Driver Framework](https://docs.microsoft.com/windows-hardware/drivers/wdf/)

### Prerequisites

-   The client driver must have created the framework USB target device object.

    If you are using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code performs those tasks. The template code obtains the handle to the target device object and stores in the device context.

    A KMDF client driver must obtain a WDFUSBDEVICE handle by calling the [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) method. For more information, see "Device source code" in [Understanding the USB client driver code structure (KMDF)](understanding-the-kmdf-template-code-for-usb.md).

-   The client driver must have a handle to the framework target pipe object. For more information, see [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

Instructions
------------

### <a href="" id="determine-the-cause-of-the-error-condition"></a>Step 1: Determine the cause of the error condition

The client driver initiates a data transfer by using a USB Request Block (URB). After the request completes, the USB driver stack returns a USBD status code that indicates whether the transfer was successful or it failed. In a failure, the USBD code indicates the reason for failure.

-   If you submitted URB by calling the [**WdfUsbTargetDeviceSendUrbSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550105) method, check the **Hdr.Status** member of the [**URB**](https://msdn.microsoft.com/library/windows/hardware/ff538923) structure after the method returns.
-   If you submitted the URB asynchronously by calling the [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) method, check the URB status in the [*EVT_WDF_REQUEST_COMPLETION_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff540745). The *Params* parameter points to a [**WDF\_REQUEST\_COMPLETION\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552454) structure. To check the USBD status code, inspect the **Usb-&gt;UsbdStatus** member. For information about the code, see [USBD\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff539136).

Transfer failures can result from a device error, such as USBD\_STATUS\_STALL\_PID or USBD\_STATUS\_BABBLE\_DETECTED. They can also result due to an error reported by the host controller, such as USBD\_STATUS\_XACT\_ERROR.

### <a href="" id="determine-whether-the-device-is-connected-to-the-port"></a>Step 2: Determine whether the device is connected to the port

Before issuing any request that resets the pipe or the device, make sure that the device is connected. You can determine the connected state of the device by calling the [**WdfUsbTargetDeviceIsConnectedSynchronous**](https://msdn.microsoft.com/library/windows/hardware/ff550095) method.

### <a href="" id="cancel-all-pending-transfers-to-the-pipe"></a>Step 3: Cancel all pending transfers to the pipe

Before sending any requests that reset the pipe or port, cancel all pending transfer requests to the pipe, which the USB driver stack has not yet completed. You can cancel requests in one of these ways:

-   Stop the I/O target by calling the [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) method.

    To stop the I/O target, first, get the WDFIOTARGET handle associated with the framework pipe object by calling the [**WdfUsbTargetPipeGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff551146) method. By using the handle, call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680). In the call, set the action to **WdfIoTargetCancelSentIo** (see [**WDF\_IO\_TARGET\_SENT\_IO\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff552388)) to instruct the framework to cancel all requests that the USB driver stack has not completed. For requests that have been completed, the client driver must wait for its completion callback to get invoked by the framework.

-   Send an abort-pipe request. You can send the request by calling one of these methods:
    -   Call the [**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129) method.

        The call is synchronous and returns only after all pending requests are canceled. [**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129) takes an optional *Request* parameter. We recommend that you pass a WDFREQUEST handle to a preallocated framework request object. The parameter enables the framework of use the specified request object instead of an internal request object that the driver cannot access. This parameter value ensures that **WdfUsbTargetPipeAbortSynchronously** does not fail due to insufficient memory.

    -   Call the [**WdfUsbTargetPipeFormatRequestForAbort**](https://msdn.microsoft.com/library/windows/hardware/ff551132) method to format a request object for an abort-pipe request, and then send the request by calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) method.

        If the driver sends the request asynchronously, then it must specify a pointer to the driver's [*EVT_WDF_REQUEST_COMPLETION_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff540745) that the driver implements. To specify the pointer, call the [**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030) method.

        The driver can send the request synchronously by specifying WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS as one of the request options in [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027). If you send the request synchronously, then call [**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129) instead.

### <a href="" id="reset-the-usb-pipe"></a>Step 4: Reset the USB pipe

Start the error recovery by resetting the pipe. You can send a reset-pipe request by calling one of these methods:

-   Call the [**WdfUsbTargetPipeResetSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551156) to send a reset pipe request synchronously.
-   Call the [**WdfUsbTargetPipeFormatRequestForReset**](https://msdn.microsoft.com/library/windows/hardware/ff551138) method to format a request object for a reset-pipe request, and then send the request by calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) method. Those calls are similar to the ones for the abort-pipe request, as described in step 3.

**Note**  Do not send any new transfer requests until the reset-pipe operation is complete.

 

The reset-pipe request clears the error condition in the device and the host controller hardware. To clear the device error, the USB driver stack sends a CLEAR\_FEATURE control request to the device by using the ENDPOINT\_HALT feature selector. The recipient for the request is the endpoint that is associated with the pipe. If the error condition occurred on an isochronous pipe, then the driver stack takes no action to clear the device because, in case of errors, isochronous endpoints are cleared automatically.

To clear the host controller error, the driver stack clears the HALT state of the pipe and resets the data toggle of the pipe to 0.

### <a href="" id="reset-the-usb-port"></a>Step 5: Reset the USB port

If a reset-pipe operation does not clear the error condition and data transfers continue to fail, send a reset-port request.

1.  Cancel all transfers to the device. To do so, enumerate all pipes in the current configuration and cancel pending requests scheduled for each pipe.
2.  Stop the I/O target for the device.

    Call the [**WdfUsbTargetDeviceGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff550093) method to get a WDFIOTARGET handle associated with the framework target device object. Then, call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) and specify the WDFIOTARGET handle. In call, set the action to **WdfIoTargetCancelSentIo** (WDF\_IO\_TARGET\_SENT\_IO\_ACTION).

3.  Send a reset-port request by calling the [**WdfUsbTargetDeviceResetPortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550097) method.

A reset-port operation causes the device to get re-enumerated on the USB bus. The USB driver stack preserves the device configuration after the enumeration. The client driver can use the previously obtained pipe handles because the driver stack ensures that existing pipe handles remain valid.

You cannot reset an individual function of a composite device. For a composite device, when the client driver of a particular function sends a reset-port request, the entire device is reset. If the USB device maintains state, that reset-port request can affect the client drivers of other functions. Therefore, it's important that the client driver attempts to reset the pipe before resetting the port.

### <a href="" id="cycle-the-usb-port"></a>Step 6: Cycle the USB port

A cycle-port operation is similar to the device that is unplugged and plugged back to the port, except the device is not disconnected electrically. The device is disconnected and reconnected in software. This operation leads to device reset and enumeration. As a result, the PnP Manager rebuilds the device node.

If a reset-port operation does not clear the error condition and data transfers continue to fail, send a cycle-port request.

1.  Cancel all transfers to the device. Make sure that you cancel pending request scheduled for each pipe in the current configuration (see step 3).
2.  Stop the I/O target for the device.

    Call the [**WdfUsbTargetDeviceGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff550093) method to get a WDFIOTARGET handle associated with the framework target device object. Then, call [**WdfIoTargetStop**](https://msdn.microsoft.com/library/windows/hardware/ff548680) and specify the WDFIOTARGET handle. In call, set the action to **WdfIoTargetCancelSentIo** (WDF\_IO\_TARGET\_SENT\_IO\_ACTION).

3.  Send a cycle-port request by calling one of these methods:
    -   Call the [**WdfUsbTargetDeviceCyclePortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550080) to send a cycle-port request synchronously.
    -   Call the [**WdfUsbTargetDeviceFormatRequestForCyclePort**](https://msdn.microsoft.com/library/windows/hardware/ff550084) method to format a request object for a cycle-port request, and then send the request by calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) method. Those calls are similar to the ones for the abort-pipe request, as described in step 3.

The client driver can send transfer requests to the device only after the cycle-port request has completed. That is because the device node gets removed while the USB driver stack processes the cycle-port request.

The cycle-port request causes the device to get re-enumerated. The USB driver stack informs the PnP Manager that the device has been disconnected. The PnP Manager tears down device stack associated with the client driver. The driver stack resets the device, re-enumerates it on the USB bus, and informs the PnP Manager that a device has been connected. PnP Manager then rebuilds the device stack for the USB device.

As a result of cycle port operation, any application that has a handle open to the device gets a device removal notification (if the application registered for such a notification). In response, the application might report a device-disconnected message to the user. Because it impacts user experience, the client driver should opt for a cycle-port request only if other recovery mechanisms do not resolve the error condition.

Similar to the reset-port operation (described in step 6), for a composite device, cycle-port operation affects the entire device and not individual functions of the device.

## Related topics
[USB I/O Transfers](usb-device-i-o.md)  



