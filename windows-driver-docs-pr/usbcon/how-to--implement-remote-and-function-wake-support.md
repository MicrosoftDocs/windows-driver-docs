---
title: How to Implement Function Suspend in a Composite Driver
description: This article provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices).
ms.date: 01/16/2024
---

# How to implement function suspend in a composite driver

This article provides an overview of function suspend and function remote wake-up features for Universal Serial Bus (USB) 3.0 multi-function devices (composite devices). In this article, you'll learn about implementing those features in a driver that controls a composite device. The article applies to composite drivers that replace Usbccgp.sys.

The Universal Serial Bus (USB) 3.0 specification defines a new feature called *function suspend*. The feature enables an individual function of a composite device to enter a low-power state, independently of other functions. Consider a composite device that defines a function for keyboard and another function for mouse. The user keeps the keyboard function in working state but doesn't move the mouse for a period of time. The client driver for the mouse can detect the idle state of the function and send the function to suspend state while the keyboard function stays in working state.

The entire device can transition to suspend state regardless of the power state of any function within the device. If a particular function and the entire device enter suspend state, the suspend state of the function is retained while the device is in suspend state, and throughout the device's suspend entry and exit processes.

Similar to a USB 2.0 device's remote wake-up feature (see [Remote Wake-up of USB Devices](remote-wakeup-of-usb-devices.md)), an individual function in a USB 3.0 composite device can wake up from a low-power state without impacting the power states of other functions. This feature is called *function remote wake-up*. The feature is explicitly enabled by the host by sending a protocol request that sets the remote wake-up bits in the device's firmware. This process is called *arming the function for remote wake-up*. For information about the remote wake-related bits, see Figure 9-6 in the official USB specification.

If a function is armed for remote wake-up, the function (when in suspend state) retains enough power to generate a wake-up *resume signal* when a user event occurs on the physical device. As a result of that resume signal, the client driver can then exit the suspend state of the associated function. In the example for the mouse function in the composite device, when the user wiggles the mouse that is in idle state, the mouse function sends a resume signal to the host. On the host, the USB driver stack detects which function woke up and propagates the notification to the client driver of the corresponding function. The client driver can then wake up the function and enter working state.

For the client driver, the steps for sending a function to suspend state and waking up the function is similar to a single-function device driver sending the entire device to suspend state. The following procedure summarizes those steps.

1. Detect when the associated function is in idle state.
1. Send an idle I/O request packet (IRP).
1. Submit a request to arm its function for remote wake-up by sending a wait-wake I/O request packet (IRP).
1. Transition the function to a low power state by sending **Dx** power IRPs (**D2** or **D3**).

For more information about the preceding steps, see "Sending a USB Idle Request IRP" in [USB Selective Suspend](usb-selective-suspend.md).
A composite driver creates a physical device object (PDO) for each function in the composite device and handles power requests sent by the client driver (the FDO of the function device stack). In order for a client driver to successfully enter and exit suspend state for its function, the composite driver must support function suspend and remote wake-up features, and process the received power requests.

In Windows 8, the USB driver stack for USB 3.0 devices supports those features. In addition, function suspend and function remote wake-up implementation has been added to the Microsoft-provided [USB generic parent driver](usb-common-class-generic-parent-driver.md) (Usbccgp.sys), which is the Windows default composite driver. If you're writing a custom composite driver, your driver must handle requests related to function suspend and remote wake-up requests, as per the following procedure.

## Step 1: Determine whether the USB driver stack supports function suspend

In the start-device routine (**[IRP_MN_START_DEVICE](../kernel/irp-mn-start-device.md)**) of your composite driver, perform the following steps:

1. Call the **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)** routine to determine whether the underlying USB driver stack supports the function suspend capability. The call requires a valid USBD handle that you obtained in your previous call to the **[USBD_CreateHandle](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_createhandle)** routine.

  A successful call to **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)** determines whether the underlying USB driver stack supports function suspend. The call can return an error code indicating that the USB driver stack doesn't support function suspend or the attached device isn't a USB 3.0 multi-function device.

1. If the **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)** call indicates that function suspend is supported, register the composite device with the underlying USB driver stack. To register the composite device, you must send an **[IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_register_composite_device)** I/O control request. For more information about this request, see [How to Register a Composite Device](register-a-composite-driver.md).

  The registration request uses the **[REGISTER_COMPOSITE_DEVICE](/windows-hardware/drivers/ddi/usbdlib/ns-usbdlib-_register_composite_device)** structure to specify that information about the composite driver. Make sure you set **CapabilityFunctionSuspend** to 1 to indicate that the composite driver supports function suspend.

For code example that shows how to determine whether the USB driver stack supports function suspend, see **[USBD_QueryUsbCapability](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_queryusbcapability)**.

## Step 2: Handle the idle IRP

The client driver can send an idle IRP (see **[IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)**). The request is sent after the client driver has detected an idle state for the function. The IRP contains a pointer to callback completion routine (called *idle callback*) that is implemented by the client driver. Within the idle callback, the client performs tasks, such as canceling pending I/O transfers, just before sending the function to suspend state.

