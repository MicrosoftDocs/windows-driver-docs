---
title: Checking for Traverse Privilege on IRP_MJ_CREATE
description: Checking for Traverse Privilege on IRP_MJ_CREATE
keywords:
- IRP_MJ_CREATE
- traverse privileges WDK file systems
- security checks WDK file systems , IRP_MJ_CREATE
- privileges WDK file systems
- paths WDK file systems
- generic security checks WDK file systems
- SeChangeNotifyPrivilege
ms.date: 03/16/2022
---

# Checking for Traverse Privilege on IRP_MJ_CREATE

One of the primary concerns [**IRP_MJ_CREATE**](./irp-mj-create.md) checks is whether the caller has *traverse [privilege](privileges.md)*, which is the right to access the path to an object. That is, a caller can have access to a file object such as *dirA/dirB/file*, but not have permission to access the contents of the directories along that file object's path (*dirA* and *dirA/dirB*).

By default, Windows grants traverse privilege to all users. The "User Right" constant is [**SeChangeNotifyPrivilege**](/windows/win32/secauthz/privilege-constants), which maps to [**FILE_TRAVERSE**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatefile) in an [**ACCESS_MASK**](access-mask.md). As a security feature, system administrators can remove traverse privilege from a user.

Since most callers do have traverse privilege, one of the first checks that the file system normally does is to check for this privilege in the [**AccessState->Flags**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) field of the IRP's security context:

```cpp
    BOOLEAN traverseCheck = 
        !(IrpContext->IrpSp->Parameters.Create.SecurityContext->AccessState->Flags
            & TOKEN_HAS_TRAVERSE_PRIVILEGE);
```

The file system uses **Flags** to track which access rights have been granted in the progress of an operation. The file system can then just quickly check the access state bits first, and avoid the expense of an access check call if access has already been granted (**traverseCheck** = 0).

If traverse privilege has not previously been granted, the file system must do a traverse check on each directory along the path to the file being opened. In the partial code snippet below, the traverse check is done using a generic routine, typically used for most security checks:

```cpp

{
// accessParams is passed to the file system and is normally based
// on the fields of the same name from the IRP.

// Only one thread can be looking at this data structure in memory
// at a time (and potentially changing it), so acquire a lock on it.

    SeLockSubjectContext(
        &accessParams.AccessState->SubjectSecurityContext);

// Check whether the desired access can be granted.
// For this example, assume desiredAccess = FILE_TRAVERSE

    granted = SeAccessCheck( Fcb->SecurityDescriptor,
        &AccessParams.AccessState->SubjectSecurityContext,
        TRUE,
        AccessParams.desiredAccess,
        0,
        &Privileges,
        IoGetFileObjectGenericMapping(),
        AccessParams.AccessMode,
        &AccessParams.GrantedAccess,
        &AccessParams.status );

    // The file system uses AccessState to cache access privileges
    // that have been granted thus far along the operation's code
    // path. Update AccessState with the newly acquired Privileges.
    
    if (Privileges != NULL) {

        (void) SeAppendPrivileges(AccessParams.AccessState, Privileges );
        SeFreePrivileges( Privileges );
        Privileges = NULL;
    }

    if (granted) {
        //
        // The desired access was granted, so clear the
        // granted bits from desiredAccess. 
        //
        AccessParams.desiredAccess &= 
            ~(AccessParams.GrantedAccess | MAXIMUM_ALLOWED);
 
        if (!checkOnly) {
        //
        // The caller wants to modify the access state for this 
        // request
        //
            AccessParams.AccessState->PreviouslyGrantedAccess |= 
                AccessParams.GrantedAccess;

        if (maxDesired) {

            maxDelete = 
                (BOOLEAN)(AccessParams.AccessState->PreviouslyGrantedAccess & 
                    DELETE);
            maxReadAttr = 
                (BOOLEAN)(AccessParams.AccessState->PreviouslyGrantedAccess & 
                    FILE_READ_ATTRIBUTES);
        }
        AccessParams.AccessState->RemainingDesiredAccess &= 
            ~(AccessParams.GrantedAccess | MAXIMUM_ALLOWED);
    }

    // Release the lock on the security context
    SeUnlockSubjectContext(&accessParams.AccessState->SubjectSecurityContext);  
}
```

This function performs a generic security check. This function must deal with the following issues in doing so:

- It must specify the correct security descriptor to use for the check.

- It must pass along the security context (these are the credentials of the entity performing the operation).

- It must update the access state based upon the results of the security check.

- It must account for the MAXIMUM_ALLOWED option (see *ntifs.h*). The MAXIMUM_ALLOWED option specifies that the file system should set the access to the maximum possible access allowed by the file system (read/write/delete, for example). Very few applications use the MAXIMUM_ALLOWED option because this option is not supported on the FASTFAT file system. Because the MAXIMUM_ALLOWED option bit is not one of the access bits that the FASTFAT file system recognizes, it rejects access requests to the given file. An application that attempts to open a file on a FASTFAT volume with the MAXIMUM_ALLOWED option set will find that the request fails. For details, see the **FatCheckFileAccess** function in the Acchksup.c source file of the FASTFAT sample code that the WDK contains.

Note that for a simple traverse check, the requested access would be **FILE_TRAVERSE** and the security descriptor would be that of the directory through which the caller is attempting to traverse, not the requested access from the original **IRP_MJ_CREATE** IRP.
