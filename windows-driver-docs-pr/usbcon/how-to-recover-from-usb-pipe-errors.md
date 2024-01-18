---
title: How to Recover From USB Pipe Errors
description: This article provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this article cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes.
ms.date: 01/16/2024
ms.custom: contperf-fy21q3
---

# How to recover from USB pipe errors

> [!NOTE]
> This article is for device driver developers. If you're experiencing difficulty with a USB device, please see [Troubleshoot common USB problems](https://support.microsoft.com/windows/troubleshoot-common-usb-problems-5e9a9b49-ad43-702e-083e-6107e95deb88)

This article provides information about steps you can try when a data transfer to a USB pipe fails. The mechanisms described in this article cover abort, reset, and cycle port operations on bulk, interrupt, and isochronous pipes.

A USB client driver communicates with its device by sending control transfers to the default endpoint; data transfers to bulk, interrupt, and isochronous endpoints of the device. At times, those transfers can fail due to various reasons, such as a stall condition in the endpoint. If the transfer fails, the associated pipe can't process requests until the error condition is cleared.

For control transfers, the USB driver stack clears the error conditions automatically. For data transfers, the client must take appropriate steps to recover from the error condition. When a data transfer fails, the USB driver stack reports the error to the client driver through failed USBD status codes. Based on the status code, the driver can then provide an error recovery mechanism.

This article provides guidelines about error recovery through these operations.

- Reset the USB pipe
- Reset the USB port to which the device is connected
- Cycle the USB port to re-enumerate the device stack for the client driver

To clear an error condition, start with the reset-pipe operation and perform more complex operations, such as reset-port and cycle-port, only if it's necessary.

***About coordinating various recovery mechanisms:***

The client driver must coordinate the different operations for recovery and ensure that only one method is used at a given time. For example, consider a device with two endpoints: a bulk and an interrupt. After sending a few data transfer requests to the device, the driver notices that requests fail on the bulk pipe. To recover from those errors, the driver resets the bulk pipe. However, that operation doesn't resolve the transfer errors and bulk transfers continue to fail. Therefore, the driver issues a request to reset the USB port. Meanwhile, the transfers start to fail on the interrupt pipe, and then a reset-device request. To recover from the interrupt transfer failures, the driver issues a reset-pipe request on the interrupt pipe. If those two operations aren't coordinated, the driver can start two reset-device operations simultaneously, due to failures on both pipes. Those simultaneous operations can be problematic.

The client driver must make sure that at a given time, the driver performs only one reset-port or cycle-port operation. During those operations, a reset-pipe operation shouldn't be in progress on any pipe and the driver must not issue a new reset-pipe request.

## What you need to know

This article uses the [Kernel-Mode Driver Framework (KMDF)](../wdf/index.md).

### Prerequisites

- The client driver must have created the framework USB target device object.

    If you're using the USB templates that are provided with Microsoft Visual Studio Professional 2012, the template code performs those tasks. The template code obtains the handle to the target device object and stores in the device context.

    A KMDF client driver must obtain a WDFUSBDEVICE handle by calling the **[WdfUsbTargetDeviceCreateWithParameters](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)** method. For more information, see "Device source code" in [Understanding the USB client driver code structure (KMDF)](understanding-the-kmdf-template-code-for-usb.md).

- The client driver must have a handle to the framework target pipe object. For more information, see [How to enumerate USB pipes](how-to-get-usb-pipe-handles.md).

## Step 1: Determine the cause of the error condition

The client driver initiates a data transfer by using a USB Request Block (URB). After the request completes, the USB driver stack returns a USBD status code that indicates whether the transfer was successful or it failed. In a failure, the USBD code indicates the reason for failure.

