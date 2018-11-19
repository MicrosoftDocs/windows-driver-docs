---
title: Supporting Passive-Level Interrupts
description: Starting with framework version 1.11, WDF drivers can create interrupt objects that require passive-level handling.
ms.assetid: E464F885-928C-40BC-A09F-7A7921F8FF37
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Passive-Level Interrupts


Starting with framework version 1.11, Kernel-Mode Driver Framework (KMDF) and User-Mode Driver Framework (UMDF) drivers running on Windows 8 or later versions of the operating system can create interrupt objects that require passive-level handling. If the driver configures an interrupt object for passive-level interrupt handling, the framework calls the driver's interrupt service routine (ISR) and other [interrupt object event callback functions](https://msdn.microsoft.com/library/windows/hardware/dn265640) at IRQL = PASSIVE\_LEVEL while holding a passive-level interrupt lock.

If you are developing a framework-based driver for a System on a Chip (SoC) platform, you can use passive-mode interrupts to communicate with an off-SoC device over a low-speed bus, such as I²C, SPI, or UART.

Otherwise, you should use [interrupts that require handling at the device's IRQL](creating-an-interrupt-object.md) (DIRQL). If your driver supports message-signaled interrupts (MSIs), you must use DIRQL interrupt handling. In versions 1.9 and earlier, the framework always processes interrupts at IRQL = DIRQL.

This topic describes how to [create](#creating-a-passive-level-interrupt), [service](#servicing), and [synchronize](#synchronizing) passive-level interrupts.

## Creating a Passive-Level Interrupt


To create a passive-level interrupt object, a driver must initialize a [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347) structure and pass it to the [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) method. In the configuration structure, the driver should:

-   Set the **PassiveHandling** member to TRUE.
-   Provide an [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function, to be called at passive level.
-   Optionally set the **AutomaticSerialization** to TRUE. If the driver sets **AutomaticSerialization** to TRUE, then the framework synchronizes execution of the interrupt object's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback functions with callback functions from other objects that are underneath the interrupt's parent object.
-   Optionally, the driver can provide either an [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback function, to be called at IRQL = PASSIVE\_LEVEL, or an [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function, to be called at IRQL = DISPATCH\_LEVEL.

For additional information on setting the above members of the configuration structure, see [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347).
For information about enabling and disabling passive-level interrupts, see [Enabling and Disabling Interrupts](enabling-and-disabling-interrupts.md).

## <a href="" id="servicing"></a>Servicing a Passive-Level Interrupt


The [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function, which runs at IRQL = PASSIVE\_LEVEL with the passive-level interrupt lock held, typically schedules an interrupt work item or interrupt DPC to process interrupt-related information at a later time. Framework-based drivers implement work item or DPC routines as [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) or [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback functions.

To schedule the execution of an [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback function, a driver calls [**WdfInterruptQueueWorkItemForIsr**](https://msdn.microsoft.com/library/windows/hardware/hh439270) from within the [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function.

To schedule the execution of an [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function, a driver calls [**WdfInterruptQueueDpcForIsr**](https://msdn.microsoft.com/library/windows/hardware/ff547371) from within the [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function. (Recall that a driver's *EvtInterruptIsr* callback function can call [**WdfInterruptQueueWorkItemForIsr**](https://msdn.microsoft.com/library/windows/hardware/hh439270) or **WdfInterruptQueueDpcForIsr**, but not both.)

Most drivers use a single [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) or [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function for each type of interrupt. If your driver creates multiple framework interrupt objects for each device, consider using a separate *EvtInterruptWorkItem* or *EvtInterruptDpc* callback for each interrupt.

Drivers typically complete I/O requests in their [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) or [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback functions.

The following code example demonstrates how a driver using passive-level interrupts might schedule a [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback from within its [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) function.

```cpp
BOOLEAN

EvtInterruptIsr(
    _In_  WDFINTERRUPT Interrupt,
    _In_  ULONG        MessageID
    )
/*++

  Routine Description:

    This routine responds to interrupts generated by the hardware.
    It stops the interrupt and schedules a work item for 
    additional processing.

    This ISR is called at PASSIVE_LEVEL (passive-level interrupt handling).

  Arguments:
  
    Interrupt - a handle to a framework interrupt object
    MessageID - message number identifying the device's
        hardware interrupt message (if using MSI)

  Return Value:

    TRUE if interrupt recognized.

--*/
{
    
    UNREFERENCED_PARAMETER(MessageID);

    NTSTATUS                status;
    PDEV_CONTEXT            devCtx;
    WDFREQUEST              request;
    WDF_MEMORY_DESCRIPTOR   memoryDescriptor;
    INT_REPORT              intReport = {0};
    BOOLEAN                 intRecognized;
    WDFIOTARGET             ioTarget;
    ULONG_PTR               bytes;
    WDFMEMORY               reqMemory;

    intRecognized = FALSE;

    //         
    // Typically the pattern in most ISRs (DIRQL or otherwise) is to:
    // a) Check if the interrupt belongs to this device (shared interrupts).
    // b) Stop the interrupt if the interrupt belongs to this device.
    // c) Acknowledge the interrupt if the interrupt belongs to this device.
    //
   
   
    //
    // Retrieve device context so that we can access our queues later.
    //    
    devCtx = GetDevContext(WdfInterruptGetDevice(Interrupt));

     
    //
    // Init memory descriptor.
    //    
    WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(
                         &memoryDescriptor,
                         &intReport,
                         sizeof(intReport);

    //
    // Send read registers/data IOCTL. 
    // This call stops the interrupt and reads the data at the same time.
    // The device will reinterrupt when a new read is sent.
    //
    bytes = 0;
    status = WdfIoTargetSendIoctlSynchronously(
                             ioTarget,
                             NULL,
                             IOCTL_READ_REPORT,
                             &memoryDescriptor,
                             NULL,
                             NULL,
                             &bytes);
     
    //
    // Return from ISR if this is not our interrupt.
    // 
    if (intReport->Interrupt == FALSE) {
        goto exit;
    }

    intRecognized = TRUE;

    //
    // Validate the data received.
    //
    ...

    //
    // Retrieve the next read request from the ReportQueue which
    // stores all the incoming IOCTL_READ_REPORT requests
    // 
    request = NULL;
    status = WdfIoQueueRetrieveNextRequest(
                            devCtx->ReportQueue,
                            &request);

    if (!NT_SUCCESS(status) || (request == NULL)) {
        //
        // No requests to process. 
        //
        goto exit;
    }
    
    //
    // Retrieve the request buffer.
    //
    status = WdfRequestRetrieveOutputMemory(request, &reqMemory);

    //
    // Copy the data read into the request buffer.
    // The request will be completed in the work item.
    //
    bytes = intReport->Data->Length;
    status = WdfMemoryCopyFromBuffer(
                            reqMemory,
                            0,
                            intReport->Data,
                            bytes);

    //
    // Report how many bytes were copied.
    //
    WdfRequestSetInformation(request, bytes);

    //
    // Forward the request to the completion queue.
    //
    status = WdfRequestForwardToIoQueue(request, devCtx->CompletionQueue);
    
    //
    // Queue a work-item to complete the request.
    //
    WdfInterruptQueueWorkItemForIsr(FxInterrupt);

exit:
    return intRecognized;
}

VOID
EvtInterruptWorkItem(
    _In_ WDFINTERRUPT   Interrupt,
    _In_ WDFOBJECT      Device
    )
/*++

Routine Description:

    This work item handler is triggered by the interrupt ISR.

Arguments:

    WorkItem - framework work item object

Return Value:

    None

--*/
{
    UNREFERENCED_PARAMETER(Device);

    WDFREQUEST              request;
    NTSTATUS                status;
    PDEV_CONTEXT            devCtx;
    BOOLEAN                 run, rerun;
    
    devCtx = GetDevContext(WdfInterruptGetDevice(Interrupt));

    WdfSpinLockAcquire(devCtx->WorkItemSpinLock);
    if (devCtx->WorkItemInProgress) {
        devCtx->WorkItemRerun = TRUE;
        run = FALSE;
    }
    else {
        devCtx->WorkItemInProgress = TRUE;
        devCtx->WorkItemRerun = FALSE;
        run = TRUE;
    }
    WdfSpinLockRelease(devCtx->WorkItemSpinLock);

    if (run == FALSE) {
        return;
    }

    do {  
        for (;;) {
            //
            // Complete all report requests in the completion queue.
            //
            request = NULL;
            status = WdfIoQueueRetrieveNextRequest(devCtx->CompletionQueue, 
                                                   &request);
            if (!NT_SUCCESS(status) || (request == NULL)) {
                break;
            }
            
            WdfRequestComplete(request, STATUS_SUCCESS);
        }
        
        WdfSpinLockAcquire(devCtx->WorkItemSpinLock);
        if (devCtx->WorkItemRerun) {
            rerun = TRUE;
            devCtx->WorkItemRerun = FALSE;
        }
        else {
            devCtx->WorkItemInProgress = FALSE;
            rerun = FALSE;
        }
        WdfSpinLockRelease(devCtx->WorkItemSpinLock);
    }
    while (rerun);
}

VOID
EvtIoInternalDeviceControl(
    _In_  WDFQUEUE      Queue,
    _In_  WDFREQUEST    Request,
    _In_  size_t        OutputBufferLength,
    _In_  size_t        InputBufferLength,
    _In_  ULONG         IoControlCode
    )
{
    NTSTATUS            status;
    DEVICE_CONTEXT      devCtx;
    devCtx = GetDeviceContext(WdfIoQueueGetDevice(Queue));
    
    switch (IoControlCode) 
    {
    ...
    case IOCTL_READ_REPORT:

        //
        // Forward the request to the manual ReportQueue to be completed
        // later by the interrupt work item.
        //
        status = WdfRequestForwardToIoQueue(Request, devCtx->ReportQueue);
        break;
   
    ...
    }

    if (!NT_SUCCESS(status)) {
        WdfRequestComplete(Request, status);
    }
}
```

## <a href="" id="synchronizing"></a>Synchronizing a Passive-Level Interrupt


To prevent deadlock, follow these guidelines when writing a driver that implements passive-level interrupt handling:

-   If **AutomaticSerialization** is set to TRUE, do not [send synchronous requests](sending-i-o-requests-synchronously.md) from within an [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) callback function.
-   Release the passive-level interrupt lock before [completing I/O requests](completing-i-o-requests.md).
-   Provide [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714), [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730), and [*EvtInterruptWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh406422) as necessary.
-   If your driver must perform interrupt-related work in an arbitrary thread context, such as in a [request handler](request-handlers.md), use [**WdfInterruptTryToAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/hh439284) and [**WdfInterruptReleaseLock**](https://msdn.microsoft.com/library/windows/hardware/ff547376). Do not call [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340), [**WdfInterruptSynchronize**](https://msdn.microsoft.com/library/windows/hardware/ff547389), [**WdfInterruptEnable**](https://msdn.microsoft.com/library/windows/hardware/ff547354), or [**WdfInterruptDisable**](https://msdn.microsoft.com/library/windows/hardware/ff547351) from an arbitrary thread context. For an example of a deadlock scenario that can be caused by calling **WdfInterruptAcquireLock** from an arbitrary thread context, see the Remarks section of [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340).

    If the call to [**WdfInterruptTryToAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/hh439284) fails, the driver can postpone its interrupt-related work to a work item. In that work item, the driver can safely acquire the interrupt lock by calling [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340). For more information, see [**WdfInterruptTryToAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/hh439284).

    In a non-arbitrary thread context, such as a work item, the driver can call [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340) or [**WdfInterruptSynchronize**](https://msdn.microsoft.com/library/windows/hardware/ff547389).

For more information about using interrupt locks, see [Synchronizing Interrupt Code](synchronizing-interrupt-code.md).

 

 





