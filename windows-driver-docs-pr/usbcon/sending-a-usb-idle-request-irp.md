---
Description: 'When a device goes idle, the client driver informs the bus driver by sending an idle request IRP (IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION).'
MS-HAID:
- 'usbpower\_ed24b6c4-8cfd-48de-89d3-258940b1cad8.xml'
- 'buses.sending\_a\_usb\_idle\_request\_irp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Sending a USB Idle Request IRP
author: windows-driver-content
---

# Sending a USB Idle Request IRP


When a device goes idle, the client driver informs the bus driver by sending an idle request IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)). After the bus driver determines that it is safe to put the device in a low power state, it calls the callback routine that the client device driver passed down the stack with the idle request IRP.

In the callback routine, the client driver must cancel all pending I/O operations and wait for all USB I/O IRPs to complete. It then can issue an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request to change the WDM device power state to **D2**. The callback routine must wait for the **D2** request to complete before returning. For more information about the idle notification callback routine, see [USB Idle Notification Callback Routine](usb-idle-notification-callback-routine.md).

The bus driver does not complete the idle request IRP after calling the idle notification callback routine. Instead, the bus driver holds the idle request IRP pending until one of the following conditions is true:

-   An **IRP\_MN\_SUPRISE\_REMOVAL** or **IRP\_MN\_REMOVE\_DEVICE IRP** is received. When one of these IRPs is received the idle request IRP completes with STATUS\_CANCELLED.
-   The bus driver receives a request to put the device into a working power state (**D0**). Upon receiving this request bus driver completes the pending idle request IRP with STATUS\_SUCCESS.

The following restrictions apply to the use of idle request IRPs:

-   Drivers must be in device power state **D0** when sending an idle request IRP.
-   Drivers must send just one idle request IRP per device stack.

The following WDM example code illustrates the steps that a device driver takes to send a USB idle request IRP. Error checking has been omitted in the following code example.

1.  Allocate and initialize the [**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270) IRP
    ```
    irp = IoAllocateIrp (DeviceContext->TopOfStackDeviceObject->StackSize, FALSE);
    nextStack = IoGetNextIrpStackLocation (irp);
    nextStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
    nextStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION;
    nextStack->Parameters.DeviceIoControl.InputBufferLength =
    sizeof(struct _USB_IDLE_CALLBACK_INFO);
    ```

2.  Allocate and initialize the idle request information structure (USB\_IDLE\_CALLBACK\_INFO).
    ```
    idleCallbackInfo = ExAllocatePool (NonPagedPool,
    sizeof(struct _USB_IDLE_CALLBACK_INFO));
    idleCallbackInfo->IdleCallback = IdleNotificationCallback;
    // Put a pointer to the device extension in member IdleContext
    idleCallbackInfo->IdleContext = (PVOID) DeviceExtension;  
    nextStack->Parameters.DeviceIoControl.Type3InputBuffer =
    idleCallbackInfo;
    ```

3.  Set a completion routine.

    The client driver must associate a completion routine with the idle request IRP. For more information about the idle notification completion routine and example code, see [USB Idle Request IRP Completion Routine](usb-idle-request-irp-completion-routine.md).

    ```
    IoSetCompletionRoutine (irp,
     IdleNotificationRequestComplete,
       DeviceContext,
       TRUE,
       TRUE,
       TRUE);
     
    ```

4.  Store the idle request in the device extension.
    ```
    deviceExtension->PendingIdleIrp = irp;
     
    ```

5.  Send the Idle request to the parent driver.
    ```
    ntStatus = IoCallDriver (DeviceContext->TopOfStackDeviceObject, irp);
    ```

## Related topics
[USB Selective Suspend](usb-selective-suspend.md)  
[USB Power Management](usb-power-management.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Sending%20a%20USB%20Idle%20Request%20IRP%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


