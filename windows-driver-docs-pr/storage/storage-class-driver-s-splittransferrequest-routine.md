---
title: Storage Class Driver's SplitTransferRequest Routine
description: Storage Class Driver's SplitTransferRequest Routine
ms.assetid: 4f449d3b-9a0a-4ff9-a7fb-bfa21b8a56c0
keywords:
- SplitTransferRequest
- noncontiguous pages WDK storage
- splitting transfer requests
- transfer request splitting WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's SplitTransferRequest Routine


## <span id="ddk_storage_class_drivers_splittransferrequest_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_SPLITTRANSFERREQUEST_ROUTINE_KG"></span>


The STORAGE\_ADAPTER\_DESCRIPTOR data returned to the *GetDescriptor* routine indicates the transfer capabilities of a given HBA to the class driver. In particular, this data indicates the **MaximumTransferLength** in bytes and the **MaximumPhysicalPages**: that is, how many noncontiguous pages the HBA can manage in the physical memory backing a system buffer (i.e., the extent of its scatter/gather support).

Most class drivers store a pointer to this configuration data in the device extension of each device object because storage class drivers are responsible for splitting all transfer requests that exceed the HBA's capability to transfer data. In other words, a class driver's [**DispatchReadWrite**](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine must determine whether each IRP requests a transfer that is more than the HBA can handle in a single transfer operation.

For example, such a *DispatchReadWrite* routine could have code similar to the following:

```cpp
PSTORAGE_ADAPTER_DESCRIPTOR adapterDescriptor = 
    commonExtension->PartitionZeroExtension->AdapterDescriptor;
ULONG transferPages;
ULONG maximumTransferLength = 
    adapterDescriptor->MaximumTransferLength;
    :        : 
// 
// Calculate number of pages in this transfer 
// 
transferPages = ADDRESS_AND_SIZE_TO_SPAN_PAGES( 
                    MmGetMdlVirtualAddress(Irp->MdlAddress), 
                        currentIrpStack->Parameters.Read.Length);
// 
// Check whether requested length is greater than the maximum number 
// of bytes that can be transferred in a single operation 
// 
if (currentIrpStack->Parameters.Read.Length > maximumTransferLength ||
        transferPages > adapterDescriptor->MaximumPhysicalPages) { 
    transferPages = adapterDescriptor->MaximumPhysicalPages - 1;
    if (maximumTransferLength > transferPages << PAGE_SHIFT) { 
        maximumTransferLength = transferPages << PAGE_SHIFT; 
    } 
    IoMarkIrpPending(Irp); 
    SplitTransferRequest(DeviceObject, 
                            Irp, 
                            maximumTransferLength); 
    return STATUS_PENDING; 
} 
    :        : 
```

The class driver cannot tell how many physical breaks the buffer will have once it has been mapped, so it must assume that each page in the transfer is discontiguous and compare the number of pages against the number of physical breaks allowed.

Note that such a driver's *DispatchReadWrite* routine calls **IoMarkIrpPending** and returns STATUS\_PENDING immediately after a call to its *SplitTransferRequest* routine with the original IRP.

To carry out the original transfer request, the driver's *SplitTransferRequest* routine creates one or more IRPs to handle subbuffers that are sized to suit the HBA's capabilities. For each such IRP, the *SplitTransferRequest* routine:

-   Sets up an SRB, usually by calling an internal *BuildRequest* routine (see [Storage Class Driver's BuildRequest Routine](storage-class-driver-s-buildrequest-routine.md))

-   Copies the MDL address from the original IRP to the new IRP

-   Sets the **DataBuffer** in the SRB to an offset in bytes into the MDL for this piece of the transfer

-   Sets up its *IoCompletion* routine before sending the IRP on to the port driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)

To track each piece of the transfer, *SplitTransferRequest* registers an *IoCompletion* routine for each driver-allocated IRP it sends to the next-lower driver. The *IoCompletion* routine maintains a count of completed partial transfer requests in the original IRP, using **InterlockedIncrement** and **InterlockedDecrement** to ensure that the count is accurate.

Such an *IoCompletion* routine must free any IRPs and/or SRBs the driver has allocated and must complete the original IRP when all requested data has been transferred or when the class driver has exhausted retries of the IRP and must fail it due to device transfer errors.

 

 




