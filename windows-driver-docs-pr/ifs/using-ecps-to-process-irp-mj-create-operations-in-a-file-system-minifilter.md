---
title: Using ECPs to process IRP_MJ_CREATE in a file system filter driver
description: Using ECPs to Process IRP_MJ_CREATE Operations in a File System Filter Driver
ms.date: 09/09/2021
ms.localizationpriority: medium
---

# Using ECPs to process IRP_MJ_CREATE operations in a file system filter driver

You can use extra create parameters (ECPs) in your file system filter driver to process [**IRP_MJ_CREATE**](./irp-mj-create.md) operations. Your file system filter driver can call the routines in the following sections to retrieve, set (add), acknowledge, and remove ECPs for the **IRP_MJ_CREATE** operation. You can also determine the operating-system space from which the ECPs originated.

## Retrieving ECPs

To retrieve ECPs for the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation:

1. Call [**FltGetEcpListFromCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetecplistfromcallbackdata) (or [**FsRtlGetEcpListFromIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetecplistfromirp)) to retrieve a pointer to the ([**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85))) that is associated with the create operation.

2. Perform either of the following operations:
    - Call [**FltGetNextExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetnextextracreateparameter) (or [**FsRtlGetNextExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetnextextracreateparameter)) to retrieve a pointer to the next (or first) ECP context structure in the ECP list.
    - Call [**FltFindExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfindextracreateparameter) (or [**FsRtlFindExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfindextracreateparameter)) to search the ECP list for an ECP context structure of a given type. Either routine returns a pointer to the ECP context structure if the structure is found.

## Setting ECPs

To set ECPs for the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation, your file system filter driver will either:

- Set ECPs in an existing ECP_LIST.

- Set ECPs in a newly created ECP_LIST.

### Setting ECPs in an existing ECP_LIST

To set ECPs in an *existing* [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) that is associated with the create operation:

1. Call [**FltGetEcpListFromCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetecplistfromcallbackdata) (or [**FsRtlGetEcpListFromIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetecplistfromirp)) to retrieve a pointer to the **ECP_LIST** that is associated with the create operation.

2. Call [**FltAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) (or [**FsRtlAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameter)) to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3. Call [**FltInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinsertextracreateparameter) (or [**FsRtlInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertextracreateparameter)) to insert ECP context structures into the [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

### Setting ECPs in a newly created ECP_LIST

If an [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) is not currently associated with the create operation, you'll need to create one and then set ECPs in it:

1. Call [**FltAllocateExtraCreateParameterList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterlist) (or [**FsRtlAllocateExtraCreateParameterList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameterlist)) to allocate memory for an [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

2. Call [**FltAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) (or [**FsRtlAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameter)) to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3. Call [**FltInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinsertextracreateparameter) (or [**FsRtlInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertextracreateparameter)) to insert ECP context structures into the [**ECP_LIST**](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)).

4. Call [**FltSetEcpListIntoCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetecplistintocallbackdata) (or [**FsRtlSetEcpListIntoIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlsetecplistintoirp)) to attach an ECP list to the create operation.

## Removing ECPs

To remove ECPs for the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation:

1. Call [**FltRemoveExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltremoveextracreateparameter) (or [**FsRtlRemoveExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveextracreateparameter)) to search an ECP list for an ECP context structure. If the ECP context structure is found, the routine detaches the ECP context structure from the ECP list.

2. To free the memory for the detached ECP context structure, call [**FltFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameter) (or [**FsRtlFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfreeextracreateparameter)). You can call these routines to free memory for the ECP context structure if you allocated the memory in one of the following ways:

    - You called [**FltAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) (or [**FsRtlAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameter)) to allocate paged memory pool
    - You called [**FltAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterfromlookasidelist) (or [**FsRtlAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist)) to allocate memory pool from a lookaside list

## Marking ECPs as acknowledged, or determining acknowledge status

Call the following routines to either mark ECPs as acknowledged or determine whether the ECPs are marked as acknowledged:

- Call [**FltAcknowledgeEcp**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltacknowledgeecp) (or [**FsRtlAcknowledgeEcp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlacknowledgeecp)) to mark an ECP context structure as acknowledged. The ECP can be marked as looked at, used, processed, or any other condition of the ECP.

- Call [**FltIsEcpAcknowledged**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltisecpacknowledged) (or [**FsRtlIsEcpAcknowledged**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlisecpacknowledged)) to determine whether an ECP context structure is marked as acknowledged.

## Determining origination mode

Call [**FltIsEcpFromUserMode**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltisecpfromusermode) (or [**FsRtlIsEcpFromUserMode**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlisecpfromusermode)) to determine whether an ECP context structure originated from user mode. A file system filter driver can refuse to accept an ECP context structure that originated from user mode.

## Using lookaside lists to allocate ECPs

Call the following routines to allocate ECPs from [lookaside lists](/windows-hardware/drivers/kernel/using-lookaside-lists) and to manage the lookaside lists and ECPs:

- Call [**FltInitExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinitextracreateparameterlookasidelist) (or [**FsRtlInitExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinitextracreateparameterlookasidelist)) to initialize a paged or nonpaged pool lookaside list that is used for the allocation of one or more ECP context structures of fixed size.

- Call [**FltDeleteExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeleteextracreateparameterlookasidelist) (or [**FsRtlDeleteExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtldeleteextracreateparameterlookasidelist)) to free the lookaside list.

- Call [**FltAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterfromlookasidelist) (or [**FsRtlAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist)) to allocate memory pool from the lookaside list for an ECP context structure and to generate a pointer to that structure.

- Call [**FltFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameter) (or [**FsRtlFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfreeextracreateparameter)) to free the memory for the ECP context structures.
