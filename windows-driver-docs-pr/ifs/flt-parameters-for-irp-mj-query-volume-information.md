---
title: FLT_PARAMETERS for IRP_MJ_QUERY_VOLUME_INFORMATION union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_QUERY_VOLUME_INFORMATION.
keywords: ["FLT_PARAMETERS for IRP_MJ_QUERY_VOLUME_INFORMATION union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
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

# FLT_PARAMETERS for IRP_MJ_QUERY_VOLUME_INFORMATION union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_QUERY_VOLUME_INFORMATION**](irp-mj-query-volume-information.md).

## Syntax

``` C
typedef union _FLT_PARAMETERS {
  ...    ;
  struct {
    ULONG                                  Length;
    FS_INFORMATION_CLASS POINTER_ALIGNMENT FsInformationClass;
  } QueryVolumeInformation;
  PVOID  VolumeBuffer;
  ...    ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

## Members

- **QueryVolumeInformation**: Structure containing the following members.

- **Length**: Length, in bytes, of the buffer at **VolumeBuffer**.

- **FsInformationClass**: Type of volume information that the file system returns. One of the following:

  | Value | Meaning |
  | ----- | ------- |
  | FileFsAttributeInformation | Return a [**FILE_FS_VOLUME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_volume_information) that contains information about the volume, such as the volume label, serial number, and creation time. |
  | FileFsControlInformation | Return a [**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information) structure that contains file system control information about the volume. |
  | FileFsDeviceInformation | Return a [**FILE_FS_DEVICE_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_fs_device_information) structure that contains device information for the volume. |
  | FileFsDriverPathInformation | Return a [**FILE_FS_DRIVER_PATH_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_driver_path_information) structure that contains information about whether a specified driver is in the I/O path for the volume. The originator of the IRP_MJ_QUERY_VOLUME_INFORMATION request must store the name of the driver into the FILE_FS_DRIVER_PATH_INFORMATION structure before sending the IRP to the file system volume device stack. |
  | FileFsFullSizeInformation | Return a [**FILE_FS_FULL_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_full_size_information) structure that contains information about the total amount of space available on the volume. |
  | FileFsObjectIdInformation | Return a [**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information) structure that contains file-system-specific object ID information for the volume. Note that this is not the same as the (globally unique identifier [GUID]-based) unique volume name that the operating system assigns. |
  | FileFsSizeInformation | Return a [**FILE_FS_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_size_information) structure that contains information about the amount of space on the volume that is available to the user associated with the thread that originated the IRP_MJ_QUERY_VOLUME_INFORMATION request. |
  | FileFsVolumeInformation | Return a [**FILE_FS_VOLUME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_volume_information) that contains information about the volume, such as the volume label, serial number, and creation time. |
  | FileFsSectorSizeInformation | Return a [**FILE_FS_SECTOR_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_driver_path_information) structure that contains information about the physical and logical sector sizes of a volume. |

- **VolumeBuffer**: Pointer to the output buffer where the volume information is to be returned.

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for IRP_MJ_QUERY_VOLUME_INFORMATION operations contains the parameters for an IRP-based query-volume-information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an FLT_IO_PARAMETER_BLOCK structure.

IRP_MJ_QUERY_VOLUME_INFORMATION is an IRP-based operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FILE_FS_ATTRIBUTE_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_attribute_information)

[**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information)

[**FILE_FS_DEVICE_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_fs_device_information)

[**FILE_FS_DRIVER_PATH_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_driver_path_information)

[**FILE_FS_FULL_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_full_size_information)

[**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information)

**FILE_FS_SECTOR_SIZE_INFORMATION**
[**FILE_FS_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_size_information)

[**FILE_FS_VOLUME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_volume_information)

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**IRP_MJ_QUERY_INFORMATION**](irp-mj-query-information.md)

[**ZwQueryVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvolumeinformationfile)
