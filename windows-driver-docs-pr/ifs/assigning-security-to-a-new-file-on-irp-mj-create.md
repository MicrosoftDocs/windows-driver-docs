---
title: Assigning Security to a New File on IRP\_MJ\_CREATE
description: Assigning Security to a New File on IRP\_MJ\_CREATE
ms.assetid: f01a09c4-f71f-4b9e-99c8-9bc7ca5ca316
keywords: ["IRP_MJ_CREATE", "new file security WDK file systems", "security checks WDK file systems , IRP_MJ_CREATE", "security descriptors WDK file systems , new files"]
---

# Assigning Security to a New File on IRP\_MJ\_CREATE


## <span id="ddk_assigning_security_to_a_new_file_on_irp_mj_create_if"></span><span id="DDK_ASSIGNING_SECURITY_TO_A_NEW_FILE_ON_IRP_MJ_CREATE_IF"></span>


The final task in create handling is assigning security to the new file. While the Windows security model supports inheritance (individual ACE entries are marked in such a way that they are inherited when new files or directories are created) this is implemented outside the file system. Thus, the bulk of the logic within the file system is dedicated to storing the new security descriptor. Here is a sample routine:

```
NTSTATUS FsdAssignInitialSecurity( PIRP_CONTEXT IrpContext, 
        PFCB Fcb, PFCB Directory)
{
    NTSTATUS status = STATUS_SUCCESS;
    BOOLEAN CreateDir = ((IrpContext->IrpSp->Parameters.Create.Options
        &amp; FILE_DIRECTORY_FILE)==FILE_DIRECTORY_FILE);
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
                              &amp;SecurityDescriptor, 
                              CreateDir, 
                              &amp;AccessState->SubjectSecurityContext,
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
        SeDeassignSecurity(&amp;SecurityDescriptor);
        Fcb->SecurityDescriptorLength = 0;
        return STATUS_NO_MEMORY;
    }

    RtlCopyMemory(Fcb->SecurityDescriptor, SecurityDescriptor, 
        Fcb->SecurityDescriptorLength);
 
    SeDeassignSecurity(&amp;SecurityDescriptor);
 
    //
    // Store the SD persistently (this is file system specific).
    //
    (void) FsdStoreSecurityDescriptor(IrpContext, Fcb);

    return STATUS_SUCCESS;
}
```

Note that the logic of constructing the initial security descriptor (understanding inheritance, for example) is not handled within the file system. This is in keeping with the simple model for handling security descriptors within the file systems layer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Assigning%20Security%20to%20a%20New%20File%20on%20IRP_MJ_CREATE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