- If you submitted URB by calling the **[WdfUsbTargetDeviceSendUrbSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicesendurbsynchronously)** method, check the **Hdr.Status** member of the **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure after the method returns.
- If you submitted the URB asynchronously by calling the **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** method, check the URB status in the *[EVT_WDF_REQUEST_COMPLETION_ROUTINE](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine)*. The *Params* parameter points to a **[WDF_REQUEST_COMPLETION_PARAMS](/windows-hardware/drivers/ddi/wdfrequest/ns-wdfrequest-_wdf_request_completion_params)** structure. To check the USBD status code, inspect the **Usb-&gt;UsbdStatus** member. For information about the code, see [USBD_STATUS](/previous-versions/windows/hardware/drivers/ff539136(v=vs.85)).

Transfer failures can result from a device error, such as USBD_STATUS_STALL_PID or USBD_STATUS_BABBLE_DETECTED. They can also result due to an error reported by the host controller, such as USBD_STATUS_XACT_ERROR.

## Step 2: Determine whether the device is connected to the port

Before issuing any request that resets the pipe or the device, make sure that the device is connected. You can determine the connected state of the device by calling the **[WdfUsbTargetDeviceIsConnectedSynchronous](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceisconnectedsynchronous)** method.

## Step 3: Cancel all pending transfers to the pipe

Before sending any requests that reset the pipe or port, cancel all pending transfer requests to the pipe, which the USB driver stack hasn't yet completed. You can cancel requests in one of these ways:

- Stop the I/O target by calling the **[WdfIoTargetStop](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop)** method.

    To stop the I/O target, first, get the WDFIOTARGET handle associated with the framework pipe object by calling the **[WdfUsbTargetPipeGetIoTarget](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipegetiotarget)** method. By using the handle, call **[WdfIoTargetStop](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop)**. In the call, set the action to **WdfIoTargetCancelSentIo** (see **[WDF_IO_TARGET_SENT_IO_ACTION](/windows-hardware/drivers/ddi/wdfiotarget/ne-wdfiotarget-_wdf_io_target_sent_io_action)**)** to instruct the framework to cancel all requests that the USB driver stack hasn't completed. For requests that have been completed, the client driver must wait for its completion callback to get invoked by the framework.

- Send an abort-pipe request. You can send the request by calling one of these methods:

  - Call the **[WdfUsbTargetPipeAbortSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeabortsynchronously)** method.

    The call is synchronous and returns only after all pending requests are canceled. **[WdfUsbTargetPipeAbortSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeabortsynchronously)** takes an optional *Request* parameter. We recommend that you pass a WDFREQUEST handle to a preallocated framework request object. The parameter enables the framework of use the specified request object instead of an internal request object that the driver can't access. This parameter value ensures that **WdfUsbTargetPipeAbortSynchronously** doesn't fail due to insufficient memory.

  - Call the **[WdfUsbTargetPipeFormatRequestForAbort](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforabort)** method to format a request object for an abort-pipe request, and then send the request by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** method.

    If the driver sends the request asynchronously, then it must specify a pointer to the driver's *[EVT_WDF_REQUEST_COMPLETION_ROUTINE](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine)* that the driver implements. To specify the pointer, call the **[WdfRequestSetCompletionRoutine](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetcompletionroutine)** method.

    The driver can send the request synchronously by specifying WDF_REQUEST_SEND_OPTION_SYNCHRONOUS as one of the request options in **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)**. If you send the request synchronously, then call **[WdfUsbTargetPipeAbortSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeabortsynchronously)** instead.

## Step 4: Reset the USB pipe

Start the error recovery by resetting the pipe. You can send a reset-pipe request by calling one of these methods:

- Call the **[WdfUsbTargetPipeResetSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpiperesetsynchronously)** to send a reset pipe request synchronously.

- Call the **[WdfUsbTargetPipeFormatRequestForReset](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeformatrequestforreset)** method to format a request object for a reset-pipe request, and then send the request by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** method. Those calls are similar to the ones for the abort-pipe request, as described in step 3.

> [!NOTE]
> Do not send any new transfer requests until the reset-pipe operation is complete.

The reset-pipe request clears the error condition in the device and the host controller hardware. To clear the device error, the USB driver stack sends a CLEAR_FEATURE control request to the device by using the ENDPOINT_HALT feature selector. The recipient for the request is the endpoint that is associated with the pipe. If the error condition occurred on an isochronous pipe, then the driver stack takes no action to clear the device because, in case of errors, isochronous endpoints are cleared automatically.

