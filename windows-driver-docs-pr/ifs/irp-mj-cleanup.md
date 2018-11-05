---
title: IRP_MJ_CLEANUP
description: IRP\_MJ\_CLEANUP
ms.assetid: e4593d99-a721-4ab1-82a5-b32b9c312b25
keywords: ["IRP_MJ_CLEANUP Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_CLEANUP
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_CLEANUP


## When Sent


Receipt of the IRP\_MJ\_CLEANUP request indicates that the handle reference count on a file object has reached zero. (In other words, all handles to the file object have been closed.) Often it is sent when a user-mode application has called the Microsoft Win32 **CloseHandle** function (or when a kernel-mode driver has called [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417)) on the last outstanding handle to a file object.

It is important to note that when all handles to a file object have been closed, this does not necessarily mean that the file object is no longer being used. System components, such as the Cache Manager and the Memory Manager, might hold outstanding references to the file object. These components can still read to or write from a file, even after an IRP\_MJ\_CLEANUP request is received.

## Operation: File System Drivers


If the target device object is the file system's control device object, the file system driver must complete the IRP.

Otherwise, the file system driver should process the cleanup request.

## Operation: File System Filter Drivers


If the target device object is the filter driver's control device object, the filter driver must complete the IRP.

Otherwise, the filter driver should pass the IRP down to the next-lower driver on the stack after performing any needed processing.

File system filter driver writers should note that [**IoCreateStreamFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548296) causes an IRP\_MJ\_CLEANUP request to be sent to the file system driver stack for the volume. Because file systems often create stream file objects as a side effect of operations other than IRP\_MJ\_CREATE, it is difficult for filter drivers to reliably detect stream file object creation. Thus a filter driver should expect to receive IRP\_MJ\_CLEANUP and IRP\_MJ\_CLOSE requests for previously unseen file objects.

Filter driver writers should also note that, unlike [**IoCreateStreamFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548296), [**IoCreateStreamFileObjectLite**](https://msdn.microsoft.com/library/windows/hardware/ff548306) does not cause an IRP\_MJ\_CLEANUP request to be sent to the file system driver stack. For this reason, and because file systems often create stream file objects as a side effect of operations other than IRP\_MJ\_CREATE, it is difficult for filter drivers to reliably detect stream file object creation. Thus filter drivers should expect to receive IRP\_MJ\_CLOSE requests for previously unseen file objects.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a cleanup request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--flags"></a>*Irp-&gt;Flags*  
The following flags are set for this request:

IRP\_CLOSE\_OPERATION

IRP\_SYNCHRONOUS\_API

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_CLEANUP and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*
Specifies IRP\_MJ\_CLEANUP.

## See also


[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoCreateStreamFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548296)

[**IoCreateStreamFileObjectLite**](https://msdn.microsoft.com/library/windows/hardware/ff548306)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_CLEANUP (WDK Kernel Reference)**](https://msdn.microsoft.com/library/windows/hardware/ff550718)

[**IRP\_MJ\_CLOSE**](irp-mj-close.md)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

[**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417)

 

 






