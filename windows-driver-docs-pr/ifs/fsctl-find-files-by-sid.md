---
title: FSCTL_FIND_FILES_BY_SID control code
description: The FSCTL_FIND_FILES_BY_SID control code searches a directory for a file whose creator and owner matche the specified SID.
keywords: ["FSCTL_FIND_FILES_BY_SID control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_FIND_FILES_BY_SID
api_type:
- NA
ms.date: 01/04/2022
---

# FSCTL_FIND_FILES_BY_SID control code

The FSCTL_FIND_FILES_BY_SID control code searches a directory for a file whose creator and owner matches the specified security ID (SID).

To perform this operation, minifilter drivers call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) and file systems, redirectors, and legacy file system filter drivers call [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

*FileObject*  
[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file object pointer for the directory to search. This parameter is required and cannot be **NULL**.

*FileHandle*  
[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The file handle for the directory to search. This parameter is required and cannot be **NULL**.

*FsControlCode*  
A control code for the operation. Use FSCTL_FIND_FILES_BY_SID for this operation.

*InputBuffer*  
A pointer to an input buffer that is described by the [**FIND_BY_SID_DATA**](/windows/win32/api/winioctl/ns-winioctl-find_by_sid_data) structure.

*InputBufferLength*  
The length, in bytes, of the buffer at *InputBuffer*.

*OutputBuffer*  
A pointer to a caller-allocated array of quad-aligned [**FIND_BY_SID_OUTPUT**](/windows/win32/api/winioctl/ns-winioctl-find_by_sid_output) structures that receive the fully qualified path names for each file.

*OutputBufferLength*  
Size, in bytes, of the data returned in the buffer that is pointed to by the *OutputBuffer* parameter.

## Remarks

When [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) and [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) process the **FSCTL_FIND_FILES_BY_SID** control code, these routines check every file and directory on the volume. This operation might be slow if there are many files on the volume, even if the directory to search is very small.

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**SID**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_sid)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))