> [!NOTE]
> The idle IRP mechanism is optional for client drivers of USB 3.0 devices. However, most client drivers are written to support both USB 2.0 and USB 3.0 devices. To support USB 2.0 devices, the driver must send the idle IRP, because the composite driver relies on that IRP to track the power state of each function. If all functions are idle, the composite driver sends the entire device to suspend state.

Upon receiving the idle IRP from the client driver, the composite driver must immediately invoke the idle callback to notify the client driver that the client driver may send the function to suspend state.

## Step 3: Send a request for remote wake-up notification

The client driver can submit a request to arm its function for remote wake-up by submitting an **[IRP_MJ_POWER](../kernel/irp-mj-power.md)** IRP with minor function code set to **[IRP_MN_WAIT_WAKE](../kernel/irp-mn-wait-wake.md)** (wait-wake IRP). The client driver submits this request only if the driver wants to enter working state as a result of a user event.

Upon receiving the wait-wake IRP, the composite driver must send the **[IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_request_remote_wake_notification)** I/O control request to the USB driver stack. The request enables the USB driver stack to notify the composite driver when the stack receives the notification about the resume signal. The **IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION** uses the **[REQUEST_REMOTE_WAKE_NOTIFICATION](/windows-hardware/drivers/ddi/usbdlib/ns-usbdlib-_request_remote_wake_notification)** structure to specify the request parameters. One of the values that the composite driver must specify is the function handle for the function that is armed for remote wake-up. The composite driver obtained that handle in a previous request to register the composite device with the USB driver stack. For more information about composite driver registration requests, see [How to Register a Composite Device](register-a-composite-driver.md).

In the IRP for the request, the composite driver supplies a pointer to a (remote wake-up) completion routine, which is implemented by the composite driver.

The following example code shows how to send a remote wake-up request.

```cpp
/*++

Description:
    This routine sends a IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION request
    to the USB driver stack. The IOCTL is completed by the USB driver stack
    when the function wakes up from sleep.

    Parameters:
    parentFdoExt: The device context associated with the FDO for the
    composite driver.

    functionPdoExt: The device context associated with the PDO (created by
    the composite driver) for the client driver.
--*/

VOID
SendRequestForRemoteWakeNotification(
    __inout PPARENT_FDO_EXT parentFdoExt,
    __inout PFUNCTION_PDO_EXT functionPdoExt
)

{
    PIRP                                irp;
    REQUEST_REMOTE_WAKE_NOTIFICATION    remoteWake;
    PIO_STACK_LOCATION                  nextStack;
    NTSTATUS                            status;

    // Allocate an IRP
    irp =  IoAllocateIrp(parentFdoExt->topDevObj->StackSize, FALSE);

    if (irp)
    {

        //Initialize the USBDEVICE_REMOTE_WAKE_NOTIFICATION structure
        remoteWake.Version = 0;
        remoteWake.Size = sizeof(REQUEST_REMOTE_WAKE_NOTIFICATION);
        remoteWake.UsbdFunctionHandle = functionPdoExt->functionHandle;
        remoteWake.Interface = functionPdoExt->baseInterfaceNumber;

        nextStack = IoGetNextIrpStackLocation(irp);

        nextStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
        nextStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION;

        nextStack->Parameters.Others.Argument1 = &remoteWake;

        // Caller's completion routine will free the IRP when it completes.

        SetCompletionRoutine(functionPdoExt->debugLog,
                             parentFdoExt->fdo,
                             irp,
                             CompletionRemoteWakeNotication,
                             (PVOID)functionPdoExt,
                             TRUE, TRUE, TRUE);

        // Pass the IRP
        IoCallDriver(parentFdoExt->topDevObj, irp);

    }

    return;
}
```

The **[IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_request_remote_wake_notification)** request is completed by the USB driver stack during the wake-up process when it receives notification about the resume signal. During that time, the USB driver stack also invokes the remote wake-up completion routine.

The composite driver must keep the wait-wake IRP pending and queue it for later processing. The composite driver must complete that IRP when the driver's remote wake-up completion routine gets invoked by the USB driver stack.

## Step 4: Send a request to arm the function for remote wake-up

To send the function to a low-power state, the client driver submits an **[IRP_MN_SET_POWER](../kernel/irp-mn-set-power.md)** IRP with the request to change the Windows Driver Model (WDM) device power state to **D2** or **D3**. Typically, the client driver sends **D2** IRP if the driver sent a wait-wake IRP earlier to request remote wake-up. Otherwise, the client driver sends **D3** IRP.

