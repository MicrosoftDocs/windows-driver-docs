---
title: IRP_MJ_READ (FS and filter drivers)
description: IRP_MJ_READ
keywords: ["IRP_MJ_READ Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_READ
api_type:
- NA
ms.date: 03/13/2023
ms.topic: reference
---

# IRP_MJ_READ (FS and filter drivers)

## When Sent

The I/O Manager or a file system driver sends the IRP_MJ_READ request. This request can be sent, for example, when a user-mode application has called a Win32 function such as **ReadFile**, or when a kernel-mode component has called [**ZwReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile).

## Operation: File System Drivers

The file system driver should extract and decode the file object to determine the parameters and minor function code.

For memory descriptor list (MDL) read requests, the file system should check the minor function code to determine which operation is requested. The following are the valid minor function codes, which can be used only for cached file I/O:

- IRP_MN_COMPLETE
- IRP_MN_COMPLETE_MDL
- IRP_MN_COMPLETE_MDL_DPC
- IRP_MN_COMPRESSED
- IRP_MN_DPC
- IRP_MN_MDL
- IRP_MN_MDL_DPC
- IRP_MN_NORMAL

For more information about handling this IRP, study the CDFS and FASTFAT samples that are included in the Windows Driver Kit (WDK).

## Operation: Legacy File System Filter Drivers

The filter driver should perform any needed processing and, depending on the nature of the filter, should perform one of the following actions:

- Complete or fail the IRP, or
- Pass the IRP down to the next-lower driver on the stack.

## Parameters

A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) for the given IRP to get a pointer to its own stack location in the IRP. In the following parameters, **Irp** points to the [**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) and **IrpSp** points to the [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location). The driver can use the information that is set in the following members of the IRP and the IRP stack location to process a read request:

- **DeviceObject** is a pointer to the target device object.

- **Irp->AssociatedIrp.SystemBuffer** points to a system-supplied buffer to be used as an intermediate system buffer, if the DO_BUFFERED_IO flag is set in **DeviceObject->Flags**. Otherwise, this member is set to **NULL**.

- **Irp->IoStatus** points to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and information about the requested operation. For more information, see the description of the *IoStatusBlock* parameter to [**ZwReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile).

- **Irp->MdlAddress** is the address of a memory descriptor list (MDL) describing the pages that contain the data to be read.

- **Irp->UserBuffer* points to a caller-supplied output buffer that receives the data that is read from the file.

- **IrpSp->FileObject** points to the file object that is associated with **DeviceObject**. If the FO_SYNCHRONOUS_IO flag is set in **IrpSp->FileObject->Flags**, the file object was opened for synchronous I/O.

  The **IrpSp->FileObject** parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE_OBJECT structure. The **RelatedFileObject** field of the FILE_OBJECT structure isn't valid during the processing of IRP_MJ_READ and shouldn't be used.

- **IrpSp->MajorFunction** is set to IRP_MJ_READ.

- **IrpSp->MinorFunction** specifies the operation being requested and contains one of the following values:

- IRP_MN_COMPLETE
- IRP_MN_COMPLETE_MDL
- IRP_MN_COMPLETE_MDL_DPC
- IRP_MN_COMPRESSED
- IRP_MN_DPC
- IRP_MN_MDL
- IRP_MN_MDL_DPC
- IRP_MN_NORMAL

- **IrpSp->Parameters.Read.ByteOffset** is a LARGE_INTEGER variable that specifies the starting byte offset within the file of the data to be read.

- **IrpSp->Parameters.Read.Key**is the key value associated with a byte-range lock on the target file.

- **IrpSp->Parameters.Read.Length** is the length in bytes of the data to be read. If the read operation is successful, the number of bytes read is returned in the **Information** member of the [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure pointed to by *Irp->IoStatus*.

## Remarks

File systems round write and read operations at end of file up to a multiple of the sector size of the underlying file storage device. When filters process pre-read or pre-write operations, those filters that allocate and swap buffers need to round up the size of an allocated buffer to a multiple of the sector size of the associated device. If they don't, the length of data transferred from the underlying file system will exceed the allocated length of the buffer. For more information about swapping buffers, see [swapBuffers Minifilter Sample](/samples/browse/).

## See also

[**CcMdlRead**](/previous-versions/ff539159(v=vs.85))

[**CcMdlReadComplete**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ccmdlreadcomplete)

[**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation)

[**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)

[**IRP_MJ_READ (WDK Kernel Reference)**](../kernel/irp-mj-read.md)

[**IRP_MJ_WRITE**](irp-mj-write.md)

[**ZwReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile)
