---
title: Adding Auditing on IRP\_MJ\_CREATE
description: Adding Auditing on IRP\_MJ\_CREATE
ms.assetid: cb71fe83-44f4-48dd-8fff-250f1d27c123
keywords: ["IRP_MJ_CREATE", "auditing WDK file systems", "security checks WDK file systems , IRP_MJ_CREATE"]
---

# Adding Auditing on IRP\_MJ\_CREATE


## <span id="ddk_adding_auditing_on_irp_mj_create_if"></span><span id="DDK_ADDING_AUDITING_ON_IRP_MJ_CREATE_IF"></span>


Another important aspect of the security checks within a file system is to add auditing (if necessary). Typically, this is done as part of the same set of routines that make security decisions, since the purpose of auditing is to record the security decisions made by the system. For example, the following code could be used to implement auditing within a file system after completing the access checks:

```
{
UNICODE_STRING FileAuditObjectName;

RtlInitUnicodeString(&amp;FileAuditObjectName, L"File");

if ( SeAuditingFileOrGlobalEvents (AccessGranted, 
        &amp;Fcb->SecurityDescriptor, 
        &amp;AccessState->SubjectSecurityContext)) {
    //
    // Must pass complete Windows path name, including device name.
    //
    ConstructAuditFileName(Irp, Fcb, &amp;AuditName);

    if (IrpSp->Parameters.Create.SecurityContext->FullCreateOptions 
            &amp; FILE_DELETE_ON_CLOSE) {
        SeOpenObjectForDeleteAuditAlarm(&amp;FileAuditObjectName,
                                        NULL,
                                        &amp;AuditName,
                                        &amp;Fcb->SecurityDescriptor,
                                        AccessState,
                                        FALSE, // Object not created.
                                        // Was it  successful?  
                                        // Based on SeAccessCheck
                                        SeAccessCheckAccessGranted, 
                                        // UserMode or KernelMode
                                        EffectiveMode, 
                                        &amp;AccessState->GenerateOnClose
                                        );
    } else {
        SeOpenObjectAuditAlarm(&amp;FileAuditObjectName,
                               NULL,
                               &amp;AuditName,
                               &amp;Fcb->SecurityDescriptor,
                               AccessState,
                               FALSE, // object not created
                               // Was it successful?  
                               // Based on SeAccessCheck
                               AccessGranted, 
                               // UserMode or KernelMode
                               EffectiveMode, 
                               &amp;AccessState->GenerateOnClose
                               );
    }

    //
    // Free file name here if needed.
    //
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Adding%20Auditing%20on%20IRP_MJ_CREATE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




