---
title: USB Selective Suspend
description: This article provides information about choosing the correct mechanism for the selective suspend feature.
ms.date: 05/01/2025
ai-usage: ai-assisted
---

# USB selective suspend

> [!NOTE]
> This article is for device driver developers. If you're experiencing difficulty with a USB device, see [Fix USB-C problems in Windows](https://support.microsoft.com/windows/fix-usb-c-problems-in-windows-f4e0e529-74f5-cdae-3194-43743f30eed2)

The USB selective suspend feature allows the hub driver to suspend an individual port without affecting the operation of the other ports on the hub. This functionality is particularly useful in portable computers as it helps conserve battery power. Many devices, such as biometric scanners, only require power intermittently. Suspending such devices, when they aren't in use, reduces overall power consumption. More importantly, any device that isn't selectively suspended might prevent the USB host controller from disabling its transfer schedule, which resides in system memory. Direct memory access (DMA) transfers by the host controller to the scheduler can prevent the system's processors from entering deeper sleep states, such as C3.

To selectively suspend a USB device, two different mechanisms exist: idle request IRPs (**[IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)**) and set power IRPs (**[IRP_MN_SET_POWER](../kernel/irp-mn-set-power.md)**). The mechanism to use depends on the type of device: composite or noncomposite.

## Selecting a selective suspend mechanism

Client drivers for an interface on a composite device, that enable the interface for remote wake-up with a wait wake IRP (IRP_MN_WAIT_WAKE), must use the idle request IRP (**[IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)**) mechanism to selectively suspend a device.

For information about remote wake-up, see:

- [Remote wake-up of USB devices](./remote-wakeup-of-usb-devices.md)
- [Overview of wait/wake operation](../kernel/overview-of-wait-wake-operation.md)

In Windows 10 and later versions, driver writers have more choices for powering down devices. Although these versions support the Windows idle request IRP mechanism, drivers aren't required to use it.

This section explains the Windows selective suspend mechanism.

## Sending a USB idle request IRP

When a device goes idle, the client driver informs the bus driver by sending an idle request IRP (**[IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)**). After the bus driver determines that it's safe to put the device in a low power state, it calls the callback routine that the client device driver passed down the stack with the idle request IRP.

In the callback routine, the client driver must cancel all pending I/O operations and wait for all USB I/O IRPs to complete. It then can issue an **[IRP_MN_SET_POWER](../kernel/irp-mn-set-power.md)** request to change the WDM device power state to **D2**. The callback routine must wait for the **D2** request to complete before returning. For more information about the idle notification callback routine, see [Implementing a USB Idle Request IRP Callback Routine](../network/implementing-a-usb-idle-request-irp-callback-routine.md).

The bus driver doesn't complete the idle request IRP after calling the idle notification callback routine. Instead, the bus driver holds the idle request IRP pending until one of the following conditions is true:

- An **IRP_MN_SUPRISE_REMOVAL** or **IRP_MN_REMOVE_DEVICE IRP** is received. When one of these IRPs isreceived, the idle request IRP completes with STATUS_CANCELLED.
- The bus driver receives a request to put the device into a working power state (**D0**). Upon receiving this request, the bus driver completes the pending idle request IRP with STATUS_SUCCESS.

The following restrictions apply to the use of idle request IRPs:

- Drivers must be in device power state **D0** when sending an idle request IRP.
- Drivers must send just one idle request IRP per device stack.

The following WDM example code illustrates the steps that a device driver takes to send a USB idle request IRP. Error checking is omitted in the following code example.

1. Allocate and initialize the **[IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION](/windows-hardware/drivers/ddi/usbioctl/ni-usbioctl-ioctl_internal_usb_submit_idle_notification)** IRP

    ```cpp
    irp = IoAllocateIrp (DeviceContext->TopOfStackDeviceObject->StackSize, FALSE);
    nextStack = IoGetNextIrpStackLocation (irp);
    nextStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
    nextStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION;
    nextStack->Parameters.DeviceIoControl.InputBufferLength =
    sizeof(struct _USB_IDLE_CALLBACK_INFO);
    ```

1. Allocate and initialize the idle request information structure (USB_IDLE_CALLBACK_INFO).

    ```cpp
    idleCallbackInfo = ExAllocatePool (NonPagedPool,
    sizeof(struct _USB_IDLE_CALLBACK_INFO));
    idleCallbackInfo->IdleCallback = IdleNotificationCallback;
    // Put a pointer to the device extension in member IdleContext
    idleCallbackInfo->IdleContext = (PVOID) DeviceExtension;
    nextStack->Parameters.DeviceIoControl.Type3InputBuffer = idleCallbackInfo;
    ```

1. Set a completion routine.

    The client driver must associate a completion routine with the idle request IRP. For more information about the idle notification completion routine and example code, see [Implementing a USB Idle Request IRP Completion Routine](../network/implementing-a-usb-idle-request-irp-completion-routine.md).

    ```cpp
    IoSetCompletionRoutine (irp,
        IdleNotificationRequestComplete,
        DeviceContext,
        TRUE,
        TRUE,
        TRUE);
    ```

