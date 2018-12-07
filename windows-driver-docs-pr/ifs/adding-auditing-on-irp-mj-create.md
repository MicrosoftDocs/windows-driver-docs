---
title: Adding Auditing on IRP_MJ_CREATE
description: Adding Auditing on IRP_MJ_CREATE
ms.assetid: cb71fe83-44f4-48dd-8fff-250f1d27c123
keywords:
- IRP_MJ_CREATE
- auditing WDK file systems
- security checks WDK file systems , IRP_MJ_CREATE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Auditing on IRP\_MJ\_CREATE


## <span id="ddk_adding_auditing_on_irp_mj_create_if"></span><span id="DDK_ADDING_AUDITING_ON_IRP_MJ_CREATE_IF"></span>


Another important aspect of the security checks within a file system is to add auditing (if necessary). Typically, this is done as part of the same set of routines that make security decisions, since the purpose of auditing is to record the security decisions made by the system. For example, the following code could be used to implement auditing within a file system after completing the access checks:

```cpp
{
UNICODE_STRING FileAuditObjectName;

RtlInitUnicodeString(&FileAuditObjectName, L"File");

if ( SeAuditingFileOrGlobalEvents (AccessGranted, 
        &Fcb->SecurityDescriptor, 
        &AccessState->SubjectSecurityContext)) {
    //
    // Must pass complete Windows path name, including device name.
    //
    ConstructAuditFileName(Irp, Fcb, &AuditName);

    if (IrpSp->Parameters.Create.SecurityContext->FullCreateOptions 
            & FILE_DELETE_ON_CLOSE) {
        SeOpenObjectForDeleteAuditAlarm(&FileAuditObjectName,
                                        NULL,
                                        &AuditName,
                                        &Fcb->SecurityDescriptor,
                                        AccessState,
                                        FALSE, // Object not created.
                                        // Was it  successful?  
                                        // Based on SeAccessCheck
                                        SeAccessCheckAccessGranted, 
                                        // UserMode or KernelMode
                                        EffectiveMode, 
                                        &AccessState->GenerateOnClose
                                        );
    } else {
        SeOpenObjectAuditAlarm(&FileAuditObjectName,
                               NULL,
                               &AuditName,
                               &Fcb->SecurityDescriptor,
                               AccessState,
                               FALSE, // object not created
                               // Was it successful?  
                               // Based on SeAccessCheck
                               AccessGranted, 
                               // UserMode or KernelMode
                               EffectiveMode, 
                               &AccessState->GenerateOnClose
                               );
    }

    //
    // Free file name here if needed.
    //
}
```

 

 




