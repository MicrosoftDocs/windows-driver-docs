---
title: Using ECPs to Process IRP_MJ_CREATE in File System Filter Drivers
description: Using ECPs to Process IRP_MJ_CREATE Operations in a File System Filter Driver
ms.date: 10/16/2019
ms.localizationpriority: medium
---

# Using ECPs to Process IRP_MJ_CREATE Operations in a File System Filter Driver

You can use ECPs in your file system filter driver to process [**IRP_MJ_CREATE**](./irp-mj-create.md) operations. Your file system filter driver can call the routines in the following sections to retrieve, acknowledge, add, and remove ECPs for the **IRP_MJ_CREATE** operation. You can also determine the operating-system space from which the ECPs originated.

## Retrieving ECPs

Your file system filter driver can follow these steps to retrieve ECPs for the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation:

1. Call the [**FltGetEcpListFromCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetecplistfromcallbackdata) or [**FsRtlGetEcpListFromIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetecplistfromirp) routine to retrieve a pointer to an ECP context structure list (ECP_LIST) that is associated with the create operation.

2. Perform either of the following operations:
    - Call the [**FltGetNextExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetnextextracreateparameter) or [**FsRtlGetNextExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetnextextracreateparameter) routine to retrieve a pointer to the next (or first) ECP context structure in the ECP list.
    - Call the [**FltFindExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfindextracreateparameter) or [**FsRtlFindExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfindextracreateparameter) routine to search the ECP list for an ECP context structure of a given type. Either routine returns a pointer to the ECP context structure if the structure is found.

## Setting ECPs

To set ECPs for the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation, your file system filter driver can first either retrieve an existing ECP context structure list (ECP_LIST) that is associated with the create operation, or allocate ECP_LIST and an ECP context structure and insert the ECP context structure in the ECP_LIST.

### Setting ECPs in an Existing ECP_LIST

Your file system filter driver can follow these steps to set ECPs in an existing ECP_LIST that is associated with the create operation:

1. Call the [**FltGetEcpListFromCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetecplistfromcallbackdata) or [**FsRtlGetEcpListFromIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetecplistfromirp) routine to retrieve a pointer to an ECP context structure list (ECP_LIST) that is associated with the create operation.

2. Call the [**FltAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) or [**FsRtlAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameter) routine to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3. Call the [**FltInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinsertextracreateparameter) or [**FsRtlInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertextracreateparameter) routine to insert ECP context structures into the [ECP_LIST](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

### Setting ECPs in a Newly Created ECP_LIST

Your file system filter driver can follow these steps to set ECPs in a newly created ECP_LIST that is associated with the create operation:

1. Call the [**FltAllocateExtraCreateParameterList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterlist) or [**FsRtlAllocateExtraCreateParameterList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameterlist) routine to allocate memory for an [ECP_LIST](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

2. Call the [**FltAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) or [**FsRtlAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameter) routine to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3. Call the [**FltInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinsertextracreateparameter) or [**FsRtlInsertExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertextracreateparameter) routine to insert ECP context structures into the [ECP_LIST](/previous-versions/windows/hardware/drivers/ff540148(v=vs.85)) structure.

4. Call the [**FltSetEcpListIntoCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetecplistintocallbackdata) or [**FsRtlSetEcpListIntoIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlsetecplistintoirp) routine to attach an ECP list to the create operation.

## Removing ECPs

Your file system filter driver can follow these steps to remove ECPs for the [**IRP_MJ_CREATE**](./irp-mj-create.md) operation:

1. Call the [**FltRemoveExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltremoveextracreateparameter) or [**FsRtlRemoveExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveextracreateparameter) routine to search an ECP list for an ECP context structure. If the ECP context structure is found, the routine detaches the ECP context structure from the ECP list.

2. To free the memory for the detached ECP context structure, call the [**FltFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameter) or [**FsRtlFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfreeextracreateparameter) routine. You can call these routines to free memory for the ECP context structure if you have allocated the memory in one of the following ways:

    - You called the [**FltAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameter) or [**FsRtlAllocateExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameter) routine to allocate paged memory pool
    - You called the [**FltAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterfromlookasidelist) or [**FsRtlAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist) routine to allocate memory pool from a lookaside list

## Marking ECPs as Acknowledged, or Determining Acknowledge Status

Your file system filter driver can call the following routines to either mark ECPs as acknowledged or determine whether the ECPs are marked as acknowledged:

- Call the [**FltAcknowledgeEcp**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltacknowledgeecp) or [**FsRtlAcknowledgeEcp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlacknowledgeecp) routine to mark an ECP context structure as acknowledged. The ECP can be marked as looked at, used, processed, or any other condition of the ECP.

- Call the [**FltIsEcpAcknowledged**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltisecpacknowledged) or [**FsRtlIsEcpAcknowledged**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlisecpacknowledged) routine to determine whether an ECP context structure is marked as acknowledged.

## Determining Origination Mode

Your file system filter driver can call the [**FltIsEcpFromUserMode**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltisecpfromusermode) or [**FsRtlIsEcpFromUserMode**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlisecpfromusermode) routine to determine whether an ECP context structure originated from user mode. A file system filter driver can refuse to accept an ECP context structure that originated from user mode.

## Using Lookaside Lists to Allocate ECPs

Your file system filter driver can call the following routines to allocate ECPs from lookaside lists and to manage the lookaside lists and ECPs:

- Call the [**FltInitExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltinitextracreateparameterlookasidelist) or [**FsRtlInitExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinitextracreateparameterlookasidelist) routine to initialize a paged or nonpaged pool lookaside list that is used for the allocation of one or more ECP context structures of fixed size.

- Call the [**FltDeleteExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeleteextracreateparameterlookasidelist) or [**FsRtlDeleteExtraCreateParameterLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtldeleteextracreateparameterlookasidelist) routine to free the lookaside list.

- Call the [**FltAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocateextracreateparameterfromlookasidelist) or [**FsRtlAllocateExtraCreateParameterFromLookasideList**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlallocateextracreateparameterfromlookasidelist) routine to allocate memory pool from the lookaside list for an ECP context structure and to generate a pointer to that structure.

- Call the [**FltFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfreeextracreateparameter) or [**FsRtlFreeExtraCreateParameter**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfreeextracreateparameter) routine to free the memory for the ECP context structures.
