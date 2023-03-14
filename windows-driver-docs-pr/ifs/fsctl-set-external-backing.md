---
title: FSCTL_SET_EXTERNAL_BACKING control code
description: The FSCTL_SET_EXTERNAL_BACKING control code sets the backing source for a file, such as a Windows Image Format (WIM) file or compressed file, by an external backing provider.
keywords: ["FSCTL_SET_EXTERNAL_BACKING control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_EXTERNAL_BACKING
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_SET_EXTERNAL_BACKING control code

The **FSCTL_SET_EXTERNAL_BACKING** control code sets the backing source for a file, such as a Windows Image Format (WIM) file or compressed file, by an external backing provider. Content for externally backed files may be sourced on volumes other than on volume where the file resides.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file pointer object of the file for which backing is set. This parameter is required and cannot be NULL.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The handle of the file for which backing is set. This parameter is required and cannot be NULL.

- **FsControlCode** [in]: The control code for the operation. Use **FSCTL_SET_EXTERNAL_BACKING** for this operation.

- **InputBuffer** [in]: A pointer to the input buffer, which contains [**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info) structure followed by the provider data. For WIM backed files, **WOF_EXTERNAL_INFO** is followed by a [**WIM_PROVIDER_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_external_info) structure.

- **InputBufferLength** [in]: Size of the data provided in the *InputBuffer*.

- **OutputBuffer** [out]: None. Set to NULL.

- **OutputBufferLength** [in]: Set to 0.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate NTSTATUS values is returned.

## Remarks

When the backing provider for the data source added is the WIM provider, the input buffer will contain a [**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info) structure followed by a [**WIM_PROVIDER_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_external_info) structure. The **InputBufferLength** in this case will be **sizeof**(**WOF_EXTERNAL_INFO**) + **sizeof**(**WIM_PROVIDER_EXTERNAL_INFO**).

Individually compressed files offer good compression for data which will not be modified, including executable files. If these are opened for write the file will be transparently decompressed. To specify an individually compressed file,, the input buffer will contain a [**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info) structure followed by a [**FILE_PROVIDER_EXTERNAL_INFO_V1**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_provider_external_info_v1) structure. The *InputBufferLength* in this case will be **sizeof**(**WOF_EXTERNAL_INFO**) + **sizeof**(**FILE_PROVIDER_EXTERNAL_INFO_V1**). Individual compressed files are available starting with Windows 10.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 8.1 Update |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

[**FSCTL_DELETE_EXTERNAL_BACKING**](fsctl-delete-external-backing.md)

[**FSCTL_GET_EXTERNAL_BACKING**](fsctl-get-external-backing.md)

[**WIM_PROVIDER_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_external_info)

[**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info)
