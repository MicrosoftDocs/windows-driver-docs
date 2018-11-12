---
title: IRP_MJ_READ
description: IRP_MJ_READ
ms.assetid: f2f909ff-4af6-433e-9f3c-9692b5ab7171
keywords: ["IRP_MJ_READ Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_READ
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_READ


## When Sent


The IRP\_MJ\_READ request is sent by the I/O Manager or by a file system driver. This request can be sent, for example, when a user-mode application has called a Microsoft Win32 function such as **ReadFile**, or when a kernel-mode component has called [**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072).

## Operation: File System Drivers


The file system driver should extract and decode the file object to determine the parameters and minor function code.

For memory descriptor list (MDL) read requests, the file system should check the minor function code to determine which operation is requested. The following are the valid minor function codes, which can be used only for cached file I/O:

- IRP\_MN\_COMPLETE

- IRP\_MN\_COMPLETE\_MDL

- IRP\_MN\_COMPLETE\_MDL\_DPC

- IRP\_MN\_COMPRESSED

- IRP\_MN\_DPC

- IRP\_MN\_MDL

- IRP\_MN\_MDL\_DPC

- IRP\_MN\_NORMAL

For more information about handling this IRP, study the CDFS and FASTFAT samples that are included in the Windows Driver Kit (WDK).

## Operation: File System Filter Drivers


The filter driver should perform any needed processing and, depending on the nature of the filter, either complete or fail the IRP or pass it down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information contained in the following members of the IRP and the IRP stack location in processing a read request:

<a href="" id="deviceobject"></a>*DeviceObject*  

Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  

Pointer to a system-supplied buffer to be used as an intermediate system buffer, if the DO\_BUFFERED\_IO flag is set in *DeviceObject-&gt;Flags*. Otherwise, this member is set to **NULL**.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  

Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation. For more information, see the description of the *IoStatusBlock* parameter to [**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072).

<a href="" id="irp--mdladdress"></a>*Irp-&gt;MdlAddress*  

Address of a memory descriptor list (MDL) describing the pages that contain the data to be read.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  

Pointer to a caller-supplied output buffer that receives the data that is read from the file.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  

Pointer to the file object that is associated with *DeviceObject*. If the FO\_SYNCHRONOUS\_IO flag is set in *IrpSp-&gt;FileObject-&gt;Flags*, the file object was opened for synchronous I/O.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_READ and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  

Specifies IRP\_MJ\_READ.

<a href="" id="irpsp--minorfunction"></a>*IrpSp-&gt;MinorFunction*  

Specifies the operation being requested and contains one of the following:

- IRP\_MN\_COMPLETE

- IRP\_MN\_COMPLETE\_MDL

- IRP\_MN\_COMPLETE\_MDL\_DPC

- IRP\_MN\_COMPRESSED

- IRP\_MN\_DPC

- IRP\_MN\_MDL

- IRP\_MN\_MDL\_DPC

- IRP\_MN\_NORMAL

<a href="" id="irpsp--parameters-read-byteoffset"></a>*IrpSp-&gt;Parameters.Read.ByteOffset*

A LARGE\_INTEGER variable that specifies the starting byte offset within the file of the data to be read.

<a href="" id="irpsp--parameters-read-key"></a>*IrpSp-&gt;Parameters.Read.Key*

Key value associated with a byte-range lock on the target file.

<a href="" id="irpsp--parameters-read-length"></a>*IrpSp-&gt;Parameters.Read.Length*

Length in bytes of the data to be read. If the read operation is successful, the number of bytes read is returned in the **Information** member of the [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure pointed to by *Irp-&gt;IoStatus*.

Remarks
-------

File systems round write and read operations at end of file up to a multiple of the sector size of the underlying file storage device. When processing pre-read or pre-write operations, filters that allocate and swap buffers need to round the size of an allocated buffer up to a multiple of the sector size of the associated device. If they do not, the length of data transferred from the underlying file system will exceed the allocated length of the buffer. For more information about swapping buffers, see [swapBuffers Minifilter Sample](http://go.microsoft.com/fwlink/p/?linkid=256055).

## See also


[**CcMdlRead**](https://msdn.microsoft.com/library/windows/hardware/ff539159)

[**CcMdlReadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff539163)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_READ (WDK Kernel Reference)**](https://msdn.microsoft.com/library/windows/hardware/ff550794)

[**IRP\_MJ\_WRITE**](irp-mj-write.md)

[**ZwReadFile**](https://msdn.microsoft.com/library/windows/hardware/ff567072)

 

 






