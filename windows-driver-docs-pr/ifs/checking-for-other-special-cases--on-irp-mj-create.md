---
title: Checking for Other Special Cases on IRP\_MJ\_CREATE
author: windows-driver-content
description: Checking for Other Special Cases on IRP\_MJ\_CREATE
ms.assetid: e6af44c2-fd39-469b-8530-cf88edb329f7
keywords: ["IRP_MJ_CREATE", "security checks WDK file systems , IRP_MJ_CREATE"]
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

```
{
ULONG NewAccess = Supersede ? DELETE : FILE_WRITE_DATA;
ACCESS_MASK AddedAccess = 0;
PACCESS_MASK DesiredAccess = 
    &amp;IrpSp->Paramters.Create.SecurityContext->DesiredAccess;

//
// If the caller does not have restore privilege, they must have write
// access to the EA and attributes for overwrite or supersede.
//
if (0 == (AccessState->Flags &amp; TOKEN_HAS_RESTORE_PRIVILEGE)) {
    *DesiredAccess |= FILE_WRITE_EA | FILE_WRITE_ATTRIBUTES;

    //
    // Does the caller already have this access?
    //
    if (AccessState->PreviouslyGrantedAccess &amp; NewAccess) {

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Checking%20for%20Other%20Special%20Cases%20%20on%20IRP_MJ_CREATE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


