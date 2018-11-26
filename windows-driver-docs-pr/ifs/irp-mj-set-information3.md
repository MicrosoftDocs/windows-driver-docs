---
title: IRP_MJ_SET_INFORMATION
description: IRP_MJ_SET_INFORMATION
ms.assetid: 2a6c837c-85c9-46d8-85d8-d779f22be54e
keywords:
- IRP_MJ_SET_INFORMATION
- security WDK file systems , adding security checks
- security checks WDK file systems , IRP_MJ_SET_INFORMATION
- rename operations WDK file systems
- hard link operations WDK file systems
- names WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_SET\_INFORMATION


The rename and hard link cases in set information might require a security check under certain circumstances. Specifically, if the caller wants to delete the target of the rename or hard link by setting the **ReplaceIfExists** field to **TRUE**, the file system must perform a security check to ensure that the caller has appropriate permission to delete the target. In addition, there can be certain types of files that the file system, as a matter of policy, does not wish to allow to be deleted in this fashion (registry hives and paging files, for example). The following code example determines if the caller has the appropriate security permissions to delete the file:

```cpp
NTSTATUS FsdCheckDeleteFileAccess(POW_IRP_CONTEXT IrpContext, 
                                  PSECURITY_DESCRIPTOR targetSD, 
                                  PFCB ParentFcb)
{
    SECURITY_SUBJECT_CONTEXT SubjectContext;
    BOOLEAN Granted;
    NTSTATUS status = STATUS_SUCCESS;
    PPRIVILEGE_SET Privileges = NULL;
    ACCESS_MASK GrantedAccess;

    //
    // See if the user has DELETE access to the target.
    //
    SeCaptureSubjectContext( &SubjectContext );

    SeLockSubjectContext( &SubjectContext );

    Granted = SeAccessCheck(targetSD,           // Target&#39;s SD.
                            &SubjectContext,    // Captured security context.
                            TRUE,               // Tokens are locked.
                            DELETE,             // we only care about delete 
                            0,                  // previously granted access.
                            &Privileges,        // privilege_set
                            IoGetFileObjectGenericMapping(), // Generic mappings.
                            UserMode,           // Mode
                            &GrantedAccess,     // Granted access mask
                            &status );          // Error code

    //
    // Do not need privilege set, so release it.
    //
    if (Privileges != NULL) { 

        SeFreePrivileges( Privileges ); 
        Privileges = NULL;
    }

    if (!Granted) {

        status = STATUS_SUCCESS;

        //
        // The user does not have DELETE access to the target, but 
        // could have FILE_DELETE_CHILD access to the parent directory.
        //
        (void) FsdLoadSecurityDescriptor(IrpContext, ParentFcb);
        if (!ParentFcb->SecurityDescriptor) {
            //
            // fine - no security is fine - he gets to do what he wants 
            //
            SeUnlockSubjectContext( &SubjectContext );
            SeReleaseSubjectContext( &SubjectContext );
            return STATUS_SUCCESS;
        }

 
        Granted = SeAccessCheck(&ParentFcb->SecurityDescriptor,
                                &SubjectContext,   // Captured security context.
                                TRUE,              // Tokens are locked.
                                FILE_DELETE_CHILD, // we only care about delete 
                                0,                 // Previously granted access.
                                &Privileges,       // privilege_set
                                IoGetFileObjectGenericMapping(), // Generic mappings
                                UserMode,          // mode
                                &GrantedAccess,    // Granted access mask
                                &status );         // Error code
        //
        // Release privileges
        //
        if (Privileges != NULL) { 
            SeFreePrivileges( Privileges ); 
            Privileges = NULL;
        }
    }
    SeUnlockSubjectContext( &SubjectContext );
    SeReleaseSubjectContext( &SubjectContext );
    return status;
}
```

This code can be used for both the rename and hard link creation case.

Note that it is outside the scope of this document to discuss policy level code where the file system decides to disallow the delete based upon the type of file being deleted.

 

 




