---
title: FSCTL_LMR_GET_LINK_TRACKING_INFORMATION Control Code
description: The FSCTL_LMR_GET_LINK_TRACKING_INFORMATION control code retrieves the link tracking information for a file.
keywords: ["FSCTL_LMR_GET_LINK_TRACKING_INFORMATION control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_LMR_GET_LINK_TRACKING_INFORMATION
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_LMR_GET_LINK_TRACKING_INFORMATION control code

The **FSCTL_LMR_GET_LINK_TRACKING_INFORMATION** control code retrieves the link tracking information for a file.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. A file object pointer for the remote volume. This parameter is required and cannot be **NULL**.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. A handle for the remote volume. This parameter is required and cannot be **NULL**.

- **FsControlCode** [in]: A control code for the operation. Use **FSCTL_LMR_GET_LINK_TRACKING_INFORMATION** for this operation.

- **InputBuffer** [in]: None.

- **InputBufferLength** [in]: Not used.

- **OutputBuffer** [out]: A [**LINK_TRACKING_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-link_tracking_information) structure that contains the link tracking information of the file.

- **OutputBufferLength** [out]: The size, in bytes, of the buffer pointed to by **OutputBuffer**.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function returns the appropriate NTSTATUS error code.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h*) |
