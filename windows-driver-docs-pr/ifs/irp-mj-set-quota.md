---
title: IRP_MJ_SET_QUOTA
description: IRP\_MJ\_SET\_QUOTA
ms.assetid: 256c349b-48cb-4a9f-a60a-89503d8f3f58
keywords: ["IRP_MJ_SET_QUOTA Installable File System Drivers"]
topic_type:
- apiref
api_name:
- IRP_MJ_SET_QUOTA
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# IRP\_MJ\_SET\_QUOTA


## When Sent


The IRP\_MJ\_SET\_QUOTA request is sent by the I/O Manager. It can be sent, for example, when a user-mode application has called a Microsoft Win32 method such as **IDiskQuotaControl::SetQuotaState**.

## Operation: File System Drivers


IRP\_MJ\_SET\_QUOTA and IRP\_MJ\_QUERY\_QUOTA existed in Windows NT 4.0 but were not used by file systems. On Windows 2000 and later systems, they are used for disk quota support in NTFS. Support for these IRPs by new file systems is optional.

## Operation: File System Filter Drivers


The filter driver should pass this IRP down to the next-lower driver on the stack, unless it needs to explicitly override quota behavior.

## Parameters


A file system or filter driver calls [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) with the given IRP to get a pointer to its own [**stack location**](https://msdn.microsoft.com/library/windows/hardware/ff550659) in the IRP, shown in the following list as *IrpSp*. (The IRP is shown as *Irp*.) The driver can use the information that is set in the following members of the IRP and the IRP stack location in processing a set quota information request:

<a href="" id="deviceobject"></a>*DeviceObject*  
Pointer to the target device object.

<a href="" id="deviceobject--flags"></a>*DeviceObject-&gt;Flags*  
If the DO\_BUFFERED\_IO flag is set, the caller has requested METHOD\_BUFFERED I/O. Otherwise, the caller has requested METHOD\_NEITHER I/O.

<a href="" id="irp--associatedirp-systembuffer"></a>*Irp-&gt;AssociatedIrp.SystemBuffer*  
Pointer to a system-supplied buffer to be used as an intermediate system buffer, if the DO\_BUFFERED\_IO flag is set in *DeviceObject-&gt;Flags*. Otherwise, this member is set to **NULL**.

<a href="" id="irp--iostatus"></a>*Irp-&gt;IoStatus*  
Pointer to an [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure that receives the final completion status and information about the requested operation.

<a href="" id="irp--userbuffer"></a>*Irp-&gt;UserBuffer*  
Pointer to a caller-supplied buffer that contains the quota entries to be added or modified for the volume.

<a href="" id="irpsp--fileobject"></a>*IrpSp-&gt;FileObject*  
Pointer to the file object that is associated with *DeviceObject*.

The *IrpSp-&gt;FileObject* parameter contains a pointer to the **RelatedFileObject** field, which is also a FILE\_OBECT structure. The **RelatedFileObject** field of the FILE\_OBJECT structure is not valid during the processing of IRP\_MJ\_SET\_QUOTA and should not be used.

<a href="" id="irpsp--majorfunction"></a>*IrpSp-&gt;MajorFunction*  
Specifies IRP\_MJ\_SET\_QUOTA.

<a href="" id="irpsp--parameters-setquota-length"></a>*IrpSp-&gt;Parameters.SetQuota.Length*  
Specifies the length, in bytes, of the buffer pointed to by *Irp-&gt;UserBuffer*.

## See also


[**FILE\_QUOTA\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff540342)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671)

[**IoCheckQuotaBufferValidity**](https://msdn.microsoft.com/library/windows/hardware/ff548279)

[**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174)

[**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)

[**IRP\_MJ\_QUERY\_QUOTA**](irp-mj-query-quota.md)

 

 






