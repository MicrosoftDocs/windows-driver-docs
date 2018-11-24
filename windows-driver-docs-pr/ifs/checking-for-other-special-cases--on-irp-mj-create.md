---
title: Checking for Other Special Cases on IRP_MJ_CREATE
description: Checking for Other Special Cases on IRP_MJ_CREATE
ms.assetid: e6af44c2-fd39-469b-8530-cf88edb329f7
keywords:
- IRP_MJ_CREATE
- security checks WDK file systems , IRP_MJ_CREATE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking for Other Special Cases on IRP\_MJ\_CREATE


## <span id="ddk_checking_for_other_special_cases_on_irp_mj_create_if"></span><span id="DDK_CHECKING_FOR_OTHER_SPECIAL_CASES_ON_IRP_MJ_CREATE_IF"></span>


Other special case handling must occur during the IRP\_MJ\_CREATE handling within the file system if the caller does not have SeChangeNotifyPrivilege. For example, a file that can be opened by using its file ID or object ID may not allow the caller to obtain the path to that file, since the caller might not have traverse permission to get to the object by means of the directory tree structure.

The cases you may wish to consider in your file system:

-   **FILE\_OPEN\_BY\_FILE\_ID** — the name of the file should not be made available to the caller. Since this information (traverse permission) is only known during the create operation, and will not be available during a file information query call, information on traverse permission must be computed by the file system during the IRP\_MJ\_CREATE.

-   **SL\_OPEN\_TARGET\_DIRECTORY** — the target file might not exist and the directory must be checked for file creation access. If the target does exist, it might require a delete access check. Normally the delete access check is done at the time of the rename operation during IRP\_MJ\_SET\_INFORMATION processing.

-   **FILE\_SUPERSEDE** and **FILE\_OVERWRITE** — destructive operations require additional access rights, even if the caller did not explicitly request them. For example, a file system might require DELETE access in order to perform a supersede operation.

-   **FILE\_CREATE**, **FILE\_OPEN\_IF**, and **FILE\_OVERWRITE\_IF** — constructive operations require access to the parent directory where the new object is being created. This is a check on the containing directory, not on the object itself, and thus similar to the earlier code sample.

-   **SL\_FORCE\_ACCESS\_CHECK** — if this value is set in the I/O stack location, the check must be performed as if the call were from user mode, not kernel mode. Thus, calls to security monitor routines should specify **UserMode** even if the call originated within a kernel mode server.

-   *File/directory deletion* — this might be based upon the ACL state of the file (for example, FILE\_WRITE\_DATA access implicitly allows delete; if you can delete the data, you have effective delete permissions on the file) as well as the ACL state of the directory (FILE\_DELETE\_CHILD permission on the containing directory, for example).

The following code example demonstrates the special case handling for FILE\_SUPERSEDE and FILE\_OVERWRITE, both cases where additional access is implicitly required by the caller, even if it was not requested.

```cpp
{
ULONG NewAccess = Supersede ? DELETE : FILE_WRITE_DATA;
ACCESS_MASK AddedAccess = 0;
PACCESS_MASK DesiredAccess = 
    &IrpSp->Paramters.Create.SecurityContext->DesiredAccess;

//
// If the caller does not have restore privilege, they must have write
// access to the EA and attributes for overwrite or supersede.
//
if (0 == (AccessState->Flags & TOKEN_HAS_RESTORE_PRIVILEGE)) {
    *DesiredAccess |= FILE_WRITE_EA | FILE_WRITE_ATTRIBUTES;

    //
    // Does the caller already have this access?
    //
    if (AccessState->PreviouslyGrantedAccess & NewAccess) {

        //
        // No - they need this as well
        //
        *DesiredAccess |= NewAccess;

    }

    //
    // Now check access using SeAccessCheck (omitted)
    //

}
```

This code sample is a good example of where file system policy takes precedence. The caller did not request DELETE access or FILE\_WRITE\_DATA access, but such access is inherent in the operation being performed based upon the semantics of the file system.

 

 




