---
title: Checking for Traverse Privilege on IRP\_MJ\_CREATE
description: Checking for Traverse Privilege on IRP\_MJ\_CREATE
ms.assetid: 9ba743d6-8e78-4f9a-9cb8-cb98f734c290
keywords: ["IRP_MJ_CREATE", "traverse privileges WDK file systems", "security checks WDK file systems , IRP_MJ_CREATE", "privileges WDK file systems", "paths WDK file systems", "generic security checks WDK file systems", "SeChangeNotifyPrivilege"]
---

# Checking for Traverse Privilege on IRP\_MJ\_CREATE


## <span id="ddk_checking_for_traverse_privilege_on_irp_mj_create_if"></span><span id="DDK_CHECKING_FOR_TRAVERSE_PRIVILEGE_ON_IRP_MJ_CREATE_IF"></span>


One of the primary concerns [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) checks is whether the caller has traverse privilege (does the caller have the right to access the path to the object). Since most callers have traverse privilege, one of the first checks normally done within the file system is checking for the traverse privilege:

```
    BOOLEAN traverseCheck = 
        !(IrpContext->IrpSp->Parameters.Create.SecurityContext->AccessState->Flags
            &amp; TOKEN_HAS_TRAVERSE_PRIVILEGE);
```

Note that the traverse privilege check relies upon the state information passed to the file system from the I/O manager. This information is based upon whether the caller holds SeChangeNotifyPrivilege. If the caller does not hold this privilege, a traverse check must be done on each directory. In the example below, the traverse check is done using a generic routine, typically used for most security checks:

{

```
    SeLockSubjectContext(
        &amp;accessParams.AccessState->SubjectSecurityContext);
//
// Note: AccessParams is passed to us and is normally based on
//       the fields of the same name from the IRP
//

    granted = SeAccessCheck( Fcb->SecurityDescriptor,
        &amp;AccessParams.AccessState->SubjectSecurityContext,
        TRUE,
        AccessParams.desiredAccess,
        0,
        &amp;Privileges,
        IoGetFileObjectGenericMapping(),
        AccessParams.AccessMode,
        &amp;AccessParams.GrantedAccess,
        &amp;AccessParams.status );

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
        AccessParams.desiredAccess &amp;= 
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
                (BOOLEAN)(AccessParams.AccessState->PreviouslyGrantedAccess &amp; 
                    DELETE);
            maxReadAttr = 
                (BOOLEAN)(AccessParams.AccessState->PreviouslyGrantedAccess &amp; 
                    FILE_READ_ATTRIBUTES);
        }
        AccessParams.AccessState->RemainingDesiredAccess &amp;= 
            ~(AaccessParams.GrantedAccess | MAXIMUM_ALLOWED);
    }
    SeUnlockSubjectContext(&amp;accessParams.AccessState->SubjectSecurityContext);  
}
```

This function performs a generic security check. This function must deal with the following issues in doing so:

-   It must specify the correct security descriptor to use for the check.

-   It must pass along the security context (these are the credentials of the entity performing the operation).

-   It must update the access state based upon the results of the security check.

-   It must account for the MAXIMUM\_ALLOWED option (see the ntifs.h include file that the WDK includes for details). The MAXIMUM\_ALLOWED option specifies that the file system should set the access to the maximum possible access allowed by the file system (read/write/delete, for example). Very few applications use the MAXIMUM\_ALLOWED option because this option is not supported on the FASTFAT file system. Because the MAXIMUM\_ALLOWED option bit is not one of the access bits that the FASTFAT file system recognizes, it rejects access requests to the given file. An application that attempts to open a file on a FASTFAT volume with the MAXIMUM\_ALLOWED option set will find that the request fails. For details, see the **FatCheckFileAccess** function in the Acchksup.c source file of the FASTFAT sample code that the WDK contains.

Note that for a simple traverse check, the requested access would be FILE\_TRAVERSE and the security descriptor would be that of the directory through which the caller is attempting to traverse, not the requested access from the original IRP\_MJ\_CREATE IRP.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Checking%20for%20Traverse%20Privilege%20on%20IRP_MJ_CREATE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




