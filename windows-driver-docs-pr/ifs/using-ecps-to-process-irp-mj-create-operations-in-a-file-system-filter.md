---
title: Using ECPs to Process IRP_MJ_CREATE in File System Filter Drivers
description: Using ECPs to Process IRP_MJ_CREATE Operations in a File System Filter Driver
ms.assetid: 969709a9-cdca-4a1a-95a0-0bb89cd17693
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using ECPs to Process IRP\_MJ\_CREATE Operations in a File System Filter Driver


You can use ECPs in your file system filter driver to process [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operations. Your file system filter driver can call the routines in the following sections to retrieve, acknowledge, add, and remove ECPs for the **IRP\_MJ\_CREATE** operation. You can also determine the operating-system space from which the ECPs originated.

### <span id="Retrieving_ECPs"></span><span id="retrieving_ecps"></span><span id="RETRIEVING_ECPS"></span>Retrieving ECPs

Your file system filter driver can follow these steps to retrieve ECPs for the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation:

1.  Call the [**FltGetEcpListFromCallbackData**](https://msdn.microsoft.com/library/windows/hardware/ff543016) or [**FsRtlGetEcpListFromIrp**](https://msdn.microsoft.com/library/windows/hardware/ff546015) routine to retrieve a pointer to an ECP context structure list (ECP\_LIST) that is associated with the create operation.

2.  Perform either of the following operations:
    -   Call the [**FltGetNextExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff543104) or [**FsRtlGetNextExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff546028) routine to retrieve a pointer to the next (or first) ECP context structure in the ECP list.
    -   Call the [**FltFindExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff542094) or [**FsRtlFindExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545968) routine to search the ECP list for an ECP context structure of a given type. Either routine returns a pointer to the ECP context structure if the structure is found.

### <span id="Setting_ECPs"></span><span id="setting_ecps"></span><span id="SETTING_ECPS"></span>Setting ECPs

To set ECPs for the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation, your file system filter driver can first either retrieve an existing ECP context structure list (ECP\_LIST) that is associated with the create operation, or allocate ECP\_LIST and an ECP context structure and insert the ECP context structure in the ECP\_LIST.

Your file system filter driver can follow these steps to set ECPs in an existing ECP\_LIST that is associated with the create operation:

1.  Call the [**FltGetEcpListFromCallbackData**](https://msdn.microsoft.com/library/windows/hardware/ff543016) or [**FsRtlGetEcpListFromIrp**](https://msdn.microsoft.com/library/windows/hardware/ff546015) routine to retrieve a pointer to an ECP context structure list (ECP\_LIST) that is associated with the create operation.

2.  Call the [**FltAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff541728) or [**FsRtlAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545609) routine to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3.  Call the [**FltInsertExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff543305) or [**FsRtlInsertExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff546179) routine to insert ECP context structures into the [ECP\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff540148) structure.

Your file system filter driver can follow these steps to set ECPs in a newly created ECP\_LIST that is associated with the create operation:

1.  Call the [**FltAllocateExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff541741) or [**FsRtlAllocateExtraCreateParameterList**](https://msdn.microsoft.com/library/windows/hardware/ff545632) routine to allocate memory for an [ECP\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff540148) structure.

2.  Call the [**FltAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff541728) or [**FsRtlAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545609) routine to allocate paged memory pool for an ECP context structure and to generate a pointer to that structure.

3.  Call the [**FltInsertExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff543305) or [**FsRtlInsertExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff546179) routine to insert ECP context structures into the [ECP\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff540148) structure.

4.  Call the [**FltSetEcpListIntoCallbackData**](https://msdn.microsoft.com/library/windows/hardware/ff544510) or [**FsRtlSetEcpListIntoIrp**](https://msdn.microsoft.com/library/windows/hardware/ff547250) routine to attach an ECP list to the create operation.

### <span id="Removing_ECPs"></span><span id="removing_ecps"></span><span id="REMOVING_ECPS"></span>Removing ECPs

Your file system filter driver can follow these steps to remove ECPs for the [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) operation:

1.  Call the [**FltRemoveExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff544339) or [**FsRtlRemoveExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff547203) routine to search an ECP list for an ECP context structure. If the ECP context structure is found, the routine detaches the ECP context structure from the ECP list.

2.  To free the memory for the detached ECP context structure, call the [**FltFreeExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff542957) or [**FsRtlFreeExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545989) routine. You can call these routines to free memory for the ECP context structure if you have allocated the memory in one of the following ways:
    -   You called the [**FltAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff541728) or [**FsRtlAllocateExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545609) routine to allocate paged memory pool
    -   You called the [**FltAllocateExtraCreateParameterFromLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff541734) or [**FsRtlAllocateExtraCreateParameterFromLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545616) routine to allocate memory pool from a lookaside list

### <span id="Marking_ECPs_as_Acknowledged__or_Determining_Acknowledge_Status"></span><span id="marking_ecps_as_acknowledged__or_determining_acknowledge_status"></span><span id="MARKING_ECPS_AS_ACKNOWLEDGED__OR_DETERMINING_ACKNOWLEDGE_STATUS"></span>Marking ECPs as Acknowledged, or Determining Acknowledge Status

Your file system filter driver can call the following routines to either mark ECPs as acknowledged or determine whether the ECPs are marked as acknowledged:

-   Call the [**FltAcknowledgeEcp**](https://msdn.microsoft.com/library/windows/hardware/ff541661) or [**FsRtlAcknowledgeEcp**](https://msdn.microsoft.com/library/windows/hardware/ff545574) routine to mark an ECP context structure as acknowledged. The ECP can be marked as looked at, used, processed, or any other condition of the ECP.

-   Call the [**FltIsEcpAcknowledged**](https://msdn.microsoft.com/library/windows/hardware/ff543321) or [**FsRtlIsEcpAcknowledged**](https://msdn.microsoft.com/library/windows/hardware/ff546808) routine to determine whether an ECP context structure is marked as acknowledged.

### <span id="Determining_Origination_Mode"></span><span id="determining_origination_mode"></span><span id="DETERMINING_ORIGINATION_MODE"></span>Determining Origination Mode

Your file system filter driver can call the [**FltIsEcpFromUserMode**](https://msdn.microsoft.com/library/windows/hardware/ff543325) or [**FsRtlIsEcpFromUserMode**](https://msdn.microsoft.com/library/windows/hardware/ff546813) routine to determine whether an ECP context structure originated from user mode. A file system filter driver can refuse to accept an ECP context structure that originated from user mode.

### <span id="Using_Lookaside_Lists_to_Allocate_ECPs"></span><span id="using_lookaside_lists_to_allocate_ecps"></span><span id="USING_LOOKASIDE_LISTS_TO_ALLOCATE_ECPS"></span>Using Lookaside Lists to Allocate ECPs

Your file system filter driver can call the following routines to allocate ECPs from lookaside lists and to manage the lookaside lists and ECPs:

-   Call the [**FltInitExtraCreateParameterLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff543261) or [**FsRtlInitExtraCreateParameterLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff546102) routine to initialize a paged or nonpaged pool lookaside list that is used for the allocation of one or more ECP context structures of fixed size.

-   Call the [**FltDeleteExtraCreateParameterLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff541973) or [**FsRtlDeleteExtraCreateParameterLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545849) routine to free the lookaside list.

-   Call the [**FltAllocateExtraCreateParameterFromLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff541734) or [**FsRtlAllocateExtraCreateParameterFromLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545616) routine to allocate memory pool from the lookaside list for an ECP context structure and to generate a pointer to that structure.

-   Call the [**FltFreeExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff542957) or [**FsRtlFreeExtraCreateParameter**](https://msdn.microsoft.com/library/windows/hardware/ff545989) routine to free the memory for the ECP context structures.

 

 




