---
title: Checking the Oplock State of an IRP_MJ_SET_INFORMATION operation
description: Checking the Oplock State of an IRP_MJ_SET_INFORMATION operation
ms.date: 11/25/2019
---

# Checking the Oplock State of an IRP_MJ_SET_INFORMATION operation

The following IRP_MJ_SET_INFORMATION operations check oplock state:

- FileEndOfFileInformation
- FileAllocationInformation
- FileValidDataLengthInformation
- FileRenameInformation
- FileShortNameInformation
- FileLinkInformation
- FileDispositionInformation

## Checking oplock state for FileEndOfFileInformation, FileAllocationInformation, and FileValidDataLengthInformation operations

This information applies when the following operations are being performed on a file or stream:

- A caller attempts to change the logical size of the stream. Note that when the cache manager's lazy writer thread attempts to set a new end of file, no oplock check is made. This is because the check is made previously when the real write request is received.

- A caller attempts to change the allocated size of the stream.

### Conditions for a Level 2 request type

- Always break to None.

- No acknowledgment is required; the operation proceeds immediately.

### Conditions for all other request types

- Break on IRP_MJ_SET_INFORMATION (for FileEndOfFileInformation, FileAllocationInformation, and FileValidDataLengthInformation) when the operation occurs on a FILE_OBJECT with an oplock key that differs from the key of the FILE_OBJECT that owns the oplock. If the oplock is broken, break to None.

- Acknowledgement requirements vary as follows:

  - Read request: No acknowledgment is required; the operation proceeds immediately.

  - Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (i.e., without waiting for the acknowledgment).

  - Level 1, Batch, Filter, Read-Write, and Read-Write-Handle requests: An acknowledgment must be received before the operation continues.

## Checking oplock state for FileRenameInformation, FileShortNameInformation, and FileLinkInformation operations

This information applies when the following operations are being performed on a file or stream:

- The file or stream is being renamed.

- A short name is being set for the file.

- A hard link is being created for the file. This affects oplock state if the new hard link is superseding an existing link to a different file, and the oplock exists on the link being superseded.

- An ancestor directory of the stream on which the oplock exists is being renamed, or the ancestor directory's short name is being set.

### Conditions for Level 1, Level 2, Read, and Read-Write operations

- The oplock is not broken.

- No acknowledgement is required, and the operation proceeds immediately.

### Conditions for Batch, Filter, Read-Handle, and Read-Write-Handle operations

- Break on IRP_MJ_SET_INFORMATION (for FileRenameInformation, FileShortNameInformation, and FileLinkInformation) when the operation occurs on a FILE_OBJECT with an oplock key that differs from the key of the FILE_OBJECT that owns the oplock. If the oplock is broken:

  - Batch and Filter requests break to None.

  - Read-Handle requests break to Read.

  - Read-Write-Handle requests break to Read-Write.

- An acknowledgment must be received before the operation continues.
  
## Checking oplock state for FileDispositionInformation operations

This information applies when a caller tries to delete the file.

- Break on IRP_MJ_SET_INFORMATION (for FileDispositionInformation) when the operation occurs on a FILE_OBJECT with an oplock key that differs from the key of the FILE_OBJECT that owns the oplock, **AND** when [FILE_DISPOSITION_INFORMATION](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information).DeleteFile is **TRUE****. If the oplock is broken:

  - Read-Handle requests break to Read.

  - Read-Write-Handle requests break to Read-Write.

- An acknowledgment must be received before the operation continues.
