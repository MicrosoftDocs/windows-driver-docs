---
title: Create Processing
description: Create Processing
ms.assetid: c15a56d2-47db-4124-8250-f25f69d2d4e3
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , create processing
- create processing WDK file systems
- Security Reference Monitor WDK
- IRP_MJ_CREATE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Create Processing


## <span id="ddk_create_processing_if"></span><span id="DDK_CREATE_PROCESSING_IF"></span>


For a file system, most of the interesting security work occurs during [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) processing. It is this step that must analyze the incoming request, determine whether the caller has appropriate rights to perform the operation, and grant or deny the operation as appropriate. Fortunately, for file system developers, most of the decision mechanism is implemented within the Security Reference Monitor. Thus, in most cases, the file system need only call the appropriate Security Reference Monitor routines to properly determine access. The risk for a file system occurs when it fails to call these routines as necessary and inappropriately grants access to a caller.

For a standard file system, such as the FAT file system, the checks that are made as part of IRP\_MJ\_CREATE are primarily semantics checks. For example, the FAT file system has numerous checks to ensure that IRP\_MJ\_CREATE processing is allowed based upon the state of the file or directory. These checks made by the FAT file system include checks for read-only media (for example, attempts to perform destructive "create" operations, such as overwrite or supersede, on read-only media are not allowed), share access checks, and oplock checks. One of the most difficult parts of this analysis is to realize that an operation at one level (the file level, for example) may in fact be disallowed because of the state of a different level resource (the volume level, for example). For example, a file may not be opened if another process has exclusively locked the volume. Common cases to check would include:

-   Is the file level open compatible with the volume level state? Volume-level locking must be obeyed. Thus, if one process holds an exclusive volume level lock, only threads within that process can open files. Threads from other processes must not be allowed to open files.

-   Is the file level open compatible with the media state? Certain "create" operations modify the file as part of the "create" operation. This would include overwrite, supersede, and even updating the last access time on the file. These "create" operations are not allowed on read-only media and the last access time is not updated.

-   Is the volume level open compatible with the file level state? An exclusive volume open would not be allowed if there are existing files opened on the volume. This is a common problem for new developers because they attempt to open the volume and find that it fails. When this fails, FSCTL\_DISMOUNT\_VOLUME can be used to invalidate open handles and force a dismount, allowing exclusive access to the newly mounted volume.

In addition, file attributes must be compatible. A file with the read-only attribute cannot be opened for write access. Note that the desired access should be checked after expansion of the generic rights are expanded. For example, this check within the FASTFAT file system is in the **FatCheckFileAccess** function (see the Acchksup.c source file from the fastfat samples that the WDK contains).

The following code example is specific to the FAT semantics. A file system that implements DACLs as well, would do an additional security check using the Security Reference Monitor routines ([**SeAccessCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563674), for example.)

```cpp
    //
    //  check for a read-only Dirent
    //

    if (FlagOn(DirentAttributes, FAT_DIRENT_ATTR_READ_ONLY)) {

        //
        //  Check the desired access for a read-only Dirent
        // Don&#39;t allow 
        //  WRITE, FILE_APPEND_DATA, FILE_ADD_FILE,
        //  FILE_ADD_SUBDIRECTORY, and FILE_DELETE_CHILD
        //

        if (FlagOn(*DesiredAccess, ~(DELETE |
                                     READ_CONTROL |
                                     WRITE_OWNER |
                                     WRITE_DAC |
                                     SYNCHRONIZE |
                                     ACCESS_SYSTEM_SECURITY |
                                     FILE_READ_DATA |
                                     FILE_READ_EA |
                                     FILE_WRITE_EA |
                                     FILE_READ_ATTRIBUTES |
                                     FILE_WRITE_ATTRIBUTES |
                                     FILE_EXECUTE |
                                     FILE_LIST_DIRECTORY |
                                     FILE_TRAVERSE))) {

            DebugTrace(0, Dbg, "Cannot open readonly\n", 0);

            try_return( Result = FALSE );
        }
```

A more subtle check implemented by FASTFAT is to ensure that the access requested by the caller is something about which the FAT file system is aware (in the **FatCheckFileAccess** function in Acchksup.c from the fastfat sample that the WDK contains):

The following code example demonstrates an important concept for file system security. Check to ensure that what is passed to your file system does not fall outside the bounds of what you expect. The conservative and proper approach from the perspective of security is that if you do not understand an access request, you should reject that request.

```cpp
    //
    // Check the desired access for the object. 
    // Reject what we do not understand.
    // The model of file systems using ACLs is that
    // they do not type the ACL to the object that the 
    // ACL is on. 
    // Permissions are not checked for consistency vs.
    // the object type - dir/file.
    //

    if (FlagOn(*DesiredAccess, ~(DELETE |
                                 READ_CONTROL |
                                 WRITE_OWNER |
                                 WRITE_DAC |
                                 SYNCHRONIZE |
                                 ACCESS_SYSTEM_SECURITY |
                                 FILE_WRITE_DATA |
                                 FILE_READ_EA |
                                 FILE_WRITE_EA |
                                 FILE_READ_ATTRIBUTES |
                                 FILE_WRITE_ATTRIBUTES |
                                 FILE_LIST_DIRECTORY |
                                 FILE_TRAVERSE |
                                 FILE_DELETE_CHILD |
                                 FILE_APPEND_DATA))) {

        DebugTrace(0, Dbg, "Cannot open object\n", 0);

        try_return( Result = FALSE );
    }
```

Fortunately for file systems, once the security check has been done during the initial create processing, subsequent security checks are performed by the I/O manager. Thus, for example, the I/O manager ensures that user-mode applications do not perform a write operation against a file that has been opened only for read access. In fact, a file system should not attempt to enforce read-only semantics against the file object, even if it was opened only for read access, during the IRP\_MJ\_WRITE dispatch routine. This is due to the way the memory manager associates a specific file object with a given section object. Subsequent writing through that section will be sent as IRP\_MJ\_WRITE operations on the file object, even though the file was opened read-only. In other words, the access enforcement is done when a file handle is converted into the corresponding file object at Nt system service entry points by [**ObReferenceObjectByHandle**](https://msdn.microsoft.com/library/windows/hardware/ff558679).

There are two additional places within a file system where semantic security checks must be made similar to "create" processing:

-   During rename or hard link processing.

-   When processing file system control operations.

Rename processing and file system control processing is discussed in subsequent sections.

Note that this is not an exhaustive list of semantic issues related to "create" processing. The intent of this section is to draw attention to these issues for file system developers. All semantic issues must be identified for a specific file system, implemented to meet the specific semantics, and tested to ensure that the implementation handles the various cases.

 

 




