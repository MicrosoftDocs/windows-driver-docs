---
Description: In many cases, a bus driver might call a driver's idle request IRP completion routine.
title: USB Idle Request IRP Completion Routine
---

# USB Idle Request IRP Completion Routine


In many cases, a bus driver might call a driver's idle request IRP completion routine. If this occurs, a client driver must detect why the bus driver completed the IRP. The returned status code can provide this information. If the status code is not STATUS\_POWER\_STATE\_INVALID, the driver should put its device in **D0** if the device is not already in **D0**. If the device is still idle, the driver can submit another idle request IRP.

**Note**  The idle request IRP completion routine should not block waiting for a **D0** power request to complete. The completion routine can be called in the context of a power IRP by the hub driver, and blocking on another power IRP in the completion routine can lead to a deadlock.

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
    
    if(!NT_SUCCESS(ntStatus) &amp;&amp; ntStatus != STATUS_NOT_SUPPORTED) 
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

    InterlockedExchange(&amp;DeviceExtension->IdleReqPend, 0);

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

    KeSetEvent(&amp;DeviceExtension->IdleIrpCompleteEvent, IO_NO_INCREMENT, FALSE);

    return STATUS_MORE_PROCESSING_REQUIRED;
}

```

## Related topics


[USB Selective Suspend](usb-selective-suspend.md)

[USB Power Management](usb-power-management.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Idle%20Request%20IRP%20Completion%20Routine%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