1. Store the idle request in the device extension.

    ```cpp
    deviceExtension->PendingIdleIrp = irp;
    ```

1. Send the Idle request to the parent driver.

    ```cpp
    ntStatus = IoCallDriver (DeviceContext->TopOfStackDeviceObject, irp);
    ```

## Canceling a USB idle request

Under certain circumstances, a device driver might need to cancel an idle request IRP submitted to the bus driver. This situation might occur if the device is removed, becomes active after being idle and sending the idle request, or if the entire system is transitioning to a lower system power state.

The client driver cancels the idle IRP by calling **[IoCancelIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp)**. The following table describes three scenarios for canceling an idle IRP and specifies the action the driver must take:

| Scenario | Idle request cancellation mechanism |
|---|---|
| The client driver cancels the idle IRP and the USB idle notification callback routine hasn't been called. | The USB driver stack completes the idle IRP. Because the device never left the **D0**, the driver doesn't change the device state. |
| The client driver cancels the idle IRP, the USB driver stack calls the USB idle notification callback routine, and it hasn't yet returned. | It's possible that the USB idle notification callback routine is invoked even though the client driver has invoked cancellation on the IRP. In this case, the client driver's callback routine must still power down the device by sending the device to a lower power state synchronously.<br><br>When the device is in the lower power state, the client driver can then send a **D0** request.<br><br>Alternatively, the driver can wait for the USB driver stack to complete the idle IRP and then send the **D0** IRP.<br><br>If the callback routine is unable to put the device into a low power state due to insufficient memory to allocate a power IRP, it should cancel the idle IRP and exit immediately. The idle IRP isn't completed until the callback routine returns. Therefore, the callback routine shouldn't block waiting for the canceled idle IRP to complete. |
| The device is already in a low power state. | If the device is already in a low power state, the client driver can send a **D0** IRP. The USB driver stack completes the idle request IRP with STATUS_SUCCESS.<br><br>Alternatively, the driver can cancel the idle IRP, wait for the USB driver stack to complete the idle IRP, and then send a **D0** IRP. |

## USB idle request IRP completion routine

In many cases, a bus driver might call a driver's idle request IRP completion routine. If this situation occurs, a client driver must detect why the bus driver completed the IRP. The returned status code can provide this information. If the status code isn't STATUS_POWER_STATE_INVALID, the driver should put its device in **D0** if the device isn't already in **D0**. If the device is still idle, the driver can submit another idle request IRP.

> [!NOTE]
> The idle request IRP completion routine shouldn't block waiting for a **D0** power request to complete. The completion routine can be called in the context of a power IRP by the hub driver, and blocking on another power IRP in the completion routine can lead to a deadlock.

The following list indicates how a completion routine for an idle request should interpret some common status codes:

| Status Code | Description |
|---|---|
| STATUS_SUCCESS | Indicates that the device should no longer be suspended. However, drivers should verify that their devices are powered, and put them in **D0** if they aren't already in **D0**. |
| STATUS_CANCELLED | The bus driver completes the idle request IRP with STATUS_CANCELLED in any of the following circumstances:<ul><li>The device driver canceled the IRP.</li><li>A system power state change is required.</li></ul> |
| STATUS_POWER_STATE_INVALID | Indicates that the device driver requested a **D3** power state for its device. When this occurs, the bus driver completes all pending idle IRPs with STATUS_POWER_STATE_INVALID. |
| STATUS_DEVICE_BUSY | Indicates that the bus driver already holds an idle request IRP pending for the device. Only one idle IRP can be pending at a time for a given device. Submitting multiple idle request IRPs is an error on the part of the power policy owner. The driver writer addresses the error. |

The following code example shows a sample implementation for the idle request completion routine.