Upon receiving the **D2** IRP, the composite driver must first determine whether a wait-wake IRP is pending from a previous request sent by the client driver. If that IRP is pending, the composite driver must arm the function for remote wake-up. To do so, the composite driver must send a SET_FEATURE control request to the first interface of the function, to enable the device to send a resume signal. To send the control request, allocate a **[URB](/windows-hardware/drivers/ddi/usb/ns-usb-_urb)** structure by calling the **[USBD_UrbAllocate](/windows-hardware/drivers/ddi/usbdlib/nf-usbdlib-usbd_urballocate)** routine and call the **[UsbBuildFeatureRequest](/previous-versions/ff538932(v=vs.85))** macro to format the **URB** for a SET_FEATURE request. In the call, specify URB_FUNCTION_SET_FEATURE_TO_INTERFACE as the operation code and the USB_FEATURE_FUNCTION_SUSPEND as the feature selector. In the *Index* parameter, set **Bit 1** of the most significant byte. That value is copied to the **wIndex** field in the setup packet of the transfer.

The following example shows how to send a SET_FEATURE control request.

```cpp
/*++

Routine Description:

Sends a SET_FEATURE for REMOTE_WAKEUP to the device using a standard control request.

Parameters:
parentFdoExt: The device context associated with the FDO for the
composite driver.

functionPdoExt: The device context associated with the PDO (created by
the composite driver) for the client driver.

Returns:

NTSTATUS code.

--*/
VOID
    NTSTATUS SendSetFeatureControlRequestToSuspend(
    __inout PPARENT_FDO_EXT parentFdoExt,
    __inout PFUNCTION_PDO_EXT functionPdoExt,
    )

{
    PURB                            urb
    PIRP                            irp;
    PIO_STACK_LOCATION              nextStack;
    NTSTATUS                        status;

    status = USBD_UrbAllocate(parentFdoExt->usbdHandle, &urb);

    if (!NT_SUCCESS(status))
    {
        //USBD_UrbAllocate failed.
        goto Exit;
    }

    //Format the URB structure.
    UsbBuildFeatureRequest (
        urb,
        URB_FUNCTION_SET_FEATURE_TO_INTERFACE, // Operation code
        USB_FEATURE_FUNCTION_SUSPEND,          // feature selector
        functionPdoExt->firstInterface,           // first interface of the function
        NULL);

    irp =  IoAllocateIrp(parentFdoExt->topDevObj->StackSize, FALSE);

    if (!irp)
    {
        // IoAllocateIrp failed.
        status = STATUS_INSUFFICIENT_RESOURCES;

        goto Exit;
    }

    nextStack = IoGetNextIrpStackLocation(irp);

    nextStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;

    nextStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_SUBMIT_URB;

    //  Attach the URB to the IRP.
    USBD_AssignUrbToIoStackLocation(nextStack, (PURB)urb);

    // Caller's completion routine will free the IRP when it completes.
    SetCompletionRoutine(functionPdoExt->debugLog,
        parentFdoExt->fdo,
        irp,
        CompletionForSuspendControlRequest,
        (PVOID)functionPdoExt,
        TRUE, TRUE, TRUE);


    // Pass the IRP
    IoCallDriver(parentFdoExt->topDevObj, irp);


Exit:
    if (urb)
    {
        USBD_UrbFree( parentFdoExt->usbdHandle, urb);
    }

    return status;

}
```

The composite driver then sends the **D2** IRP down to the USB driver stack. If all other functions are in suspend state, the USB driver stack suspends the port by manipulating certain port registers on the controller.

## Remarks

In the mouse function example, because the remote wake-up feature is enabled (see step 4), the mouse function generates a resume signal on the wire upstream to the host controller when the user wiggles the mouse. The controller then notifies the USB driver stack by sending a notification packet that contains information about the function that woke up. For information about the Function Wake Notification, see Figure 8-17 in the USB 3.0 specification.

Upon receiving the notification packet, the USB driver stack completes the pending **[IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_request_remote_wake_notification)** request (see step 3) and invokes the (remote wake-up) completion callback routine that was specified in the request and implemented by the composite driver. When the notification reaches the composite driver, it notifies the corresponding client driver that the function has entered working state by completing the wait-wake IRP that the client driver had sent earlier.

In the (remote wake-up) completion routine, the composite driver should queue a work item to complete the pending wait-wake IRP. For USB 3.0 devices, the composite driver wakes up only the function that sends the resume signal and leaves other functions in suspend state. Queuing the work item ensures compatibility with existing implementation for function drivers of USB 2.0 devices. For information about queuing a work item, see **[IoQueueWorkItem](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioqueueworkitem)**.

The worker thread completes the wait-wake IRP and invokes the client driver's completion routine. The completion routine then sends a **D0** IRP to enter the function in working state. Before completing the wait-wake IRP, the composite driver should call **[PoSetSystemWake](/windows-hardware/drivers/ddi/wdm/nf-wdm-posetsystemwake)** to mark the wait-wake IRP as the one that contributed to waking up the system from suspend state. The power manager logs an Event Tracing for Windows (ETW) event (viewable in the global system channel) that includes information about devices that woke up the system.

## Related topics

- [USB Power Management](usb-power-management.md)
- [USB Selective Suspend](usb-selective-suspend.md)
