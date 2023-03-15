---
title: FLT_PARAMETERS for IRP_MJ_SET_VOLUME_INFORMATION union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_SET_VOLUME_INFORMATION.
keywords: ["FLT_PARAMETERS for IRP_MJ_SET_VOLUME_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FLT_PARAMETERS for IRP_MJ_SET_VOLUME_INFORMATION union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_SET_VOLUME_INFORMATION**](irp-mj-set-volume-information.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                  Length;
    FS_INFORMATION_CLASS POINTER_ALIGNMENT FsInformationClass;
    PVOID                                  VolumeBuffer;
  } SetVolumeInformation;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **SetVolumeInformation**: Structure containing the following members.

- **Length**: Length, in bytes, of the buffer at **VolumeBuffer**.

- **FsInformationClass**: Type of information to be set for the volume. One of the following:

| Value | Meaning |
| ----- | ------- |
| FileFsControlInformation | Set [**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information) for the volume. |
| FileFsLabelInformation | Set [**FILE_FS_LABEL_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_label_information) for the volume. |
| FileFsObjectIdInformation | Set [**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information) for the volume. |

- **VolumeBuffer**: Pointer to the input buffer that contains the values of the volume information to be set.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_SET_VOLUME_INFORMATION**](irp-mj-set-volume-information.md) operations contains the parameters for a set-volume-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_SET_VOLUME_INFORMATION is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information)

[**FILE_FS_LABEL_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_label_information)

[**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP_MJ_SET_VOLUME_INFORMATION**](irp-mj-set-volume-information.md)

[**ZwSetVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetvolumeinformationfile)