To clear the host controller error, the driver stack clears the HALT state of the pipe and resets the data toggle of the pipe to 0.

## Step 5: Reset the USB port

If a reset-pipe operation doesn't clear the error condition and data transfers continue to fail, send a reset-port request.

1. Cancel all transfers to the device. To do so, enumerate all pipes in the current configuration and cancel pending requests scheduled for each pipe.

1. Stop the I/O target for the device.

    Call the **[WdfUsbTargetDeviceGetIoTarget](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetiotarget)** method to get a WDFIOTARGET handle associated with the framework target device object. Then, call **[WdfIoTargetStop](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop)** and specify the WDFIOTARGET handle. In call, set the action to **WdfIoTargetCancelSentIo** (WDF_IO_TARGET_SENT_IO_ACTION).

1. Send a reset-port request by calling the **[WdfUsbTargetDeviceResetPortSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceresetportsynchronously)** method.

A reset-port operation causes the device to get re-enumerated on the USB bus. The USB driver stack preserves the device configuration after the enumeration. The client driver can use the previously obtained pipe handles because the driver stack ensures that existing pipe handles remain valid.

You can't reset an individual function of a composite device. For a composite device, when the client driver of a particular function sends a reset-port request, the entire device is reset. If the USB device maintains state, that reset-port request can affect the client drivers of other functions. Therefore, it's important that the client driver attempts to reset the pipe before resetting the port.

## Step 6: Cycle the USB port

A cycle-port operation is similar to the device that is unplugged and plugged back to the port, except the device isn't disconnected electrically. The device is disconnected and reconnected in software. This operation leads to device reset and enumeration. As a result, the PnP Manager rebuilds the device node.

If a reset-port operation doesn't clear the error condition and data transfers continue to fail, send a cycle-port request.

1. Cancel all transfers to the device. Make sure that you cancel pending request scheduled for each pipe in the current configuration (see step 3).

1. Stop the I/O target for the device.

    Call the **[WdfUsbTargetDeviceGetIoTarget](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicegetiotarget)** method to get a WDFIOTARGET handle associated with the framework target device object. Then, call **[WdfIoTargetStop](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop)** and specify the WDFIOTARGET handle. In call, set the action to **WdfIoTargetCancelSentIo** (WDF_IO_TARGET_SENT_IO_ACTION).

1. Send a cycle-port request by calling one of these methods:
    - Call the **[WdfUsbTargetDeviceCyclePortSynchronously](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecycleportsynchronously)** to send a cycle-port request synchronously.
    - Call the **[WdfUsbTargetDeviceFormatRequestForCyclePort](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceformatrequestforcycleport)** method to format a request object for a cycle-port request, and then send the request by calling **[WdfRequestSend](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)** method. Those calls are similar to the ones for the abort-pipe request, as described in step 3.

The client driver can send transfer requests to the device only after the cycle-port request has completed. That is because the device node gets removed while the USB driver stack processes the cycle-port request.

The cycle-port request causes the device to get re-enumerated. The USB driver stack informs the PnP Manager that the device has been disconnected. The PnP Manager tears down device stack associated with the client driver. The driver stack resets the device, re-enumerates it on the USB bus, and informs the PnP Manager that a device has been connected. PnP Manager then rebuilds the device stack for the USB device.

As a result of cycle port operation, any application that has a handle open to the device gets a device removal notification (if the application registered for such a notification). In response, the application might report a device-disconnected message to the user. Because it impacts user experience, the client driver should opt for a cycle-port request only if other recovery mechanisms don't resolve the error condition.

Similar to the reset-port operation (described in step 6), for a composite device, cycle-port operation affects the entire device and not individual functions of the device.

## Related topics

- [Kernel-Mode Driver Framework](../wdf/index.md)
- [USB I/O Transfers](usb-device-i-o.md)
