---
title: IRP\_MJ\_QUERY\_SECURITY and IRP\_MJ\_SET\_SECURITY
author: windows-driver-content
description: IRP\_MJ\_QUERY\_SECURITY and IRP\_MJ\_SET\_SECURITY
ms.assetid: 64216496-55f0-4ad4-b475-341ed9eb6886
keywords: ["IRP_MJ_QUERY_SECURITY", "IRP_MJ_SET_SECURITY", "security WDK file systems , adding security checks", "security checks WDK file systems , IRP_MJ_SET_SECURITY", "security checks WDK file systems , IRP_MJ_QUERY_SECURITY", "security descriptors WDK file systems , security checking", "descriptors WDK file systems , security checking", "retrieving security descriptors", "querying security descriptors"]
---

# IRP\_MJ\_QUERY\_SECURITY and IRP\_MJ\_SET\_SECURITY


Fortunately for a file system, the actual storage and retrieval of security descriptors is relatively opaque. This is due to the nature of security descriptors in a self-relative format that does not require any understanding of the descriptor by the file system. Thus, processing a query operation is normally a very simple exercise. Here is an example from a file system implementation:

```
NTSTATUS FsdCommonQuerySecurity( PIRP_CONTEXT IrpContext)
{
    NTSTATUS status = STATUS_SUCCESS;
    PSECURITY_DESCRIPTOR LocalPointer;

    // Need to add code to lock the FCB here

    status = FsdLoadSecurityDescriptor(IrpContext, IrpContext->Fcb);
 
    if (NT_SUCCESS(status) ) {
 
        //
        // copy the SecurityDescriptor into the callers buffer
        // note that this copy can throw an exception that must be handled
        // (code to handle the exception was omitted here for brevity)
        //
        LocalPointer = IrpContext->Fcb->SecurityDescriptor;

        status = SeQuerySecurityDescriptorInfo(
     &amp;IrpContext->IrpSp->Parameters.QuerySecurity.SecurityInformation,
            (PSECURITY_DESCRIPTOR)IrpContext->Irp->UserBuffer,
            &amp;IrpContext->IrpSp->Parameters.QuerySecurity.Length,
            &amp;LocalPointer );
 
        //
        // CACLS utility expects OVERFLOW
        //
        if (status == STATUS_BUFFER_TOO_SMALL ) {
            status = STATUS_BUFFER_OVERFLOW;
        }
    }
 
    // Need to add code to unlock the FCB here

    return status;
}
```

Note that this routine relies on an external function to load the actual security descriptor from persistent storage (in this implementation, that routine only loads the security descriptor if it has not previously been loaded). Since the security descriptor is opaque to the file system, the security reference monitor must be used to copy the descriptor into the user's buffer. We note two points with respect to this code sample:

1.  The conversion of the error code STATUS\_BUFFER\_TOO\_SMALL into the warning code STATUS\_BUFFER\_OVERFLOW is necessary in order to provide correct behavior for some Windows security tools.

2.  Errors in handling the user buffer can, and will, arise because both query and set security operations are normally done using the user buffer directly. Note that this is controlled by the **Flags** member of the DEVICE\_OBJECT created by the file system. In a file system implementation based on this code, the calling function would need to use a \_\_try block to protect against an invalid user buffer.

The specifics of how the file system loads a security descriptor from storage (the **FsdLoadSecurityDescriptor** function in this example) will depend entirely on the implementation of security descriptor storage in the file system.

Storing a security descriptor is a bit more involved. File systems may need to determine whether the security descriptor matches an existing security descriptor if the file system supports security descriptor sharing. For non-matching security descriptors, the file system may need to allocate new storage for this new security descriptor. Below is a sample routine for replacing the security descriptor on a file.

