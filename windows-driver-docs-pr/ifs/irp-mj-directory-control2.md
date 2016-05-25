---
title: IRP\_MJ\_DIRECTORY\_CONTROL
author: windows-driver-content
description: IRP\_MJ\_DIRECTORY\_CONTROL
ms.assetid: 27c2de1c-5550-4211-97cc-4c66f18d3b99
keywords: ["IRP_MJ_DIRECTORY_CONTROL", "security WDK file systems , adding security checks", "security checks WDK file systems , IRP_MJ_DIRECTORY_CONTROL", "directory controls WDK file systems"]
---

# IRP\_MJ\_DIRECTORY\_CONTROL


Security is a consideration when processing certain directory control operations, notably those dealing with change notifications. The security concern is that a directory change notification might return information about specific files that have changed. If the user does not have the privilege to traverse the path to the directory, information about the change cannot be returned to the user. Otherwise, the user now has a mechanism for learning additional information about the directory that the user should not have.

Support for directory change notification by the file system run-time library allows a file system to specify a callback function for performing a traverse check before it returns a directory change notification. This callback function takes a large number of parameters. For security considerations, the following three parameters are important:

-   *NotifyContext*--the context of the directory where the change notification is active. This will be the *FsContext* parameter that is passed in to the call to **FsRtlNotifyFilterChangeDirectory**. Note that **FsRtlNotifyFilterChangeDirectory** is available on Windows XP and later. Windows 2000 systems used the **FsRtlNotifyFullChangeDirectory** function, which is similar.

-   *TargetContext*--the context of the file that has changed. This will be the *TargetContext* parameter passed by the file system when it calls **FsRtlNotifyFilterReportChange**.

-   *SubjectContext*--the security context of the thread requesting the directory change notification. This is the subject security context captured by the file system at the time the directory change notification call is made to **FsRtlNotifyFilterChangeDirectory**.

When a change occurs, the file system indicates this to the file system run-time library. The file system run-time library will then call the callback function provided by the file system to verify that the caller can be given information about the change. Note that the file system only needs to register a callback function if the check is required for the caller. This is the case if the caller does not have SeChangeNotifyPrivilege enabled, as indicated by the TOKEN\_HAS\_TRAVERSE\_PRIVILEGE in the caller's security token.

Inside the callback function, the file system must perform a traverse check from the directory specified by the *NotifyContext* parameter, to the file that changed, specified by the *TargetContext* parameter. The sample routine below performs such a check.

```
BOOLEAN 
FsdNotifyTraverseCheck ( 
    IN PDIRECTORY_CONTEXT OriginalDirectoryContext, 
    IN PFILE_CONTEXT ModifiedDirectoryContext,      
    IN PSECURITY_SUBJECT_CONTEXT SubjectContext
    )
{
  BOOLEAN AccessGranted = TRUE;
  PFILE_CONTEXT CurrentDirectoryContext;
  ACCESS_MASK GrantedAccess;
  NTSTATUS Status;
  PPRIVILEGE_SET Privileges = NULL;
  PFILE_CONTEXT TopDirectory;


  //
  //  Nothing to do  if there is no file context.
  //
  if (ModifiedDirectoryContext == NULL) {
 
    return TRUE;
  }
 
  //
  // If the directory that changed is the original directory, 
  // we can return , since the caller has access. 
  // Note that the directory  context is unique to the specific 
  // open instance, while the modified directory context 
  // represents the per-file/directory context. 
  // How these data structures work in your file system will vary.
  //
  if (OriginalDirectoryContext->FileContext == ModifiedDirectoryContext) {
    return TRUE;
  }
 
  //
  // Lock the subject context.
  //
  SeLockSubjectContext(SubjectContext);
 
 
  for( TopDirectory = OriginalDirectoryContext->FileContext,
          CurrentDirectoryContext = ModifiedDirectoryContext;
          CurrentDirectoryContext == TopDirectory || !AccessGranted;
          CurrentDirectoryContext = CurrentDirectoryContext->ParentDirectory) {
    //
    // Ensure we have the current security descriptor loaded for 
    // this directory.
    //
    FsdLoadSecurity( NULL, CurrentDirectoryContext);
 
    //
    // Perform traverse check.
    //
    AccessGranted = SeAccessCheck( 
            CurrentDirectoryContext->SecurityDescriptor,
            SubjectContext,
            TRUE,
            FILE_TRAVERSE,
            0,
            &amp;Privileges,
            IoGetFileObjectGenericMapping(),
            UserMode,
            &amp;GrantedAccess,
            &amp;Status);
 
    //
    // At this point, exit the loop if access was not granted, 
    // or if the parent directory is the same as where the change 
    // notification was made.
    //
 
  }
 
  //
  // Unlock subject context.
  //
  SeUnlockSubjectContext(SubjectContext);
 
  return AccessGranted;
}
```

This routine is likely to be substantially different for file systems that cache security information, or that have different data structures for tracking files and directories (for example, files that use a structure for tracking links between files and directories). File systems supporting links are not considered in this sample in an attempt to simplify the example.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_DIRECTORY_CONTROL%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


