---
Description: This section provides information about choosing the correct mechanism for the selective suspend feature.
title: USB Selective Suspend
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Selective Suspend


This section provides information about choosing the correct mechanism for the selective suspend feature.

In Microsoft Windows XP and later operating systems, the USB core stack supports a modified version of the "selective suspend" feature that is described in revision 2.0 of the Universal Serial Bus Specification.

The USB selective suspend feature allows the hub driver to suspend an individual port without affecting the operation of the other ports on the hub. Selective suspension of USB devices is especially useful in portable computers, since it helps conserve battery power. Many devices, such as fingerprint readers and other kinds of biometric scanners, only require power intermittently. Suspending such devices, when the device is not in use, reduces overall power consumption. More importantly, any device that is not selectively suspended may prevent the USB host controller from disabling its transfer schedule, which resides in system memory. DMA transfers by the host controller to the scheduler can prevent the system's processors from entering deeper sleep states, such as C3. The Windows selective suspend behavior is different for devices operating in Windows XP and Windows Vista and later versions of Windows.

There are two different mechanisms for selectively suspending a USB device: idle request IRPs ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) and set power IRPs ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)). The mechanism to use depends on the operating system and the type of device: composite or non-composite.

##  Selecting a Selective Suspend Mechanism


Client drivers, for an interface on a composite device, that enable the interface for remote wakeup with a wait wake IRP (IRP\_MN\_WAIT\_WAKE), must use the idle request IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) mechanism to selectively suspend a device.

For information about remote wakeup, see:

[Remote Wakeup of USB Devices](https://docs.microsoft.com/windows-hardware/drivers/usbcon/remote-wakeup-of-usb-devices)

[Overview of Wait/Wake Operation](https://docs.microsoft.com/windows-hardware/drivers/kernel/overview-of-wait-wake-operation)

The version of the Windows operating system determines the way drivers for non-composite devices enable selective suspend.

-   Windows XP: On Windows XP all client drivers must use idle request IRPs ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)) to power down their devices. Client drivers must not use WDM power IRPs to selectively suspend their devices. Doing so will prevent other devices from selectively suspending. See "USB Global Suspend"  for more information.
-   Windows Vista and later versions of Windows: Driver writers have more choices for powering down devices in Windows Vista and in the later versions of Windows. Although Windows Vista supports the Windows idle request IRP mechanism, drivers are not required to use it.

The following table shows the scenarios that require the use of the idle request IRP and the ones that can use a WDM power IRP to suspend a USB device:

| Windows Version     | Function on Composite Device, Armed for Wake | Function on Composite Device, Not Armed for Wake | Single Interface USB Device |
|---------------------|----------------------------------------------|--------------------------------------------------|-----------------------------|
| Windows 7           | Must use idle request IRP                    | Can use WDM Power IRP                            | Can use WDM Power IRP       |
| Windows Server 2008 | Must use idle request IRP                    | Can use WDM Power IRP                            | Can use WDM Power IRP       |
| Windows Vista       | Must use idle request IRP                    | Can use WDM Power IRP                            | Can use WDM Power IRP       |
| Windows Server 2003 | Must use idle request IRP                    | Must use idle request IRP                        | Must use idle request IRP   |
| Windows XP          | Must use idle request IRP                    | Must use idle request IRP                        | Must use idle request IRP   |



This section explains the Windows selective suspend mechanism and includes the following topics:

# Sending a USB Idle Request IRP


When a device goes idle, the client driver informs the bus driver by sending an idle request IRP ([**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270)). After the bus driver determines that it is safe to put the device in a low power state, it calls the callback routine that the client device driver passed down the stack with the idle request IRP.

In the callback routine, the client driver must cancel all pending I/O operations and wait for all USB I/O IRPs to complete. It then can issue an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request to change the WDM device power state to **D2**. The callback routine must wait for the **D2** request to complete before returning. For more information about the idle notification callback routine, see "USB Idle Notification Callback Routine".

The bus driver does not complete the idle request IRP after calling the idle notification callback routine. Instead, the bus driver holds the idle request IRP pending until one of the following conditions is true:

-   An **IRP\_MN\_SUPRISE\_REMOVAL** or **IRP\_MN\_REMOVE\_DEVICE IRP** is received. When one of these IRPs is received the idle request IRP completes with STATUS\_CANCELLED.
-   The bus driver receives a request to put the device into a working power state (**D0**). Upon receiving this request bus driver completes the pending idle request IRP with STATUS\_SUCCESS.

The following restrictions apply to the use of idle request IRPs:

-   Drivers must be in device power state **D0** when sending an idle request IRP.
-   Drivers must send just one idle request IRP per device stack.

The following WDM example code illustrates the steps that a device driver takes to send a USB idle request IRP. Error checking has been omitted in the following code example.

1.  Allocate and initialize the [**IOCTL\_INTERNAL\_USB\_SUBMIT\_IDLE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff537270) IRP
    ```cpp
    irp = IoAllocateIrp (DeviceContext->TopOfStackDeviceObject->StackSize, FALSE);
    nextStack = IoGetNextIrpStackLocation (irp);
    nextStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
    nextStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION;
    nextStack->Parameters.DeviceIoControl.InputBufferLength =
    sizeof(struct _USB_IDLE_CALLBACK_INFO);
    ```

2.  Allocate and initialize the idle request information structure (USB\_IDLE\_CALLBACK\_INFO).
    ```cpp
    idleCallbackInfo = ExAllocatePool (NonPagedPool,
    sizeof(struct _USB_IDLE_CALLBACK_INFO));
    idleCallbackInfo->IdleCallback = IdleNotificationCallback;
    // Put a pointer to the device extension in member IdleContext
    idleCallbackInfo->IdleContext = (PVOID) DeviceExtension;  
    nextStack->Parameters.DeviceIoControl.Type3InputBuffer =
    idleCallbackInfo;
    ```

3.  Set a completion routine.

    The client driver must associate a completion routine with the idle request IRP. For more information about the idle notification completion routine and example code, see "USB Idle Request IRP Completion Routine".

    ```cpp
    IoSetCompletionRoutine (irp,
     IdleNotificationRequestComplete,
       DeviceContext,
       TRUE,
       TRUE,
       TRUE);

    ```

4.  Store the idle request in the device extension.
    ```cpp
    deviceExtension->PendingIdleIrp = irp;

    ```

5.  Send the Idle request to the parent driver.
    ```cpp
    ntStatus = IoCallDriver (DeviceContext->TopOfStackDeviceObject, irp);
    ```

## Canceling a USB Idle Request


Under certain circumstances, a device driver might need to cancel an idle request IRP that has been submitted to the bus driver. This might occur if the device is removed, becomes active after being idle and sending the idle request, or if the entire system is transitioning to a lower system power state.

The client driver cancels the idle IRP by calling [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338). The following table describes three scenarios for canceling an idle IRP and specifies the action the driver must take:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Scenario</th>
<th>Idle Request Cancellation Mechanism</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The client driver has canceled the idle IRP and the USB driver stack has not called the &quot;USB Idle Notification Callback Routine&quot;.</td>
<td><p>The USB driver stack completes the idle IRP. Because the device never left the <strong>D0</strong>, the driver does not change the device state.</p></td>
</tr>
<tr class="even">
<td>The client driver has canceled the idle IRP, the USB driver stack has called the USB idle notification callback routine, and it has not yet returned.</td>
<td><p>It is possible that the USB idle notification callback routine is invoked even though the client driver has invoked cancellation on the IRP. In this case, the client driver&#39;s callback routine must still power down the device by sending the device to a lower power state synchronously.</p>
<p>When the device is in the lower power state, the client driver can then send a <strong>D0</strong> request.</p>
<p>Alternatively, the driver can wait for the USB driver stack to complete the idle IRP and then send the <strong>D0</strong> IRP.</p>
<p>If the callback routine is unable to put the device into a low power state due to insufficient memory to allocate a power IRP, it should cancel the idle IRP and exit immediately. The idle IRP will not be completed until the callback routine has returned; therefore, the callback routine should not block waiting for the canceled idle IRP to complete.</p></td>
</tr>
<tr class="odd">
<td>The device is already in a low power state.</td>
<td><p>If the device is already in a low power state, the client driver can send a <strong>D0</strong> IRP. The USB driver stack completes the idle request IRP with STATUS_SUCCESS.</p>
<p>Alternatively, the driver can cancel the idle IRP, wait for the USB driver stack to complete the idle IRP, and then send a <strong>D0</strong> IRP.</p></td>
</tr>
</tbody>
</table>

