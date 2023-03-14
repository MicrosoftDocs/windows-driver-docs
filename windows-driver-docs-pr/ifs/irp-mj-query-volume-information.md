---
title: IRP_MJ_QUERY_VOLUME_INFORMATION (FS and filter drivers)
description: IRP_MJ_QUERY_VOLUME_INFORMATION
keywords: ["IRP_MJ_QUERY_VOLUME_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_QUERY_VOLUME_INFORMATION
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_QUERY_VOLUME_INFORMATION (FS and filter drivers)

## When Sent

The I/O Manager sends the **IRP_MJ_QUERY_VOLUME_INFORMATION** request. It can be sent, for example, when a user-mode application has called a Win32 function such as [**GetDiskFreeSpace**](/windows/win32/api/fileapi/nf-fileapi-getdiskfreespacea) or **GetFileType**.

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine whether the target device object is the file system's control device object. If it is, and if the request has been issued on a handle that is a volume open (or an open of an object on the volume), the file system driver should process the request and complete the IRP.

Otherwise, the file system driver should fail the query and complete the IRP.

The types of volume information that can be queried are file-system-dependent, but generally include the following values:

- FileFsAttributeInformation
- FileFsDeviceInformation
- FileFsSizeInformation
- FileFsVolumeInformation

For a list of all possible information types, see **IrpSp->Parameters.QueryVolume.FsInformationClass**.

## Operation: Network Redirect Drivers

A network redirector that receives a request for FileFsDeviceInformation, must include FILE_REMOTE_DEVICE as one of the options for the **DeviceCharacteristics** member of the [**FILE_FS_DEVICE_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_fs_device_information) structure returned.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a query volume information request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied output buffer where the volume information is to be returned. This information is stored in one of the following structures:

  - FILE_FS_ATTRIBUTE_INFORMATION
  - FILE_FS_CONTROL_INFORMATION
  - FILE_FS_DEVICE_INFORMATION
  - FILE_FS_DRIVER_PATH_INFORMATION
  - FILE_FS_FULL_SIZE_INFORMATION
  - FILE_FS_OBJECTID_INFORMATION
  - FILE_FS_SIZE_INFORMATION
  - FILE_FS_VOLUME_FLAGS_INFORMATION
  - FILE_FS_VOLUME_INFORMATION
  - FILE_FS_SECTOR_SIZE_INFORMATION

  The FileFsVolumeFlagsInformation class and the associated [**FILE_FS_VOLUME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_volume_information) structure are available on Windows Vista and later versions.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **Irp->UserBuffer** is an optional pointer to a caller-supplied output buffer into which the contents of **Irp->AssociatedIrp.SystemBuffer** are copied during I/O completion by the I/O manager. Drivers don't use this buffer to return any data for the request.

- **IrpSp->FileObject** points to the file object that is associated with *DeviceObject*.

  The**IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of **IRP_MJ_QUERY_VOLUME_INFORMATION** and shouldn't be used.

- **IrpSp->MajorFunction** is set to **IRP_MJ_QUERY_VOLUME_INFORMATION**.

- **IrpSp->Parameters.QueryVolume.FsInformationClass** is the type of volume information to be returned by the file system. This member can be one of the following values.

| Value | Meaning |
| ----- | ------- |
| FileFsAttributeInformation | Return a [**FILE_FS_ATTRIBUTE_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_attribute_information) structure that contains attribute information about the file system responsible for the volume. |
| FileFsControlInformation | Return a [**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information) structure that contains file system control information about the volume. |
| FileFsDeviceInformation | Return a [**FILE_FS_DEVICE_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_fs_device_information) structure that contains device information for the volume. |
| FileFsDriverPathInformation | Return a [**FILE_FS_DRIVER_PATH_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_driver_path_information) structure that contains information about whether a specified driver is in the I/O path for the volume. The originator of the **IRP_MJ_QUERY_VOLUME_INFORMATION** request must store the name of the driver into the **FILE_FS_DRIVER_PATH_INFORMATION** structure before sending the IRP to the file system volume device stack. |
| FileFsFullSizeInformation | Return a [**FILE_FS_FULL_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_full_size_information) structure that contains information about the total amount of space available on the volume. |
| FileFsObjectIdInformation | Return a [**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information) structure that contains file-system-specific object ID information for the volume. This object ID information isn't the same as the (GUID-based) unique volume name that the operating system assigned. |
| FileFsSizeInformation | Return a [**FILE_FS_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_size_information) structure containing information about the amount of space on the volume that is available to the user associated with the thread that originated the **IRP_MJ_QUERY_VOLUME_INFORMATION** request. |
| FileFsVolumeInformation | Return a [**FILE_FS_VOLUME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_volume_information) that contains information about the volume such as the volume label, serial number, and creation time. |
| FileFsSectorSizeInformation | Return a [**FILE_FS_SECTOR_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_sector_size_information) structure that contains information about the physical and logical sector sizes of a volume. |

- **IrpSp->Parameters.QueryVolume.Length** is the length, in bytes, of the buffer pointed to by **Irp->UserBuffer**. On return, this variable receives the number of bytes written to the buffer.

## See also

[**FILE_FS_ATTRIBUTE_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_attribute_information)

[**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information)

[**FILE_FS_DEVICE_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_fs_device_information)

[**FILE_FS_DRIVER_PATH_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_driver_path_information)

[**FILE_FS_FULL_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_full_size_information)

[**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information)

[**FILE_FS_SECTOR_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_sector_size_information)

[**FILE_FS_SIZE_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_size_information)

[**FILE_FS_VOLUME_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_volume_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_SET_VOLUME_INFORMATION**](irp-mj-set-volume-information.md)

[**ZwQueryVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvolumeinformationfile)

[**ZwSetVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetvolumeinformationfile)
