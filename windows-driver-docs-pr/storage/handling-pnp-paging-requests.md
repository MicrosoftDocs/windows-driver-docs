---
title: Handling PnP Paging Requests
description: Handling PnP Paging Requests
ms.assetid: c30c70d9-69c6-42d7-ae69-9c2421ba1d53
keywords:
- storage filter drivers WDK , PnP
- filter drivers WDK storage , PnP
- SFD WDK storage , PnP
- PnP WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling PnP Paging Requests


## <span id="ddk_handling_pnp_paging_requests_kg"></span><span id="DDK_HANDLING_PNP_PAGING_REQUESTS_KG"></span>


A storage filter driver must handle PnP paging requests ([**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) with [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) and **Parameters.UsageNotification.Type** set to **DeviceUsageTypePaging**) if the function driver it is filtering handles this IRP.

The following items must be added to the DeviceExtension of the Filter DO:

ULONG PagingCount;

KEVENT PagingCountEvent;

Upon receiving PnP paging requests, a storage filter driver must update both the PagingCount and the setting of the **DO\_POWER\_PAGABLE** bit in the Filter DO. The timing of the update of the **DO\_POWER\_PAGABLE** bit depends on whether the bit is being set or cleared. If the IRP indicates that the bit should be set, then the filter driver must set it *before* forwarding the IRP down the driver stack. But if the IRP indicates that the bit should be cleared, then the filter driver should not clear the bit right away. It must first forward the IRP, then wait for lower drivers to return their status and clear the bit only if the lower drivers return **STATUS\_SUCCESS**.

The following traces the flow of actions taken by the storage filter driver. Please refer to the pseudocode sample immediately beneath the outline to see a representation of this outline in C code:

A. Verify that the device has been started. If not, fail with **STATUS\_DEVICE\_NOT\_READY**.

B. Synchronize on the PagingCountEvent (KeWaitForSingleObject( PagingCountEvent, ...)).

C. If removing the last paging device ( (! **Parameters.UsageNotification.InPath** &&
(PagingCount == 1) ) then
1.  Set a local Boolean to **TRUE**, and

2.  If the **DO\_POWER\_INRUSH** bit is not set in the Filter DO, then set the **DO\_POWER\_PAGABLE** bit.

    The following explains why the **DO\_POWER\_PAGABLE** bit must be set on the way down and not on the way up:

    The power requirements state that if any lower device object sets the **DO\_POWER\_PAGABLE** bit, all higher-level drivers must do the same. If the filter driver fails to set the **DO\_POWER\_PAGABLE** bit prior to sending the paging request IRP down the stack, it could violate this condition as follows:

    Suppose the filter driver does not set the **DO\_POWER\_PAGABLE** bit in its Filter DO before forwarding the paging request IRP to the drivers beneath it in the driver stack. Next suppose that a lower driver sets the **DO\_POWER\_PAGABLE** bit in its own DO. Finally, suppose that prior to the completion of the IRP by the filter driver a power IRP occurs. At that point, the **DO\_POWER\_PAGABLE** bit would be cleared in the Filter DO but would be set in the DO of the lower-level driver, causing a system crash.

    It is safe to set the **DO\_POWER\_PAGABLE** bit before forwarding a paging request down the stack, because there is no longer an active paging file on the filter driver's device, and therefore no more paging I/O will occur on it. If the request to remove this paging file succeeds, the filter driver will be done. If the request fails, the filter driver can restore the original state of its flags by simply clearing the **DO\_POWER\_PAGABLE** bit prior to completing the IRP. Because the paging file requests are serialized, there is no danger that some other thread will have modified this bit since the filter driver last altered it.

D. Synchronously forward the IRP to the lower drivers.

E. If the IRP completes successfully, then

1.  Call IoAdjustPagingPathCount(&PagingCount, **Parameters.UsageNotification.InPath**) to increment or decrement the PagingCount. IoAdjustPagingPathCount does an InterlockedIncrement or InterlockedDecrement of the PagingCount depending on the value in **Parameters.UsageNotification.InPath**. A value of **TRUE** indicates that a paging file is being added, so increment the PagingCount; a value of **FALSE** indicates that a paging file is being removed, so decrement the PagingCount.

2.  If **Parameters.UsageNotification.InPath** is **TRUE**, a paging file is being added, so clear the **DO\_POWER\_PAGABLE** bit.

F. Else if the IRP fails, then

1.  Check the local Boolean to see if **DO\_POWER\_PAGABLE** was set in the Filter DO on the way down.

2.  If **DO\_POWER\_PAGABLE** was set on the way down, clear it.

G. End Synchronization (KeSetEvent(PagingCountEvent, ...)).

### <span id="pseudocode_example"></span><span id="PSEUDOCODE_EXAMPLE"></span>Pseudocode Example

The sections marked by letters (*//A*, *//B*, etc.) in the following code sample map to the letters of the outline above.

```cpp
case DeviceUsageTypePaging: { 
    BOOLEAN setPageable = FALSE; 
    BOOLEAN addPageFile = irpStack -> 
                          Parameters.UsageNotification.InPath; 
 
 // A 
    if((addPageFile) && 
        (extension -> CurrentPnpState != 
        IRP_MN_START_DEVICE)) { 
            status = STATUS_DEVICE_NOT_READY; 
            break; 
        } 
 // B 
    KeWaitForSingleObject(&commonExtension -> PagingCountEvent, 
                                    Executive, KernelMode, 
                                    FALSE, NULL); 
 // C 
    if (!addPageFile && commonExtension -> PagingCount == 1 ) { 
        // The last paging file is no longer active.
        // Set the DO_POWER_PAGABLE bit before 
        // forwarding the paging request down the 
        // stack.
        if (!(DeviceObject->Flags & DO_POWER_INRUSH)) { 
            DeviceObject->Flags |=             DO_POWER_PAGABLE; 
            setPageable = TRUE; 
        ) 
    ) 
 // D 
        status = ForwardIrpSynchronous(commonExtension, Irp); 
 // E
        if (NT_SUCCESS(status)) { 
            IoAdjustPagingPathCount(&commonExtension -> PagingCount, 
                                    addPageFile); 
        if (addPageFile && commonExtension -> PagingCount == 1) { 
            // Once the lower device objects have 
            // succeeded the addition of the paging 
            // file, it is illegal to fail the 
            // request. It is also the time to 
            // clear the Filter DO&#39;s 
            //DO_POWER_PAGABLE flag.
 
            DeviceObject->Flags &= ~DO_POWER_PAGABLE; 
            } 
        } else { 
 // F 
        if (setPageable == TRUE) { 
            DeviceObject->Flags &= ~DO_POWER_PAGABLE; 
            setPageable = FALSE; 
        } 
    } 
 // G 
        KeSetEvent(&commonExtension->PagingCountEvent, 
                                    IO_NO_INCREMENT, FALSE); 
                                    break;
    } *Do not use or delete the last paragraph mark. It maintains the template setup and formats.
```

 

 




