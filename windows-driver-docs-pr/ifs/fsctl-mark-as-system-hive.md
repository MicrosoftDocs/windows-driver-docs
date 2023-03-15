---
title: FSCTL_MARK_AS_SYSTEM_HIVE control code
description: The FSCTL_MARK_AS_SYSTEM_HIVE control code informs the file system that the specified file contains the registry's system hive.
keywords: ["FSCTL_MARK_AS_SYSTEM_HIVE control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_MARK_AS_SYSTEM_HIVE
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_MARK_AS_SYSTEM_HIVE control code

The **FSCTL_MARK_AS_SYSTEM_HIVE** control code informs the file system that the specified file contains the registry's system hive. The file system must flush system hive data to disk at just the right moment to avoid deadlocks and to ensure data integrity. Do not use this file system control code with any file other than the file that contains the registry's system hive. This control code does not work with a directory or volume handle. File system redirectors that access files on remote machines treat this control code as a no-op.

Only kernel-level components can use this filesystem control code.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. File object pointer for the user file. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. Handle for the user file. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: The control code for the operation. Use **FSCTL_MARK_AS_SYSTEM_HIVE** for this operation.

- **InputBuffer** [in]: Not used. Assign a value of **NULL** to this parameter.

- **InputBufferLength** [in]: Not used.

- **OutputBuffer** [out]: Not used. Assign a value of **NULL** to this parameter.

- **OutputBufferLength** [out]: Not used.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function returns the appropriate NTSTATUS error code.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h*) |
