---
title: Basic Calling Pattern for Version-3 DMA Routines
description: To perform a DMA transfer that uses the routines in version 3 of the DMA operations interface, your driver should follow the steps described in the following list.
ms.assetid: 5D73120F-79F5-4C9A-8AE5-25D5CF9B06F5
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Basic Calling Pattern for Version-3 DMA Routines


To perform a DMA transfer that uses the routines in version 3 of the DMA operations interface, your driver should follow the steps described in the following list. These steps are common to both subordinate devices and bus-master devices. Version 3 of this interface is available starting with Windows 8. For more information about the routines in this interface, see [**DMA\_OPERATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff544071).

## Step 1: Obtain a DMA adapter object


In preparation for a DMA transfer, the driver calls the [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220) routine to obtain a DMA adapter object. A DMA adapter object is a software object that represents either a bus-master device, or a request line on a system DMA controller. This object contains the DMA operations interface for the bus that is used to transfer data to or from the device. Additionally, this object synchronizes the driver's access to the shared resources that are required to perform the transfer. For more information, see [Introduction to Adapter Objects](introduction-to-adapter-objects.md).

## Step 2: Obtain a description of the required DMA resources


The driver calls the [**GetDmaTransferInfo**](https://msdn.microsoft.com/library/windows/hardware/hh451125) routine to get a description of the DMA resources that it needs to perform the transfer.

The input parameters to this call describe the memory buffer to use for the transfer, and the direction (read or write) of the transfer.

The resource requirements obtained from this call include the number of map registers and the size of the scatter/gather list that is needed to describe the data buffer for the transfer. In the subsequent call to the [**AllocateAdapterChannelEx**](https://msdn.microsoft.com/library/windows/hardware/hh406340) routine (see [step 3](#step-3)), the driver supplies the map register count as an input parameter.

## Step 3: Request the required DMA resources


The driver calls the [**AllocateAdapterChannelEx**](https://msdn.microsoft.com/library/windows/hardware/hh406340) routine to allocate resources to assign to the DMA adapter object. These resources include a DMA channel and map registers.

An **AllocateAdapterChannelEx** call can be asynchronous or synchronous.

If the DMA\_SYNCHRONOUS\_CALLBACK flag is not set, the call is asynchronous. In this case, the *ExecutionRoutine* parameter points to a caller-supplied execution routine that is called when the requested resources are available. If successful, an asynchronous **AllocateAdapterChannelEx** call returns STATUS\_SUCCESS without waiting for the execution routine to run.

If the DMA\_SYNCHRONOUS\_CALLBACK flag is set, the **AllocateAdapterChannelEx** call is synchronous. In this case, the *ExecutionRoutine* parameter in the call is optional, and **AllocateAdapterChannelEx** behaves as follows:

-   If *ExecutionRoutine* is non-NULL, and the DMA resources can be allocated immediately, **AllocateAdapterChannelEx** calls the execution routine in the context of the calling thread. After the execution routine finishes running, **AllocateAdapterChannelEx** returns STATUS\_SUCCESS. If the resources are not immediately available, **AllocateAdapterChannelEx** fails and returns error status code STATUS\_INSUFFICIENT\_RESOURCES.

-   If *ExecutionRoutine* is NULL, and **AllocateAdapterChannelEx** can immediately allocate the DMA resources, **AllocateAdapterChannelEx** returns STATUS\_SUCCESS. If all resources are not immediately available, the call fails with error status code STATUS\_INSUFFICIENT\_RESOURCES.

For synchronous calls that return STATUS\_SUCCESS, if the *MapRegisterBase* parameter to **AllocateAdapterChannelEx** is non-NULL, **AllocateAdapterChannelEx** writes the base address of the allocated map registers to the address pointed to by the *MapRegisterBase* parameter. If *ExecutionRoutine* is NULL, *MapRegisterBase* must be non-NULL. If *ExecutionRoutine* is non-NULL, the *MapRegisterBase* parameter to **AllocateAdapterChannelEx** is optional, and the execution routine receives the map register base address as an input parameter.

For asynchronous **AllocateAdapterChannelEx** calls, *ExecutionRoutine* must be non-NULL, and the execution routine receives the map register base address as an input parameter.

In subsequent calls to the [**MapTransferEx**](https://msdn.microsoft.com/library/windows/hardware/hh406521) routine (see [step 5](#step-5)), the driver supplies the map register base address as an input parameter.

If *ExecutionRoutine* is non-NULL, the execution routine returns a status value to indicate the disposition of the allocated resources. For system DMA transfers, this return value must be **KeepObject**. This value informs the operating system that the adapter object (and all of its allocated resources) is in use and should not be freed. If no execution routine is supplied, the driver must instead call the [**FreeAdapterObject**](https://msdn.microsoft.com/library/windows/hardware/hh451107) routine and supply **KeepObject** as the *AllocationOption* parameter.

## Step 4: If necessary, cancel the pending resource request


After an **AllocateAdapterChannelEx** call queues a DMA adapter to wait for DMA resources, the driver can, if necessary, call the [**CancelAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/hh406374) routine to cancel the pending resource request.

If **CancelAdapterChannel** returns TRUE, the resource request is successfully canceled. If an execution routine was supplied in the **AllocateAdapterChannelEx** call, this routine does not run.

If **CancelAdapterChannel** returns FALSE, the resource request cannot be canceled because it was already granted. If an execution routine was supplied in the **AllocateAdapterChannelEx** call, this routine will be called.

## Step 5: Initialize the DMA resources and start the DMA transfer


The driver calls [**MapTransferEx**](https://msdn.microsoft.com/library/windows/hardware/hh406521) to initialize the DMA resources and to start the DMA transfer. This call might occur in the same driver thread that calls **AllocateAdapterChannelEx**, or it might occur in the execution routine that the driver supplies to **AllocateAdapterChannelEx**. If more than one **MapTransferEx** call is required to transfer the entire DMA data buffer, a later **MapTransferEx** call might occur in the completion routine for the previous **MapTransferEx** call.

**MapTransferEx** supports chained MDLs as input parameters. Each MDL describes a region of the DMA buffer that is contiguous in virtual memory. When **MapTransferEx** builds the scatter/gather list, it automatically handles transitions from one virtually contiguous buffer region to the next without driver intervention. For more information, see [Using the MapTransferEx Routine](using-the-maptransferex-routine.md).

For a system DMA transfer, a pointer to a DMA completion routine can be passed to **MapTransferEx** in the optional *DmaCompletionRoutine* parameter. This routine is scheduled to run at dispatch level in response to an interrupt from the system DMA controller that indicates that the DMA transfer is complete.

If **MapTransferEx** is unable to map the entire requested transfer size, it will set the \**Length* output parameter to the length that was mapped, and return STATUS\_SUCCESS.

## Step 6: If necessary, perform hardware-specific operations


**MapTransferEx** returns STATUS\_SUCCESS to indicate that the DMA transfer is successfully initiated. On some platforms, the driver might have to take some additional action, outside of the **MapTransferEx** call, to start the transfer, but this type of delayed start is not required for all platforms. Drivers must not depend on such delays for decisions about using and freeing allocated resources.

The routines in the DMA operations interface maintain cache coherency for DMA transfers in a way that is transparent to the drivers that use these routines. On platforms that do not enforce cache coherency in hardware, **MapTransferEx** ensures that processor data caches are flushed before write (memory-to-device) transfers. For read (device-to-memory) transfers, the caches are invalidated during the call to the [**FlushAdapterBuffersEx**](https://msdn.microsoft.com/library/windows/hardware/hh451102) routine (see [step 8](#step-8)) that follows every **MapTransferEx** call.

## Step 7: Receive notification when the DMA transfer finishes


When a DMA transfer completes, the driver is notified in one of these two ways:

-   An interrupt to the device driver, for a bus-master device
-   Execution of the driver-supplied completion routine, for a subordinate device that uses a system DMA controller

For a system DMA transfer, a driver can supply a completion routine to **MapTransferEx** as an input parameter.
## Step 8: Flush any data that remains in the cache


After the DMA transfer completes, the driver must call the [**FlushAdapterBuffersEx**](https://msdn.microsoft.com/library/windows/hardware/hh451102) routine to flush any data that remains in the cache. The driver must call **FlushAdapterBuffersEx** after every **MapTransferEx** call.

If a **MapTransferEx** call maps only a part of the DMA data buffer, the driver must call **MapTransferEx** again to map the remaining data. A complex transfer might require several **MapTransferEx** calls. For each additional **MapTransferEx** call, repeat steps 5 through 8.

## Step 9: Free the DMA channel and map registers


After the entire DMA data buffer is successfully mapped and the final transfer completes, the driver must call the [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff549101) routine to free the DMA channel and any previously allocated map registers.

## Step 10: Release the DMA adapter object


After all DMA transfers are complete and any previously allocated map registers are freed, the driver calls the [**PutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff559965) routine to release the adapter object.

 

 




