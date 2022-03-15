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
ms.date: 03/15/2022
---

# Checking for Traverse Privilege on IRP_MJ_CREATE

One of the primary concerns [**IRP_MJ_CREATE**](./irp-mj-create.md) checks is whether the caller has *traverse privilege*, which is the right to access the path to an object. For example, the caller can have access to a file object, but not have permission to access the directories along that file object's path.

Since most callers do have traverse privilege, one of the first checks that the file system normally does is to check for this privilege:

```cpp
    BOOLEAN traverseCheck = 
        !(IrpContext->IrpSp->Parameters.Create.SecurityContext->AccessState->Flags
            & TOKEN_HAS_TRAVERSE_PRIVILEGE);
```

This traverse privilege check relies on the state information passed to the file system from the I/O manager, and is based on whether the caller holds [**SeChangeNotifyPrivilege**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_se_exports). If the caller does not hold **SeChangeNotifyPrivilege**, the file system must do a traverse check on each directory along the object's path. In the example below, the traverse check is done using a generic routine, typically used for most security checks:

{

```cpp
    SeLockSubjectContext(
        &accessParams.AccessState->SubjectSecurityContext);
//
// WHO IS "US"?

// Note: AccessParams is passed to us and is normally based on
//       the fields of the same name from the IRP
//

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

    if (Privileges != NULL) {
        //

// WHY DOES A TRAVERSE CHECK REQUIRE CHANGING THE AccessState??

        // this changes the AccessState
        //
        (void) SeAppendPrivileges(AccessParams.AccessState, Privileges );
        SeFreePrivileges( Privileges );
        Privileges = NULL;
    }

//
    if (granted) {
        //
        // delete granted bits from desired bits
        //
        AccessParams.desiredAccess &= 
            ~(AccessParams.GrantedAccess | MAXIMUM_ALLOWED);
 
        if (!checkOnly) {
        //
        // the caller wants to modify the access state for this 
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
            ~(AaccessParams.GrantedAccess | MAXIMUM_ALLOWED);
    }
    SeUnlockSubjectContext(&accessParams.AccessState->SubjectSecurityContext);  
}
```

This function performs a generic security check. This function must deal with the following issues in doing so:

- It must specify the correct security descriptor to use for the check.

- It must pass along the security context (these are the credentials of the entity performing the operation).

- It must update the access state based upon the results of the security check.

- It must account for the MAXIMUM_ALLOWED option (see *ntifs.h include file that the WDK includes for details). The MAXIMUM_ALLOWED option specifies that the file system should set the access to the maximum possible access allowed by the file system (read/write/delete, for example). Very few applications use the MAXIMUM_ALLOWED option because this option is not supported on the FASTFAT file system. Because the MAXIMUM_ALLOWED option bit is not one of the access bits that the FASTFAT file system recognizes, it rejects access requests to the given file. An application that attempts to open a file on a FASTFAT volume with the MAXIMUM_ALLOWED option set will find that the request fails. For details, see the **FatCheckFileAccess** function in the Acchksup.c source file of the FASTFAT sample code that the WDK contains.

Note that for a simple traverse check, the requested access would be FILE_TRAVERSE and the security descriptor would be that of the directory through which the caller is attempting to traverse, not the requested access from the original IRP_MJ_CREATE IRP.
