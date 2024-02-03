---
title: IRP_MJ_WRITE (FS and Filter Drivers)
description: IRP_MJ_WRITE
keywords: ["IRP_MJ_WRITE Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_WRITE
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_WRITE (FS and filter drivers)

## When Sent

The I/O Manager or a file system driver sends the IRP_MJ_WRITE request. This request can be sent, for example, when a user-mode application has called a Win32 function such as **WriteFile** or when a kernel-mode component has called [**ZwWriteFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile).

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine the parameters and minor function code.

For MDL write requests, the file system should check the minor function code to determine which operation is requested. The following are the valid minor function codes, which can be used only for cached file I/O:

- IRP_MN_COMPLETE
- IRP_MN_COMPLETE_MDL
- IRP_MN_COMPLETE_MDL_DPC
- IRP_MN_COMPRESSED
- IRP_MN_DPC
- IRP_MN_MDL
- IRP_MN_MDL_DPC
- IRP_MN_NORMAL

For more information about how to handle this IRP, study the FASTFAT sample that is included in the Windows Driver Kit (WDK).

## Operation: Legacy File System Filter Drivers

The filter driver should perform any needed processing and, depending on the nature of the filter, perform one of the following actions:

- Complete or fail the IRP, or
- Pass the IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a create request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied buffer to be used as an intermediate system buffer, if the DO_BUFFERED_IO flag is set in **DeviceObject->Flags**. Otherwise, this member is set to **NULL**.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. If the IRP_MJ_WRITE request fails, the file system's write dispatch routine returns an error NTSTATUS value, and the value of **Irp->IoStatus.Information** is undefined and shouldn't be used.

- **Irp->MdlAddress** is the address of a memory descriptor list (MDL) that describes the pages to which the data is to be written.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**. If the FO_SYNCHRONOUS_IO flag is set in **IrpSp->FileObject->Flags**, the file object was opened for synchronous I/O.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_WRITE and shouldn't be used.

- **IrpSp->Flags**: If the SL_FORCE_DIRECT_WRITE flag is set, kernel-mode drivers can write to volume areas that they normally can't write to because of direct write blocking. Direct write blocking was implemented for security reasons in Windows Vista and later operating systems. This flag is checked both at the file system layer and storage stack layer. For more information about direct write blocking, see [Blocking Direct Write Operations to Volumes and Disks](/windows-hardware/drivers/ddi/index). The SL_FORCE_DIRECT_WRITE flag is available in Windows Vista and later versions of Windows.

- **IrpSp->MajorFunction** is set to IRP_MJ_WRITE.

- **IrpSp->MinorFunction** specifies the operation being requested and contains one of the following:

  - IRP_MN_COMPLETE
  - IRP_MN_COMPLETE_MDL
  - IRP_MN_COMPLETE_MDL_DPC
  - IRP_MN_COMPRESSED
  - IRP_MN_DPC
  - IRP_MN_MDL
  - IRP_MN_MDL_DPC
  - IRP_MN_NORMAL

- **IrpSp->Parameters.Write.ByteOffset** is a LARGE_INTEGER variable that specifies the starting byte offset within the file of the data to be written.

  Under certain circumstances, this parameter might contain a special value. For example, when true, the following condition indicates that the current end of file should be used instead of an explicit file offset value: **IrpSp->Parameters.Write.ByteOffset.LowPart** == FILE_WRITE_TO_END_OF_FILE and **IrpSp->Parameters.Write.ByteOffset.HighPart** == -1

- **IrpSp->Parameters.Write.Key** is the key value associated with a byte-range lock on the target file.

- **IrpSp->Parameters.Write.Length** is the length in bytes of the data to be written. If the write operation is successful, the number of bytes written is returned in the **Information** member of the IO_STATUS_BLOCK structure pointed to by **Irp->IoStatus**.

## Remarks

File systems round write and read operations at end of file up to a multiple of the sector size of the underlying file storage device. When filters process pre-read or pre-write operations, those filters that allocate and swap buffers need to round up the size of an allocated buffer to a multiple of the sector size of the associated device. If they don't, the length of data transferred from the underlying file system will exceed the allocated length of the buffer. For more information about swapping buffers, see [swapBuffers Minifilter Sample](/samples/browse/).

## See also

[**CcMdlWriteComplete**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ccmdlwritecomplete)

[**CcPrepareMdlWrite**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ccpreparemdlwrite)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_READ**](irp-mj-read.md)

[**IRP_MJ_WRITE (WDK Kernel Reference)**](../kernel/irp-mj-write.md)

[**ZwWriteFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile)
