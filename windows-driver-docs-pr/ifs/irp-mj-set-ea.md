---
title: IRP_MJ_SET_EA
description: IRP\_MJ\_SET\_EA
ms.assetid: f9e1f867-a473-46ac-a1c0-63534c4c0755
keywords: ["IRP_MJ_SET_EA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_EA
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_SET\_EA


## When Sent


The I/O Manager sends the IRP\_MJ\_SET\_EA request to set a file's extended attributes.

## Operation: File System Drivers


If the file system supports extended attributes, the file system driver should process the request and complete the IRP. Otherwise, the file system driver should return **STATUS\_EAS\_NOT\_SUPPORTED**.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a set extended attributes request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a system-supplied input buffer that contains the extended attribute information to be set. Used for METHOD\_BUFFERED I/O.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--mdladdress"></a>*Irp-&gt;MdlAddress*  
Address of a memory descriptor list (MDL) describing an input buffer that receives the extended attribute information. Used for METHOD\_DIRECT I/O.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
Pointer to a caller-supplied [**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)-structured input buffer that receives the extended attribute information. Used for METHOD\_NEITHER I/O.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_SET\_EA and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_SET\_EA.

<a href="" id="irpsp--parameters-setea-length"></a>*IrpSp-&gt;Parameters.SetEa.Length*  
Length in bytes of the input buffer.

## See also


[**FILE\_FULL\_EA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff545793)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoCheckEaBufferValidity**](https://msdn.microsoft.com/library/windows/hardware/ff548252)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_QUERY\_EA**](irp-mj-query-ea.md)

 

 