```cpp
/*
Routine Description:
  Completion routine for idle notification IRP

Arguments:
    DeviceObject - pointer to device object
    Irp - I/O request packet
    DeviceExtension - pointer to device extension

Return Value:
    NT status value
--*/

NTSTATUS
IdleNotificationRequestComplete(
    IN PDEVICE_OBJECT DeviceObject,
    IN PIRP Irp,
    IN PDEVICE_EXTENSION DeviceExtension
    )
{
    NTSTATUS                ntStatus;
    POWER_STATE             powerState;
    PUSB_IDLE_CALLBACK_INFO idleCallbackInfo;

    ntStatus = Irp->IoStatus.Status;

    if(!NT_SUCCESS(ntStatus) && ntStatus != STATUS_NOT_SUPPORTED)
    {

        //Idle IRP completes with error.
        switch(ntStatus)
        {
        case STATUS_INVALID_DEVICE_REQUEST:
            //Invalid request.
            break;

        case STATUS_CANCELLED:
            //1. The device driver canceled the IRP.
            //2. A system power state change is required.
            break;

        case STATUS_POWER_STATE_INVALID:
            // Device driver requested a D3 power state for its device
            // Release the allocated resources.
            goto IdleNotificationRequestComplete_Exit;

        case STATUS_DEVICE_BUSY:
            //The bus driver already holds an idle IRP pending for the device.
            break;

        default:
            break;
        }

        // If IRP completes with error, issue a SetD0
        //Increment the I/O count because
        //a new IRP is dispatched for the driver.
        //This call is not shown.
        powerState.DeviceState = PowerDeviceD0;

        // Issue a new IRP
        PoRequestPowerIrp (
            DeviceExtension->PhysicalDeviceObject,
            IRP_MN_SET_POWER,
            powerState,
            (PREQUEST_POWER_COMPLETE) PoIrpCompletionFunc,
            DeviceExtension,
            NULL);
    }

IdleNotificationRequestComplete_Exit:

    idleCallbackInfo = DeviceExtension->IdleCallbackInfo;
    DeviceExtension->IdleCallbackInfo = NULL;
    DeviceExtension->PendingIdleIrp = NULL;
    InterlockedExchange(&DeviceExtension->IdleReqPend, 0);

    if(idleCallbackInfo)
    {
        ExFreePool(idleCallbackInfo);
    }

    DeviceExtension->IdleState = IdleComplete;

    // Because the IRP was created using IoAllocateIrp,
    // the IRP needs to be released by calling IoFreeIrp.
    // Also return STATUS_MORE_PROCESSING_REQUIRED so that
    // the kernel does not reference this.
    IoFreeIrp(Irp);
    KeSetEvent(&DeviceExtension->IdleIrpCompleteEvent, IO_NO_INCREMENT, FALSE);
    return STATUS_MORE_PROCESSING_REQUIRED;
}
```

## USB idle notification callback routine

The bus driver (either an instance of the hub driver or the generic parent driver) determines when it's safe to suspend its device's children. If it is, it calls the idle notification callback routine supplied by each child's client driver.

The function prototype for USB_IDLE_CALLBACK is as follows:

```cpp
typedef VOID (*USB_IDLE_CALLBACK)(__in PVOID Context);
```

A device driver must take the following actions in its idle notification callback routine:

- Request an **[IRP_MN_WAIT_WAKE](../kernel/irp-mn-wait-wake.md)** IRP for the device if the device must be armed for remote wakeup.
- Cancel all I/O and prepare the device to go to a lower power state.
- Put the device in a WDM sleep state by calling **[PoRequestPowerIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp)** with the *PowerState* parameter set to the enumerator value PowerDeviceD2 (defined in wdm.h; ntddk.h).

Both the hub driver and the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) call the idle notification callback routine at IRQL = PASSIVE_LEVEL. The callback routine can then block while it waits for the power state change request to complete.

The callback routine is invoked only while the system is in **S0** and the device is in **D0**.

The following restrictions apply to idle request notification callback routines:

- Device drivers can initiate a device power state transition from **D0** to **D2** in the idle notification callback routine, but no other power state transition is allowed. In particular, a driver must not attempt to change its device to **D0** while executing its callback routine.
- Device drivers must not request more than one power IRP from within the idle notification callback routine.

### Arming devices for wakeup in the idle notification callback routine

The idle notification callback routine should determine whether its device has an **[IRP_MN_WAIT_WAKE](../kernel/irp-mn-wait-wake.md)** request pending. If no IRP_MN_WAIT_WAKE request is pending, the callback routine should submit an IRP_MN_WAIT_WAKE request before suspending the device. For more information about the wait wake mechanism, see [Supporting Devices That Have WakeUp Capabilities](../kernel/supporting-devices-that-have-wake-up-capabilities.md).

## USB global suspend

The USB 2.0 Specification defines global suspend as the suspension of the entire bus behind a USB host controller by ceasing all USB traffic on the bus, including start-of-frame packets. Downstream devices that aren't already suspended detect the Idle state on their upstream port and enter the suspend state on their own. Windows doesn't implement global suspend in this manner. Windows always selectively suspends each USB device behind a USB host controller before it ceases all USB traffic on the bus.

### Conditions for global suspend

Windows 10 and later versions are more aggressive about selectively suspending USB hubs. The USB hub driver selectively suspends any hub where all of its attached devices are in **D1**, **D2**, or **D3** device power state. The entire bus enters global suspend once all USB hubs are selectively suspended. The USB driver stack treats a device as Idle whenever the device is in a WDM device state of **D1**, **D2**, or **D3**.

## Enabling selective suspend

Selective suspend is enabled by default. To enable selective suspend support for a given root hub and its child devices, select the checkbox on the **Power Management** tab for the USB root hub in **Device Manager**.

Alternatively, you can enable or disable selective suspend by setting the value of **HcDisableSelectiveSuspend** under the software key of the USB port driver. A value of 1 disables selective suspend. A value of 0 enables selective suspend.

Client drivers shouldn't try to determine whether selective suspend is enabled before sending idle requests. They should submit idle requests whenever the device is idle. If the idle request fails the client driver should reset the idle timer and retry.

## Related topics

- [USB Power Management](usb-power-management.md)
