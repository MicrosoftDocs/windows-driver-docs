---
title: Checking for Traverse Privilege on IRP_MJ_CREATE
description: Checking for Traverse Privilege on IRP_MJ_CREATE
ms.assetid: 9ba743d6-8e78-4f9a-9cb8-cb98f734c290
keywords:
- IRP_MJ_CREATE
- traverse privileges WDK file systems
- security checks WDK file systems , IRP_MJ_CREATE
- privileges WDK file systems
- paths WDK file systems
- generic security checks WDK file systems
- SeChangeNotifyPrivilege
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking for Traverse Privilege on IRP\_MJ\_CREATE


## <span id="ddk_checking_for_traverse_privilege_on_irp_mj_create_if"></span><span id="DDK_CHECKING_FOR_TRAVERSE_PRIVILEGE_ON_IRP_MJ_CREATE_IF"></span>


One of the primary concerns [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) checks is whether the caller has traverse privilege (does the caller have the right to access the path to the object). Since most callers have traverse privilege, one of the first checks normally done within the file system is checking for the traverse privilege:

```cpp
    BOOLEAN traverseCheck = 
        !(IrpContext->IrpSp->Parameters.Create.SecurityContext->AccessState->Flags
            & TOKEN_HAS_TRAVERSE_PRIVILEGE);
```

Note that the traverse privilege check relies upon the state information passed to the file system from the I/O manager. This information is based upon whether the caller holds SeChangeNotifyPrivilege. If the caller does not hold this privilege, a traverse check must be done on each directory. In the example below, the traverse check is done using a generic routine, typically used for most security checks:

{

```cpp
    SeLockSubjectContext(
        &accessParams.AccessState->SubjectSecurityContext);
//
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
        // this changes the AccessState
        //
        (void) SeAppendPrivileges(AccessParams.AccessState, Privileges );
        SeFreePrivileges( Privileges );
        Privileges = NULL;
    }

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

-   It must specify the correct security descriptor to use for the check.

-   It must pass along the security context (these are the credentials of the entity performing the operation).

-   It must update the access state based upon the results of the security check.

-   It must account for the MAXIMUM\_ALLOWED option (see the ntifs.h include file that the WDK includes for details). The MAXIMUM\_ALLOWED option specifies that the file system should set the access to the maximum possible access allowed by the file system (read/write/delete, for example). Very few applications use the MAXIMUM\_ALLOWED option because this option is not supported on the FASTFAT file system. Because the MAXIMUM\_ALLOWED option bit is not one of the access bits that the FASTFAT file system recognizes, it rejects access requests to the given file. An application that attempts to open a file on a FASTFAT volume with the MAXIMUM\_ALLOWED option set will find that the request fails. For details, see the **FatCheckFileAccess** function in the Acchksup.c source file of the FASTFAT sample code that the WDK contains.

Note that for a simple traverse check, the requested access would be FILE\_TRAVERSE and the security descriptor would be that of the directory through which the caller is attempting to traverse, not the requested access from the original IRP\_MJ\_CREATE IRP.

 

 