## USB Idle Request IRP Completion Routine


In many cases, a bus driver might call a driver's idle request IRP completion routine. If this occurs, a client driver must detect why the bus driver completed the IRP. The returned status code can provide this information. If the status code is not STATUS\_POWER\_STATE\_INVALID, the driver should put its device in **D0** if the device is not already in **D0**. If the device is still idle, the driver can submit another idle request IRP.

**Note**  The idle request IRP completion routine should not block waiting for a **D0** power request to complete. The completion routine can be called in the context of a power IRP by the hub driver, and blocking on another power IRP in the completion routine can lead to a deadlock.

The following list indicates how a completion routine for an idle request should interpret some common status codes:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STATUS_SUCCESS</p></td>
<td><p>Indicates that the device should no longer be suspended. However, drivers should verify that their devices are powered, and put them in <strong>D0</strong> if they are not already in <strong>D0</strong>.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_CANCELLED</p></td>
<td><p>The bus driver completes the idle request IRP with STATUS_CANCELLED in any of the following circumstances:</p>
<ul>
<li>The device driver canceled the IRP.</li>
<li>A system power state change is required.</li>
<li>On Windows XP, the device driver for one of the connected USB devices failed to put its device in <strong>D2</strong> while executing its idle request callback routine. As a result, the bus driver completed all pending idle request IRPs.</li>
</ul></td>
</tr>
<tr class="odd">
<td><p>STATUS_POWER_STATE_INVALID</p></td>
<td><p>Indicates that the device driver requested a <strong>D3</strong> power state for its device. When this occurs, the bus driver completes all pending idle IRPs with STATUS_POWER_STATE_INVALID.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_DEVICE_BUSY</p></td>
<td><p>Indicates that the bus driver already holds an idle request IRP pending for the device. Only one idle IRP can be pending at a time for a given device. Submitting multiple idle request IRPs is an error on the part of the power policy owner, and should be addressed by the driver writer.</p></td>
</tr>
</tbody>
</table>



The following code example shows a sample implementation for the idle request completion routine.

