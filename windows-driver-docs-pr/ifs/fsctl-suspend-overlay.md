---
title: FSCTL_SUSPEND_OVERLAY control code
description: The FSCTL_SUSPEND_OVERLAY control code suspends a backing source attached to a volume, preventing access to the backing source and allowing it to be modified or removed.
keywords: ["FSCTL_SUSPEND_OVERLAY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SUSPEND_OVERLAY
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_SUSPEND_OVERLAY control code

The **FSCTL_SUSPEND_OVERLAY** control code suspends a backing source attached to a volume, preventing access to the backing source and allowing it to be modified or removed.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

``` syntax
BOOL 
   WINAPI 
   DeviceIoControl( (HANDLE)       hDevice,         // handle to device
                    (DWORD)        FSCTL_SUSPEND_OVERLAY, // dwIoControlCode
                    (LPDWORD)      lpInBuffer,      // input buffer
                    (DWORD)        nInBufferSize,   // size of input buffer
                    (LPDWORD)      lpOutBuffer,     // output buffer
                    (DWORD)        nOutBufferSize,  // size of output buffer
                    (LPDWORD)      lpBytesReturned, // number of bytes returned
                    (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```

## Parameters

- **Instance** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

- **FileObject** [in]: [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file pointer object of the volume for which the overlay is updated. This parameter is required and cannot be NULL.

- **FileHandle** [in]: [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The handle of the volume for which the overlay is updated. This parameter is required and cannot be NULL.

- **FsControlCode** [in]: The control code for the operation. Use **FSCTL_SUSPEND_OVERLAY** for this operation.

- **InputBuffer** [in]: A pointer to the input buffer, which must contain a [**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info) structure. When required, additional provider specific data is included immediately after **WOF_EXTERNAL_INFO**. If the provider is a WIM file, a [**WIM_PROVIDER_SUSPEND_OVERLAY_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_suspend_overlay_input) structure is included after **WOF_EXTERNAL_INFO**.

- **InputBufferLength** [in]: Set to **sizeof**([**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info)) plus the size of any additional provider input data.

- **OutputBuffer** [out]: Not used. Set to NULL.

- **OutputBufferLength** [in]: Set to 0.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values.

| Code | Meaning |
| ---- | ------- |
| STATUS_ACCESS_DENIED | The requestor does not have administrative privileges. |
| STATUS_BUFFER_TOO_SMALL | The length of the input buffer pointed to by **InputBuffer**, and specified by **InputBufferLength**, is too small. |
| STATUS_INTERNAL_ERROR | The requested volume is not accessible. |
| STATUS_INVALID_DEVICE_REQUEST | The backing service is not present or not started. |

## Remarks

When the backing source to remove is a Windows Imaging Format (WIM) file, the input buffer will contain a [**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info) structure followed by a [**WIM_PROVIDER_SUSPEND_OVERLAY_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_suspend_overlay_input) structure. The *InputBufferLength* in this case will be **sizeof**(WOF_EXTERNAL_INFO) + **sizeof**([**WIM_PROVIDER_REMOVE_OVERLAY_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_remove_overlay_input)). The **DataSourceId** value in **WIM_PROVIDER_SUSPEND_OVERLAY_INPUT** must be for a WIM file previously added in an [**FSCTL_ADD_OVERLAY**](fsctl-add-overlay.md) request.

Additional backing providers will define their own specific input parameter structures.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |

## See also

[**FSCTL_REMOVE_OVERLAY**](fsctl-remove-overlay.md)

[**FSCTL_UPDATE_OVERLAY**](fsctl-update-overlay.md)

[**FSCTL_GET_EXTERNAL_BACKING**](fsctl-get-external-backing.md)

[**FSCTL_SET_EXTERNAL_BACKING**](fsctl-set-external-backing.md)
