---
title: IRP\_MJ\_SET\_EA
description: IRP\_MJ\_SET\_EA
ms.assetid: f9e1f867-a473-46ac-a1c0-63534c4c0755
keywords: ["IRP_MJ_SET_EA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_EA
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20IRP_MJ_SET_EA%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





