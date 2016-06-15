---
title: IRP\_MJ\_SET\_INFORMATION
author: windows-driver-content
description: IRP\_MJ\_SET\_INFORMATION
ms.assetid: d164be8d-cf42-4b96-9883-e0f8223bfde4
---

# IRP\_MJ\_SET\_INFORMATION


Certain IRP\_MJ\_SET\_INFORMATION operations check oplock state. The following six operations perform this check:

### <span id="FileEndOfFileInformation__FileAllocationInformation__and_FileValidDataLengthInformation"></span><span id="fileendoffileinformation__fileallocationinformation__and_filevaliddatalengthinformation"></span><span id="FILEENDOFFILEINFORMATION__FILEALLOCATIONINFORMATION__AND_FILEVALIDDATALENGTHINFORMATION"></span>FileEndOfFileInformation, FileAllocationInformation, and FileValidDataLengthInformation

This information applies when the following operations are being performed on a file or stream:

-   A caller attempts to change the logical size of the stream. Note that when the cache manager's lazy writer thread attempts to set a new end of file, no oplock check is made. This is because the check is made previously when the real write request is received.

-   A caller attempts to change the allocated size of the stream.

Request Type
Conditions
Level 1

Batch

Filter

Read-Handle

Read-Write

Read-Write-Handle

Broken on IRP\_MJ\_SET\_INFORMATION (for FileEndOfFileInformtion, FileAllocationInformation, and FileValidDataLengthInformation) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   For the Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (i.e., without waiting for the acknowledgment).

-   For all other request types: An acknowledgment must be received before the operation continues.

Read

Broken on IRP\_MJ\_SET\_INFORMATION (for FileEndOfFileInformtion, FileAllocationInformation, and FileValidDataLengthInformation) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   No acknowledgment is required, the operation proceeds immediately.

Level 2

-   Always break to None.

-   No acknowledgment is required, the operation proceeds immediately.

 

### <span id="FileRenameInformation__FileShortNameInformation__and_FileLinkInformation"></span><span id="filerenameinformation__fileshortnameinformation__and_filelinkinformation"></span><span id="FILERENAMEINFORMATION__FILESHORTNAMEINFORMATION__AND_FILELINKINFORMATION"></span>FileRenameInformation, FileShortNameInformation, and FileLinkInformation

This information applies when the following operations are being performed on a file or stream:

-   The file or stream is being renamed.

-   A short name is being set for the file.

-   A hard link is being created for the file. This affects oplock state if the new hard link is superseding an existing link to a different file, and the oplock exists on the link being superseded.

-   An ancestor directory of the stream on which the oplock exists is being renamed, or the ancestor directory's short name is being set.

Request Type
Conditions
Batch

Filter

Broken on IRP\_MJ\_SET\_INFORMATION (for FileRenameInformation, FileShortNameInformation, and FileLinkInformation) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   An acknowledgment must be received before the operation continues.

Read-Handle

Broken on IRP\_MJ\_SET\_INFORMATION (for FileRenameInformation, FileShortNameInformation, and FileLinkInformation) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to Read.

-   An acknowledgment must be received before the operation continues.

Read-Write-Handle

Broken on IRP\_MJ\_SET\_INFORMATION (for FileRenameInformation, FileShortNameInformation, and FileLinkInformation) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to Read-Write.

-   An acknowledgment must be received before the operation continues.

Level 1

Level 2

Read

Read-Write

-   The oplock is not broken, no acknowledgment is required, and the operation proceeds immediately.

 

### <span id="FileDispositionInformation"></span><span id="filedispositioninformation"></span><span id="FILEDISPOSITIONINFORMATION"></span>FileDispositionInformation

This information applies when a caller tries to delete the file.

Request Type
Conditions
Read-Handle

Broken on IRP\_MJ\_SET\_INFORMATION (for FileDispositionInformation) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

    **AND**

-   [**FILE\_DISPOSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545765).DeleteFile is **TRUE**.

If the oplock is broken:

-   Break to Read.

-   An acknowledgment must be received before the operation continues.

Read-Write-Handle

Broken on IRP\_MJ\_SET\_INFORMATION (for FileDispositionInformation) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

    **AND**

-   [**FILE\_DISPOSITION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545765).DeleteFile is **TRUE**.

If the oplock is broken:

-   Break to Read-Write.

-   An acknowledgment must be received before the operation continues.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_SET_INFORMATION%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


