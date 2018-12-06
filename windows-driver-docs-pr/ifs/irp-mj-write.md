---
title: IRP_MJ_WRITE
description: IRP_MJ_WRITE
ms.assetid: 8f16a579-1598-4f70-8d88-dfe877daec31
keywords: ["IRP_MJ_WRITE Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_WRITE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_WRITE


## When Sent


The IRP\_MJ\_WRITE request is sent by the I/O Manager or by a file system driver. This request can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **WriteFile** or when a kernel-mode component has called [**ZwWriteFile**](https://msdn.microsoft.com/library/windows/hardware/ff567121).

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine the parameters and minor function code.

For MDL write requests, the file system should check the minor function code to determine which operation is requested. The following are the valid minor function codes, which can be used only for cached file I/O:

- IRP\_MN\_COMPLETE

- IRP\_MN\_COMPLETE\_MDL

- IRP\_MN\_COMPLETE\_MDL\_DPC

- IRP\_MN\_COMPRESSED

- IRP\_MN\_DPC

- IRP\_MN\_MDL

- IRP\_MN\_MDL\_DPC

- IRP\_MN\_NORMAL

For more information about how to handle this IRP, study the FASTFAT sample that is included in the Windows Driver Kit (WDK).

## Operation: File System Filter Drivers


The filter driver should perform any needed processing and, depending on the nature of the filter, either complete or fail the IRP, or pass it down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a create request:

<a href="" id="deviceobject"></a>*DeviceObject*  

A pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  

A pointer to a system-supplied buffer to be used as an intermediate system buffer, if the DO\_BUFFERED\_IO flag is set in *DeviceObject-&gt;Flags*. Otherwise, this member is set to **NULL**.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  

A pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation. If the IRP\_MJ\_WRITE request fails, the file system's write dispatch routine returns an error NTSTATUS value, and the value of *Irp-&gt;IoStatus.Information* is undefined and should not be used.

<a href="" id="irp--mdladdress"></a>*Irp-&gt;MdlAddress*  

The address of a memory descriptor list (MDL) that describes the pages to which the data is to be written.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*

A pointer to the file object that is associated with *DeviceObject*. If the FO\_SYNCHRONOUS\_IO flag is set in *IrpSp-&gt;FileObject-&gt;Flags*, the file object was opened for synchronous I/O.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBJECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_WRITE and should not be used.

<a href="" id="irpsp--flags"></a>*IrpSp-&gt;Flags*  

If the SL\_FORCE\_DIRECT\_WRITE flag is set, kernel-mode drivers can write to volume areas that they normally cannot write to because of direct write blocking. Direct write blocking was implemented for security reasons in Windows Vista and later operating systems. This flag is checked both at the file system layer and storage stack layer. For more information about direct write blocking, see [Blocking Direct Write Operations to Volumes and Disks](https://msdn.microsoft.com/library/windows/hardware/ff551353). The SL\_FORCE\_DIRECT\_WRITE flag is available in Windows Vista and later versions of Windows.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*

Specifies IRP\_MJ\_WRITE.

<a href="" id="irpsp--minorfunction"></a>*IrpSp-&gt;MinorFunction*  

Specifies the operation being requested and contains one of the following:

-   IRP\_MN\_COMPLETE

-   IRP\_MN\_COMPLETE\_MDL

-   IRP\_MN\_COMPLETE\_MDL\_DPC

-   IRP\_MN\_COMPRESSED

-   IRP\_MN\_DPC

-   IRP\_MN\_MDL

-   IRP\_MN\_MDL\_DPC

-   IRP\_MN\_NORMAL

<a href="" id="irpsp--parameters-write-byteoffset"></a>*IrpSp-&gt;Parameters.Write.ByteOffset*  

A LARGE\_INTEGER variable that specifies the starting byte offset within the file of the data to be written.

Under certain circumstances, this parameter might contain a special value. For example:

-   If the following condition is true, this indicates that the current end of file should be used instead of an explicit file offset value:

    *IrpSp-&gt;Parameters.Write.ByteOffset.LowPart* == FILE\_WRITE\_TO\_END\_OF\_FILE and *IrpSp-&gt;Parameters.Write.ByteOffset.HighPart* == -1

<a href="" id="irpsp--parameters-write-key"></a>*IrpSp-&gt;Parameters.Write.Key*  

Key value associated with a byte-range lock on the target file.

<a href="" id="irpsp--parameters-write-length"></a>*IrpSp-&gt;Parameters.Write.Length*  

Length in bytes of the data to be written. If the write operation is successful, the number of bytes written is returned in the **Information** member of the IO\_STATUS\_BLOCK structure pointed to by *Irp-&gt;IoStatus*.

Remarks
-------

File systems round write and read operations at end of file up to a multiple of the sector size of the underlying file storage device. When processing pre-read or pre-write operations, filters that allocate and swap buffers need to round the size of an allocated buffer up to a multiple of the sector size of the associated device. If they do not, the length of data transferred from the underlying file system will exceed the allocated length of the buffer. For more information about swapping buffers, see [swapBuffers Minifilter Sample](http://go.microsoft.com/fwlink/p/?linkid=256055).

## See also


[**CcMdlWriteComplete**](https://msdn.microsoft.com/library/windows/hardware/ff539172)

[**CcPrepareMdlWrite**](https://msdn.microsoft.com/library/windows/hardware/ff539181)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_READ**](irp-mj-read.md)

[**IRP\_MJ\_WRITE (WDK Kernel Reference)**](https://msdn.microsoft.com/library/windows/hardware/ff550819)

[**ZwWriteFile**](https://msdn.microsoft.com/library/windows/hardware/ff567121)

 

 






