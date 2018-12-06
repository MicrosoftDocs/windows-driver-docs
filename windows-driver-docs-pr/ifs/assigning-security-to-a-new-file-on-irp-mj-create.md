---
title: Assigning Security to a New File on IRP_MJ_CREATE
description: Assigning Security to a New File on IRP_MJ_CREATE
ms.assetid: f01a09c4-f71f-4b9e-99c8-9bc7ca5ca316
keywords:
- IRP_MJ_CREATE
- new file security WDK file systems
- security checks WDK file systems , IRP_MJ_CREATE
- security descriptors WDK file systems , new files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Assigning Security to a New File on IRP\_MJ\_CREATE


## <span id="ddk_assigning_security_to_a_new_file_on_irp_mj_create_if"></span><span id="DDK_ASSIGNING_SECURITY_TO_A_NEW_FILE_ON_IRP_MJ_CREATE_IF"></span>


The final task in create handling is assigning security to the new file. While the Windows security model supports inheritance (individual ACE entries are marked in such a way that they are inherited when new files or directories are created) this is implemented outside the file system. Thus, the bulk of the logic within the file system is dedicated to storing the new security descriptor. Here is a sample routine:

```cpp
NTSTATUS FsdAssignInitialSecurity( PIRP_CONTEXT IrpContext, 
        PFCB Fcb, PFCB Directory)
{
    NTSTATUS status = STATUS_SUCCESS;
    BOOLEAN CreateDir = ((IrpContext->IrpSp->Parameters.Create.Options
        & FILE_DIRECTORY_FILE)==FILE_DIRECTORY_FILE);
    PACCESS_STATE AccessState = 
    IrpContext->IrpSp->Parameters.Create.SecurityContext->AccessState;
    PSECURITY_DESCRIPTOR SecurityDescriptor = NULL;

    //
    // Make sure the parent directory&#39;s security descriptor is loaded.
    //
    (void) FsdLoadSecurityDescriptor(IrpContext, Directory);

    //
    // don&#39;t care about the return code here, as it is handled later
    //
    if (Directory->SecurityDescriptor == NULL) {

        //
        // If the parent has no security, then we are outside
        // of the normal Windows paradigm.
        //
        // The child (that is, the target of the create) will also have
        // a NULL SD.
        //
        // Note that you can always assign security to the file object 
        // explicitly at later on.
        //
        return STATUS_SUCCESS;

    }

    //
    // Now create the security descriptor.
    //
    status = SeAssignSecurity(Directory->SecurityDescriptor, 
                              AccessState->SecurityDescriptor,
                              &SecurityDescriptor, 
                              CreateDir, 
                              &AccessState->SubjectSecurityContext,
                              IoGetFileObjectGenericMapping(),
                              PagedPool);

    if (!NT_SUCCESS(status)) {

        return status;
    }

    //
    // Associate the SD with the file; use our own storage so when 
    // cleanup occurs it is unnecessary to know if the storage came from the 
    // security reference monitor.
     //
    Fcb->SecurityDescriptorLength = 
        RtlLengthSecurityDescriptor( SecurityDescriptor );
 
    Fcb->SecurityDescriptor = ExAllocatePoolWithTag(PagedPool, 
        Fcb->SecurityDescriptorLength, &#39;DSyM&#39;);

    if (!Fcb->SecurityDescriptor) {
        //
        // There is no paged pool.
        //
        SeDeassignSecurity(&SecurityDescriptor);
        Fcb->SecurityDescriptorLength = 0;
        return STATUS_NO_MEMORY;
    }

    RtlCopyMemory(Fcb->SecurityDescriptor, SecurityDescriptor, 
        Fcb->SecurityDescriptorLength);
 
    SeDeassignSecurity(&SecurityDescriptor);
 
    //
    // Store the SD persistently (this is file system specific).
    //
    (void) FsdStoreSecurityDescriptor(IrpContext, Fcb);

    return STATUS_SUCCESS;
}
```

Note that the logic of constructing the initial security descriptor (understanding inheritance, for example) is not handled within the file system. This is in keeping with the simple model for handling security descriptors within the file systems layer.

 

 




