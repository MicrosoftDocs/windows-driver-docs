---
title: IRP_MJ_SET_VOLUME_INFORMATION (FS and filter drivers)
description: IRP_MJ_SET_VOLUME_INFORMATION
keywords: ["IRP_MJ_SET_VOLUME_INFORMATION Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_VOLUME_INFORMATION
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_SET_VOLUME_INFORMATION (FS and filter drivers)

## When Sent

The I/O Manager sends the IRP_MJ_SET_VOLUME_INFORMATION request. It can be sent, for example, when a user-mode application has called a Win32 function such as **SetVolumeLabel**.

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine whether it represents a user volume open. If it does, the file system driver should set the appropriate volume information and complete the IRP. Otherwise, the file system should complete the IRP as appropriate without setting the volume information.

The types of volume information that can be set are file system-dependent, but generally include one or more of the following values:

- FileFsControlInformation
- FileFsLabelInformation
- FileFsObjectIdInformation

For a list of all possible information types, see the FS_INFORMATION_CLASS enumeration in *ntifs.h*.

## Operation: Legacy File System Filter Drivers

The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a set volume information request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to an input buffer that contains the values of the volume information to be set. This information is stored in one of the following structures:

  - FILE_FS_CONTROL_INFORMATION
  - FILE_FS_LABEL_INFORMATION
  - FILE_FS_OBJECTID_INFORMATION

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_SET_VOLUME_INFORMATION and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_SET_VOLUME_INFORMATION.

- **IrpSp->Parameters.SetVolume.FsInformationClass** is the type of information to be set for the volume, and can be one of the following:

  | Value | Meaning |
  | ----- | ------- |
  | FileFsControlInformation | Set [**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information) for the volume. |
  | FileFsLabelInformation | Set [**FILE_FS_LABEL_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_label_information) for the volume. |
  | FileFsObjectIdInformation | Set [**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information) for the volume. |

- **IrpSp->Parameters.SetVolume.Length** is the length, in bytes, of the buffer pointed to by **Irp->AssociatedIrp.SystemBuffer**.

## See also

[**FILE_FS_CONTROL_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_file_fs_control_information)

[**FILE_FS_LABEL_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_label_information)

[**FILE_FS_OBJECTID_INFORMATION**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_fs_objectid_information)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_QUERY_VOLUME_INFORMATION**](irp-mj-query-volume-information.md)

[**ZwQueryVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryvolumeinformationfile)

[**ZwSetVolumeInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetvolumeinformationfile)