```
NTSTATUS FsdCommonSetSecurity(PIRP_CONTEXT IrpContext)
{
    NTSTATUS status = STATUS_SUCCESS;
    PSECURITY_DESCRIPTOR SavedDescriptorPtr = 
        IrpContext->Fcb->SecurityDescriptor;
    ULONG SavedDescriptorLength = 
        IrpContext->Fcb->SecurityDescriptorLength;
    PSECURITY_DESCRIPTOR newSD = NULL;
    POW_FCB Fcb = IrpContext->Fcb;
    ULONG Information = IrpContext->Irp->IoStatus.Information;

    //
    // make sure that the FCB security descriptor is up to date
    //
    status = FsdLoadSecurityDescriptor(IrpContext, Fcb);

    if (!NT_SUCCESS(status)) {
      //
      // Something is seriously wrong 
      //
      IrpContext->Irp->IoStatus.Status = status;
      IrpContext->Irp->IoStatus.Information = 0;
      return status;
    }        
 
    status = SeSetSecurityDescriptorInfo(
       NULL,
       &amp;IrpContext->IrpSp->Parameters.SetSecurity.SecurityInformation,
       IrpContext->IrpSp->Parameters.SetSecurity.SecurityDescriptor,
       &amp;Fcb->SecurityDescriptor,
       PagedPool,
       IoGetFileObjectGenericMapping()
       );

    if (!NT_SUCCESS(status)) {

        //
        // restore things  and return
        //
        Fcb->SecurityDescriptorLength = SavedDescriptorLength;
        Fcb->SecurityDescriptor = SavedDescriptorPtr;
        IrpContext->Irp->IoStatus.Status = status;
        IrpContext->Irp->IoStatus.Information = 0;

        return status;
    }

    //
    // get the new length
    //
    Fcb->SecurityDescriptorLength = 
        RtlLengthSecurityDescriptor(Fcb->SecurityDescriptor);

    //
    // allocate our own private SD to replace the one from
    // SeSetSecurityDescriptorInfo so we can track our memory usage
    //
    newSD = ExAllocatePoolWithTag(PagedPool, 
        Fcb->SecurityDescriptorLength, &#39;DSyM&#39;);

    if (!newSD) {
 
      //
      // paged pool is empty
      //
      SeDeassignSecurity(&amp;Fcb->SecurityDescriptor);
      status = STATUS_NO_MEMORY;
      Fcb->SecurityDescriptorLength = SavedDescriptorLength;
      Fcb->SecurityDescriptor = SavedDescriptorPtr;
 
      //
      // make sure FCB security is in a valid state
      //
      IrpContext->Irp->IoStatus.Status = status;
      IrpContext->Irp->IoStatus.Information = 0;
 
      return status;
 
    } 
 
    //
    // store the new security on disk
    //
    status = FsdStoreSecurityDescriptor(IrpContext, Fcb);

    if (!NT_SUCCESS(status)) {
      //
      // great- modified the in-core SD but couldn&#39;t get it out
      // to disk. undo everything. 
      //
      ExFreePool(newSD);
      SeDeassignSecurity(&amp;Fcb->SecurityDescriptor);
      status = STATUS_NO_MEMORY;
      Fcb->SecurityDescriptorLength = SavedDescriptorLength;
      Fcb->SecurityDescriptor = SavedDescriptorPtr;
      IrpContext->Irp->IoStatus.Status = status;
      IrpContext->Irp->IoStatus.Information = 0;
 
      return status;
    }
 
    //
    // if we get here everything worked! 
    //
    RtlCopyMemory(newSD, Fcb->SecurityDescriptor, 
        Fcb->SecurityDescriptorLength);
 
    //
    // deallocate the security descriptor
    //
    SeDeassignSecurity(&amp;Fcb->SecurityDescriptor);
 
    //
    // this either is the new private SD or NULL if 
    // memory allocation failed
    //
    Fcb->SecurityDescriptor = newSD;

    //
    // free the memory from the previous descriptor
    //
    if (SavedDescriptorPtr) {
      //
      // this  must always be from private allocation
      //
      ExFreePool(SavedDescriptorPtr);
 
    }        
 
    IrpContext->Irp.IoStatus = status;
    IrpContext->Irp.Information = Information;

    return status;
}
```

Note that this is an area in which implementation varies dramatically from file system to file system. For example, a file system that supports security descriptor sharing would need to add explicit logic to find a matching security descriptor. This sample is only an attempt to provide guidance to implementers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_QUERY_SECURITY%20and%20IRP_MJ_SET_SECURITY%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