```ManagedCPlusPlus
/*Routine Description:

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

## USB Idle Notification Callback Routine


The bus driver (either an instance of the hub driver or the generic parent driver) determines when it is safe to suspend its device's children. If it is, it calls the idle notification callback routine supplied by each child's client driver.

The function prototype for USB\_IDLE\_CALLBACK is as follows:

``` syntax
typedef VOID (*USB_IDLE_CALLBACK)(__in PVOID Context);
```

A device driver must take the following actions in its idle notification callback routine:

-   Request an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) IRP for the device if the device needs to be armed for remote wakeup.
-   Cancel all I/O and prepare the device to go to a lower power state.
-   Put the device in a WDM sleep state by calling [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) with the *PowerState* parameter set to the enumerator value PowerDeviceD2 (defined in wdm.h; ntddk.h). In Windows XP, a driver must not put its device in PowerDeviceD3, even if the device is not armed for remote wake.

In Windows XP, a driver must rely on an idle notification callback routine to selectively suspend a device. If a driver running in Windows XP puts a device in a lower power state directly without using an idle notification callback routine, this might prevent other devices in the USB device tree from suspending. For more details, see "USB Global Suspend".

Both the hub driver and the [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) call the idle notification callback routine at IRQL = PASSIVE\_LEVEL. This allows the callback routine to block while it waits for the power state change request to complete.

The callback routine is invoked only while the system is in **S0** and the device is in **D0**.

The following restrictions apply to idle request notification callback routines:

-   Device drivers can initiate a device power state transition from **D0** to **D2** in the idle notification callback routine, but no other power state transition is allowed. In particular, a driver must not attempt to change its device to **D0** while executing its callback routine.
-   Device drivers must not request more than one power IRP from within the idle notification callback routine.

### Arming Devices for Wakeup in the Idle Notification Callback Routine


The idle notification callback routine should determine whether its device has an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request pending. If no IRP\_MN\_WAIT\_WAKE request is pending, the callback routine should submit an IRP\_MN\_WAIT\_WAKE request before suspending the device. For more information about the wait wake mechanism, see [Supporting Devices That Have WakeUp Capabilities](https://msdn.microsoft.com/library/windows/hardware/ff563907).


## USB Global Suspend


The USB 2.0 Specification defines Global Suspend as the suspension of the entire bus behind a USB host controller by ceasing all USB traffic on the bus, including start-of-frame packets. Downstream devices that are not already suspended detect the Idle state on their upstream port and enter the suspend state on their own. Windows does not implement Global Suspend in this manner. Windows always selectively suspends each USB device behind a USB host controller before it will cease all USB traffic on the bus.

-   [Conditions for Global Suspend in Windows 7](#conditions-for-global-suspend-in-windows-7)
-   [Conditions for Global Suspend in Windows Vista](#conditions-for-global-suspend-in-windows-vista)
-   [Conditions for Global Suspend in Windows XP](#conditions-for-global-suspend-in-windows-xp)
-   [Related topics](#related-topics)

### Conditions for Global Suspend in Windows 7


Windows 7 is more aggressive about selectively suspending USB hubs than Windows Vista. The Windows 7 USB hub driver will selectively suspend any hub where all of its attached devices are in **D1**, **D2**, or **D3** device power state. The entire bus will enter Global Suspend once all USB hubs are selective suspended. The Windows 7 USB driver stack treats a device as Idle whenever the device is in a WDM device state of **D1**, **D2**, or **D3**.

### Conditions for Global Suspend in Windows Vista


The requirements for doing a global suspend are more flexible in Windows Vista than in Windows XP.

In particular, the USB stack treats a device as Idle in Windows Vista whenever the device is in a WDM device state of **D1**, **D2**, or **D3**.

The following diagram illustrates a scenario that might occur in Windows Vista.

![diagram illustrating a global suspend in windows vista](images/global-suspendlh.png)

This diagram illustrates a situation very similar to the one depicted in the section "Conditions for Global Suspend in Windows XP". However, in this case Device 3 qualifies as an Idle device. Since all devices are idle, the bus driver is able to call the idle notification callback routines associated with the pending idle request IRPs. Each driver suspends its device and the bus driver suspends the USB host controller as soon as it is safe to do so.

On Windows Vista all non-hub USB devices must be in **D1**, **D2**, or **D3** before Global Suspend will be initiated, at which time all USB hubs, including the root hub, will be suspended. This means that any USB client driver that does not support selective suspend will prevent the bus from entering Global Suspend.

### Conditions for Global Suspend in Windows XP


In order to maximize power savings on Windows XP, it is important that every device driver use idle request IRPs to suspend its device. If one driver suspends its device with an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request instead of an idle request IRP, it could prevent other devices from suspending.

The following diagram illustrates a scenario that might occur in Windows XP.

![diagram illustrating a global suspend in windows xp](images/global-suspendxp.png)

In this figure, device 3 is in power state D3 and does not have an idle request IRP pending. Device 3 does not qualify as an idle device for purposes of a global suspend in Windows XP, because it does not have an idle request IRP pending with its parent. This prevents the bus driver from calling the idle request callback routines associated with the drivers of other devices in the tree.

## Enabling Selective Suspend


Selective suspend is disabled for upgrade versions of Microsoft Windows XP. It is enabled for clean installations of Windows XP, Windows Vista, and later versions of Windows.

To enable selective suspend support for a given root hub and its child devices, select the checkbox on the **Power Management** tab for the USB root hub in **Device Manager**.

Alternatively, you can enable or disable selective suspend by setting the value of **HcDisableSelectiveSuspend** under the software key of the USB port driver. A value of 1 disables selective suspend. A value of 0 enables selective suspend.

For instance, the following lines in Usbport.inf disable selective suspend for a Hydra OHCI controller:

```cpp
[OHCI_NOSS.AddReg.NT]
HKR,,"HcDisableSelectiveSuspend",0x00010001,1
```

Client drivers should not try to determine whether selective suspend is enabled before sending idle requests. They should submit idle requests whenever the device is idle. If the idle request fails the client driver should reset the idle timer and retry.

## Related topics
[USB Power Management](usb-power-management.md)  



